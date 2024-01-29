
def test_hash_generator(app):
    filename = app.filename_generator("abc")

    assert filename.filename_generator == "abc"

    