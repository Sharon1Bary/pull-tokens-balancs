from moralis import evm_api


def get_erc20(tb) -> dict:

    api_key = "CHB8kMsmbtK2t7voBh1ZT8UQoODIemiDsdjp44bA0SCymhLU6q57c6cvP38dy6dP"
    params = {"address": "0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11", "chain": "eth"}

    for i in evm_api.token.get_wallet_token_balances(api_key=api_key, params=params):
        tb[i["token_address"]] = i["balance"]
    return tb


if __name__ == "__main__":

    try:
        tb_res = get_erc20({})

        # print all the tokens and balance for each token in the pool.
        print(tb_res)

        # print the number of the tokens in the pool.
        print(len(tb_res))
    except Exception as e:
        print(e)
