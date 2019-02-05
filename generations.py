import base58
import binascii
import hashlib
import ecdsa


def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d


def hex_to_byte(hexadecimal):
    return bytearray.fromhex(hexadecimal)


def add_main_network(private_hex):
    return f'80{private_hex}'


def generate_private_wif(private_hex):
    private_hex_with_network = add_main_network(private_hex)
    sha256a = hashlib.sha256(binascii.unhexlify(private_hex_with_network)).hexdigest()
    sha256b = hashlib.sha256(binascii.unhexlify(sha256a)).hexdigest()
    return base58.b58encode(binascii.unhexlify(private_hex_with_network+sha256b[:8])).decode()


def generate_public_address(private_hex):
    public_key = generate_public_key(private_hex)
    public_key_with_network = '04' + binascii.hexlify(public_key.to_string()).decode()
    hash160 = ripemd160(hashlib.sha256(binascii.unhexlify(public_key_with_network)).digest()).digest()
    public_address_a = b"\x00" + hash160
    checksum = hashlib.sha256(hashlib.sha256(public_address_a).digest()).digest()[:4]
    return base58.b58encode(public_address_a + checksum).decode()


def generate_public_key(private_hex):
    private_hex_bytes = hex_to_byte(private_hex)
    sk = ecdsa.SigningKey.from_string(private_hex_bytes, curve=ecdsa.SECP256k1)
    return sk.get_verifying_key()
