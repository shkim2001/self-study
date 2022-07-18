class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = collections.Counter(words[0])
        for word in words:
            res = res & collections.Counter(word)
        return list(res.elements())
        