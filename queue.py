class queue:
	def __init__(self,l):
		self.l=l
		
	def insert(self,i=None, priority=None, p_index=None):
		if priority:
			if p_index==None:
				p_index=0
			self.l.insert(p_index, priority)
			self.front=priority
		elif i:
			self.l.append(i)
			self.rear=i

	def get(self):
		a = self.l.pop(0)
		self.front=self.l[0]
		return a

	def pop(self,index=None, value=None):
		if index:
			r=self.l.pop(index)
		elif value:
			r=self.l.pop(self.l.index(value))
		return r
		
	def print_q(self):
		p_q=[]
		for i in self.l:
			p_q.append(str(i))
		print(" <-- ".join(p_q))
		return self.l
		
	def reverse(self):
		l_hold=[]
		for i in range(len(self.l)-1, -1,-1):
			l_hold.append(self.l[i])
		self.l=l_hold
		return self.l
		
	def __repr__(self):
		return str(self.l)

l=[1,2,3,4]
a = queue(l)
