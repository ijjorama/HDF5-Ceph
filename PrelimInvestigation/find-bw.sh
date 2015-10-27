#!/bin/sh
i=$1


grep 10000  th-pt-${i}_001.out | while read val ; do echo  $i ${val} | awk -F ' ' '{ print $1, $NF}' ; done
