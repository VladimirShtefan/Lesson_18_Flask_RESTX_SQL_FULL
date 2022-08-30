from flask import g


def test_app(app, database):
    with app.test_client().get('/'):
        assert getattr(g, 'session') == database.session

