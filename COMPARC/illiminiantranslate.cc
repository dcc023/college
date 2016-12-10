#include <iostream>
#include <string>
using namespace std;

int main()
{


	//Defined Goals:
	/*Create a translator capable of taking a string 
	of characters as input and translating the chars by 1, 
	depending of whether it is a vowel or consonant
	*/

	//Defined way of implimentation:
	/*
	1)Take in an array of chars as input. For example: "E. X. A."
	2)Run through each char and translate based on whether or not it
	is a consonant or vowel
	3)Output result
	*/

	//Local Variables
	string input; //Holds the input of chars as a variable


	//Retrieve line as input
	//Interate through each character of the input
	getline(cin,input);
		

	for(int i = 0; i != input.length();i++)
	{
		//cout << input.length() << endl;
		char c = input[i];//Store char of input as a variable
		char o;//Output

		//Check whether the character is a constant or a vowel

		//Vowels
		if(c == 'a')
		{
			cout << 'e';
		}
		else if(c == 'e')
		{
			cout << 'i';

		}
		else if(c == 'i')
		{
			cout << 'o';

		}
		else if(c == 'o')
		{
			cout << 'u';
	
		}
		else if(c == 'u')
		{
			cout << 'a';

		}
		
		//Spaces
		else if (c == ' ')
		{
			cout << ' ';	
			
		}

		//Consonants
		else if (c == 'z')//Skip a
		{
			cout << 'b';
		}
		else if (c == 'd')//Skip e
		{
			cout << 'f';
		}
		else if (c == 'h')//Skip i
		{
			cout << 'j';
		}
		else if (c == 'n')//Skip o
		{
			cout << 'p';
		}
		else if (c == 't')//Skip u
		{
			cout << 'v';
		}
		//Rest of the consonants
		else
		{
			o = c + 1;
			cout << o;
		}
		
	
	}
	cout << endl;
	
}
