class CrudService:

	def __init__(self, repos):
		self.repos = repos

	def GetAll(self):
		return self.repos.GetAll()

	def GetById(self, Id):
		return self.repos.Get(Id)

	def Create(self, Dto):
		return self.repos.Create(Dto)

	def Update(self, Id, Dto):
		return self.repos.Update(Id, Dto)

	def Delete(self, Id):
		return self.repos.Delete(Id)
