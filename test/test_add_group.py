# -*- coding: utf-8 -*-

from model.group import Group

def test_test_empty_group(app):
    app.group.create(Group(name="",header="",footer=""))
    app.session.logout()

def test_test_add_group(app):
    app.group.create(Group(name="Groupe4",header="Groun",footer="groupe"))


