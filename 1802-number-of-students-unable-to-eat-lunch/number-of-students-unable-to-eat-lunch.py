class Solution:
    def countStudents(self, st: List[int], sw: List[int]) -> int:
        for q in sw:
            if q not in st:
                return len(st)

            st.remove(q)

        return 0