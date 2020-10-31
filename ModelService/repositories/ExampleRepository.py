from CrudRepository import CrudRepository


class ExampleRepository(CrudRepository):
	def __init__(self, model):
		super().__init__(model)
