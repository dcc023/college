#!/bin/sh
foo=fred
echo {$foo:-bar}

unset foo
echo $foo

foo=fud
echo ${foo:-bar}

	
