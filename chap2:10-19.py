#10 readlines
def kadai10(file):
    file = open(file)
    line_no = len(file.readlines())
    file.close()
    return line_no

#11 tab to space
def kadai11(file):
    file = open(file)
    f_read = file.read()
    f_read = f_read.replace('\t',' ')
    print f_read
    file.close()

#12 cut and write colunm
def kadai12(file_src, file_dest, col_no):
    file_src = open(file_src)
    file = file_src.readlines()
    file_dest = open(file_dest, 'w')

    for line in file:
        file_dest.write('%s \n' % line.split()[col_no])

    file_src.close()
    file_dest.close()

#13 join 2 files's colunm copy the spectified colunm in source file to spectified colunm in destination file
def kadai13(file_src, src_col, file_dest, dest_col):
    file_src = open(file_src)
    file_scr_read = file_src.readlines()
    file_dest1 = open(file_dest, 'r')
    file_dest_read = file_dest1.readlines()     #read destination file
    colunm = []

    for line in file_scr_read:                  #read source colunm
        colunm.append(line.split()[src_col])

    i=0
    file_dest2 = open(file_dest, 'w')
    for line in file_dest_read:
        a = line.split()                        #make a copy of each line
        a[dest_col] = colunm[i]                 #replace the corret colunm of that line
        i+=1
        file_dest2.write('\t'.join(a) + '\n')

    file_src.close()
    file_dest1.close()
    file_dest2.close()

#14 read n lines from the beginning
def kadai14(file, N):
    file = open(file)
    lines = file.readlines()
    for line in lines[:N]:
        print line

#15 read n lines from the ending
def kadai15(file, N):
    file = open(file)
    lines = file.readlines()
    for line in lines[len(lines):len(lines)-N-1:-1]:
        print line

#16 split a file in to many files
def kadai16(file, N):
    file = open(file)
    lines = file.readlines()
    print len(lines)

    if N <= 0:
        for i in xrange(len(lines)-1,1,-1):
            if len(lines)%i == 0:
                break
        no_of_files = i
        no_of_lines = int(len(lines)/no_of_files)
    else:
        no_of_files = N
        no_of_lines = len(lines)%N
        if len(lines)%N != 0:
            no_of_lines +=1

    for i in xrange(0,no_of_files,1):
        file_dest = open('/home/viet/Documents/split no%s.txt' % str(i+1), 'w')
        file_dest.writelines(lines[i*no_of_lines:(i+1)*no_of_lines])
        file_dest.close()

#17
def kadai17(file):
    pref = set()

    with open(file) as txt:
        line = txt.readline()
        while line:
            pref.add(line.split()[0])
            line = txt.readline()

    for pref in prefectures:
        print(pref)

#18 sorting
def kadai18(file):
    txt = open(file)
    lines = txt.readlines()
    for line in sorted(lines, key=lambda meow: meow.split()[2], reverse=True):
        print line
    txt.close()

#19 sorting
def kadai19(file, n):
    f = open(file)

    colfreq = {}
    for line in f:
        line = line.rstrip()
        cols = line.split()
        val = cols[n-1]
        if colfreq.has_key(val):
            colfreq[val] += 1
        else:
            colfreq[val] = 1
    f.close()

    keys = sorted(colfreq.keys(), key=lambda x:colfreq[x], reverse=True)
    for v in keys:
        print '%s %s' % (colfreq[v], v)

# main
def main():
    file_source = ('/home/viet/Documents/hightemp.txt')
    #file_dest1 = ('/home/viet/Documents/col1.txt')
    #file_dest2 = ('/home/viet/Documents/col2.txt')
    print kadai10(file_source)


if __name__ == '__main__':
    main()
