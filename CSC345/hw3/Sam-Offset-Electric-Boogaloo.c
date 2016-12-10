#include <stdio.h>
#define NUM_LOOPS 500000

long long sum = 0;

void counting_function(void *ptr) //passing a pointer to fn. See, we take a pointer as a paramter, which is what &offset1 was. We threw a pointer to that variable up here.
{
	int offset =*(int *) ptr; //But you can't use pointers for calculations. So...we copy the value of the mem address the pointer's point at??? So we made a copy anyway. A copy of what's at the
				 //memory adress of which ptr equals because an address is what was passed into it which is the address of offset1 which when dereference we can see the value at that
				//address and OH MY GOD THIS EXPLAINATION IS LIKE A KINGDOM HEARTS PLOT SUMMARY.
	// dereferencing a pointer var

	for(int i=0; i<NUM_LOOPS; i++) //WOAH THE 90s. More like the 500000 times you're gonna run this thing.
	{
		sum=sum+offset;
	}
}

int main(void)
{
	int offset1 =100; //Okay, yeah. Make a fancy variable n' that.
	// creating a variable to be passed to fn
	counting_function(&offset1);// passing address of variable. That'll tell the function 'Hey! Look at this thing I made instead of making your own copy!'
	printf("Sum = %lld\n", sum); //After that guff is done, sum is still global.
	return 0; //Done. uwu
}
