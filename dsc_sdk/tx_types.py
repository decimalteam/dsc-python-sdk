from .proto.decimal.coin.v1 import tx_pb2 as coin_tx
from .proto.decimal.nft.v1 import tx_pb2 as nft_tx
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_coin

from typing import List

### decimal coin transaction

def MsgCreateCoin(sender: str, denom: str, title: str, crr: int, 
    initial_volume: str, initial_reserve: str, limit_volume: str,
    identity: str) -> coin_tx.MsgCreateCoin:
    return coin_tx.MsgCreateCoin(
        sender = sender,
        denom = denom,
        title = title,
        crr = crr,
        initial_volume = initial_volume,
        initial_reserve = initial_reserve,
        limit_volume = limit_volume,
        identity = identity,
    )

def MsgUpdateCoin(sender: str, denom: str, limit_volume: str, identity: str) -> coin_tx.MsgUpdateCoin:
    return coin_tx.MsgUpdateCoin(
        sender = sender,
        denom = denom,
        limit_volume = limit_volume,
        identity = identity,
    )

def MsgBuyCoin(sender: str, denom_to_buy: str, amount_to_buy: str,
    denom_to_sell: str, max_amount_to_sell: str) -> coin_tx.MsgBuyCoin:
    return coin_tx.MsgBuyCoin(
        sender = sender,
        coin_to_buy = cosmos_coin.Coin(denom=denom_to_buy, amount=amount_to_buy),
        max_coin_to_sell = cosmos_coin.Coin(denom=denom_to_sell, amount=max_amount_to_sell)
    )

def MsgSellCoin(sender: str, denom_to_sell: str, amount_to_sell: str,
    denom_to_buy: str, min_amount_to_buy: str) -> coin_tx.MsgSellCoin:
    return coin_tx.MsgSellCoin(
        sender = sender,
        coin_to_sell = cosmos_coin.Coin(denom=denom_to_sell, amount=amount_to_sell),
        min_coin_to_buy = cosmos_coin.Coin(denom=denom_to_buy, amount=min_amount_to_buy)
    )

def MsgSendCoin(sender: str, recipient: str, denom: str, amount: str) -> coin_tx.MsgSendCoin:
    return coin_tx.MsgSendCoin(
        sender = sender,
        recipient = recipient,
        coin = cosmos_coin.Coin(denom=denom, amount=amount)
    )

def MultiSendEntry(recipient: str, denom: str, amount: str) -> coin_tx.MultiSendEntry:
    return coin_tx.MultiSendEntry(
        recipient = recipient,
        coin = cosmos_coin.Coin(denom=denom, amount=amount),
    )

def MsgMultiSendCoin(sender: str, sends: List[coin_tx.MultiSendEntry]) -> coin_tx.MsgMultiSendCoin:
    return coin_tx.MsgMultiSendCoin(
        sender = sender,
        sends = sends,
    )

def MsgBurnCoin(sender: str, denom: str, amount: str) -> coin_tx.MsgBurnCoin:
    return coin_tx.MsgBurnCoin(
        sender = sender,
        coin = cosmos_coin.Coin(denom=denom, amount=amount),
    )

# TODO: MsgRedeemCheck

### decimal nft transaction

def MsgSendToken(sender: str, recipient: str, token_id: str, sub_token_ids: List[int]) -> nft_tx.MsgSendToken:
    return nft_tx.MsgSendToken(
        sender = sender,
        recipient = recipient,
        token_id = token_id,
        sub_token_ids = sub_token_ids,
    )