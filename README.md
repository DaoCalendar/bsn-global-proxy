# BSN Proxy

Original contributor: [muxueqz](https://github.com/muxueqz/bsn-proxy)

This is a single file utility to adopt BSN service to standard CKB and Ethereum node rpc. It support both [CKB node rpc](https://github.com/nervosnetwork/ckb/blob/master/rpc/README.md), and [ckb-indexer rpc](https://github.com/nervosnetwork/ckb-indexer) calls.

Usage:
ckb
```py
$ python3 ./bsn-proxy-ckb.py --bsn-url 'https://hk.bsngate.com/api/<your-app-id>/Nervos-Mainnet/rpc' --api-key '<your-api-key>'
```
If everything goes well, you will have a ckb node rpc server at `http://localhost:8114/rpc`, adn a ckb-indexer rpc server at `http://localhost:8114/indexer`.

Ethereum

[ethereum json rpc handbook](http://cw.hubwiz.com/card/c/ethereum-json-rpc-api/)

```py
$ python3 ./bsn-proxy-eth.py --bsn-url 'https://hk.bsngate.com/api/<your-app-id>/ETH-Mainnet/rpc' --api-key '<your-api-key>'
```
[Off-BSN-Access-wiki](https://global.bsnbase.com/static/tmpFile/bzsc/6permissionlessservices/6-4-1.html)

Please register [BSN global](https://global.bsnbase.com/) to obtain a free or high performance plan.
