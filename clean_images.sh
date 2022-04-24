#!/bin/bash

parent="../projectyl.github.io"
cd $parent
count=0
for file in $(ls _posts/); do
	echo $file
	grep ".*assets/images/.*" "_posts/$file"
done


