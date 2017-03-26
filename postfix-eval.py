# Modify the postfix evaluation algorithm so that it can handle errors.

## post fix evaluation
class Stack:
	"""docstring for ClassName"""
	def __init__(self):
		Stack.items = []

	def isEmpty(self):
		return len(Stack.items) == 0

	def push(self, item):
		Stack.items.append(item)

	def pop(self):
		return Stack.items.pop()

	def peek(self):
		return Stack.items[len(Stack.items) - 1]

	def size(self):
		return len(Stack.items)
		


def postfixEval(expr):
	numericList = "0123456789"
	operList = "+-*/"
	oprndStack = Stack()
	tokenList = expr.split()
	# handling error
	if len(tokenList) <= 1:
		print("Error: infix expr is too short")
	# handling error2
	char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numericList = "0123456789"
	operList = "+-*/()"
	allList = (char + numericList + operList)
	for token in tokenList:
		if not token in allList:
			print("Error: illegal token")

	# if it is number push to oprndStack, else do the math 
	for token in tokenList:
		if token in numericList:
			oprndStack.push(int(token))
		else:
			oprnd2 = oprndStack.pop()
			oprnd1 = oprndStack.pop()
			result = doMath(oprnd1, oprnd2, token)
			oprndStack.push(int(result))
	return oprndStack.pop()

def	doMath(oprnd1, oprnd2, operator1):
	if operator1 == "+":
		return (int(oprnd1 + oprnd2))
	elif operator1 == "-":
		return (int(oprnd1 + oprnd2))
	elif operator1 == "*":
		return (int(oprnd1 + oprnd2))
	else:
		return (int(oprnd1 + oprnd2))

print(postfixEval('7 8 +'))
print(postfixEval('7'))
print(postfixEval('7 & 8'))
#print(postfixEval('10 + 3 * 5 / (16 - 4)'))