from anytree import Node, RenderTree
# ........................................................
abc = ["x", "b", "c", "d"]
print(abc[0])
print(abc[1])
print(abc[2])
print(abc[3])
abc[0] = "a"
len(abc)
# ..............................................
num = []

# append() function to push
# element in the stack
num.append('a')
num.append('b')
num.append('c')

print(num)

print(num.pop())
print(num.pop())
print(num.pop())

print('Stack after elements are popped:')
print(num)

# ..........................................................
# dict
ao = {
    'y':3,
    'z':int('y') ** 2,
    'a':(int('z') - int('y')),
    'b':(int('z') + int('y')),
    'c':(int('z')*int('y')),
    'd':(int('z') / int('y')),
}
print(ao)


# Declare a dictionary
aBz = {'Name': 'Taro', 'Age': 12, 'Class': '1-C', 'Results': '78'}

print("The name is," + aBz['Name'])
print("The age of" + aBz['Name'] + "is" + aBz['Age'])

# ..................................................................
# tree like data
a  = Node( "a" , parent=None )
b = Node( "b", parent=a )
c = Node( "c", parent=b )
d  = Node( "d",  parent=b )
e  = Node( "e",  parent=c )
f  = Node( "f",  parent=d )
g  = Node( "g",  parent=d )

for pre, fill, node in RenderTree(a):
    print("%s%s" % (pre, node.name))


for pre, fill, node in RenderTree(udo):
    print("%s%s" % (pre, node.name))
