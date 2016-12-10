#include <stdio.h>
#include <string.h>

int main()
{
	char input[20];//Buffer of 20 characters to be the input
	char key[20] = "ohyeahharderdaddy";//key to xor
	char output[20]; //Buffer of characters to be the output
	int i;

	fgets(input,20,stdin); //Get input of 20 characters from the command line.
	input[strlen(input)-1] = '\0';
	
	
	
	for(i = 0; i < strlen(input); i++)
	{
		output[i] = input[i]^key[i];
		printf("%c",output[i]);
		
		
		
	}
	

	
}
