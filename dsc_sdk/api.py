import requests
import json
from typing import Tuple
import codecs

class DscAPI:
    """
    Base class to perform operations on Decimal API.
    Create new instance of api with passing base URL to DecimalAPI class.
    """

    def __init__(self, gate_url: str):
        self.gate_url = gate_url
        if self.gate_url[-1] != '/':
            self.gate_url += '/'
    
    def get_parameters(self):
        """
        load base blockchain parameters: chain_id, base denom
        """
        resp = json.loads(self.__request_gate("rpc/genesis"))
        self.__chain_id = resp["result"]["genesis"]["chain_id"]
        self.__base_denom = resp["result"]["genesis"]["app_state"]["coin"]["params"]["base_denom"]

    def get_chain_id(self):
        return self.__chain_id

    def get_base_denom(self):
        return self.__base_denom

    def get_account_number_and_sequence(self, address: str) -> Tuple[int, int]:
        self.__validate_address(address)
        resp = json.loads(self.__request_gate(f'rpc/accounts/{address}'))
        return (int(resp["account"]["base_account"]["account_number"]), int(resp["account"]["base_account"]["sequence"]))

    def broadcast(self, tx_bytes: bytes):
        resp = json.loads(self.__request_gate("rpc/txs", method="post", payload={"hexTx": tx_bytes.hex()}))
        return TxResult(
            hash = resp["result"]["hash"],
            code = resp["result"]["code"],
            log = resp["result"]["log"],
            codespace = resp["result"]["codespace"],
        )

    def simulate_fee(self, tx_bytes: bytes, fee_denom: str) -> str:
        resp = self.__request_gate("rpc/simulate_fee", method="post", payload = {
            "tx_bytes": list(tx_bytes),
            "feeCoin": fee_denom,
        })
        return resp

    @staticmethod
    def __validate_address(address: str):
        if len(address) < 41 or not address.startswith('dx'):
            raise Exception('Invalid address')

    def __request_gate(self, path: str, method: str = 'get', payload=None, options={}):
        url = (self.gate_url + path)
        if method == 'get':
            if len(options) > 0:
                response = requests.get(url, params=options)
            else:
                response = requests.get(url)
        else:
            response = requests.post(url, payload)
        return response.text        

class TxResult:
    def __init__(self, hash="", code=0, log="", codespace=""):
        self.hash = hash
        self.code = code
        self.log = log
        self.codespace = codespace