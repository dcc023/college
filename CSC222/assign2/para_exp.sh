#!/bin/sh
foo=fred
echo $foo

unset foo
echo ${foo:-bar}

foo=fud
echo ${foo:-bar}
