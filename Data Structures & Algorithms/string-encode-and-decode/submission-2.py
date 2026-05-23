class Solution:

    def encode(self, strs: List[str]) -> str:
        s1 = ''
        for s in strs:
            s1+=str(len(s))+'#'+s
        return s1

    def decode(self, s: str) -> List[str]:
        i=0
        print(s)
        ans=[]
        while i<len(s):
            # print(i)
            j=i 
            while j<len(s) and s[j]!='#':
                j+=1
            n=int(s[i:j])+1
            # print(s[i+1:i+n])
            ans.append(s[j+1:j+n])
            i=j+n
        return ans

        