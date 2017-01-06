class Employees:
	"""docstring for Employees"""
	def __init__(self, name, title, start_date):
		self.name = name
		self.title = title
		self.start_date = start_date

	def getName(self):
		return self.name

	def getTitle(self):
		return self.title

	def getStartDate(self):
		return self.start_date

employee1 = Employees("Mary Brown", "Purchaser", "010717")

print(employee1.title)

print(Employees.getName(employee1) + " is the " + Employees.getTitle(employee1) + " at our company.")