
import array

# mengonversi string ke dalam array.array

B = array.array('b')
B.fromstring("Python")
print(B)

for karakter in B:
    print("%c" % karakter, end='')