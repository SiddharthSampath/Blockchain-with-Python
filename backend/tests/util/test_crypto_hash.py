from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    assert crypto_hash("one",2,[3]) == crypto_hash([3],"one",2)
    assert crypto_hash("test") == "4d967a30111bf29f0eba01c448b375c1629b2fed01cdfcc3aed91f1b57d5dd5e"