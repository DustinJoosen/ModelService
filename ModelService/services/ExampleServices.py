from CrudService import CrudService


class ExampleService(CrudService):
	def __init__(self):
		repos = ExampleRepository(ExampleModel)
		super().__init__(repos)
