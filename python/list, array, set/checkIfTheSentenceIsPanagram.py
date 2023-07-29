class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        sentenceAlpha = set()

        for character in sentence.lower():
            if character.isalpha():
                sentenceAlpha.add(character)

        return len(sentenceAlpha) == 26
