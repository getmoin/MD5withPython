# MD5 Checksums with Python

## Introduction
The world of computing is filled with Cloud, Distributed Computing, and Containers. With this tech in the market, we rarely find an organization using On-prem servers. Hybrid cloud and Intra-cloud is a common practices.

For example, If you take Data Engineering concepts, an Engineer will take data from multiple sources, and processes it in multiple tools for different analysis goals. And to transmit data from one source to another, it's extremely important to verify the data we sent from the source is the exact replica we receive at the destination.


## History MD5's
To figure this out, early engineers and computer scientists came up with a concept called MD5 Checksums. It is a Hashing algorithm that will generate a unique Hash code for a set of Data. So, when we transmit data, the TCP protocol will hash the data, and at the reception, the TCP protocol will validate the hashed code. If it matches then it sends it to the application layer. If not, it will fail the received packet. 

**Fact Check: **Now, if you are using TCP anywhere in your application (the Internet runs on TCP/IP protocol) then technically, you do not need this as it's a built-in feature. 

**Well, what is MD5?** If you google it, you may find a good technical mumbo jumbo. And for my beginner viewers, I will try to explain it in simple terms. 
So it's basically a Crypto-graphic Algorithm with 32 hexadecimal characters (Hexadecimal - 16 symbols or digit values from 0 to 9, & A, B, C, D, E, F.) If we give data to this Algorithm, it will generate a unique 32-character Hexadecimal value. That's it!

## Applications/Demand:
But some applications have tight validation rules and strong compliance policies. Like Health and pharmacy-related data, Aerospace and aviation-related data, military and defense-related data, and so on and so forth. (If it's too critical, they may use some other / their own algorithms. But the concept of the Algorithm remains the same).

## Now, how to Implement it?
Python language is known for its libraries. An open-source language with lots of dev community around. So yes, we do already have an Algorithm that specifically implements the MD5 Checksums. It can be imported from the haslib package which is pre-installed in Python 3.9

So, lets see how we can implement the code:
```python
   import hashlib as h
    import json
    
    f = open('./sample.json')
    input = json.load(f)
    
    def functions():
        try:
            filteredMsg = input['message']
            encodeMD5 = filteredMsg.encode('utf-8')
    
            generateMD5 = h.md5(encodeMD5).hexdigest()
            print(generateMD5)
    
        except Exception as er:
            print("Error occured while generating the MD5 Checksums. The error is: ", er)
    
    functions()
```
As we can see, we can implement it pretty easily. We just need to import the hashlib package, take the data, encode the data into UTF-8 format, and boom, run a small function called h.md5, and you are good to go. That's it!

Lets check the sample data just for reference:
```json
{
    "message": "904, 1004, 1251, 4283, 4796, 6099, 7834, 7972, 8749, 8885, 9423, 10474, 10917, 10941, 11719, 11745, 21009, 28430, 29258, 29360, 29614, 30611, 33072, 34607, 34832, 39192, 40736, 41716, 42538, 42724, 43258, 43708, 45531, 47079, 48533, 49511, 52576, 55285, 56179, 56180, 56706, 56896, 57212, 57402, 58643, 58715, 61024, 61281, 65073, 65404, 67351, 67782, 67923, 68563, 68592, 70314, 71577, 72067, 74707, 75396, 77760, 78835, 79412, 79844, 81637, 83929, 84621, 86934, 91025, 91950, 92284, 92768, 93388, 94654, 95941, 96584, 99700"
}
```
This is JSON data with the message as a Key value and some random list of comma-separated integers in the pair value.

By generating this code, we have the hex value of dd45093cbbf7a144eba0bca9b3fe82f9
So this is how you can generate an MD5 Checksum for your data in simple steps with Python.

I tried my best to explain it neatly. I hope you did not find difficulty reading this post. 
Thanks, and have a great day!

- Moin Mohd