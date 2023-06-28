import sys
import os
import os.path

n = sys.argv[1] #noise level to check

timeout = False
counterexample = False
counter = 0 #number of correctly classified inputs

for r in range(0,40): #forall inputs
    strng = str(n) + "-percent/r" + str(r)

    if os.path.isfile(strng+"/Exec_time.txt"):
        with open(strng+"/Exec_time.txt","r") as file:
            for line in file:
                if "e :=" in line:
                    counterexample = True #counterexample exists
                    break
                if "Timeout reached" in line: #execution was terminated
                    timeout = True

        with open(strng+"/output.txt","r") as outputfile:
            for line in outputfile:
                if "-- no counterexample found with bound 2" not in line: #counterexample does not exist
                    counter = counter + 1

print("======================================================================")
if timeout==True:
    print("SMV terminated on some or all input instances.")

if counterexample==True or counter<34:
    print("Counterexample exists...Input noise beyond network's noise tolerance.")
else:
    print("Noise is within the tolerance bounds.")
print("======================================================================")
