from model.contact import Contact

def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("test", "dfvwfv", "vsdfvw",
                                        "vsfv", "vfvebertb","bebergb",
                                        "fbeb", "beregr", "ebegrber",
                                        "begbe", "oiwjtgijrt",
                                        "gbtbthh", "hrth", "hrhr", "thth",
                                        "11", "September",
                                        "2000", "12", "June", "2004"))
    app.contact.delete_first_contact()

