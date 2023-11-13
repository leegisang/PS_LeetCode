class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ranked_paper_list = sorted(citations, reverse=True)
        for i in range(len(ranked_paper_list)):
            if ranked_paper_list[i] < i+1:
                return i
        return i + 1