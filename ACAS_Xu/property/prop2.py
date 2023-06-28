import random
import sys
import array

###############################INITIALIZE EMPTY ARRAYS FOR NETWORK PARAMETERS

w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
w6 = []
w7 = []
b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []
b7 = []

############################################################################
###############################OPENING NNET FILE AND CREATING EMPTY SMV FILE

#print(sys.argv[1][:-4]) #remove last 3 characters of input string i.e., extension removed
nnet = open(sys.argv[1], "r")
smv = open(sys.argv[1][:-5]+".smv","w")

############################################################################
#########################READING AND STORING NETWORK PARAMETERS IN VARIABLES

for i, line in enumerate(nnet):
#Hidden Layer 1
    if i in range(10,60):
        w1.append(line[:-2])
    if i in range(60,110):
        b1.append(float(line[:-2]))
        
#Hidden Layer 2
    if i in range(110,160):
        w2.append(line[:-2])
    if i in range(160,210):
        b2.append(float(line[:-2]))
        
#Hidden Layer 3
    if i in range(210,260):
        w3.append(line[:-2])
    if i in range(260,310):
        b3.append(float(line[:-2]))
        
#Hidden Layer 4
    if i in range(310,360):
        w4.append(line[:-2])
    if i in range(360,410):
        b4.append(float(line[:-2]))
        
#Hidden Layer 5
    if i in range(410,460):
        w5.append(line[:-2])
    if i in range(460,510):
        b5.append(float(line[:-2]))
        
#Hidden Layer 6
    if i in range(510,560):
        w6.append(line[:-2])
    if i in range(560,610):
        b6.append(float(line[:-2]))
        
#Output Layer
    if i in range(610,615):
        w7.append(line[:-2]) #removing \n and , at the end of the string
    if i in range(615,620):
        b7.append(float(line[:-2]))

#Changing string weight arrays to float weight arrays
rows = len(w1) #number of rows in matrix
columns = len(w1[0].split(",")) #number of columns in matrix
for row in range(rows):
    w1[row] = w1[row].split(",")
    for column in range(columns):
        w1[row][column] = float(w1[row][column])

rows = len(w2) #number of rows in matrix
columns = len(w2[0].split(",")) #number of columns in matrix
for row in range(rows):
    w2[row] = w2[row].split(",")
    for column in range(columns):
        w2[row][column] = float(w2[row][column])
        
rows = len(w3) #number of rows in matrix
columns = len(w3[0].split(",")) #number of columns in matrix
for row in range(rows):
    w3[row] = w3[row].split(",")
    for column in range(columns):
        w3[row][column] = float(w3[row][column])
        
rows = len(w4) #number of rows in matrix
columns = len(w4[0].split(",")) #number of columns in matrix
for row in range(rows):
    w4[row] = w4[row].split(",")
    for column in range(columns):
        w4[row][column] = float(w4[row][column])
        
rows = len(w5) #number of rows in matrix
columns = len(w5[0].split(",")) #number of columns in matrix
for row in range(rows):
    w5[row] = w5[row].split(",")
    for column in range(columns):
        w5[row][column] = float(w5[row][column])

rows = len(w6) #number of rows in matrix
columns = len(w6[0].split(",")) #number of columns in matrix
for row in range(rows):
    w6[row] = w6[row].split(",")
    for column in range(columns):
        w6[row][column] = float(w6[row][column])
        
rows = len(w7) #number of rows in matrix
columns = len(w7[0].split(",")) #number of columns in matrix
for row in range(rows):
    w7[row] = w7[row].split(",")
    for column in range(columns):
        w7[row][column] = float(w7[row][column])
        
#print(len(w1),len(w1[0]))
#print(w7)
#print(b1)
############################################################################
##############################WRITING NETWORK ARCHITECTURE INTO THE SMV FILE

smv.write("--*************************************************************--\n")
smv.write("MODULE relu(i)\n \n")
smv.write("DEFINE\n")
smv.write("out := (i<0) ? 0 : i;\n")
smv.write("--*************************************************************--\n \n")

smv.write("MODULE main\n")
smv.write("VAR\n")
smv.write("i1_coarse : integer;\n")
smv.write("i2_coarse : integer;\n")
smv.write("i3_coarse : integer;\n")
smv.write("i4_coarse : integer;\n")
smv.write("i5_coarse : integer;\n")
smv.write("flg : {0,1};\n \n")

##writing network equations

smv.write("--**Instantiating ReLU activation neurons in 1st Hidden Layer**--\n \n")
for i in range(50):
    smv.writelines(["n1_",str(i+1)," : relu("])
    for j in range(5):
        smv.writelines(["i",str(j+1)," * w1_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b1_",str(i+1),");\n \n"])

