#!/bin/sh
foo() {
  echo "Function foo is executing"
  echo $1
  shift
}
echo "script starting"
foo 1 2 3 4
echo "script ended"
exit 0
