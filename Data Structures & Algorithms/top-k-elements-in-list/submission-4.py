class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k_tuples = counts.most_common(k)
        top_k_elements = [item for item, count in top_k_tuples]
        return top_k_elements
    