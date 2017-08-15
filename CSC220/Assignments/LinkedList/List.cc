/****************************************************
 * Dylan Campbell
 * 10-18-2015
 * List.cc
 ****************************************************/

#include <iostream>
using namespace std;

const int MAX_SIZE = 30;

class List
{
private:
    // list node definition
    struct Node
    {
        int data;
        Node *link;
    };

    Node *head;	// the head of the list
    Node *tail;	// the tail of the list
    Node *curr;	// the current position in the list
    int num_items;	// the number of items in the list

public:
    // constructor
    // remember that an empty list has a "size" of -1 and its "position" is at -1
    List()
    {
        head = tail = curr = NULL;
        num_items = 0;
    }

    // copy constructor
    // clones the list l and sets the last element as the current
    List(const List& l)
    {
        *this = l;
    }

    // copy constructor
    // clones the list l and sets the last element as the current
    void operator=(const List& l)
    {
        num_items = l.num_items;
        Node *n = l.head;
        head = new Node;
        head->data = n->data;
        head->link = NULL;
        curr = tail = head;

        for(int i = 1; i < l.GetSize(); i++)
        {
            n = n->link;
            curr->link = new Node;
            curr->link->data = n->data;
            curr->link->link = NULL;
            curr = curr->link;
            tail = curr;
        }
    }

    // navigates to the beginning of the list
    void First()
    {
        curr = head;
    }

    // navigates to the end of the list
    // the end of the list is at the last valid item in the list
    void Last()
    {
        curr = tail;
    }

    // navigates to the specified element (0-index)
    // this should not be possible for an empty list
    // this should not be possible for invalid positions
    void SetPos(int pos)
    {
        if(!IsEmpty() && pos >= 0 && pos < GetSize())
        {
            Node *n = head;
            while(pos > 0)
            {
                n = n->link;
                pos--;
            }
            curr = n;
        }
    }

    // navigates to the previous element
    // this should not be possible for an empty list
    // there should be no wrap-around
    void Prev()
    {
        if(!IsEmpty() && curr != head)
        {
            Node *n = head;
            while(n->link != curr)
            {
                n = n->link;
            }
            curr = n;
        }
    }

    // navigates to the next element
    // this should not be possible for an empty list
    // there should be no wrap-around
    void Next()
    {
        if(!IsEmpty() && curr != tail)
        {
            curr = curr->link;
        }
    }

    // returns the location of the current element (or -1)
    int GetPos()
    {
        if(IsEmpty())
        {
            return -1;
        }
        else
        {
            int pos = 0;//Position to record
            Node *n = head;
            while(n != curr)
            {
                n = n->link;
                pos++;//Keep track of position until reaching curr;
            }
            return pos;
        }

    }

    // returns the value of the current element (or -1)
    int GetValue()
    {
        if(!(num_items == 0))
        {
            return curr->data;
        }
        else
        {
            return -1;
        }
    }

    // returns the size of the list
    // size does not imply capacity
    int GetSize() const
    {
        return num_items;
    }

    // inserts an item before the current element
    // the new element becomes the current
    // this should not be possible for a full list
    void InsertBefore(int data)
    {
        if(!IsFull())
        {
            Node *n = new Node;
            n->data = data;
            n->link = NULL;
            if(IsEmpty())
            {
                head = n;
                tail = n;
                curr = n;
                num_items++;
            }
            else
            {
                if(curr == head)
                {
                    n->link = head;
                    head = n;
                    curr = n;
                    num_items++;

                }
                else
                {
                    Prev();
                    InsertAfter(data);
                }
            }
        }
    }

    // inserts an item after the current element
    // the new element becomes the current
    // this should not be possible for a full list
    void InsertAfter(int data)
    {
        if(!IsFull())
        {
            Node *n = new Node;
            n->data = data;
            n->link = NULL;
            if(IsEmpty())
            {
                head = n;
                tail = n;
                curr = n;
                num_items++;
            }
            else
            {
                if(curr == tail)
                {
                    curr->link = n;
                    tail = n;
                    curr = n;
                    num_items++;
                }
                else
                {
                    n->link = curr->link;
                    curr->link = n;
                    curr = n;
                    num_items++;
                }
            }
        }
    }

    // removes the current element (collapsing the list)
    // this should not be possible for an empty list
    void Remove()
    {
        if(!IsEmpty())
        {
            if(curr == head)
            {
                head = head->link;
                delete curr;
                curr = head;
                if(tail == NULL)
                {
                    tail = head;
                }
            }
            else
            {
                Node *n = curr;
                Prev();
                curr->link = n->link;
                if(tail == n)
                    tail = curr;
                Next();
                delete n;

            }
            num_items--;

        }
    }

    // replaces the value of the current element with the specified value
    // this should not be possible for an empty list
    void Replace(int data)
    {
        if(!IsEmpty())
        {
            curr->data = data;
        }
    }

    // returns if the list is empty
    bool IsEmpty() const
    {
        return(num_items == 0);
    }

    // returns if the list is full
    bool IsFull() const
    {
        return (num_items == MAX_SIZE);
    }

    // returns the concatenation of two lists
    // l should not be modified
    // l should be concatenated to the end of *this
    // the returned list should not exceed MAX_SIZE elements
    // the last element of the new list is the current
    List operator+(const List& l) const
    {
        if(head == NULL)
        {
            //If empty return l
            List newList = l;
            return newList;
        }
        else
        {
            //If l is empty return this
            //If both aren't empty return the concatenation.
            List newList = *this;
            if(l.head != NULL)
            {
                Node *n = l.head;
                //Traverse l and InsertAfter into current list
                while(n != NULL)
                {
                    newList.InsertAfter(n->data);
                    n = n->link;
                }
            }
            return newList;
        }

    }

    // returns if two lists are equal (by value)
    bool operator==(const List& l) const
    {
        if(num_items != l.num_items)
            return false;
        Node *n = head;
        Node *m = l.head;
        while(n != NULL)
        {
            if(n->data != m->data)
                return false;
            n = n->link;
            m = m->link;
        }
        return true;
    }

    // returns if two lists are not equal (by value)
    bool operator!=(const List& l) const
    {
        return (*this == l);
    }

    // returns a string representation of the entire list (e.g., 1 2 3 4 5)
    // the string "NULL" should be returned for an empty list
    friend ostream& operator<<(ostream& out, const List &l)
    {
        if(l.num_items == 0)
        {
            out << "Null";
        }
        else
        {
            Node *n = l.head;
            while(n != NULL)
            {
                out << n->data << " ";
                n = n->link;
            }

        }
        return out;
    }
};
