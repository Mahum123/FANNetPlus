#!/bin/bash

dir="basis"
for p in {1..4}
do
    for i in {1..5}
    do
        for j in {1..9}
        do
            echo "Property: "$p",  Network: "$i"_"$j

            strng="Property"${p}"/"$i"_"$j
            mkdir -p ${strng}
            cp ${dir}/commands.txt ${strng}
            cp ${dir}/main_coarse.cpp ${strng}
            cp ${dir}/nuXmv_linux64 ${strng}

            python property/prop${p}.py network/ACASXU_experimental_v2a_${i}_${j}.nnet
            cp network/ACASXU_experimental_v2a_${i}_${j}.smv Property${p}/${i}_${j}/network.smv
            rm network/ACASXU_experimental_v2a_${i}_${j}.smv

            cd Property${p}/${i}_${j}
            g++ --std=c++0x -pthread main_coarse.cpp
            ./a.out > Exec_time.txt
            rm a.out
            rm commands.txt
            rm main_coarse.cpp
            rm nuXmv_linux64
            rm network.smv
            cd ../../
        done
    done
done

python basis/Log_coarse.py
