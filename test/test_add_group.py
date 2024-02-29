from model.group import Group



def test_add_group(app):
    app.group.create(Group("uhhio", "oij;j", "jjoijio"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))



