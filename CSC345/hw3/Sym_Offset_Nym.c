
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define MAXSIZE 100
#define ITERATIONS 1000

int buffer[MAXSIZE]; // buffer. An array of ints. Classic.
int nextp, nextc; // temporary storage. For what? Pointer addresses, I'm willing to bet.
int count=0; //S'right there on the label.  A counter.
int procheck = 0;
pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER;

//Don't worry about this. We only get to this function once the threads are dead anyway.
void printfunction(void * ptr)
{
	int count = *(int *) ptr; //End goal. count here copies count global.
	if (count==0) //????????????????
	{
		printf("All items produced are consumed by the consumer \n");
	}
	else
	{
		for (int i=0; i<=count; i=i+1)
		{
			printf("%d, \t",buffer[i]); //I guess this will give all the counts left over???? This...should contain the random variables we were generating????
		}
		printf("\n");
	}
}


void *producer(void *ptr) 
{
	int item, flag=0; //2 integers, on initialized as 0. I guess this'll be an on/off flag. Roit.
	int in = *(int *) ptr; //In...okay, so we copy from count's address.

	do
	{
		pthread_mutex_lock(&mutex);
	//CRITICAL SECTION. We'll edit variables for the conzumyier. PRODUCER /MUST/ GO FIRST.
		item = (rand()%7)%10; //Okay, make a random number. Fine enough. I do wonder if this'll be critical section, since this has the same name as consumer's item. Might be an issue.
				     //Though, it seems item gets a new value every iteration, so it shouldn't matter so long as the consumer and producer are taking turns.
		flag=flag+1;	//Literally just a counter SPECIFICALLY for the producer.
		nextp=item; //nextp? Oh, that's a global int. Yup, we're in critical section. So we save our completely random variable in nextp.
		buffer[in]=nextp; //Count starts at 0, so will 'in'. In BASICALLY increments by 1 every cycle, nevermind the mod 100. So we put random values in one at a time
		in=((in+1)%MAXSIZE); //Why do we mod against MAXSIZE (100)??
		count = count + 1;
		
		pthread_mutex_unlock(&mutex);
	//CRITICAL SECTION END
	}
	while (flag<=ITERATIONS); //So flag has to go up to ITERATIONS...or, 1000.
	procheck = 1;
	pthread_exit(NULL); //Well, whatever happened, we're done once flag's done with its iterations.
}


void *consumer(void *ptr) 
{
	//Okay, this bit is just reading CS variables. No trouble.
	int item, flag=ITERATIONS; //These might be okay, because they're defined as their own variables for this function. Let's see if we can suss out what this part does. Consumer consumes, right?
	int out = *(int *) ptr; //Okay, so, 'out', like 'in', takes count, the global variable.
	do
	{
	//CRITICAL SECTION. Reads Count which can be edited by Producer at the same time.
		pthread_mutex_lock(&mutex);
		while (count >0) //Different.
		{
			nextc = buffer[out]; //next c...???? That's a global as well, only used by this one.
			out=(out+1)%MAXSIZE; //What is this?
			printf("\t\tCount = %d in consumer at Iteration = %d\n", count, flag); //erm...what exactly is consumer...consuming?
			count = count-1;
			flag=flag-1;
		}
	
	
		if (count <= 0 && procheck == 0)
		{
			printf("consumer made to wait...faster than producer.\n");
			
		}
		pthread_mutex_unlock(&mutex);
	//CRITICAL SECTION END. Flag is Cosumer's OWN variable.
	}
	while (procheck==0 || flag>=0);
	pthread_exit(NULL);
}


int main(void) //So, first, let's figure out what the fuck we're wanting to happen here. 
{
	int in=0, out=0; //pointers
	pthread_t pro, con; //Two threads. Producer and Conzumyeir
	int rc1;
	int rc2; //I guess there are error things

	// Spawn threads
	rc1 = pthread_create(&pro, NULL, producer, &count); //So, start one, with count
	rc2 = pthread_create(&con, NULL, consumer, &count); //Start the other, also with count
	//These creation functions will return integers into rc1 and rc2, respecitively. If there's no trouble, then both rc1 and 2 should be zero.
	//Now, the magic happens in produce and conzumyeir

	if (rc1) //If this is true?
	{
		printf("ERROR; return code from pthread_create() is %d\n", rc1); //I guess there was an error
		exit(-1);
	}
	if (rc2) //Same here. Error checker...?
	{
		printf("ERROR; return code from pthread_create() is %d\n", rc2);
		exit(-1);
	}

	// Wait for the threads to finish
	// Otherwise main might run to the end
	// and kill the entire process when it exits.
	pthread_join(pro, NULL);
	pthread_join(con, NULL);

	printfunction(&count); //Here's where we end it.
}
