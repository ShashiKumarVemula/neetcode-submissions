class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == '}' and st:
                if st[-1] == '{':
                    st.pop()
                else: return False
            elif ch == ')' and st:
                if st[-1] == '(':
                    st.pop()
                else: return False
            elif ch == ']' and st:
                if st[-1] == '[':
                    st.pop()
                else: return False
            else : 
                st.append(ch)
        if st:
            return False
        return True
        

        