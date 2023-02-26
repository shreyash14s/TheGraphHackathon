import requests
import pandas as pd

URL = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
LAST_TOKEN_SYMBOL = 'RESQ'

# Querying the Graph using token pagination
# Retrieves thousand token records at a time with the below attributes

GRAPH_QUERY = """
{
  tokens(
    first: 1000
    orderBy: symbol
    orderDirection: asc
    where: {symbol_gt: "%s"}
  ) {
    totalSupply
    txCount
    symbol
    volume
    volumeUSD
    whitelistPools {
      liquidity
      token0 {
        symbol
        totalValueLockedUSD
      }
      token1 {
        symbol
        totalValueLockedUSD
      }
      liquidityProviderCount
      txCount
    }
  }
}
""" % LAST_TOKEN_SYMBOL

if __name__ == "__main__":
    while True:
        r = requests.post(URL, json={'query': GRAPH_QUERY})
        js = r.json()
        if 'data' in js and js['data']['tokens']:
            print('Success!')
            break
        print('Retrying...')

    flat = []
    for i in js['data']['tokens']:
        selfLockedUsd = 0
        otherLockedUsd = 0
        for j in i['whitelistPools']:
            if j['token0']['symbol'] == i['symbol']:
                otherLockedUsd += float(j['token1']['totalValueLockedUSD'])
                selfLockedUsd += float(j['token0']['totalValueLockedUSD'])
            else:
                otherLockedUsd += float(j['token0']['totalValueLockedUSD'])
                selfLockedUsd += float(j['token1']['totalValueLockedUSD'])
        flat.append({
            'symbol': i['symbol'],
            'totalSupply': i['totalSupply'],
            'txCount': i['txCount'],
            'volume': i['volume'],
            'volumeUSD': i['volumeUSD'],
            'selfLockedUsd': selfLockedUsd,
            'otherLockedUsd': otherLockedUsd
        })

    df = pd.DataFrame(flat)

    df_merged_orig = pd.load_csv('merged.csv')
    df_merged = pd.concat([df_merged_orig, df], ignore_index=True)
    df_merged.to_csv('merged.csv', index=False)
    
    LAST_TOKEN_SYMBOL = df['symbol'].iloc[-1]
