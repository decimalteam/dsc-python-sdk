from dsc_sdk import DscAPI, Wallet, Transaction, MsgSendCoin, MsgSendToken, ether_to_wei, BuildSendAllCoin, \
    d0_to_hex, ERC20_DEFAULT_ABI, BuildSellAllCoin, MultiSendEntry, MsgMultiSendCoin, MsgSellCoin, MsgUpdateCoin
from web3 import Web3
import time

api = DscAPI("https://devnet-gate.decimalchain.com/api/", "https://devnet-val.decimalchain.com/web3/")
api.get_parameters()
print(api.get_chain_id())
print(api.get_base_denom())

############################
# block info

last_block = api.get_block_latest()
print(last_block)
last_block = api.get_block(last_block)
print(last_block)
last_block = api.get_block_validator(last_block)
print(last_block)


############################
# send transaction

step = 12

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

if step == 0:
    msg = MsgSendCoin(w1.get_address(), w2.get_address(), api.get_base_denom(), ether_to_wei(1))
    tx = Transaction.build_tx(msg)
    tx.set_memo("hello")
    txbytes = tx.sign(w1)
    #txres = api.broadcast_tx(txbytes, "sync")
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace)

if step == 1:
    msg = MsgSellCoin(w1.get_address(),
                      denom_to_sell="del",
                      amount_to_sell="10",
                      denom_to_buy='btt',
                      min_amount_to_buy="0"
                      )
    tx = Transaction.build_tx(msg)
    tx.set_memo("hello")
    txbytes = tx.sign(w1)
    #txres = api.broadcast_tx(txbytes, "sync")
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace)


############################
# calculate fee

if step == 2:
    time.sleep(3)

    an, seq = api.get_account_number_and_sequence(w1.get_address())
    w1.set_account_number(an)
    w1.set_sequence(seq)

    #msg = MsgSendToken(w1.get_address(), w2.get_address(), "ae97ec4876e2bd47775e3876e72dc521a00e8f3d", [2])
    msg = MsgSendCoin(w1.get_address(), w2.get_address(), api.get_base_denom(), ether_to_wei(1))
    tx = Transaction.build_tx(msg)
    tx.set_memo("hello")
    txbytes = tx.sign(w1)

    for coin in ["initiald", "del", "notexist"]:
        print("start calc for ", coin)
        fee = api.calculate_fee(txbytes, coin)
        print(type(fee), fee)

#txres = api.broadcast_tx(tx.SerializeToString(deterministic=True), "sync")
#print(txres.hash, txres.code, txres.codespace)

############################
# custom fee
if step == 3:
    an, seq = api.get_account_number_and_sequence(w1.get_address())
    w1.set_account_number(an)
    w1.set_sequence(seq)

    msg = MsgSendCoin(w1.get_address(), w2.get_address(), api.get_base_denom(), ether_to_wei(1))
    tx = Transaction.build_tx(msg)
    tx.set_memo("hello from python")
    tx.calculate_fee(w1, "initiald", api)
    txbytes = tx.sign(w1)
    #txres = api.broadcast_tx(txbytes, "sync")
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace, txres.log)

############################
# send all
if step == 4:
    an, seq = api.get_account_number_and_sequence(w1.get_address())
    w1.set_account_number(an)
    w1.set_sequence(seq)
    txbytes = BuildSendAllCoin(w1, api, w2.get_address(), "initiald")
    if txbytes == None:
        exit(0)
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace, txres.log)

############################
# send all
if step == 5:
    an, seq = api.get_account_number_and_sequence(w1.get_address())
    w1.set_account_number(an)
    w1.set_sequence(seq)
    txbytes = BuildSendAllCoin(w1, api, w2.get_address(), "del")
    if txbytes == None:
        exit(0)    
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace, txres.log)

############################
# sell all
if step == 6:
    an, seq = api.get_account_number_and_sequence(w1.get_address())
    w1.set_account_number(an)
    w1.set_sequence(seq)
    txbytes = BuildSellAllCoin(w1, api, w2.get_address(), "initiald")
    if txbytes == None:
        exit(0)
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace, txres.log)

############################
# erc20 bytescode
if step == 7:
    bytecode = api.erc20_build_token("some name", "tkn", "100", "1000", True, True, True)
    txhash = api.erc20_create_token(w1, bytecode)
    print(txhash)

############################
# erc20 list & abi
if step == 8:
    tokens = api.get_erc20_tokens(limit=20)
    erc20_tkn = None
    for tok in tokens:
        print(tok["address"], tok["symbol"])
        if tok["address"] == "0x09b034906710af2aa4e79f0ffa70ffad4af7313c":
            erc20_tkn = api.erc20_contract_instance(w1, "0x09b034906710af2aa4e79f0ffa70ffad4af7313c", tok["evmContract"]["abi"])
    print("token info:")
    print(erc20_tkn.functions.name().call())
    print(erc20_tkn.functions.symbol().call())
    adr1 = w1.get_checksum_address()
    adr2 = w2.get_checksum_address()
    print("balance before tx")
    print(erc20_tkn.functions.balanceOf(adr1).call() )
    print(erc20_tkn.functions.balanceOf(adr2).call() )
    txhash = erc20_tkn.functions.transfer(adr2, int(ether_to_wei(1))).transact({"from": adr1})
    txres = erc20_tkn.web3.eth.wait_for_transaction_receipt(txhash)
    print(txres)
    print("balance after tx")
    print(erc20_tkn.functions.balanceOf(adr1).call() )
    print(erc20_tkn.functions.balanceOf(adr2).call() )

############################
# erc balance
if step == 9:
    balances = api.get_account_erc_balances("0x4f5628750b2e82947cdf02ab45dd5456d919e716")
    for b in balances:
        print(b)

############################
# erc20 contract with default abi
if step == 10:
    erc20_tkn = api.erc20_contract_instance(w1, "0x21ee885dca392c4657eefe5adfa11971308de4c9", ERC20_DEFAULT_ABI)
    print("token info:")
    print(erc20_tkn.functions.name().call())
    print(erc20_tkn.functions.symbol().call())

############################
# erc20 contract with default abi
if step == 11:

    list_address = []

    for x in range(2000):
        list_address.append(
            MultiSendEntry(recipient="d010eefpeqng85844r9tyrfl8rpek3tz00kchjqae", denom="del", amount="1")
        )
    msg = MsgMultiSendCoin(sender=w1.get_address(), sends=list_address)
    tx = Transaction.build_tx(msg)
    tx.set_memo("hello")
    txbytes = tx.sign(w1)
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace)

if step == 12:
    msg = MsgUpdateCoin(w1.get_address(), "test1234", ether_to_wei(5000000), "dsa", ether_to_wei(5000000))
    tx = Transaction.build_tx(msg)
    tx.set_memo("hello")
    txbytes = tx.sign(w1)
    #txres = api.broadcast_tx(txbytes, "sync")
    txres = api.broadcast(txbytes)
    print(txres.hash, txres.code, txres.codespace)