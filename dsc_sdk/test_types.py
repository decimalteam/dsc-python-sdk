import unittest

from .tx_types import MsgCreateCoin, MsgUpdateCoin, MsgBuyCoin, MsgSellCoin, MsgSendCoin, \
    MultiSendEntry, MsgMultiSendCoin

class TestConstructors(unittest.TestCase):
    def test_create_coin(self):
        msg = MsgCreateCoin("dx1", "del", "deldeldel", 10, "1000000000", "1000000000", "1000000000", "asjdgajghsd")
        self.assertTrue(msg.IsInitialized())
    def test_update_coin(self):
        msg = MsgUpdateCoin("dx1", "del", "1000000000", "asjdgajghsd")
        self.assertTrue(msg.IsInitialized())
    def test_buy_coin(self):
        msg = MsgBuyCoin("dx1", "del", "1000000000", "asg", "10000")
        self.assertTrue(msg.IsInitialized())
    def test_sell_coin(self):
        msg = MsgSellCoin("dx1", "del", "1000000000", "asg", "10000")
        self.assertTrue(msg.IsInitialized())
    def test_send_coin(self):
        msg = MsgSendCoin("dx1", "dx1", "del", "1000000000")
        self.assertTrue(msg.IsInitialized())
    def test_multi_send_coin(self):
        sends = [
            MultiSendEntry("dx11", "del", "100"),
            MultiSendEntry("dx12", "del", "200"),
        ]
        msg = MsgMultiSendCoin("dx1", sends)
        self.assertTrue(msg.IsInitialized())
