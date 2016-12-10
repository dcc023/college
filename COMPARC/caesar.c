#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{



	//check number of command line arguments 
	if(argc < 2 || argc > 2)
	{
		printf("Warning: You have %d arguments!\n", argc);
		return 1;
		
	}

		
	//create command line argument k from string to int
	int k = atoi(argv[1]);

	char p[256];

	//Take user input and print out said input
	printf("Enter a string to rotate: ");
	fgets(p, 256, stdin);
	//printf("%s\n", p);
	
	//Rotate the input by k.
	int i = 0;
	int upper = 'A';
	int lower = 'a';

	
	for(i = 0; i < strlen(p); i++)
	{
		//check if part of the alphabet.
		if(isalpha(p[i]))
		{
			if(islower(p[i]))
			{
				printf("%c", ((p[i] - lower + k) % 26) + lower);
			}
			if(isupper(p[i]))
			{	
				printf("%c", ((p[i] - upper + k) % 26) + upper);
			}
		}
		//if it is not part of the alphabet print the character.
		else
		{	
			printf("%c", p[i]);
		}
		

		
	}
	


	return 0;
		
}
