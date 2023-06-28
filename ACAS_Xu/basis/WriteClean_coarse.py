import sys
import os

p = sys.argv[1] #property
#i = sys.argv[2]
#j = sys.argv[3]

#Create Log file
log = open("Property"+p+".txt","w")

timeout = False
counterexample = True

log.write("================================================================================================\n")
log.writelines(["                                        FOR PROPERTY ",str(p),"                  \n"])
log.write("================================================================================================\n\n")
log.write("Network \t Input Node \t Bin Combination \t Execution Time \t Counterexample\n")
log.write("----------------------------------------------------------------------------------------------\n\n")

for i in range(1,6):
    for j in range(1,10):
        for k in range(1,2):#forall input nodes
            strng = "Property" + str(p) + "/" + str(i) + "_" + str(j) 
            with open(strng+'/Exec_time.txt') as file:
                log.writelines([str(i),"_",str(j)," \t \t ",str(k)," \t \t "])
                for line in file:
                    temp = line
                    if "Timeout reached" in line: #execution was terminated - no couterexample possible
                        timeout = True
                
                if timeout==True:
                    log.write("\t \t TIMEOUT \t \t \t - \n")
                else:
                    #check if counterexample exists in output.txt
                    with open(strng+'/Output.txt') as outputfile:
                        for line in outputfile:
                            if "-- no counterexample found with bound 2" in line:
                                counterexample = False

                        if counterexample==False:
                            log.writelines(["\t \t ",temp.split(' ')[5]," sec    \t \t \t none found \n"])
                        else:
                            log.writelines(["\t \t ",temp.split(' ')[5]," sec    \t \t \t EXISTS \n"])

                timeout = False
                counterexample = True

        log.write("\n\n")

log.close()

