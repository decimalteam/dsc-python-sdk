import unittest

from .wallet import Wallet, check_address_validity

class TestWallet(unittest.TestCase):
    def test_wallet_create(self):
        w = Wallet()
        self.assertEqual(w.get_address()[:3], "dx1")
    def test_wallet_mnemonic(self):
        w = Wallet("error crane rich oval street radar price bundle very lava climb siege comic tell wrong ten gap silent shine lawsuit wise horse ball pretty")
        self.assertEqual(w.get_address(), "dx1uhvauapn5slk2wq4tglxvctl4qlylnqdczr6tj")
        w = Wallet("mad kitten give wine plate gadget hungry reject cram junior swing jealous various genre method wheel pulp symbol fun silent blossom urban blur vapor")
        self.assertEqual(w.get_address(), "dx1plcsd4tfrzggxf3znv09gk437r87gee4ywxqfe")
    def test_address_validity(self):
        self.assertTrue(check_address_validity("dx1uhvauapn5slk2wq4tglxvctl4qlylnqdczr6tj"))
        self.assertFalse(check_address_validity("dx1uhvauapn5slk2wq4tglxvctl4qlylnqdczr6t"))        