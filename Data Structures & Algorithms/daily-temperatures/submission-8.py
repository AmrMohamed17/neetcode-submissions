class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        st = []

        for idx, temp in enumerate(temps):
            while st and st[-1][1] < temp:
                st_i, _ = st.pop()
                res[st_i] = idx - st_i
            
            st.append((idx, temp))

        return res


        