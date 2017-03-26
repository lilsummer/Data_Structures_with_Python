# turning the previous program into a infix calculatr

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

def infixCalc(expr):
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
	## build stacks
	# opStack: operator stack
	# oprStack: operand stack
	# parenStack: temporart stack
	opStack = Stack()
	oprStack = Stack()
	parenStack = Stack()

	for token in tokenList:
		if token in numericList:
			oprStack.push(int(token))
		elif token == "(":
			parenStack.push(token)
		elif token == ")":
			topToken = parenStack.pop()
			while topToken != "(":
				#opStack.push(topToken)
				topToken = parenStack.pop()
		else:
			opStack.push(token)
			parenStack.push(token)
	#opStack.pop()
	#opStack.pop()
	while oprStack.size() > 1:
		operator1 = opStack.pop()
		oprnd2 = oprStack.pop()
		oprnd1 = oprStack.pop()
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




print(infixCalc('3 + ( 4 * 7 )'))