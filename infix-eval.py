# Implement a direct infix evaluator that combines the functionality of infix-to-postfix conversion and the postfix evaluation algorithm. Your evaluator should process infix tokens from left to right and use two stacks, one for operators and one for operands, to perform the evaluation.

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

def infixEval(expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numericList = "0123456789"
	operList = "+-*/()"
	tokenList = expr.split()
	postfixList = []
	## build stacks
	allList = (char + numericList + operList)
	opStack = Stack()
	oprStack = Stack()

	for token in tokenList:
		if token in numericList:
			postfixList.append(token)
			oprStack.push(int(token))
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			# if there s matched (), then pop it
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			# when current operator precedes the token, append the current operator
			while (not opStack.isEmpty()) and \
			   (prec[opStack.peek()] >= prec[token]):
				  postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	for token in postfixList[::-1]:
		if token in operList:
			opStack.push(token)
	
	while opStack.size() > 0:
		operator1 = opStack.pop()
		print(str(operator1))
		oprnd2 = oprStack.pop()
		print(str(oprnd2))
		oprnd1 = oprStack.pop()
		print(str(oprnd1))
		result = doMath(oprnd1, oprnd2, operator1)
		oprStack.push(int(result))
	return(oprStack.pop())

def	doMath(oprnd1, oprnd2, operator1):
	if operator1 == "+":
		return (int(oprnd1 + oprnd2))
	elif operator1 == "-":
		return (int(oprnd1 - oprnd2))
	elif operator1 == "*":
		return (int(oprnd1 * oprnd2))
	else:
		return (int(oprnd1 / oprnd2))

print(infixEval('3 + ( 4 * 7 )'))