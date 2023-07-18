print("about: Multiline Statements")

a=[1,
2,		# can comment inbetween
3]
print(a)
b=[1, #comma before comment
	2]
c=[1 #comma after comment
	,2]
print(b,c)

# \ character for breaking up statements "line continuation character"
if len(a) <4 \
and a[2]==3:
	print(True)


print("multiline strings")
print(""" test
\t test
test
(doesn't strip newline character automatically)""")

# also works for functions
def my_func(a,
		b):
	print(a,b)

my_func(100
		, 200)
