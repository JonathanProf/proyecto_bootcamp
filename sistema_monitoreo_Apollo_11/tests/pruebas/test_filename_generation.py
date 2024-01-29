from sistema_monitoreo_Apollo_11.utilities.FilenameGenerator import FilenameGenerator

def test_filename_generation(app):
    fg = FilenameGenerator("abc")

    assert fg.filename_generator("mission") != "APLmission-00000001.log"