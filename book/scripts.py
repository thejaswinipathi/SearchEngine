import json
import re
import codecs

def unmangle_utf8(match):
    escaped = match.group(0)                   # '\\u00e2\\u0082\\u00ac'
    hexstr = escaped.replace(r'\u00a0', '')      # 'e282ac'
    buffer = codecs.decode(hexstr, "hex")      # b'\xe2\x82\xac'

    try:
        return buffer.decode('utf8')           # '€'
    except UnicodeDecodeError:
        print("Could not decode buffer: %s" % buffer)

with open('data.json') as f:
    stringNew = f.read()
    data = json.loads(re.sub(r"(?i)(?:\\u00[0-9a-f]{2})+", unmangle_utf8, stringNew))
    print(data["titles"][13])