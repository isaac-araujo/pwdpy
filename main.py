import string
import random
def generate(quantity=1, length=8, punctuation=True, digits=True, letters=True,
            l_upper=True, l_lower=True, charset="", **kwargs):
    """ Generate a random password.

    Args:
        length (int, optional): _description_. Defaults to 8.
        punctuation (bool, optional): _description_. Defaults to True.
        digits (bool, optional): _description_. Defaults to True.
        letters (bool, optional): _description_. Defaults to True.
        l_upper (bool, optional): _description_. Defaults to True.
        l_lower (bool, optional): _description_. Defaults to True.
        
    """
    if quantity < 1:
        raise ValueError("Quantity must be greater than zero")
    if length < 1:
        raise ValueError("Length must be greater than zero") 
    if not punctuation and not digits and not letters:
        raise ValueError("At least one that argument must be True (punctuation, digits, letters)")
    
    if not charset:
        if punctuation:
            charset += string.punctuation
        if digits:
            charset += string.digits
        if letters:
            if l_upper:
                charset += string.ascii_uppercase 
            if l_lower:
                charset += string.ascii_lowercase 
    
    password_list = []
    for _ in range(quantity):
        password = []
        for _ in range(length):
            password.append(random.choice(charset))
        random.shuffle(password)
        password_list.append("".join(password))
        
    if quantity > 1:
        return password_list
    else:
        return password

    
