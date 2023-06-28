import sys

#Creating Output SMV file
old = open(sys.argv[1], "r")    #ARG 1: original network.smv file
new = open(sys.argv[4], "w")	#ARG 4: new network.smv file
r = int(sys.argv[2])            #ARG 2: input for which network.smv is rewritten
n = sys.argv[3]                 #ARG 3: noise level

#Write new smv file, editting only value of r and property
for i, line in enumerate(old):
    if "--input pointer" in line:
        new.writelines(["r := ", str(r), ";\n"])

    elif "LTLSPEC" in line:
        new.write("LTLSPEC G X ((Label_n = ")
        if r <= 20:
            new.write(str(0))
        else:
            new.write(str(1))
        new.write(") | e) | F ( ")
        for x in range(1,11):
            if x==10:
                new.writelines(["((x", str(x), " < -", str(n), ") | (x", str(x), " > ", str(n), ")) )"])
            elif x==4:
                new.writelines(["((x", str(x), " < -", str(n), ") | (x", str(x), " > ", str(n), ")) | "])
            elif x==5:
                new.writelines(["((x", str(x), " < -", str(n), ") | (x", str(x), " > ", str(n), ")) | "])
            elif x==8:
                new.writelines(["((x", str(x), " < -", str(n), ") | (x", str(x), " > ", str(n), ")) | "])
            else:
                pass

    else:
        new.write(line)

new.close()
old.close()


