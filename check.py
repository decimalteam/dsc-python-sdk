from dsc_sdk.api import DscAPI
from dsc_sdk.wallet import Wallet
from dsc_sdk.transaction import Transaction
from dsc_sdk.tx_types import MsgSendCoin, MsgSendToken
from dsc_sdk.number_helpers import ether_to_wei
import time

api = DscAPI("https://devnet-gate.decimalchain.com/api/")
api.get_parameters()
print(api.get_chain_id())
print(api.get_base_denom())

############################
# send transaction

# dx1tlykyxn3zddwm7w89raurwuvwa5apv4w32th0f
mnemonic1 = "plug tissue today frown increase race brown sail post march trick coconut laptop churn call child question match also spend play credit already travel"
w1 = Wallet(mnemonic1)
print(w1.get_address())
an, seq = api.get_account_number_and_sequence(w1.get_address())
w1.set_account_number(an)
w1.set_sequence(seq)
w1.set_chain_id(api.get_chain_id())
print(an, seq)
# dx10dtaveph2q03x3244duvmd92gkwgyll5rlulmn
mnemonic2 = "layer pass tide basic raccoon olive trust satoshi coil harbor script shrimp health gadget few armed rival spread release welcome long dust almost banana"
w2 = Wallet(mnemonic2)
print(w2.get_address())
an, seq = api.get_account_number_and_sequence(w2.get_address())
w2.set_account_number(an)
w2.set_sequence(seq)
w2.set_chain_id(api.get_chain_id())

msg = MsgSendCoin(w1.get_address(), w2.get_address(), api.get_base_denom(), ether_to_wei(1))
tx = Transaction.build_tx(msg)
tx.set_memo("hello")
txbytes = tx.sign(w1)
#txres = api.broadcast_tx(txbytes, "sync")
txres = api.broadcast(txbytes)
print(txres.hash, txres.code, txres.codespace)


############################
# calculate fee

time.sleep(3)

an, seq = api.get_account_number_and_sequence(w1.get_address())
w1.set_account_number(an)
w1.set_sequence(seq)

msg = MsgSendToken(w1.get_address(), w2.get_address(), "ae97ec4876e2bd47775e3876e72dc521a00e8f3d", [2])
tx = Transaction.build_tx(msg)
tx.set_memo("hello")
txbytes = tx.sign(w1)

fee = api.simulate_fee(txbytes, "initiald")
print(type(fee), fee)
fee = api.simulate_fee(txbytes, "del")
print(type(fee), fee)

#txres = api.broadcast_tx(tx.SerializeToString(deterministic=True), "sync")
#print(txres.hash, txres.code, txres.codespace)
