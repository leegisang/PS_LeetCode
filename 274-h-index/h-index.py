class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ranked_paper_list = sorted(citations, reverse=True)
        paper_num = len(ranked_paper_list)
        # if paper_num == 0:
        #     return 0
        for i in range(paper_num):
            ith_citations = ranked_paper_list[i]
            if ith_citations < i+1:
                return i
        return paper_num