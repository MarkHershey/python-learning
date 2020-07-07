req_id = b"123"
verb = b"predict"
payload = b"{'this is user data': 'some data'}"

string: bytes = b'"%s":' % req_id + b"{" + b'"verb":"%s",' % verb + b'"usr_data":%s' % payload + b"}"
new_msg: bytes = b"{" + string + b"}"


print(new_msg)


req_id = req_id.decode("utf-8")
verb = verb.decode("utf-8")
payload = payload.decode("utf-8")

PayloadKey_verb = "verb"
PayloadKey_usr_data = "usr_data"


payload_to_vmp = (
    "{"
    + f"'{req_id}':"
    + "{"
    + f"'{PayloadKey_verb}': '{verb}', '{PayloadKey_usr_data}': {payload}"
    + "}"
    + "}"
).encode("utf-8")

print(payload_to_vmp == new_msg)
