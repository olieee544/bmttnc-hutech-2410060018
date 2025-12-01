from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# Khởi tạo đối tượng CaesarCipher
caesar_cipher = CaesarCipher()

# API mã hóa Caesar Cipher
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu phải có plain_text và key'}), 400
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

# API giải mã Caesar Cipher
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Yêu cầu phải có cipher_text và key'}), 400
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    # POSTリクエストからキーを取得
    data = request.json
    key = data['key']
    # Playfair行列を作成
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    # POSTリクエストからプレーンテキストとキーを取得
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    # Playfair行列を作成して暗号化
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    # POSTリクエストから暗号文とキーを取得
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    # Playfair行列を作成して復号化
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})
# Hàm main để chạy Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)