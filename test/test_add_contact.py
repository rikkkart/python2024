import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("jfvjk", "dfvwfv", "vsdfvw",
                                        "vsfv", "vfvebertb","bebergb",
                                        "fbeb", "beregr", "ebegrber",
                                        "begbe", "oiwjtgijrt",
                                        "gbtbthh", "hrth", "hrhr", "thth",
                                        "11", "September",
                                        "2000", "12", "June", "2004"))
    app.logout()

def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("", "", "", "", "",
                        "", "", "", "", "", "",
                     "", "", "", "", "-", "-",
                    "", "-", "-", ""))
    app.logout()


