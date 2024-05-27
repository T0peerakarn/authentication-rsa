class Database:

  # initailize the database
  def __init__(self):
    """
      you can add your own username and password
      in the below dictionary in the format of

      [username]: [password]

      note that the username is case sensitive
    """

    self.db = {
      "test": "1234"
    }

  def sign_in(self, payload, decrypt_function):
    """
      a function to check whether the given payload,
      consist of username and encrypted password,
      is correct or not given the decrypt function
      from RSA algorithm with the private key
    """

    username = payload["username"]
    encrypted_password = payload["password"]

    decrypted_password = "".join([chr(decrypt_function(x)) for x in encrypted_password])

    # display the server side information
    # including the username, encrypted password,
    # and decrypted password
    print(f"##################################################")
    print(f"")
    print(f"Server Side")
    print(f"")
    print(f"username:           {username}")
    print(f"encrypted password: {encrypted_password}")
    print(f"decrypted password: {decrypted_password}")
    print(f"")
    print(f"##################################################")
    
    return username in self.db and self.db[username] == decrypted_password
    

  