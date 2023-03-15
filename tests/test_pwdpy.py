import pwdpy


def test_generate():
    try:
        passwords = pwdpy.generate(
        quantity=10, length=16, punctuation=True, digits=True, letters=True
    )
    except Exception:
        assert False, "error on generate method"
    
    assert len(passwords) == 10, "wrong amount of passwords"
    for pwd in passwords:
        p = False
        d = False
        l = False

        assert len(pwd) == 16, f"wrong password length: {pwd}"

        for char in pwd:
            if char in pwdpy.strings.digits:
                d = True
            if char in pwdpy.strings.punctuation:
                p = True
            if char in pwdpy.strings.ascii_letters:
                l = True

        assert d == True, f"no digits in password: {pwd}"
        assert p == True, f"no punctuation in password: {pwd}"
        assert l == True, f"no ascii_letters in password: {pwd}"


def test_entropy():
    assert pwdpy.entropy("Isaac") == 28.5
    assert pwdpy.entropy("5M{dl0U,8/4T2'1.V.B") == 124.54
