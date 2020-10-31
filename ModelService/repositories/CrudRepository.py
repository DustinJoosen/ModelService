class CrudRepository:

	def __init__(self, model):
		self.model = model

	def GetAll(self):
		return self.model.objects.all()

	def GetById(self, Id):
		return self.model.objects.get(pk=Id)

	def Create(self, Dto):
		model = self.model()
		model.Update(Dto)
		model.save()

	def Update(self, Id, Dto):
		dbModel = self.GetById(Id)
		dbModel.Update(Dto)
		dbModel.save()

	def Delete(self, Id):
		self.GetById(Id).delete()
