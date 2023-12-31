# Decimal Python SDK

Check out these links:
- [Decimal SDK docs](https://help.decimalchain.com/api-sdk/).
- [Decimal Console site](https://console.decimalchain.com/).

## Wallet API
### Generate new wallet
```python
from dsc_sdk import Wallet

wallet = Wallet()
```
### Generate wallet from mnemonic*
*if no mnemonic provided Wallet() will create instance with autogenerated mnemonic

```python
from dsc_sdk import Wallet

wallet = Wallet('erase august mask elevator sand picture north there apple equal anchor target...')
```
### Get wallet address
```python
from dsc_sdk import Wallet

wallet = Wallet()
wallet.get_mnemonic() # returns wallet mnemonic
wallet.get_address() # returns wallet address
wallet.get_ethereum_address() # returns wallet address hex (0x)
```

## Get DecimalAPI to perform transactions
To initiate api you have to pass address of the gateway for network you will work with 
```python
from dsc_sdk import DscAPI
# or you can use dsc_sdk.MAINNET_GATE, TESTNET_GATE, DEVNET_GATE
api = DscAPI("https://devnet-gate.decimalchain.com/api")

# read chain id & base coin denomination
api.get_parameters()
print(api.get_chain_id())
print(api.get_base_denom())
```

## API usage
After you initialized api instance, you can use its` broadcast() method to send prepared transaction.
Transaction creation examples can be found in this file.

```python
from dsc_sdk import DscAPI
api = DscAPI("https://devnet-gate.decimalchain.com/api")
api.broadcast(prepared_transaction_bytes)
```

## Build and send transaction

```python

# all Msg* functions is defined in tx_types.py
from dsc_sdk import DscAPI, Wallet, Transaction, MsgSendCoin, ...
# helper functions to convert integer values to valid blockchain amounts
from dsc_sdk import ether_to_wei, finney_to_wei

##### 1. initialize api
# You can also use constants
# MAINNET_GATE, TESTNET_GATE, DEVNET_GATE and MAINNET_WEB3, TESTNET_WEB3, DEVNET_WEB3
api = DscAPI("https://devnet-gate.decimalchain.com/api", "https://devnet-val.decimalchain.com/web3/")
# or, if you don't want to use web3 from API
api = DscAPI("https://devnet-gate.decimalchain.com/api")
api.get_parameters()

##### 2. create wallet and bind it to current blockchain
wallet = Wallet(mnemonic1)
an, seq = api.get_account_number_and_sequence(wallet.get_address())
wallet.set_account_number(an)
wallet.set_sequence(seq)
wallet.set_chain_id(api.get_chain_id())

##### 3. create and sign transaction

# create transaction message
# sender and recipient must be valid bech32 address
# like d01...
msg = MsgSendCoin(sender, recipient, coin_denom, ether_to_wei(1))
tx = Transaction.build_tx(msg)

# optional: set memo, set custom coin fee...
tx.set_memo("hello from python")
tx.set_fee("initiald", ether_to_wei(1))
# calculate_fee calculates fee in specified denom and set it
# wallet is used for signing and for right transaction length
tx.calculate_fee(wallet, "initiald", api)

# sign transaction and get transaction bytes to send
tx_bytes = tx.sign(wallet)

##### 4. send transaction and examine result
txres = api.broadcast(tx_bytes)
print(txres.hash, txres.code, txres.codespace)

```

## Known transaction message types (constructors)

NOTE:
- `sender` and `recipient` must be valid bech32 addresses with `d0` prefix
- `validator...` must be valid bech32 addresses with `d0valoper` prefix
- `amount` must be integer value in string representation

### Coin module contructors
- `MsgCreateCoin(sender: str, denom: str, title: str, crr: int, initial_volume: str, initial_reserve: str, limit_volume: str,     identity: str)` (Message to create custom coin)
    - `denom` - short ticket for coin, first symbol must be letter, others must be letters and digits, up to 10 symbols
    - `crr` - constant reserve ratio, integer value between 10 and 100
    - `initial_volume`, `initial_reserve`, `limit_volume` - big integers as string, inital amount of custom coin, initial reserve in base coin, limit for custom coin amount
- `MsgUpdateCoin(sender: str, denom: str, limit_volume: str, identity: str)` (Message to update custom coin limit volume and identity, only creator can update coin, limit must be greater than current volume)
- `MsgBuyCoin(sender: str, denom_to_buy: str, amount_to_buy: str, denom_to_sell: str, max_amount_to_sell: str)` (Message to buy coin)
- `MsgSellCoin(sender: str, denom_to_sell: str, amount_to_sell: str, denom_to_buy: str, min_amount_to_buy: str)` (Message to sell coin)
- `MsgSendCoin(sender: str, recipient: str, denom: str, amount: str)` (Message to send coin from sender to recipient)
- `MsgMultiSendCoin(sender: str, sends: List[coin_tx.MultiSendEntry]), MultiSendEntry(recipient: str, denom: str, amount: str)` (Message to send possible different coins for sender to multiple recipients)
- `MsgBurnCoin(sender: str, denom: str, amount: str)` (Message to burn coin volume (not reserve), coin will be substracted from sender balance)
- `MsgRedeemCheck(sender: str, check: str, proof: str)` (Message to redeem check)
    - `check` - base58 encoded check bytes
    - `proof` - password for check

helper to send all coins
- `BuildSendAllCoin(signer: Wallet, api, recipient: str, coin_denom: str) -> bytes` (return signed transaction bytes)

### Multisig module contructors
- `MsgCreateWallet(sender: str, owners: List[str], weights: List[int], threshold: int)` (Message to create multisig wallet)
    - `owners` - list of valid account addresses
    - `weights` - voting weights of owners
    - `threshold` - threshold level to execute transaction
- `MsgCreateTransaction(sender: str, wallet: str, msg)` (Message to create multisig transaction, sender must be one of wallets owner)
    - `msg` - result of any Msg* constructor
- `MsgSignTransaction(sender: str, id: str)` (Message to sign, sender must be one of wallets owner)
    - `id` - multisig transaction id, bech32 value with prefix `d0mstx`

### NFT module constructors
- `MsgMintToken(sender: str, denom: str, token_id: str, token_uri: str, allow_mint: bool, recipient: str, quantity: int, reserve_denom: str, reserve_amount: str)` (Message to mint NFT token)
    - `denom` - name of NFT collection
    - `token_id` - blockchain unique token identifier
    - `token_uri` - blockchain unique URI
    - `allow_mint` - allow to mint subtoken
    - `recipient` - recipient of NFT subtokens
    - `quantity` - amount of NFT subtokens to mint
    - `reserve_denom` - denom of coin to reserve subtokens
    - `reserve_amount` - amount of coin to reserve subtokens PER ONE SUBTOKEN
- `MsgUpdateToken(sender: str, token_id: str, token_uri: str)` (Message to update token URI, only creator can do that)
- `MsgUpdateReserve(sender: str, token_id: str, sub_token_ids: List[int], reserve_denom: str, reserve_amount: str)` (Message to update subtokens reserve, only creator can do that)
- `MsgSendToken(sender: str, recipient: str, token_id: str, sub_token_ids: List[int])` (Message to send subtokens from sender to recipient)
- `MsgBurnToken(sender: str, token_id: str, sub_token_ids: List[int])` (Message to burn subtokens, only creator can do that, subtokens reserve will be return to creator)

### Swap module constructors
- `MsgInitializeSwap(sender: str, recipient: str, amount: str, token_symbol: str, transaction_number: str, from_chain: int, dest_chain: int)` (Message to initialize coin swap from one blockchain to other)
    - `recipient` - address in other blockchain
    - `amount` - amount of coin/token
    - `token_symbol` - coin denom/token symbol
    - `transaction number` - unique transaction number
    - `from_chain` - source blockchain id in swap chains records
    - `dest_chain` - desctination blockchain id in swap chains records

### Validator module constructors
- `MsgCreateValidator(operator_address: str, reward_address: str, pubkey: bytes, moniker: str, identity: str, website: str, security_contact: str, details: str, commission: str, stake_denom: str, stake_amount: str)` (Message to create validator)
    - `operator_address` - sender address encoded as bech32 with prefix `d0valoper`
    - `reward_address` - address to receive validator rewards, bech32 address with prefix `d0`
    - `pubkey` - node public key bytes
    - `moniker, indentity, website, security_contact, details` - validator description
    - `commission` - part of rewards to send to `reward_address`, must be string representation of floating point value between 0.0 and 1.0
    - `stake_denom, stake_amount` - creator initial coin stake
- `MsgEditValidator(operator_address: str, reward_address: str, moniker: str, identity: str, website: str, security_contact: str, details: str)` (Message to change validator reward address, description)
- `MsgSetOnline(validator: str)` (Message to set validator online)
- `MsgSetOffline(validator: str)` (Message to set validator offline)
- `MsgDelegate(delegator: str, validator: str, coin_denom: str, coin_amount: str)` (Message to delegate coin to validator)
- `MsgDelegateNFT(delegator: str, validator: str, token_id: str, sub_token_ids: List[int])` (Message to delegate NFT subtokens to validator)
- `MsgRedelegate(delegator: str, validator_src: str, validator_dst: str, coin_denom: str, coin_amount: str)` (Message to redelegate coins from one validator to other)
- `MsgRedelegateNFT(delegator: str, validator_src: str, validator_dst: str, token_id: str, sub_token_ids: List[int])` (Message to redelegate NFT subtokens from one validator to other)
- `MsgUndelegate(delegator: str, validator: str, coin_denom: str, coin_amount: str)` (Message to undelegate coin from validator)
- `MsgUndelegateNFT(delegator: str, validator: str, token_id: str, sub_token_ids: List[int])` (Message to undelegate NFT subtokens from validator)
- `MsgCancelRedelegation(delegator: str, validator_src: str, validator_dst: str, creation_height: int, coin_denom: str, coin_amount: str)` (Message to cancel coin redelegation)
- `MsgCancelRedelegationNFT(delegator: str, validator_src: str, validator_dst: str, creation_height: int, token_id: str, sub_token_ids: List[int])` (Message to cancel NFT subtoken redelegation)
- `MsgCancelUndelegation(delegator: str, validator: str, creation_height: int, coin_denom: str, coin_amount: str)` (Message to cancel coin undelegation)
- `MsgCancelUndelegationNFT(delegator: str, validator: str, creation_height: int, token_id: str, sub_token_ids: List[int])` (Message to cancel NFT subtokens undelegation)

## Known API query methods

```
get_account_balances(self, address: str) -> Dict[str, str]

get_account_erc_balances(self, hex_address: str) -> List[ERCBalance]

get_erc20_tokens(self, limit=10, offset=0)

```

## Helper functions

- `ether_to_wei` : convert integer value to valid amount representation ( * 10^18)
- `finney_to_wei` : convert integer value to valid amount representation ( * 10^15)
- `wei_to_ether` : convert amount string representation to float value ( / 10^18)
- `check_address_validity` : check bech32 address; return true if it's valid bech32 representation 
- `d0_to_hex`, `hex_to_d0` : convert DSC address ith prefix d0 to/from Ethereum hex presentation
