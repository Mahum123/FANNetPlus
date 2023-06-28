#!/bin/bash

count=0
bin1=9
bin2=9
bin3=9
bin4=9
bin5=9

dir="basis"

echo " "
echo "==========================================="
echo "               PROPERTY 1                  "
echo "==========================================="
echo " "
echo " "

p=1
for i in {1..5} #for all networks
do
    for j in {1..9}
    do
        echo "============NETWORK: "$i"_"$j"============"
        for k in {1..5}
        do
         
            echo "---Working on Input Node: "$k"..."
            #For node1 as the variable input node
            if [ $k -eq 1 ]
            then
                for bin2 in {1..4}
                do
                    for bin3 in {1..4}
                    do
                        for bin4 in {1..2}
                        do
                            for bin5 in {1..2}
                            do
                                #create dirctory
                                strng="Logs/Property"$p"/Experiment1/"$i"_"$j"/node"$k"/"$count
                                mkdir -p ${strng}
                                cp ${dir}/commands.txt ${strng}
                                cp ${dir}/main_ris.cpp ${strng}
                                cp ${dir}/nuXmv_linux64 ${strng}
                                   
                                #write smv file
                                ((a=bin1-1))
                                ((b=bin2-1))
                                ((c=bin3-1))
                                ((d=bin4-1))
                                ((e=bin5-1))
                                python property/prop${p}.py network/ACASXU_experimental_v2a_${i}_${j}.nnet ${k} ${a} ${b} ${c} ${d} ${e}
                                cp network/ACASXU_experimental_v2a_${i}_${j}.smv ${strng}/network.smv
                                rm network/ACASXU_experimental_v2a_${i}_${j}.smv
                        
                                #run nuXmv
                                cd ${strng}
                                g++ --std=c++0x -pthread main_ris.cpp
                                ./a.out > Exec_time.txt

                                #remove everthing except results
                                rm a.out
                                rm commands.txt
                                rm main_ris.cpp
                                rm nuXmv_linux64
                                rm network.smv
                                cd ../../../../../../
                                    
                                ((count=count+1))
                            done
                        torun="python basis/Log_ris.py 1 "$i" "$j
                        value=$(eval "$torun")
                        if [ "$value" = "COUNTEREXAMPLE FOUND..." ]
                        then break 3
                        fi
                        done
                    done
                done
                count=0
                
            #For node2 as the variable input node
            elif [ $k -eq 2 ]
            then
                for bin1 in {1..3}
                do
                    for bin3 in {1..4}
                    do
                        for bin4 in {1..2}
                        do
                            for bin5 in {1..2}
                            do
                                #create dirctory
                                strng="Logs/Property"$p"/Experiment1/"$i"_"$j"/node"$k"/"$count
                                mkdir -p ${strng}
                                cp ${dir}/commands.txt ${strng}
                                cp ${dir}/main_ris.cpp ${strng}
                                cp ${dir}/nuXmv_linux64 ${strng}
                                    
                                #write smv file
                                ((a=bin1-1))
                                ((b=bin2-1))
                                ((c=bin3-1))
                                ((d=bin4-1))
                                ((e=bin5-1))
                                python property/prop${p}.py network/ACASXU_experimental_v2a_${i}_${j}.nnet ${k} ${a} ${b} ${c} ${d} ${e}
                                cp network/ACASXU_experimental_v2a_${i}_${j}.smv ${strng}/network.smv
                                rm network/ACASXU_experimental_v2a_${i}_${j}.smv
                      
                                #run nuXmv
                                cd ${strng}
                                g++ --std=c++0x -pthread main_ris.cpp
                                ./a.out > Exec_time.txt

                                #remove everthing except results
                                rm a.out
                                rm commands.txt
                                rm main_ris.cpp
                                rm nuXmv_linux64
                                rm network.smv
                                cd ../../../../../../
                                    
                                ((count=count+1))
                            done
                        torun="python basis/Log_ris.py 1 "$i" "$j
                        value=$(eval "$torun")
                        if [ "$value" = "COUNTEREXAMPLE FOUND..." ]
                        then break 3
                        fi
                        done
                    done
                done
                count=0
                
            #For node3 as the variable input node
            elif [ $k -eq 3 ]
            then
                for bin1 in {1..3}
                do
                    for bin2 in {1..4}
                    do
                        for bin4 in {1..2}
                        do
                            for bin5 in {1..2}
                            do
                                #create dirctory
                                strng="Logs/Property"$p"/Experiment1/"$i"_"$j"/node"$k"/"$count
                                mkdir -p ${strng}
                                cp ${dir}/commands.txt ${strng}
                                cp ${dir}/main_ris.cpp ${strng}
                                cp ${dir}/nuXmv_linux64 ${strng}
                                    
                                #write smv file
                                ((a=bin1-1))
                                ((b=bin2-1))
                                ((c=bin3-1))
                                ((d=bin4-1))
                                ((e=bin5-1))
                                python property/prop${p}.py network/ACASXU_experimental_v2a_${i}_${j}.nnet ${k} ${a} ${b} ${c} ${d} ${e}
                                cp network/ACASXU_experimental_v2a_${i}_${j}.smv ${strng}/network.smv
                                rm network/ACASXU_experimental_v2a_${i}_${j}.smv
                         
                                #run nuXmv
                                cd ${strng}
                                g++ --std=c++0x -pthread main_ris.cpp
                                ./a.out > Exec_time.txt

                                #remove everthing except results
                                rm a.out
                                rm commands.txt
                                rm main_ris.cpp
                                rm nuXmv_linux64
                                rm network.smv
                                cd ../../../../../../
                                    
                                ((count=count+1))
                            done
                        torun="python basis/Log_ris.py 1 "$i" "$j
                        value=$(eval "$torun")
                        if [ "$value" = "COUNTEREXAMPLE FOUND..." ]
                        then break 3
                        fi
                        done
                    done
                done
                count=0

            #For node4 as the variable input node
            elif [ $k -eq 4 ]
            then
                for bin1 in {1..3}
                do
                    for bin2 in {1..4}
                    do
                        for bin3 in {1..4}
                        do
                            for bin5 in {1..2}
                            do
                                #create dirctory
                                strng="Logs/Property"$p"/Experiment1/"$i"_"$j"/node"$k"/"$count
                                mkdir -p ${strng}
                                cp ${dir}/commands.txt ${strng}
                                cp ${dir}/main_ris.cpp ${strng}
                                cp ${dir}/nuXmv_linux64 ${strng}
                                 
                                #write smv file
                                ((a=bin1-1))
                                ((b=bin2-1))
                                ((c=bin3-1))
                                ((d=bin4-1))
                                ((e=bin5-1))
                                python property/prop${p}.py network/ACASXU_experimental_v2a_${i}_${j}.nnet ${k} ${a} ${b} ${c} ${d} ${e}
                                cp network/ACASXU_experimental_v2a_${i}_${j}.smv ${strng}/network.smv
                                rm network/ACASXU_experimental_v2a_${i}_${j}.smv
                         
                                #run nuXmv
                                cd ${strng}
                                g++ --std=c++0x -pthread main_ris.cpp
                                ./a.out > Exec_time.txt

                                #remove everthing except results
                                rm a.out
                                rm commands.txt
                                rm main_ris.cpp
                                rm nuXmv_linux64
                                rm network.smv
                                cd ../../../../../../
                                    
                                ((count=count+1))
                            done
                        torun="python basis/Log_ris.py 1 "$i" "$j
                        value=$(eval "$torun")
                        if [ "$value" = "COUNTEREXAMPLE FOUND..." ]
                        then break 3
                        fi
                        done
                    done
                done
                count=0
                    
            #For node5 as the variable input node
            else
                for bin1 in {1..3}
                do
                    for bin2 in {1..4}
                    do
                        for bin4 in {1..4}
                        do
                            for bin5 in {1..2}
                            do
                                #create dirctory
                                strng="Logs/Property"$p"/Experiment1/"$i"_"$j"/node"$k"/"$count
                                mkdir -p ${strng}
                                cp ${dir}/commands.txt ${strng}
                                cp ${dir}/main_ris.cpp ${strng}
                                cp ${dir}/nuXmv_linux64 ${strng}
                                   
                                #write smv file
                                ((a=bin1-1))
                                ((b=bin2-1))
                                ((c=bin3-1))
                                ((d=bin4-1))
                                ((e=bin5-1))
                                python property/prop${p}.py network/ACASXU_experimental_v2a_${i}_${j}.nnet ${k} ${a} ${b} ${c} ${d} ${e}
                                cp network/ACASXU_experimental_v2a_${i}_${j}.smv ${strng}/network.smv
                                rm network/ACASXU_experimental_v2a_${i}_${j}.smv
                        
                                #run nuXmv
                                cd ${strng}
                                g++ --std=c++0x -pthread main_ris.cpp
                                ./a.out > Exec_time.txt

                                #remove everthing except results
                                rm a.out
                                rm commands.txt
                                rm main_ris.cpp
                                rm nuXmv_linux64
                                rm network.smv
                                cd ../../../../../../
                                    
                                ((count=count+1))
                            done
                        torun="python basis/Log_ris.py 1 "$i" "$j
                        value=$(eval "$torun")
                        if [ "$value" = "COUNTEREXAMPLE FOUND..." ]
                        then break 3
                        fi
                        done
                    done
                done
                count=0
            fi
        done
    done
done

