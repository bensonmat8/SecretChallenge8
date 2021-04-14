
def coin_sort(amt:float) -> json:
    # Dinominations 
    dinom = [1,5,10,25,50]
    dinom_dict = {50:'half-dollar', 25:'quarter', 10:'dime'
    , 5:'nickel', 1:'penny'}
    num, rem = divmod(int(amt * 100),100)
    result = {'silver-dollar': num}
    while dinom:
        coin = dinom.pop()
        num, rem = divmod(rem, coin)
        result[dinom_dict[coin]] = num
    return json.dumps(result, indent=4)

if __name__ == '__main__':
    import json
    