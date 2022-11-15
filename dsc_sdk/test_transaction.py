import sys

import unittest

from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_coin

from .wallet import Wallet
from .transaction import build_tx, Transaction
from .tx_types import MsgSendCoin
from .number_helpers import ether_to_wei

class TestTransaction(unittest.TestCase):
    def test_protobuf_message(self):
        w = Wallet()
        w.set_account_number(10)
        w.set_chain_id("somechain")
        w.set_sequence(10)
        msg = MsgSendCoin(w.get_address(), "dx1...", "del", "100")
        build_tx(w, msg, {"memo": "aaa", "fee_denom": "del", "fee_amount":"100"})
    def test_signing_bytes(self):
        self.maxDiff = None
        w1 = Wallet("plug tissue today frown increase race brown sail post march trick coconut laptop churn call child question match also spend play credit already travel")
        w2 = Wallet("layer pass tide basic raccoon olive trust satoshi coil harbor script shrimp health gadget few armed rival spread release welcome long dust almost banana")
        w1.set_account_number(173)
        w1.set_sequence(0)
        w1.set_chain_id("decimal_2020-22110900")
        msg = MsgSendCoin(w1.get_address(), w2.get_address(), "del", ether_to_wei(1))
        tx, bz = build_tx(w1, msg, {"memo": "hello", "fee_denom": "del", "fee_amount":"0"})
        self.assertEqual(bz.hex(), "0a9c010a92010a1c2f646563696d616c2e636f696e2e76312e4d736753656e64436f696e12720a29647831746c796b79786e337a6464776d37773839726175727775767761356170763477333274683066122964783130647461766570683271303378333234346475766d643932676b7767796c6c35726c756c6d6e1a1a0a0364656c121331303030303030303030303030303030303030120568656c6c6f125b0a570a4f0a282f65746865726d696e742e63727970746f2e76312e657468736563703235366b312e5075624b657912230a2103915d3a632aaec661cc693adb5341a5f104661e6f7a85db9df1d8a7a332f781fe12040a02080112001a15646563696d616c5f323032302d323231313039303020ad01")
        self.assertEqual(tx.signatures[0].hex(), "59dc3cc63526e1a66e5ab6748ad5500f313e0553ecebe7e5fb8bfc34bccd63ed57735101a28d4fb1b8e1ebd83cb60c32c98100ee9d1858f1a4ccbb10475ee44400")
        self.assertEqual(tx.SerializeToString(deterministic=True).hex(), "0a9c010a92010a1c2f646563696d616c2e636f696e2e76312e4d736753656e64436f696e12720a29647831746c796b79786e337a6464776d37773839726175727775767761356170763477333274683066122964783130647461766570683271303378333234346475766d643932676b7767796c6c35726c756c6d6e1a1a0a0364656c121331303030303030303030303030303030303030120568656c6c6f125b0a570a4f0a282f65746865726d696e742e63727970746f2e76312e657468736563703235366b312e5075624b657912230a2103915d3a632aaec661cc693adb5341a5f104661e6f7a85db9df1d8a7a332f781fe12040a02080112001a4159dc3cc63526e1a66e5ab6748ad5500f313e0553ecebe7e5fb8bfc34bccd63ed57735101a28d4fb1b8e1ebd83cb60c32c98100ee9d1858f1a4ccbb10475ee44400")
    def test_signing_bytes(self):
        self.maxDiff = None
        w1 = Wallet("plug tissue today frown increase race brown sail post march trick coconut laptop churn call child question match also spend play credit already travel")
        w2 = Wallet("layer pass tide basic raccoon olive trust satoshi coil harbor script shrimp health gadget few armed rival spread release welcome long dust almost banana")
        w1.set_account_number(173)
        w1.set_sequence(0)
        w1.set_chain_id("decimal_2020-22110900")
        msg = MsgSendCoin(w1.get_address(), w2.get_address(), "del", ether_to_wei(1))
        tx = Transaction.build_tx(msg)
        tx.set_memo("hello")
        bz = tx.sign(w1)
        self.assertEqual(bz.hex(), "0a9c010a92010a1c2f646563696d616c2e636f696e2e76312e4d736753656e64436f696e12720a29647831746c796b79786e337a6464776d37773839726175727775767761356170763477333274683066122964783130647461766570683271303378333234346475766d643932676b7767796c6c35726c756c6d6e1a1a0a0364656c121331303030303030303030303030303030303030120568656c6c6f125b0a570a4f0a282f65746865726d696e742e63727970746f2e76312e657468736563703235366b312e5075624b657912230a2103915d3a632aaec661cc693adb5341a5f104661e6f7a85db9df1d8a7a332f781fe12040a02080112001a4159dc3cc63526e1a66e5ab6748ad5500f313e0553ecebe7e5fb8bfc34bccd63ed57735101a28d4fb1b8e1ebd83cb60c32c98100ee9d1858f1a4ccbb10475ee44400")
