from sistema_monitoreo_Apollo_11.utilities.FileContentGeneration import FileContentGenerator

def test_filecontent(app):
    fc = FileContentGenerator("filename","ColonyMoon", "080124225224","navigation system","killed")

    assert fc.get_content() != "080124225224,ColonyMoon,navigation system,killed,1652116879752302431"