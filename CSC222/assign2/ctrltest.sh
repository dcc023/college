#!/bin/sh
echo "Is it morning? Please answer yes or no"
read timeofday
if test $timeofday = "yes" ; then
  echo "Good morning"
else
  echo "Good afternoon"
fi
exit 0


Is it morning? Please answer yes or no
yes
Good morning

