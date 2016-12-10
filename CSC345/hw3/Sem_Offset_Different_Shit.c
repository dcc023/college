
#include <stdio.h>
#include <pthread.h>
#define NUM_LOOPS 500000

long long sum = 0;
// a global variable

pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER; //Well, looks like pthread has a handy mutex variable. That's helpful.

void* counting_function(void *ptr)
{
	int offset =*(int *) ptr; //Get our offset.

	for(int i=0; i<NUM_LOOPS; i++) //The loop holds the critical section.
	{
		// Start of crtical section
		pthread_mutex_lock(&mutex); //Hm...I guess this is the gate to the critical section. If a thread sees mutex is locked...well, they're stuck until the other is done.
		sum=sum+offset; //Do the thing.
		// End of critical section
		pthread_mutex_unlock(&mutex); //Wh-wait...this will still generate a problem. Won't it? Unlocking the mutex mid-for loop will give the other thread wanton access to sum.
		//AHA! I see now. One thread increments by one while the other decrements by one. The point of this program is to have the two threads cancel each other out and make the sum 0.
		//This is possible, as the threads have to take turns with sum, adding and subtracting. Even if the order they go in is inconsistant, one will always net +500000 and the other
		//will always net -500000, resulting in zero. Before, with no limits on the threads, the sum could be anything at any time, resulting in a completely random answer. It was a mess.
		//Without the limits, threads changing sum at the same time prolly did some weird fucking assembly shit and a bitwise shat itself and oh god I don't even want to think about
		//it. BOTTOM LINE: HAVE TIGHT CONTROL ON ALL THINGS IN YOUR PROGRAM, ESPECIALLY THREADS.
		//It's useless if you can't control and predict its behavior!
	}

	pthread_exit(NULL); // passing return arguments from thread
}


int main(void)
{
	int offset1 =1; //One offset for one thread
	int offset2 = -1; //Another offset for the other
	pthread_t id1, id2; //And our two chuckleheads who keep racing each other for the citical section.

	// Spawn Threads
	pthread_create(&id1, NULL, counting_function, &offset1); //So we'll send both the idiots off at the same time, as usual...
	pthread_create(&id2, NULL, counting_function, &offset2); //All the fixes are in the function called. After all, that's where the 'critical section' of shared variables are.
	
	// Join Threads
	pthread_join(id1, NULL); //Bring in one
	pthread_join(id2, NULL); //And the other. Main's done waiting, we can go.
 
	printf("Sum = %lld\n", sum); //Nice...what will this print? Probably id2's...or whoever went last, I guess ,which could be either of them.
	return 0;
}
