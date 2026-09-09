class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s))+"#"+s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        n = len(s)
        print(s)
        while s:
            hash_index = s.index('#')
            # print(hash_index)
            str_len = int(s[:hash_index])
            # print(str_len)
            decoded_strs.append(s[hash_index+1:hash_index+str_len+1])
            # print(decoded_strs)
            i = hash_index+str_len+1
            s = s[i:]
            # print(s)
        return decoded_strs
