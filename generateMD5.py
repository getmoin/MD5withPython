import hashlib as h
import json

f = open('./sample.json')
input = json.load(f)


def functions():    
    try:
        #Taking a Key value from the JSON data & Encoding it in UTF-8 format
        filteredMsg = input['message']
        encodeMD5 = filteredMsg.encode('utf-8')

        #Generate MD5 Checksum for the data and print it
        generateMD5 = h.md5(encodeMD5).hexdigest()
        print(generateMD5)

    except Exception as er:
        print("Error occured while generating the MD5 Checksums. The error is: ", er)

functions()