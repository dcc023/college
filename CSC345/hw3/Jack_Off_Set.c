

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define MAXSIZE 100
#define ITERATIONS 1000

int buffer[MAXSIZE]; // buffer. An array of ints. Classic.
int nextp, nextc; // temporary storage. For what? Pointer addresses, I'm willing to bet.
int count=0; //S'right there on the label.  A counter.
int ProFin=0; //Is the producer done? That's what this variable will keep track of.
pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER; //Awh, a semaphore! Calling it mutex1 in case I want to use another gate. I doubt I'll need a second one. EDIT: Got rid of the one.

//Don't worry about this. We only get to this function once the threads are dead anyway.
void printfunction(void * ptr)
{
	int count = *(int *) ptr; //End goal. count here copies count global.
	if (count==0) //If count is zero, then the producer has nothing else to give the consumer.
	{
		printf("All items produced are consumed by the consumer \n"); //This is what we want. After all, we can't have a producer that makes stuff the consumer misses.
	}
	else
	{
		for (int i=0; i<=count; i=i+1)
		{
			printf("%d, \t",buffer[i]); //Here, if SOMEHOW the consumer ends without taking all the producer stuff, we'll see all the left over stuff.
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
	//CRITICAL SECTION. We'll edit variables for the Consumer. PRODUCER /MUST/ GO FIRST. Why? Well, the consumer needs stuff to...you know. Consume.
		item = (rand()%7)%10; //Okay, make a random number. Fine enough. I do wonder if this'll be critical section, since this has the same name as consumer's item. Might be an issue.
				     //Though, it seems item gets a new value every iteration, so it shouldn't matter so long as the consumer and producer are taking turns.
		flag=flag+1;	//Literally just a counter SPECIFICALLY for the producer.
		nextp=item; //nextp? Oh, that's a global int. Yup, we're in critical section. So we save our completely random variable in nextp. Dunno why there's an intermediate nextp value, but whatevs.
		buffer[in]=nextp; //Count starts at 0, so will 'in'. In BASICALLY increments by 1 every cycle, rolling over to zero at 100.
		in=((in+1)%MAXSIZE); //Next one in the array. I guess the mod MAXSIZE makes it so, if we go over 100, we just roll over back to 0. Clever.
		count=count+1; //Add one to count. Count says how many thing we have to consume. It's a global variable, so Consumer can see it too.

		//All that guff with adding to count a lot until it equaled MAXSIZE was removed. I have no idea what it was there for, logically. Would just waist time and not be very helpful, as I want
		//to use count as, literally, a count of all the things the producer has, at any point, for the consumer to consume.
	//CRITICAL SECTION END
		pthread_mutex_unlock(&mutex); //AAAAAND unluock
	}
	while (flag<=ITERATIONS); //So flag has to go up to ITERATIONS...or, 1000.
	ProFin=1; //Once we're out of the loop, change the ProFin flag to 1. Consumer only reads this, so it's okay.
	pthread_exit(NULL); //Well, whatever happened, we're done once flag's done with its iterations.
}


void *consumer(void *ptr) 
{
	//Okay, this bit is just reading CS variables. No trouble.
	int item, flag=ITERATIONS; //These might be okay, because they're defined as their own variables for this function. Let's see if we can suss out what this part does. Consumer consumes, right?
	int out = *(int *) ptr; //Okay, so, 'out', like 'in', takes count, the global variable.
	do
	{
		pthread_mutex_lock(&mutex);
	//CRITICAL SECTION. Reads Count which can be edited by Producer at the same time.
		while (count >0) //count being above zero means there's things to consume!
		{
			nextc = buffer[out]; //next c...???? That's a global as well, only used by this one.
			out=(out+1)%MAXSIZE; //What is this? Rolling over, just like 'in' in the producer.
			printf("\t\tCount = %d in consumer at Iteration = %d\n", count, flag); //So, we read the buffer at the next index into nextc. That's nice.
			count = count-1; //That's one less thing to consume.
			flag=flag-1; //One less flag. Just used for the flair up above, but has nothing to do with the while loop.
		}
	
	
		if (count <= 0 && ProFin == 0) //If count is equal to zero, producer ain't made anything yet. Buuuut, if ProFin is 1, then we're not faster than producer...it's just not doing anything.
		{
			printf("consumer made to wait...faster than producer.\n");
		}
		pthread_mutex_unlock(&mutex);
	//CRITICAL SECTION END. Flag is Cosumer's OWN variable.
	}
	while (ProFin == 0 || count > 0); //While the producer isn't done stuffing my fat face, AMIRITE????
	pthread_exit(NULL);
}


int main(void) //So, first, let's figure out what we're wanting to happen here. 
{
	int in=0, out=0; //pointers
	pthread_t pro, con; //Two threads. Producer and Consumer
	int rc1;
	int rc2; //I guess there are error things

	// Spawn threads
	rc1 = pthread_create(&pro, NULL, producer, &count); //So, start one, with count
	rc2 = pthread_create(&con, NULL, consumer, &count); //Start the other, also with count
	//These creation functions will return integers into rc1 and rc2, respecitively. If there's no trouble, then both rc1 and 2 should be zero.
	//Now, the magic happens in producer and consumer

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
