
class MyObject():
	"""docstring for MyObject"""
	def __init__(self, name):
		super(MyObject).__init__()
		self.name = name
	
	def say_name(self):
		return self.name

print("Hi Friends");

obj = MyObject("Object #1");

print(  obj.say_name()  )

