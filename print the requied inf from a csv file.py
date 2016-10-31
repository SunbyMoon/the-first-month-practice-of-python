#!/usr/bin/python
import csv
  
def myread():
    with open("/haplox/users/liuming/S018_cfdna_snv-target-GB18030.csv", "r") as csvfile:
        #reader = csv.reader(csvfile)
   
        #for row in reader:
            #print row
         reader = csv.DictReader(csvfile)
        for row in reader:
            #print (row)
            #print row['cosmic']
            print row.values()[0]+ ',' + row.values()[4]
  
    csvfile.close()
 
 if __name__ == '__main__':
      myread()
