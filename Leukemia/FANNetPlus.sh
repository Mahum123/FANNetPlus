#!/bin/bash

for m in {1..20}
do 
    dir="basis"
    n=$((2*$m))
    echo " "
    echo "==========================================="
    echo "               FOR "$n"% NOISE               "
    echo "==========================================="
    echo " "
    echo " "

    for r in {0..31} 
    do
        echo "---Working on Input r:="$r"..."

        #create dirctory
        strng=$n"-percent/r"$r
        mkdir -p ${strng}
        cp ${dir}/commands.txt ${strng}
        cp ${dir}/main.cpp ${strng}
        cp ${dir}/nuXmv_linux64 ${strng}
                                   
        #write smv file
        python ${dir}/WriteSMV.py ${dir}/network.smv $r $n ${strng}/network.smv
                 
        #run nuXmv
        cd ${strng}
        g++ --std=c++0x -pthread main.cpp
        ./a.out > Exec_time.txt

        #remove everthing except results
        rm a.out
        rm commands.txt
        rm main.cpp
        rm nuXmv_linux64

        cd ../../

    done
    python ${dir}/Log.py $n
done

python smv2csv.py 


