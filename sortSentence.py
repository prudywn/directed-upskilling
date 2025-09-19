class Solution:
    def sortSentence(self, s: str) -> str:
        # Step 1: split into words
        words = s.split()

        # Step 2: sort words by the last character (index number)
        words.sort(key=lambda w: int(w[-1]))

        # Step 3: remove the digit and join back
        return " ".join(w[:-1] for w in words)
        