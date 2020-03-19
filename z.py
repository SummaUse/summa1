class Graph(): 
	def __init__(self, vertices): 
		self.graph = [[0 for column in range(vertices)] 
							for row in range(vertices)] 
		self.V = vertices 

	def isSafe(self, v, pos, path): 
		if self.graph[ path[pos-1] ][v] == 0: 
			return False

		for vertex in path: 
			if vertex == v: 
				return False

		return True

	def hamCycleUtil(self, path, pos): 

		if pos == self.V: 
			if self.graph[ path[pos-1] ][ path[0] ] == 1: 
				return True
			else: 
				return False

		for v in range(1,self.V): 

			if self.isSafe(v, pos, path) == True: 

				path[pos] = v 

				if self.hamCycleUtil(path, pos+1) == True: 
					return True

				path[pos] = -1

		return False

	def hamCycle(self): 
		path = [-1] * self.V 

		path[0] = 0

		if (self.hamCycleUtil(path,1) == False) or (len(path) !=t): 
			print ("NO") 
			return False
 
		self.printSolution(path) 
		return True

	def printSolution(self, path): 
		print ("YES") 
		for vertex in path: 
			print (w[vertex], end = " ") 
		print (w[path[0]], " ") 


a=input()
a=a.split(" ")
n=int(a[0])
m=int(a[1])
t=int(a[2])
u=[]
v=[]

for i in range(m):
    b=input()
    b=b.split(" ")
    u.append(int(b[0]))
    v.append(int(b[1]))
w=sorted(list(set(u) | set(v)))

temp=[[0]*n]*n   
        
for i in range(m):
    j=w.index(u[i])
    k=w.index(v[i])
    temp[j][k]=1

g1 = Graph(n) 
g1.graph = temp

g1.hamCycle(); 
