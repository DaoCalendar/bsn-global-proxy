# BSN Proxy

This is a single file utility to adopt BSN service to standard CKB node rpc.

Usage:

```py
$ python3 ./bsn-proxy.py --bsn-url 'https://hk.bsngate.com/api/<your-app-id>/Nervos-Mainnet/rpc' --api-key '<your-api-key>'
```

If everything goes well, you will have a ckb node rpc server at `http://localhost:8114`

Please register [BSN global](https://global.bsnbase.com/) to obtain a free or high performance plan.