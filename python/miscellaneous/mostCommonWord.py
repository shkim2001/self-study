class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        set_banned = set(banned)
        
        para_lower = paragraph.lower()
        para_lower = re.sub(r"[!?',;.]+",' ',para_lower)
        
        word_list = para_lower.split()
        counter = Counter(word_list).most_common()

        for word,_ in counter:
            if word not in set_banned:
                result = word
                break
        return result