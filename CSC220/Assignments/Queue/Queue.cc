Dylan Campbell

#include <iostream>
#include "GenericList.cc"

using namespace std;

template <class q_type>
class Queue
{
	private:
	List<q_type> list;

	public:
	Queue() //constructor
	{
		
	}
	Queue(const Queue& q)//Copy constructor
	{
		*this = q;
	}
	bool operator=(const Queue& q)//Copy constructor to overide '='
	{
		list = q.list;
	}
	q_type Enqueue(q_type data) //Add item to front of the Queue
	{
		list.Last();
		list.InsertAfter(data);
	}
	q_type Dequeue() //Return item at top of Queue and remove it
	{
		q_type front = Peek();

		list.Remove();

		return front;
	}
	q_type Peek() //Return item at top of Queue
	{
		list.First();
		return list.GetValue();
	}
	int Size() //Get size of Queue
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
	Queue operator+(const Queue& q) //returns concatenation of two Queues
	{
		Queue newQueue = *this;
		newQueue.list = newQueue.list + q.list;
		return newQueue;
	}
	bool operator==(const Queue& q) //returns if 2 Queues are equivalent
	{
		return (list == q.list);
	}
	bool operator!=(const Queue& q) //returns if 2 Queues are not equivalent
	{
		return!(*this == q);
	}


	friend ostream& operator<<(ostream& out, const Queue& q)//outputs list
	{
		out << q.list;

		return out;
	}

};
