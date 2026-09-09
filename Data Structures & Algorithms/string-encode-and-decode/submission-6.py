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
        while i < n:
            j=i
            while s[i]!='#':
                i+=1
            str_len = int(s[j:i])
            decoded_strs.append(s[i+1:i+str_len+1])
            i += str_len+1
        return decoded_strs
