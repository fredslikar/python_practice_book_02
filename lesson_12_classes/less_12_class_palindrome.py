class PalindromString(str):
    def ispalindrom(self):
        self = self.lower()
        i = 0
        j = len(self) - 1
        while i < j:
            if self[i] != self[j]:
                return False
            i = i + 1
            j = j - 1
        return True

word1 = PalindromString('Radar')
word2 = PalindromString('Rader')
print(word1, 'is palindrom?', word1.ispalindrom())
print(word2, 'is palindrom?', word2.ispalindrom())
