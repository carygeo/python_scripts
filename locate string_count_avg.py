# Use the file name mbox-short.txt as the file name
# fname = raw_input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     print line
# print "Done"

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
    
except:
    print 'File cannot be opened:', fname
    exit()
    
count = 0
spam = 0
locval = 0
    
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    count = count + 1
	
    col = line.find('0')
    val = float(line[col:100])
    
    locval = locval + val
    
    spam_avg = locval/float(count)

print "Average spam confidence:", spam_avg