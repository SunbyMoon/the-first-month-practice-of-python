#!/home/mingliu/anaconda2/bin/python

filename= "/home/mingliu/Downloads/cfDNA.fastq"
filenameoutput="/home/mingliu/Downloads/a.fastq"
fp=open("/home/mingliu/Downloads/cfDNA.fastq","r")
fpw=open("/home/mingliu/Downloads/a.fastq","w")
i=1
for line in fp.readlines():
    if i%4==0:
        #print(line)
        #print map(ord, line)
        li =  [elem+1 for elem in (map(ord, line))]
        print ''.join(map(chr, li))
        #fpw.write(line)
        fpw.write(''.join(map(chr, li)))
        i+=1
    else:
        
        print line
        fpw.write(line)
        i+=1
##        print(line)
fp.close()
fpw.close()