"""para definir configuración transversal que pueden ser usados 
en las diferentes pruebas unitarias.

todas las pruebas unitarias normalmente se hacen con funciones y asserts
"""
import pytest
from sistema_monitoreo_Apollo_11.utilities import FilenameGenerator, FileHandler
from sistema_monitoreo_Apollo_11.utilities import ReportGeneration, FileContentGeneration



@pytest.fixture(scope="session")
def app(request):

    class App:
        pass
    app = App()
    app.filename_generator = FilenameGenerator
    app.file_handler = FileHandler
    app.report_generation = ReportGeneration
    app.file_content_generation = FileContentGeneration
    
    return app