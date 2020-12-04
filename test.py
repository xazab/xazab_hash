import xazab_hash
from binascii import unhexlify, hexlify

import unittest

# xazab block #1
# moo@b1:~/.xazab$ xazabd getblockhash 1
# 0000017338dfceae23bfcc97b461142e21009e5dac5e8e40b8541eb68479a224
# moo@b1:~/.xazab$ xazabd getblock 0000017338dfceae23bfcc97b461142e21009e5dac5e8e40b8541eb68479a224
#{
#  "hash": "0000017338dfceae23bfcc97b461142e21009e5dac5e8e40b8541eb68479a224",
#  "confirmations": 62267,
#  "size": 169,
#  "height": 1,
#  "version": 536870912,
#  "versionHex": "20000000",
#  "merkleroot": "133a1c46cbd26e59d1eefc031c1d6127501a70ea7600a6cb1d6fe8e4045558db",
#  "tx": [
#    "133a1c46cbd26e59d1eefc031c1d6127501a70ea7600a6cb1d6fe8e4045558db"
#  ],
#  "time": 1602720872,
#  "mediantime": 1602720872,
#  "nonce": 50385,
#  "bits": "1e03fffc",
#  "difficulty": 0.0009765625,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000500050",
#  "nTx": 1,
#  "previousblockhash": "00000ffd590b1485b3caadc19b22e6379c733355108f107a430458cdf3407ab6",
#  "nextblockhash": "000000c51b09140be171b9a67b76195f2758fffc02ad3d10e1dad6f98d7e60bc",
#  "chainlock": false
#}

header_hex = ("02000000" +
    "b67a40f3cd5804437a108f105533739c37e6229bc1adcab385140b59fd0f0000" +
    "a71c1aade44bf8425bec0deb611c20b16da3442818ef20489ca1e2512be43eef"
    "814cdb52" +
    "f0ff0f1e" +
    "dbf70100")

best_hash = '434341c0ecf9a2b4eec2644cfadf4d0a07830358aed12d0ed654121dd9070000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_xazab_hash(self):
        self.pow_hash = hexlify(xazab_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

