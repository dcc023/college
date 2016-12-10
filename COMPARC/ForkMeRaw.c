#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	int fd[2];
	int value = 0;
	pid_t IDofTheGuys;
	int a;
	int b;
	int c;
	int d;
	pipe(fd);
	

	//Open a pipe

	IDofTheGuys = fork();
	if(IDofTheGuys == -1)
	{
		exit(0);
	}
	if(IDofTheGuys == 0)
	{
		//In That there child
		close(fd[0]); //Close reading.
		b = 5 +4;
		printf("B Changed in child. It is now...%d...Sending to Parent.\n", b);
		write(fd[1], &b, sizeof(b));
		close(fd[1]);
		exit(0); //Squick 
		
	}
	if(IDofTheGuys != 0)
	{
		close(fd[1]); //CLose Writing.
		a = 7 + 7;
		printf("A changed in Parent. It is now...%d...Getting B.\n", a);
		read(fd[0], &b, sizeof(b));
		close(fd[0]);
		printf("Parent received B as a vlaue of...%d...from child.\n", b);
		
		
		//Parenthoood
	}

	c = a + b;
        printf("C is a + b, which equals...%d...\n", c);
	d = c + 1;
	printf("D is C + 1, which equals...%d...\n", d);


	return 0;

}
