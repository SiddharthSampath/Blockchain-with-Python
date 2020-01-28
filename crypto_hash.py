import hashlib
import json

def crypto_hash(*args):
    #stringified_data = json.dumps(data)
    stringified_args = sorted(map(json.dumps,args))
    joined_data = ''.join(stringified_args)
    print(f"args : {args}")
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(crypto_hash("one",2,[3]))
    print(crypto_hash(1,"abc",[3]))

if __name__ == "__main__":
    main()
