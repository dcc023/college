
#include <stdio.h>
#include <pthread.h>
#define NUM_LOOPS 500000

long long sum = 0;
// a global variable

void* counting_function(void *ptr)
{
	int offset =*(int *) ptr; //Dereference the pointer, 'ptr', into an int named offset. A different offset from below, this...this is this FUNCTION'S own original offset, do not steal.
	for(int i=0; i<NUM_LOOPS; i++) //Okay, so, logically we should get...uh...well, 500000 for one thread, -500000 for the other.
	{ 
		sum=sum+offset; //Oh, these threads are going to get all mixed up. Oh god.
	}
	pthread_exit(NULL); //This won't end well.
}


int main(void)
{
	int offset1 =1; //Get one offset, as usual...
	int offset2 = -1; // Declare a second offset...wait, a second one??? What for???
	pthread_t id1, id2; // Declare another object of thread. Aha, commas let you make more than one object. We're dealing in twos here, oh shite.

	// Spawn Treads
	pthread_create(&id1, NULL, counting_function, &offset1); //Okay, so this one goes on its merry way, and the main goes on
	pthread_create(&id2, NULL, counting_function, &offset2); //Same here. We'll let off ANOTHER thread to do its thing...withs its OWN parameter! A different one!
	// Create your second thread
	
	// Join Threads
	pthread_join(id1, NULL); //Wait for one
	pthread_join(id2, NULL); // Join the threads back to main. Yup, wait for the other...
	printf("Sum = %lld\n", sum); //And...I have a bad feeling about this. Which one will it return? Or will it be an amalgamation of the two?
	return 0;
}
