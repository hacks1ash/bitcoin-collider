__author__ = "MiGle Gurushidze"
__copyright__ = "Copyright (C) 2004 MiGle Gurushidze"
__license__ = "Public Domain"
__version__ = "1.0"

from parse import parse_bitcoin_addresses
from generations import generate_public_address, generate_private_wif
from utils import read_text_from_file, write_text_to_file
import itertools

HEX_CHARS = '0123456789ABCDEF'

if __name__ == '__main__':
    copyright()
    print(f'\n******** Made by {__author__} ********\n')
    print('**** Getting 1000 the richest addresses ****')
    parse_bitcoin_addresses(100)
    final_bitcoin_list = list()
    text_content = read_text_from_file('bitcoin_addresses')
    for index in range(0, len(text_content)):
        text_content[index] = text_content[index].rstrip('\n')
        final_bitcoin_list.append(text_content[index])

    print('**** Starting checking addresses ****')

    for n in range(64, 65):
        for xs in itertools.product(HEX_CHARS, repeat=n):
            private_hex = ''.join(xs)
            if private_hex.count('0') != 64:
                print(private_hex)
                public_address = generate_public_address(private_hex)
                if public_address in final_bitcoin_list:
                    private_wif = generate_private_wif(private_hex)
                    write_text_to_file('cracked', private_hex)
                    write_text_to_file('cracked', private_wif)
                    write_text_to_file('cracked', public_address)
                    print('Private key found')
    else:
        print('**** Whole blockchain checked ^_^ ****')
