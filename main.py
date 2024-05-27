from rsa import Rsa
from auth_form import Form
from database import Database

def main():

  # initialize the implemented class
  rsa = Rsa()
  form = Form()
  db = Database()

  # display the public key and the private key
  # of the authentication system
  print(f"##################################################")
  print(f"")
  print(f"RSA Algorithm")
  print(f"")
  print(f"Public Key:  {rsa.public_key}")
  print(f"Private Key: {rsa.private_key}")
  print(f"")
  print(f"##################################################")

  while True:

    event, values = form.default_page.read()

    # close command
    if event == form.sg.WIN_CLOSED:
      break

    # if the button 'Sign in' was clicked,
    # the system check whether the given
    # username and password are correct or not
    if event == "Sign in" or event == "\r":

      # get username and encrypted password
      # as a payload from the form
      payload = form.get_payload(rsa.encrypt)

      # check whether the given username
      # and password are correct or note
      if db.sign_in(payload, rsa.decrypt):
        username = payload["username"]
        form.popup(f"Hi {username}!")
      else:
        form.popup("Invalid username or password.")

      print(f"")

  form.default_page.close()

if __name__ == "__main__":
  main()