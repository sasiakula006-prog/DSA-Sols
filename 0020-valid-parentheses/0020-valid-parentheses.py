class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s)%2:
            return False

        d = {'(':')','[':']','{':'}'}
        for val in s:
            if val in d:
                st.append(val)
            else:
                if st and val== d[st[-1]]:
                    st.pop()
                    continue
                else:
                    return False

        return len(st)==0
