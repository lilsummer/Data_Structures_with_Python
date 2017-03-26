import sys

class Stack:
	"""docstring for ClassName"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


#from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	## handle error here if there is A. not spaced
	if len(tokenList) <= 1:
		print("Error: infix expr is too short")
		#sys.exit()

	### handle error here if there is B. parentehese not paired
	parent = Stack()
	for token in tokenList:
		if token == '(':
			parent.push(token)
		elif token == ')':
			parent.pop()
	if parent.size() != 0:
		print("Error: parentethesis does not match")
		#sys.exit()

	## handle error here if there is C. not in the numeric operation list
	char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numericList = "0123456789"
	operList = "+-*/()"
	allList = (char + numericList + operList)
	for token in tokenList:
		if not token in allList:
			print("Error: illegal token")
			#sys.exit()

	for token in tokenList:
	#if not token in allList:
	#	print("infix has illegal character")
		if token in char or token in numericList:
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and \
			   (prec[opStack.peek()] >= prec[token]):
				  postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("( ( ( A + B ) * C "))
print(infixToPostfix("A"))
print(infixToPostfix("& &"))
