ERC20_DEFAULT_ABI = [
            {
              "type": "constructor",
              "inputs": [
                {
                  "name": "name",
                  "type": "string",
                  "internalType": "string"
                },
                {
                  "name": "symbol",
                  "type": "string",
                  "internalType": "string"
                },
                {
                  "name": "startEmission",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "stateMutability": "nonpayable"
            },
            {
              "name": "Approval",
              "type": "event",
              "inputs": [
                {
                  "name": "owner",
                  "type": "address",
                  "indexed": True,
                  "internalType": "address"
                },
                {
                  "name": "spender",
                  "type": "address",
                  "indexed": True,
                  "internalType": "address"
                },
                {
                  "name": "value",
                  "type": "uint256",
                  "indexed": False,
                  "internalType": "uint256"
                }
              ],
              "anonymous": False
            },
            {
              "name": "OwnershipTransferred",
              "type": "event",
              "inputs": [
                {
                  "name": "previousOwner",
                  "type": "address",
                  "indexed": True,
                  "internalType": "address"
                },
                {
                  "name": "newOwner",
                  "type": "address",
                  "indexed": True,
                  "internalType": "address"
                }
              ],
              "anonymous": False
            },
            {
              "name": "Transfer",
              "type": "event",
              "inputs": [
                {
                  "name": "from",
                  "type": "address",
                  "indexed": True,
                  "internalType": "address"
                },
                {
                  "name": "to",
                  "type": "address",
                  "indexed": True,
                  "internalType": "address"
                },
                {
                  "name": "value",
                  "type": "uint256",
                  "indexed": False,
                  "internalType": "uint256"
                }
              ],
              "anonymous": False
            },
            {
              "name": "allowance",
              "type": "function",
              "inputs": [
                {
                  "name": "owner",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "spender",
                  "type": "address",
                  "internalType": "address"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "approve",
              "type": "function",
              "inputs": [
                {
                  "name": "spender",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "amount",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "bool",
                  "internalType": "bool"
                }
              ],
              "stateMutability": "nonpayable"
            },
            {
              "name": "balanceOf",
              "type": "function",
              "inputs": [
                {
                  "name": "account",
                  "type": "address",
                  "internalType": "address"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "decimals",
              "type": "function",
              "inputs": [],
              "outputs": [
                {
                  "name": "",
                  "type": "uint8",
                  "internalType": "uint8"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "decreaseAllowance",
              "type": "function",
              "inputs": [
                {
                  "name": "spender",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "subtractedValue",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "bool",
                  "internalType": "bool"
                }
              ],
              "stateMutability": "nonpayable"
            },
            {
              "name": "increaseAllowance",
              "type": "function",
              "inputs": [
                {
                  "name": "spender",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "addedValue",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "bool",
                  "internalType": "bool"
                }
              ],
              "stateMutability": "nonpayable"
            },
            {
              "name": "mint",
              "type": "function",
              "inputs": [
                {
                  "name": "to",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "amount",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "outputs": [],
              "stateMutability": "nonpayable"
            },
            {
              "name": "name",
              "type": "function",
              "inputs": [],
              "outputs": [
                {
                  "name": "",
                  "type": "string",
                  "internalType": "string"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "owner",
              "type": "function",
              "inputs": [],
              "outputs": [
                {
                  "name": "",
                  "type": "address",
                  "internalType": "address"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "renounceOwnership",
              "type": "function",
              "inputs": [],
              "outputs": [],
              "stateMutability": "nonpayable"
            },
            {
              "name": "symbol",
              "type": "function",
              "inputs": [],
              "outputs": [
                {
                  "name": "",
                  "type": "string",
                  "internalType": "string"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "totalSupply",
              "type": "function",
              "inputs": [],
              "outputs": [
                {
                  "name": "",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "stateMutability": "view"
            },
            {
              "name": "transfer",
              "type": "function",
              "inputs": [
                {
                  "name": "to",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "amount",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "bool",
                  "internalType": "bool"
                }
              ],
              "stateMutability": "nonpayable"
            },
            {
              "name": "transferFrom",
              "type": "function",
              "inputs": [
                {
                  "name": "from",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "to",
                  "type": "address",
                  "internalType": "address"
                },
                {
                  "name": "amount",
                  "type": "uint256",
                  "internalType": "uint256"
                }
              ],
              "outputs": [
                {
                  "name": "",
                  "type": "bool",
                  "internalType": "bool"
                }
              ],
              "stateMutability": "nonpayable"
            },
            {
              "name": "transferOwnership",
              "type": "function",
              "inputs": [
                {
                  "name": "newOwner",
                  "type": "address",
                  "internalType": "address"
                }
              ],
              "outputs": [],
              "stateMutability": "nonpayable"
            }
]