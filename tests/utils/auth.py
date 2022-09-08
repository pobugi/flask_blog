from base64 import b64encode


def basic_auth_str(username="test_user", password="test_password"):
    return "Basic " + b64encode(("%s:%s" % (username, password)).encode("latin1")).strip().decode("latin1")


auth_header = {"Authorization": basic_auth_str()}
