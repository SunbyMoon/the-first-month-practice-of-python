#!/home/mingliu/anaconda2/bin/python
fp=open("/home/mingliu/Downloads/cfDNA.fastq","r")
fpw=open("/home/mingliu/Downloads/a.fastq","w")
i=1
for line in fp.readlines():
    if i%4==0:
        #print(line)
        #print map(ord, line)
        list1=map(ord, line)
        list2=[elem + 1 for elem in list1]
        list3=map(chr, list2)
        print ''.join(list3)
        fpw.write(''.join(list3))
        i+=1
    else:
        print line
        fpw.write(line)
        i+=1
fp.close()
fpw.close()