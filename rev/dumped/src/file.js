const crypto = require('crypto');

function decrypt(encryptedText, key, iv) {
  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
  let decrypted = decipher.update(encryptedText, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

const key = Buffer.from([
  71, 189, 15, 29, 218, 140, 219, 171,
  163, 172, 134, 13, 234, 216, 246, 163,
  181, 20, 17, 9, 28, 50, 173, 8,
  142, 177, 49, 219, 249, 214, 105, 166
])

const iv = Buffer.from([
  113, 88, 30, 151, 213,
  222, 35, 133, 187, 41,
  75, 155, 225, 92, 111,
  219
]);

const decryptedText = decrypt("db01e42197146398b0075778fbf83da11d339b61ac74ba8c7f842b372a47cdd7cffcc73f4f98d95848e044aa98ac2ba9", key, iv);
console.log('Decrypted:', decryptedText);
