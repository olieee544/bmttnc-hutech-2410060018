from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher page
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Encryption route
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    # Hiển thị kết quả trên cùng trang caesar.html
    return render_template(
        'caesar.html',
        result=encrypted_text
    )

# Decryption route
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    # Hiển thị kết quả trên cùng trang caesar.html
    return render_template(
        'caesar.html',
        result_decrypt=decrypted_text
    )

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)