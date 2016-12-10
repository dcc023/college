//by: Dylan Campbell
//last_updated: 12/10/16 at 12:06am
//
// TASK 1: |A|r|r|a|y|s|
/*
	Q:	HOW ARE ARRAYS PASSED TO FUNCTIONS IN C++?
	----------------------------------------------
	A:	Arrays are passed in C++ as a pointer that points to the head of the array.
		So the user is required to calculate the array size before passing the array,
		then passing that size with the array.
		-> Look at function arraySize for more info.
	
	Q:	IS THERE A WAY TO PASS THEM BY VALUE?
	-----------------------------------------
	A:	You can indirectly pass the array by value by wrapping it in a struct. 
		Giving you the ability to still calculate the size of the array AFTER passing it.
		-> Look at function arraySizeVal for more info.
*/


#include <iostream>
#include <vector>
using namespace std;

struct nums{ int numbers[5]; }; //Pre-defining the struct that is wrapping our array we wish to pass for arraySizeVal.


void arraySize(int arr[], int size){ //For seeing how C++ handles the array naturally. Where they pass it as a pointer.

	int i = 0;
	int failsize = (sizeof(arr)/sizeof(arr[0])); //THIS FAILS TO GIVE THE FULL SIZE OF THE ARRAY!
	cout << "This is the size it calculates incorrectly: "<< failsize << endl;
	cout << "The proper size is: " << size << endl;
}

void arraySizeVal(struct nums arr){ //For seeing what happens when wrapping the array in a struct.

	cout << "This is the size it calculates when being passed within a struct: " << (sizeof(arr.numbers)/sizeof(arr.numbers[0])) << endl;
	cout << "That is the correct size!" << endl;
}
	

int main(){

	cout << "-----------------------------" << endl;
	cout << "DEFAULT ARRAY REFERENCE PASS: " << endl;
	cout << "-----------------------------" << endl;
	int numbers[5];
	arraySize(numbers, (sizeof(numbers)/sizeof(numbers[0]))); //Size must be calculated prior to passing the array to the function.

	cout << "-----------------------------------" << endl;
	cout << "INDIRECT VALUE PASS USING A STRUCT: " << endl;
	cout << "-----------------------------------" << endl;
	struct nums a;
	arraySizeVal(a); //Passing the struct.
}
