fh =open('output8.txt','w')

a = [3, 2, 1.5, 5, 7, 6, 4, 3]

fh.write("Before Sorting " + '\n')
fh.write(str(a) + '\n')

fh.write("-----------------------------------" + '\n')
fh.write("After sorting" + '\n')
fh.write("Ascending " + '\n')
a.sort()
fh.write(str(a) + '\n')
fh.write("------------------------------------------------" + '\n')

fh.write("Descending" + '\n')
a.sort(reverse=True)
fh.write(str(a) + '\n')
fh.close
