import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="dsc-python-sdk",
    version="1.1.9",
    author="DecimalTeam",
    description="",
    long_description=long_description,
    install_requires=['asn1crypto==1.5.1', 'base58==2.0.0', 'base58check==1.0.2', 'bech32==1.2.0', 'bip32==3.3', 'cached-property==1.5.2', 'cffi==1.14.3', 'chardet==3.0.4', 'coincurve==17.0.0', 'ecdsa==0.16.1', 'eth-hash==0.3.1', 'eth-typing==2.2.2', 'eth-utils==1.10.0', 'ethereum==2.3.2', 'future==0.18.2', 'idna==2.10', 'mnemonic==0.20', 'mypy-extensions==0.4.3', 'pbkdf2==1.3', 'py-ecc==5.1.0', 'pyaes==1.6.1', 'pycparser==2.20', 'pycryptodome==3.15.0', 'pycryptodomex==3.15.0', 'pyethash==0.1.27', 'requests==2.25.0', 'protobuf==3.19.5', 'web3==5.31.1'],
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/decimalteam/dsc-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
