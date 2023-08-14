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


def test_strengthen():
    for _ in range(10):
        password = pwdpy.generate(
            length=12, punctuation=False, digits=True, letters=True
        )
        stronger_password = pwdpy.strengthen(password, increase=True)

        assert len(stronger_password) > len(password), "lenght did not changed"

        entropy_normal = pwdpy.entropy(password)
        entropy_stronger = pwdpy.entropy(stronger_password)

        assert (
            entropy_stronger > entropy_normal
        ), f"normal = {password} | stronger = {stronger_password}"

# TODO: implement test
def generate_wordlist():
    password = pwdpy.generate_wordlist(quantity=20, language="portuguese", case="upper")
