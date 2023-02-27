# Blockchain Analytics Hackathon

**Members**
- Shreyash S Sarnayak
- Siddharth Srinivasan



**Title**: Token-Based Rug Pull Detection

### Overview

This is our submission for [The Graph Hackathon@CU](https://pond-nautilus-f94.notion.site/Deep-Dive-Into-The-Graph-2bcc4aea80f04563a5ecd4c33958acf0) on 25th February 2023.

The overall analytics workflow is as follows:
- Fetch crypto and token properties from `The Graph`
- Provide data labels for currently collected token data using Rug-Pull based data sources.
- Using the above training data, train a Decision Tree classifier and use the same for classifying other tokens as facing a **Rug Pull** or otherwise.

### Miscellaneous

- **Subgraph Used**: [Uniswap v3 Hosted Service](https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3)

- **GraphQL Query**: [Link to source](https://github.com/shreyash14s/TheGraphHackathon/blob/main/thegraph_data_fetcher.py#L10)
