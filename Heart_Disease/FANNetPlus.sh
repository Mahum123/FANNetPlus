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

    for r in {0..40} 
    do

        if [ $r -eq 1 ]
        then continue
        
        elif [ $r -eq 3 ]
        then continue

        elif [ $r -eq 13 ]
        then continue

        elif [ $r -eq 17 ]
        then continue

        elif [ $r -eq 26 ]
        then continue

        elif [ $r -eq 41 ]
        then continue

        else
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
        fi
    done
    python ${dir}/Log.py $n
done

python smv2csv.py 


