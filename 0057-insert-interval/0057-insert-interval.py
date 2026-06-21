class Solution(object):
    def insert(self, intervals, newInterval):
        st,en = [],[]
        for val in intervals:
            st.append(val[0])
            en.append(val[1])
        st.append(newInterval[0])
        en.append(newInterval[1])
        st.sort()
        en.sort()
        ans = [[st[0],en[0]]]
        for i in range(1,len(st)):
            if st[i] <= ans[-1][-1]:
                ans[-1][-1] = en[i]        
            else:
                ans.append([st[i],en[i]])
        return ans