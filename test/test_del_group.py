__author__ = 'Sergei'


def test_test_del_first_group(app):
    app.session.login(username= "admin",password="secret")
    app.group.del_first_group()
    app.session.logout()

