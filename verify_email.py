import requests
def verify_email(emailadd):
    check=True
    email_address = emailadd
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address})

    status = response.json()['status']
    if status == "valid":
        check=True
    elif status == "invalid":
        check=False
    else:
        check=False
    return check