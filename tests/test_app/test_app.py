from flask import g


def test_app(client, database):
    with client.get('/'):
        assert getattr(g, 'session') == database.session

