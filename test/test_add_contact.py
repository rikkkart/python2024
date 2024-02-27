import pytest
from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("jfvjk", "dfvwfv", "vsdfvw",
                                        "vsfv", "vfvebertb","bebergb",
                                        "fbeb", "beregr", "ebegrber",
                                        "begbe", "oiwjtgijrt",
                                        "gbtbthh", "hrth", "hrhr", "thth",
                                        "11", "September",
                                        "2000", "12", "June", "2004"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("", "", "", "", "",
                        "", "", "", "", "", "",
                     "", "", "", "", "-", "-",
                    "", "-", "-", ""))
    app.session.logout()


