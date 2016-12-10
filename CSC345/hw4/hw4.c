#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
	int n = 5; //processes
	int m = 3; //resources
	int complete = 0;
	int i = 0;
	int j = 0;
	
	int Available[m]; //array for available resources
	int Max[n][m]; //Matrix for processes to tell the OS the max resources they will ever need
	int Allocation[n][m]; //matrix for how many resources each process is already using
	int Need[n][m]; //matrix for what resources the process needs currently
	int Work[m]; //used to calculate the order of allocation
	int Finish[n]; //a table that shows if a process has been allocated at the current time
	int Request[m];
	
//MAX
	//Resource A
	Max[0][0]=7;
	Max[1][0]=3;
	Max[2][0]=9;
	Max[3][0]=2;
	Max[4][0]=4;
	//Resource B
	Max[0][1]=5;
	Max[1][1]=2;
	Max[2][1]=0;
	Max[3][1]=2;
	Max[4][1]=3;
	//Resource C
	Max[0][2]=3;
	Max[1][2]=2;
	Max[2][2]=2;
	Max[3][2]=2;
	Max[4][2]=3;

//INITIAL ALLOCATIONS
	//Resource A
	Allocation[0][0]=0;
	Allocation[1][0]=2;
	Allocation[2][0]=3;
	Allocation[3][0]=2;
	Allocation[4][0]=0;
	//Resource B
	Allocation[0][1]=1;
	Allocation[1][1]=0;
	Allocation[2][1]=0;
	Allocation[3][1]=1;
	Allocation[4][1]=0;
	//Resource C
	Allocation[0][2]=0;
	Allocation[1][2]=0;
	Allocation[2][2]=2;
	Allocation[3][2]=1;
	Allocation[4][2]=2;

//AVAILABLE
	Available[0]=10;
	Available[1]=5;
	Available[3]=7;

	//Copy Max into Need
	for(i=0; i<n; i++)
	{
		for(j=0; j<m; j++)
		{
			Need[i][j] = Max[i][j];
		}
	}

	//Step One: If Request <= Need
	for(i=0; i<m; i++) //For every resource
	{
		if(Request[i]>Need[1][i])
		{
			printf("Error, Request exceeds the Need\n");
			exit(0);
		}
	}
	
	//Step Two: If Request <= Available
	for(i=0; i<m; i++)
	{
		if(Request[i]>Available[i])
		{
			printf("Error, I'm waiting..\n");
			exit(0);
		}
	}
	
	//Step Three: Perform all of the updates
	for(i=0; i<m; i++)
	{
		Available[i] = Available[i] - Request[i];
		Allocation[1][i] = Allocation[1][i] + Request[i];
		Need[1][i] = Need[1][i] - Request[i];
	}

	//Safety Check
	
	//Part 1:
	//Set all Work = Available
	for(i=0; i<m; i++)
	{
		Work[i] = Available[i];
	}

	//Set all to false in Finish
	for(i=0; i<n; i++)
	{
		Finish[i] = 0;
	}
	
	//Part 2: Find an i such that Finish[i] = False and Need[i] <= Work, If no such i, go to step 4
	i=0; //Processes
	j=0; //Resources
	int counter = 0;
	bool skip = 0;

	do
		{
			counter++;
			if(i==n) //
			{
				i=0;
			}
			
			if(Finish[i]==0) 
			{

				for(j=0; j<m; j++) //For Need vs work
				{
					if(Need[i][j]>Work[j]) //To check whether your processes Need is less than the work
					{
						skip=1; //Or else we skip the next bit
					}
				}
				if(skip == 0)
				{
					for(j=0; j<m; j++) //For all j, add the Allocation to the Workload, so we can develop a safe sequence
					{
						Work[j]=Work[j]+Allocation[i][j];
					}
					Finish[i]=1;
					counter=0;
					printf("P%d, ",i);
				}
				

			}

			if(counter == n*2) //If counter is equal to process
			{
				j=0;
				for(i=0;i<n;i++)
				{
					if(Finish[i]==0)
					{
						j=1;
						printf("\nDeadlock\n");
					}
				}
				
				complete = 1;
			}
			i++;
			skip = 0;

		}
		while(complete==0);
	printf("\n");
	return 0;
	
}
