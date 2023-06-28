#Create Log file
log = open("log_coarse.txt","w")

timeout = False
counterexample = True

for p in range(1,5):

    log.write("==========================================================\n")
    log.writelines(["                          FOR PROPERTY ",str(p),"                  \n"])
    log.write("==========================================================\n\n")
    log.write("Network \t Execution Time \t Counterexample\n")
    log.write("----------------------------------------------------------\n")

    for i in range(1,6):
        for j in range(1,10):
            strng = "Property" + str(p) + "/" + str(i) + "_" + str(j)
            with open(strng+'/Exec_time.txt') as file:
                log.writelines([str(i),"_",str(j)])
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
#                                 print(strng+'/Exec_time.txt')
                                 counterexample = False
                        if counterexample==False:
                            log.writelines(["\t \t ",temp.split(' ')[5]," sec \t \t \t none found \n"])
                        else:
                            log.writelines(["\t \t ",temp.split(' ')[5]," sec \t \t \t EXISTS \n"])

                timeout = False
                counterexample = True

    log.write("\n\n")


log.close()