smv.write("--**Instantiating ReLU activation neurons in 2nd Hidden Layer**--\n \n")
for i in range(50):
    smv.writelines(["n2_",str(i+1)," : relu("])
    for j in range(50):
        smv.writelines(["n1_",str(j+1),".out * w2_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b2_",str(i+1),");\n \n"])

smv.write("--**Instantiating ReLU activation neurons in 3rd Hidden Layer**--\n \n")
for i in range(50):
    smv.writelines(["n3_",str(i+1)," : relu("])
    for j in range(50):
        smv.writelines(["n2_",str(j+1),".out * w3_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b3_",str(i+1),");\n \n"])

smv.write("--**Instantiating ReLU activation neurons in 4th Hidden Layer**--\n \n")
for i in range(50):
    smv.writelines(["n4_",str(i+1)," : relu("])
    for j in range(50):
        smv.writelines(["n3_",str(j+1),".out * w4_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b4_",str(i+1),");\n \n"])

smv.write("--**Instantiating ReLU activation neurons in 5th Hidden Layer**--\n \n")
for i in range(50):
    smv.writelines(["n5_",str(i+1)," : relu("])
    for j in range(50):
        smv.writelines(["n4_",str(j+1),".out * w5_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b5_",str(i+1),");\n \n"])

smv.write("--**Instantiating ReLU activation neurons in 6th Hidden Layer**--\n \n")
for i in range(50):
    smv.writelines(["n6_",str(i+1)," : relu("])
    for j in range(50):
        smv.writelines(["n5_",str(j+1),".out * w6_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b6_",str(i+1),");\n \n"])


smv.write("--**********************ASSIGN BLOCK**************************--\n \n")
smv.write("--For property 2 i.e. o1_raw is not maximal\n")
smv.write("ASSIGN\n")
smv.write("    init (flg) := {0,1};\n")
smv.write("    next (flg) := ((o2_raw > o1_raw) | (o3_raw > o1_raw) | (o4_raw > o1_raw) | (o5_raw > o1_raw)) ? 0 : 1;\n\n")


smv.write("--**********************DEFINE BLOCK**************************--\n \n")
smv.write("DEFINE\n \n")
smv.write("--Normalization \n")
smv.write("mean_x1 := 19791.091;\n")
smv.write("mean_x2 := 0.0;\n")
smv.write("mean_x3 := 0.0;\n")
smv.write("mean_x4 := 650.0;\n")
smv.write("mean_x5 := 600.0;\n")
smv.write("std_x1 := 60261.0;\n")
smv.write("std_x2 := 6.28318530718;\n")
smv.write("std_x3 := 6.28318530718;\n")
smv.write("std_x4 := 1100.0;\n")
smv.write("std_x5 := 1200.0;\n\n")

smv.write("i1_raw := i1_coarse * 10000;\n")
smv.write("i2_raw := i2_coarse;\n")
smv.write("i3_raw := i3_coarse;\n")
smv.write("i4_raw := i4_coarse * 500;\n")
smv.write("i5_raw := i5_coarse * 500;\n")
smv.write("i1 := (i1_raw - mean_x1) / std_x1;\n")
smv.write("i2 := (i2_raw - mean_x2) / std_x2;\n")
smv.write("i3 := (i3_raw - mean_x3) / std_x3;\n")
smv.write("i4 := (i4_raw - mean_x4) / std_x4;\n")
smv.write("i5 := (i5_raw - mean_x5) / std_x5;\n \n")

smv.write("--Clear-of-Conflict (o1), Weak Right (o2), Strong Right (o3), Weak Left (o4), Strong Left(o5)\n")
for i in range(5):
    smv.writelines(["o",str(i+1)," := "])
    for j in range(50):
        smv.writelines(["n6_",str(j+1),".out * w7_",str(i+1),"_",str(j+1)," + "])
    smv.writelines(["b7_",str(i+1),";\n \n"])

smv.write("mean_o := 7.5188840201005975;\n")
smv.write("std_o := 373.94992;\n")
smv.write("o1_raw := (o1 * std_o) + mean_o;\n")
smv.write("o2_raw := (o2 * std_o) + mean_o;\n")
smv.write("o3_raw := (o3 * std_o) + mean_o;\n")
smv.write("o4_raw := (o4 * std_o) + mean_o;\n")
smv.write("o5_raw := (o5 * std_o) + mean_o;\n \n")

##defining Input ranges

