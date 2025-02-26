#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

// Function to compute gcd
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Function to compute modular inverse (d)
int modInverse(int e, int phi) {
    for (int d = 2; d < phi; d++) {
        if ((d * e) % phi == 1) {
            return d;
        }
    }
    return -1;
}

// Function for modular exponentiation (x^y mod p)
long long modExp(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// RSA Key Generation
void generateKeys(int &n, int &e, int &d) {
    int p = 61, q = 53;  // Example prime numbers
    n = p * q;
    int phi_n = (p - 1) * (q - 1);

    // Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 3;
    while (gcd(e, phi_n) != 1) {
        e += 2;
    }

    // Compute d, the modular inverse of e
    d = modInverse(e, phi_n);
}

// RSA Encryption: C = M^e mod n
long long encrypt(int message, int e, int n) {
    return modExp(message, e, n);
}

// RSA Decryption: M = C^d mod n
long long decrypt(long long cipher, int d, int n) {
    return modExp(cipher, d, n);
}

int main() {
    int n, e, d;
    generateKeys(n, e, d);

    cout << "Public Key: (e=" << e << ", n=" << n << ")\n";
    cout << "Private Key: (d=" << d << ", n=" << n << ")\n";

    int message;
    cout << "\nEnter an integer message to encrypt: ";
    cin >> message;

    long long cipher = encrypt(message, e, n);
    cout << "Encrypted Cipher: " << cipher << endl;

    long long decryptedMessage = decrypt(cipher, d, n);
    cout << "Decrypted Message: " << decryptedMessage << endl;

    return 0;
}
