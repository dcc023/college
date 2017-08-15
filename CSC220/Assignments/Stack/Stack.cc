Dylan Campbell

#include <iostream>
#include "GenericList.cc"

using namespace std;

template <class s_type>
class Stack
{
	private:
	List<s_type> list;

	public:
	Stack() //constructor
	{
		
	}
	Stack(const Stack& s)//Copy constructor
	{
		*this = s;
	}
	bool operator=(const Stack& s)//Copy constructor to overide '='
	{
		list = s.list;
	}
	void Push(s_type data) //Add item to top of the stack
	{
		list.First();
		list.InsertBefore(data);
	}
	s_type Pop() //Return item at top of stack and remove it
	{
		s_type top = Peek();

		list.Remove();

		return top;
	}
	s_type Peek() //Return item at top of stack
	{
		list.First();
		return list.GetValue();
	}
	int Size() //Get size of stack
	{
		return list.GetSize();
	}
	bool IsEmpty() //Return true if empty
	{
		return list.IsEmpty();
	}
	bool IsFull() //REturn true if full
	{
		return list.IsFull();
	}
	Stack operator+(const Stack& s) //returns concatenation of two stacks
	{
		Stack newStack = *this;
		newStack.list = newStack.list + s.list;
		return newStack;
	}
	bool operator==(const Stack& s) //returns if 2 stacks are equivalent
	{
		return (list == s.list);
	}
	bool operator!=(const Stack& s) //returns if 2 stacks are not equivalent
	{
		return!(*this == s);
	}


	friend ostream& operator<<(ostream& out, const Stack& s)//outputs list
	{
		out << s.list;

		return out;
	}

};