smv.write("i1_min := 0; \n")
smv.write("i1_max := 60760; \n")
smv.write("i2_min := -3.141593; \n")
smv.write("i2_max := 3.141593; \n")
smv.write("i3_min := -3.141593; \n")
smv.write("i3_max := 3.141593; \n")
smv.write("i4_min := 100; \n")
smv.write("i4_max := 1200; \n")
smv.write("i5_min := 0; \n")
smv.write("i5_max := 1200; \n \n")

##defining Weights and Biases

smv.write("--********************* Input to 1st Hidden LAYER WEIGHTS *********************--\n \n")
for i in range(50):
    for j in range(5):
        smv.writelines(["w1_",str(i+1),"_",str(j+1)," := ",str(w1[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")
smv.write("--********************** 1st to 2nd Hidden LAYER WEIGHTS **********************--\n \n")
for i in range(50):
    for j in range(50):
        smv.writelines(["w2_",str(i+1),"_",str(j+1)," := ",str(w2[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")
smv.write("--********************** 2nd to 3rd Hidden LAYER WEIGHTS **********************--\n \n")
for i in range(50):
    for j in range(50):
        smv.writelines(["w3_",str(i+1),"_",str(j+1)," := ",str(w3[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")
smv.write("--********************** 3rd to 4th Hidden LAYER WEIGHTS **********************--\n \n")
for i in range(50):
    for j in range(50):
        smv.writelines(["w4_",str(i+1),"_",str(j+1)," := ",str(w4[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")
smv.write("--********************** 4th to 5th Hidden LAYER WEIGHTS **********************--\n \n")
for i in range(50):
    for j in range(50):
        smv.writelines(["w5_",str(i+1),"_",str(j+1)," := ",str(w5[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")
smv.write("--********************** 5th to 6th Hidden LAYER WEIGHTS **********************--\n \n")
for i in range(50):
    for j in range(50):
        smv.writelines(["w6_",str(i+1),"_",str(j+1)," := ",str(w6[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")
smv.write("--******************** 6th Hidden to Output LAYER WEIGHTS *********************--\n \n")
for i in range(5):
    for j in range(50):
        smv.writelines(["w7_",str(i+1),"_",str(j+1)," := ",str(w7[i][j]),";\n"])
    smv.write("\n")
smv.write("\n")

smv.write("--************************** 1st Hidden LAYER BIASES ***************************--\n \n")
for i in range(50):
    smv.writelines(["b1_",str(i+1)," := ",str(b1[i]),";\n"])
smv.write("\n")
smv.write("--************************** 2nd Hidden LAYER BIASES ***************************--\n \n")
for i in range(50):
    smv.writelines(["b2_",str(i+1)," := ",str(b2[i]),";\n"])
smv.write("\n")
smv.write("--************************** 3rd Hidden LAYER BIASES ***************************--\n \n")
for i in range(50):
    smv.writelines(["b3_",str(i+1)," := ",str(b3[i]),";\n"])
smv.write("\n")
smv.write("--************************** 4th Hidden LAYER BIASES ***************************--\n \n")
for i in range(50):
    smv.writelines(["b4_",str(i+1)," := ",str(b4[i]),";\n"])
smv.write("\n")
smv.write("--************************** 5th Hidden LAYER BIASES ***************************--\n \n")
for i in range(50):
    smv.writelines(["b5_",str(i+1)," := ",str(b5[i]),";\n"])
smv.write("\n")
smv.write("--************************** 6th Hidden LAYER BIASES ***************************--\n \n")
for i in range(50):
    smv.writelines(["b6_",str(i+1)," := ",str(b6[i]),";\n"])
smv.write("\n")
smv.write("--***************************** Output LAYER BIASES *****************************--\n \n")
for i in range(5):
    smv.writelines(["b7_",str(i+1)," := ",str(b7[i]),";\n"])
smv.write("\n")

############################################################################
#################################################SAFETY PROPERTIES TO VERIFY

#Property as statement:
#   a = TRUE -> (X b = TRUE)
#Property to be verified by tool:
#   G(a) & FX(!b) & G(input-bounds-hold)
#Negation of property supplied:
#   F(!a) | GX(b) | F(!input-bounds-hold)

smv.write("--Property 2:\n")
smv.write("LTLSPEC G X ((i1_raw < 55947.691) | (i4_raw < 1145) | (i5_raw > 60) | (flg = 0)) | F ( ((i1_raw < i1_min) | (i1_raw > i1_max)) | ((i2_raw < i2_min) | (i2_raw > i2_max)) | ((i3_raw < i3_min) | (i3_raw > i3_max)) | ((i4_raw < i4_min) | (i4_raw > i4_max)) | ((i5_raw < i5_min) | (i5_raw > i5_max)) ) \n \n")


nnet.close()
smv.close()
