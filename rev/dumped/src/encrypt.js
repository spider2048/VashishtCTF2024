const crypto = require('crypto');

function generateIV() {
  return crypto.randomBytes(16);
}

function generateKey(keyLength) {
  return crypto.randomBytes(keyLength);
}

function encrypt(text, key, iv) {
  const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
  let encrypted = cipher.update(text, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}

function decrypt(encryptedText, key, iv) {
  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
  let decrypted = decipher.update(encryptedText, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

const key = generateKey(32);
const iv = generateIV();

console.log("KEY:", Array.from(key))
console.log("IV:", Array.from(iv))

const plaintext = 'SURGE{d92ff8be1435d85220aa3a444ecbec39}';
console.log('Plaintext:', plaintext);

const encryptedText = encrypt(plaintext, key, iv);
console.log('Encrypted:', encryptedText);

const decryptedText = decrypt(encryptedText, key, iv);
console.log('Decrypted:', decryptedText);
