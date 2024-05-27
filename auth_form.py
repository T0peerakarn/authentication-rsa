import PySimpleGUI as sg

class Form:
  
  def __init__(self):

    # initialize UI for the authentication system
    default_layout = [
      [
        sg.Push()
      ],
      [
        sg.Text(
          "username",
          font="Courier 16"
        ),
        sg.InputText(
          key="-USERNAME-",
          font="Courier 16",
          size=(20)
        )
      ],
      [
        sg.Text(
          "password",
          font="Courier 16"
        ),
        sg.InputText(
          key="-PASSWORD-",
          password_char="*",
          font="Courier 16",
          size=(20)
        )
      ],
      [
        sg.Push()
      ],
      [
        sg.Push(),
        sg.Button(
          "Sign in",
          font="Courier 16"
        ),
        sg.Push(),
      ],
      [
        sg.Push()
      ]
    ]

    self.sg = sg

    self.default_page = sg.Window(
      "Authentication Form",
      default_layout
    )

  def popup(self, message):
    """
      a function to call a formatted popup
    """
    
    self.sg.popup(
      message,
      font="Courier 16",
    )
  
  def get_payload(self, encrypt_function):
    """
      a function to create a payload of username
      and encrypted password using RSA,
      then send it to check at the database
    """
    
    username = self.default_page["-USERNAME-"].get()
    password = self.default_page["-PASSWORD-"].get()

    encrypted_password = [encrypt_function(ord(x)) for x in password]

    # display the given information from client
    print(f"##################################################")
    print(f"")
    print(f"Client Side")
    print(f"")
    print(f"username:          {username}")
    print(f"plain password:    {password}")
    print(f"ciphered password: {encrypted_password}")
    print(f"")
    print(f"##################################################")
    
    return {
      "username": username,
      "password": encrypted_password
    }
