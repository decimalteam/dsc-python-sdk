from .proto.decimal.coin.v1 import tx_pb2 as coin_tx
from .proto.decimal.nft.v1 import tx_pb2 as nft_tx
from .proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_coin

from typing import List

def MsgSendCoin(sender: str, recipient: str, denom: str, amount: str) -> coin_tx.MsgSendCoin:
    return coin_tx.MsgSendCoin(
        sender = sender,
        recipient = recipient,
        coin = cosmos_coin.Coin(denom=denom, amount=amount)
    )

def MsgSendToken(sender: str, recipient: str, token_id: str, sub_token_ids: List[int]) -> nft_tx.MsgSendToken:
    return nft_tx.MsgSendToken(
        sender = sender,
        recipient = recipient,
        token_id = token_id,
        sub_token_ids = sub_token_ids,
    )