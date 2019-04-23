k=input("enter number of row of matrix1:")
l=input("enter number of row of matrix1:")
m=input("enter number of row of matrix2:")
n=input("enter number of row of matrix2:")
if(l!=m):
	print"we cannot do matrix multiplication"
else:
	A=[[0,0,0],[0,0,0]]
	B=[[0,0],[0,0],[0,0]]
	s=[[0,0],[0,0]]
	for i in range(0,k):
		A[i]=input("enter matrix1 row in list form")
	for j in range(0,m):
		B[j]=input("enter matrix2 row in list form")
	for i in range(0,len(A)):
		print A[i]
	for j in range(0,len(B)):
		print B[j]
	for p in range(len(A)):
		for q in range(len(B[0])):
			for r in range(len(B)):
				s[p][q] +=A[p][r]*B[r][q]
for x in range(0,len(s)):
		print s[x]

