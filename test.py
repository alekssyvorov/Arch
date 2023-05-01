def check_login(login):
    import string
    flag = False
    if len(login) > 5:
        for s in login:
            if s in string.ascii_letters:
                flag = True
            else:
                flag = False
                break
    return flag

login = "qWerty"
print(check_login(login))