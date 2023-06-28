import sys
import os

p = sys.argv[1] #property
i = sys.argv[2]
j = sys.argv[3]

#Create Log file
log = open("Logs/Summary-Property"+p+".txt","a+")

timeout = False
counterexample = True

log.write("================================================================================================\n")
log.writelines(["                                        FOR PROPERTY ",str(p),"                  \n"])
log.write("================================================================================================\n\n")
log.write("Network \t Input Node \t Bin Combination \t Execution Time \t Counterexample\n")
log.write("----------------------------------------------------------------------------------------------\n\n")

#for i in range(1,6):
#    for j in range(1,10):
for k in range(1,6):#forall input nodes
    strng = "Logs/Property" + str(p) + "/Experiment1/" + str(i) + "_" + str(j) + "/node" + str(k)
    node_count = 0
    for folders in os.listdir(strng):
        node_count = node_count + 1

    #print(k,node_count)
    for n in range(0,node_count):
        #print(n)
        with open(strng+'/'+str(n)+'/Exec_time.txt') as file:
            log.writelines([str(i),"_",str(j)," \t \t ",str(k)," \t \t ",str(n)])
            for line in file:
                temp = line
                if "Timeout reached" in line: #execution was terminated - no couterexample possible
                    timeout = True
                    
            if timeout==True:
                log.write("\t \t TIMEOUT \t \t \t - \n")
            else:
                #check if counterexample exists in output.txt
                with open(strng+'/'+str(n)+'/Output.txt') as outputfile:
                    for line in outputfile:
                         if "-- no counterexample found with bound 2" in line:
#                             print(strng+'/Exec_time.txt')
                             counterexample = False
                    if counterexample==False:
                        log.writelines(["\t \t ",temp.split(' ')[5]," sec    \t \t \t none found \n"])
                    else:
                        log.writelines(["\t \t ",temp.split(' ')[5]," sec    \t \t \t EXISTS \n"])
                        print("COUNTEREXAMPLE FOUND...")
                        sys.exit(0)
            timeout = False
            counterexample = True

    log.write("\n")

log.close()

