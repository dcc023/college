/****************************************************
 * <XXXX>
 * <XXXX>
 * <Easy List>
 *
 * <a simple, short program/class description>
 ****************************************************/

#include <iostream>
using namespace std;

const int MAX_SIZE = 30;

class List
{
        private:
                int end;                // the index of the last valid item in the list
                int curr;               // the index of the current item in the list
                int list[MAX_SIZE];     // the list

        public:
                // constructor
                // remember that an empty list has a "size" of -1 and its "position" is at -1
                List()
                {
                        end = -1;
                        curr = -1;
                }

                // copy constructor
                // clones the list l and sets the last element as the current
                List(const List& l)
                {
                        *this = l; //To see what WAS in here, go to the operator= method.This constructor makes a copy. *this, remember.
                }

                // copy constructor
                // clones the list l and sets the last element as the current
                void operator=(const List& l)
                {
                        end = -1;
                        curr = -1;

                        for(int i=0; i<l.GetSize(); i++)
                        {
                                InsertAfter(l.list[i]);
                        }

                }

                // navigates to the beginning of the list
                void First()
                {
                        if(!IsEmpty())
                        {
                                curr = 0;
                        }
                }

                // navigates to the end of the list
                // the end of the list is at the last valid item in the list
                void Last()
                {
                        curr = end;
                }

                // navigates to the specified element (0-index)
                // this should not be possible for an empty list
                // this should not be possible for invalid positions
                void SetPos(int pos)
                {
                        if(!IsEmpty() && pos >= 0 && pos <= end)
                        {
                                curr = pos;
                        }
                }

                // navigates to the previous element
                // this should not be possible for an empty list
                // there should be no wrap-around
                void Prev()
                {
                        if(!IsEmpty())
                        {
                                if(curr > 0)
                                {
                                        curr--;
                                }
                        }

                }

                // navigates to the next element
                // this should not be possible for an empty list
                // there should be no wrap-around
                void Next()
                {
                        if(!IsEmpty() && curr < end)
                        {
                                curr++;
                        }
                }

                // returns the location of the current element (or -1) -1 IS FOR EMPTY LIST.
                int GetPos()
                {
                        return curr;
                }

                // returns the value of the current element (or -1)
                int GetValue()
                {
                        if (IsEmpty())
                        {
                                return -1;
                        }
                        else
                        {
                                return list[curr];
                        }
                }

                // returns the size of the list
                // size does not imply capacity
                int GetSize() const
                {
                        return (end + 1);
                }

                // inserts an item before the current element
                // the new element becomes the current
                // this should not be possible for a full list
                void InsertBefore(int data)
                {
                        if(!IsFull())
                        {
                                if(IsEmpty())
                                {
                                        curr++;
                                        list[curr] = data;
                                        end++;
                                }
                                else
                                {
                                        for (int i=end; i>=curr; i--)
                                        {
                                                list[i+1] = list[i];
                                        }
                                        list[curr] = data;
                                        end++;
                                }
                        }
                }

                // inserts an item after the current element
                // the new element becomes the current
                // this should not be possible for a full list
                void InsertAfter(int data)
                {
                        if (!IsFull())
                        {
                                if(IsEmpty())
                                {
                                        InsertBefore(data);
                                }
                                else
                                {
                                        if(curr == end)
                                        {
                                                curr++;
                                                list[curr] = data;
                                                end++;
                                        }
                                        else
                                        {
                                                curr++;
                                                InsertBefore(data);
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
                                if(curr == end)
                                {
                                        curr--;
                                        end--;
                                }
                                else
                                {
                                        for(int i=curr; i<end; i++)
                                        {
                                                list[i] = list[i+1];
                                        }
                                        end--;
                                }
                        }
                }

                // replaces the value of the current element with the specified value
                // this should not be possible for an empty list
                void Replace(int data)
                {
                        if(!IsEmpty())
                        {
                                list[curr]=data;
                        }
                }

                // returns if the list is empty
                bool IsEmpty() const
                {
                        return(end == -1);
                }

                // returns if the list is full
                bool IsFull()
                {
                        return (GetSize() == MAX_SIZE);
                }

                // returns the concatenation of two lists
                // l should not be modified
                // l should be concatenated to the end of *this
                // the returned list should not exceed MAX_SIZE elements
                // the last element of the new list is the current
                List operator+(const List& l) const
                {
                        List RetLis(*this);
                        RetLis.Last();
                        for(int i=0; i<l.GetSize(); i++)
                        {
                                RetLis.InsertAfter(l.list[i]);
                                if(RetLis.IsFull())
                                {
                                        i=l.GetSize();
                                }
                        }
                        return RetLis;
                }

                // returns if two lists are equal (by value)
                bool operator==(const List& l) const
                {
                        if(GetSize() != l.GetSize())
                        {
                                return false;
                        }
                        else
                        {
                                for(int i=0; i<GetSize(); i++)
                                {
                                        if(list[i] != l.list[i])
                                        {
                                                return false;
                                        }
                                }

                                return true;
                        }
                }

                // returns if two lists are not equal (by value)
                bool operator!=(const List& l) const
                {
                        return !(*this == l);
                }

                // returns a string representation of the entire list (e.g., 1 2 3 4 5)
                // the string "NULL" should be returned for an empty list
                friend ostream& operator<<(ostream& out, const List &l)
                {
                        if(l.IsEmpty())
                        {
                                out << "NULL";
                        }
                        else
                        {
                                for (int i=0; i < l.GetSize(); i++)
                                {
                                        out << l.list[i] << " ";
                                }
                        }
                        return out;
                }
};
