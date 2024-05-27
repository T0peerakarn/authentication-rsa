# Authentication System Using RSA Algorithm

## Overview

This project demonstrates an authentication system utilizing the RSA algorithm to ensure secure communication between the client side and the server side. The system includes a form where users input their username and password. The password is encrypted using a generated public key before being sent to the server. The server then decrypts the received data using a private key to validate the credentials. The project consists of four main files:

1. `main.py`: The driver file that coordinates the interactions between the client-side form, the server-side database, and the RSA encryption/decryption functions.
2. `auth_form.py`: The client-side form where users input their username and password.
3. `database.py`: The server-side component that receives and decrypts the data to validate user credentials.
4. `rsa.py`: The implementation of the RSA algorithm, including functions to generate large prime numbers and check their primality using the Miller-Rabin test.

## Algorithm

### RSA Algorithm

1. **Key Generation**:
    - Generate two large prime numbers.
    - Calculate the modulus \( n = p \times q \).
    - Compute the totient \(\phi(n) = (p-1) \times (q-1)\).
    - Choose a public exponent \( e \) such that \( 1 < e < \phi(n) \) and \( \gcd(e, \phi(n)) = 1 \).
    - Determine the private exponent \( d \) such that \( d \times e \equiv 1 \mod \phi(n) \).

2. **Encryption**:
    - Convert the plaintext message to a number \( m \).
    - Compute the ciphertext \( c = m^e \mod n \).

3. **Decryption**:
    - Compute the plaintext message \( m = c^d \mod n \).

### Primality Testing

- Use the Miller-Rabin primality test to check if the generated large numbers are prime.

## Tools

- **Python**: The programming language used to implement the system.
- **PySimpleGUI**: A Python library used for creating the graphical user interface for the client-side form.

## Idea

The core idea of this project is to create a secure authentication system by leveraging the RSA encryption algorithm. The process involves the following steps:

1. **Client Side**:
    - A form is presented to the user for inputting their username and password.
    - The password is encrypted using the public key before being sent to the server.

2. **Server Side**:
    - The server receives the payload containing the username and encrypted password.
    - The server decrypts the password using the private key.
    - The server checks if the decrypted credentials match the stored user information.

By implementing this system, we ensure that user passwords are transmitted securely, reducing the risk of interception or unauthorized access.

## File Descriptions

1. **main.py**:
    - Acts as the driver file.
    - Imports and calls the form class (`auth_form.py`), database class (`database.py`), and RSA class (`rsa.py`).
    - Facilitates the transfer of payloads between the client and server.
    - Calls the encryption and decryption functions from `rsa.py`.

2. **auth_form.py**:
    - Provides the user interface for entering the username and password.
    - Returns a payload consisting of the username and the encrypted password.

3. **database.py**:
    - Receives the payload from the client.
    - Decrypts the password using the private key.
    - Validates the credentials against the stored user information.

4. **rsa.py**:
    - Implements the RSA algorithm.
    - Generates large prime numbers up to 512 bits.
    - Utilizes the Miller-Rabin test to check the primality of generated numbers.
