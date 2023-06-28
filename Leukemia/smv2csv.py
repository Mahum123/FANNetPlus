import os

#READING COUNTEREXAMPLES INTO AN ARRAY
#======================================

array_of_all_counterexamples = []
for i in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]: #range(19,20): #for all noise percentage folders
    noise = str(i) + "-percent/"
#    noise = str(2*i) + "-percent/"

#If number of inputs is varying/unknow, use this block
#    n = 0
#    for folders in os.listdir(noise):
#        n = n + 1	#number of folders in noise (= number of inputs)


#Otherwise, define number of correctly classified input as n here
    n = 32

    for j in range(0,n):
        if os.path.isfile(noise+"r"+str(j)+"/network.smv"):
            with open(noise+"r"+str(j)+"/network.smv","r") as file:
                for line in file:
                    if "e :=" in line:
                        array_of_all_counterexamples.append(line.split(' | '))

#print(array_of_all_counterexamples[28][0])
#print(len(array_of_all_counterexamples[28])) #==n
#print(len(array_of_all_counterexamples[28][1].split(" & ")))

#ARRANGING COUNTEREXAMPLES
#=========================

#Split each counterexample into individual integers
temp = []
for i in range(0,len(array_of_all_counterexamples)):
    for j in range(0,len(array_of_all_counterexamples[i][1:])):
        if len(array_of_all_counterexamples[i][j].split(" & ")) == 4:
            temp.append(array_of_all_counterexamples[i][j].split(" & "))

arrayOfCounterexamples = temp #because size of temp and arrayOfCounterexamples are same
for i in range(len(temp)):
    for j in range(5): #number of input features=5
        arrayOfCounterexamples[i][j] = int(temp[i][j].split(" = ")[1])
#print(arrayOfCounterexamples)

#COUNTEREXAMPLES ACCCORDING TO MAX NOISE LEVEL
#==============================================
noise1 = []
noise2 = []
noise3 = []
noise4 = []
noise5 = []
noise6 = []
noise7 = []
noise8 = []
noise9 = []
noise10 = []
noise11 = []
noise12 = []
noise13 = []
noise14 = []
noise15 = []
noise16 = []
noise17 = []
noise18 = []
noise19 = []
noise20 = []
noise21 = []
noise22 = []
noise23 = []
noise24 = []
noise25 = []
noise26 = []
noise27 = []
noise28 = []
noise29 = []
noise30 = []
noise31 = []
noise32 = []
noise33 = []
noise34 = []
noise35 = []
noise36 = []
noise37 = []
noise38 = []
noise39 = []
noise40 = []

##print(max(max(arrayOfCounterexamples[0]),abs(min(arrayOfCounterexamples[0]))))
##max of the absolute values in a list to identify noise vector to write list in

for i in range (len(arrayOfCounterexamples)):
    if max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==1:
        noise1.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==2:
        noise2.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==3:
        noise3.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==4:
        noise4.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==5:
        noise5.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==6:
        noise6.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==7:
        noise7.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==8:
        noise8.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==9:
        noise9.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==10:
        noise10.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==11:
        noise11.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==12:
        noise12.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==13:
        noise13.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==14:
        noise14.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==15:
        noise15.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==16:
        noise16.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==17:
        noise17.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==18:
        noise18.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==19:
        noise19.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==20:
        noise20.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==21:
        noise21.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==22:
        noise22.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==23:
        noise23.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==24:
        noise24.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==25:
        noise25.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==26:
        noise26.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==27:
        noise27.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==28:
        noise28.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==29:
        noise29.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==30:
        noise30.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==31:
        noise31.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==32:
        noise32.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==33:
        noise33.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==34:
        noise34.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==35:
        noise35.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==36:
        noise36.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==37:
        noise37.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==38:
        noise39.append(arrayOfCounterexamples[i])
    elif max(max(arrayOfCounterexamples[i]),abs(min(arrayOfCounterexamples[i])))==39:
        noise39.append(arrayOfCounterexamples[i])
    else:
        noise40.append(arrayOfCounterexamples[i])
        
        
#WRITING CSV
#============
noise = open('Noise.csv', "w")

noiseCompleteSet = []
noiseCompleteSet.extend(noise1)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise2)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise3)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise4)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise5)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise6)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise7)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise8)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise9)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise10)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise11)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise12)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise13)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise14)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise15)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise16)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise17)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise18)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise19)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise20)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise21)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise22)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise23)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise24)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise25)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise26)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise27)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise28)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise29)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise30)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise31)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise32)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise33)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise34)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise35)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise36)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise37)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise38)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise39)
noiseCompleteSet.extend([0])
noiseCompleteSet.extend(noise40)

#print(len(noiseCompleteSet))
for i in range(1,len(noiseCompleteSet)):
    if noiseCompleteSet[i-1]==0:
        noise.write("0, 0, 0, 0, 0,\n")
    else:
        noise.writelines([str(noiseCompleteSet[i-1][0]),", ",str(noiseCompleteSet[i-1][1]),", ",str(noiseCompleteSet[i-1][2]),", ",str(noiseCompleteSet[i-1][3]),", ",str(noiseCompleteSet[i-1][4]), ",\n"])

noise.close()
