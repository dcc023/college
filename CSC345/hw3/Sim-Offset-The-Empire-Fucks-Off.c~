
#include <stdio.h>
#include <pthread.h> //Ohhh we're getting into some deep shit I dunno if im ready for this also WHAT
#define NUM_LOOPS 500000

long long sum = 0; 
// a global variable

void* counting_function(void *ptr)
{
	int offset =*(int *) ptr; //pointer is a number. That number is an address. What's in the address? Copy it as an integer into this here varaibale: offset.
	for(int i=0; i<NUM_LOOPS; i++) //500000 TIMES
	{
		sum=sum+offset;
	}
	pthread_exit(NULL); // return arguments from thread. This'll tell the thread it's done. It'll go over to join and everything's be hunkey dorey.
}


int main(void)
{

	int offset1 =100; //Once again, our offset is going to be 100.
	pthread_t id1; //Yup, we made a thing called 'id1', and it's a pthread_t, or just "thread". aaaaa sounds cute~
	// Declare an object of type thread

	pthread_create(&id1, NULL, counting_function, &offset1);
	// Create a thread using pthread_create with the following
	// arguments
	// First argument -> The thread object id
	// Second argument -> The attributes of the thread
	// (Default = NULL)
	// Third argument -> The function invoked by the thread
	// Fourth argument --> The variable passed into the
	//function executed by the thread (as a pointer)

	//So, in non techno babble, I guess pthreads, for now, can be seen as a fancy-schmansy way of invoking a function. That is to say, that function will run in tandem with this
	//main function. So, you gotta make a pthread first, with the whole "pthread_t id1". Then you use THAT to actually start up the thread. You know, make the thread DO something.
	//So, you give the thread attributes (NULL in this case), its job (That is, the function) and what it needs (ie, the parameters the function the thread's gonna do needs. In this
	//case, since we're running 'counting_function' in a thread, it wants a point. Boom &offset1 has you covered. Give that &offset1 to the rosy-cheeked thread and send it on its
	// way while the main function goes about its own business.

	pthread_join(id1, NULL); // Whiiich the main function doesn't do MUCH in this case. It just waits for id1, the thread we just sent off, to come back and say its done. This seems
				//especially useful, since you can specify WHICH thread you're waiting on.

	printf("Sum = %lld\n", sum); //Now that it's all said and done, WHAT'S THE FINAL ANSWER, BILLY? Sum was still a global variable so...I guess join synced the two up somehow? The thread's
				 	//changing this calling process as the calling process is doing shit. It's like doing 2 maths at the same time. Oh gosh.
	return 0; //Thanks. uwu

	//WOT I LEARNED: today I learned that threads are used for concurrent processing. IE: jobs that don't rely on each other or their variables can be done in tandem and their results, being
	//in the same memory space can be easily accessed by the calling program! So, concurrent jobs sync and stop at the same point and their results are used. Fast processing! WHORE-RAY.

}
