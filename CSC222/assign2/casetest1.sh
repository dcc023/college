#!/bin/sh
echo "Is it morning? Please answer yes or no"
read timeofday
case "$timeofday" in
  yes) echo "Good Morning";;
  y)   echo "Good Morning";;
  no)  echo "Good Afternoon";;
  n)   echo "Good Afternoon";;
  * )  echo "Sorry, answer not recognized";;
esac
exit 0

