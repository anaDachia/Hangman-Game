from __future__ import division
__author__ = 'ana'

class state_handler:


    @classmethod
    def get_words(cls, state_str):
        words = state_str.split()
        return words

    """
    checks if current template matches with a dictionary word or not
    """
    @classmethod
    def match_word(cls, dict_word, template):
        #dict_word = dict_word.rstrip()
        if len(dict_word) != len(template):
            return False
        else:
            for ind, w in enumerate(template):
                if w != dict_word[ind] and w != "_":
                    return False
        return True

    """
    for each word generates a matching dictionary based on a given template
    """
    @classmethod
    def get_matching_dict(cls, template):
        new_dict = []
        with open('./dictionary.txt')as dict:
            for word in dict:
                if state_handler.match_word(word.rstrip(),template):
                    new_dict.append(word.rstrip())
        return new_dict


    """
    computes the percentage of visiting a character in dictionary words (#words containing this char / whole words)
    """
    @classmethod
    def generate_freq_arr(cls, dict):
        freq = [0] * 26
        for word in dict:
            seen= {}
            for ch in word:
                ind = ord(ch) - ord('A')
                if (ch not in seen.keys()):
                    freq[ind] = freq[ind] + 1
                seen[ch] = True
        for ind, f in enumerate(freq):
            if len(dict) ==0:
                freq[ind]
            else:
                freq[ind] = freq[ind] / len(dict)
        return freq

    """
    same as generate_freq_arr but computing for words present in 4000 most common words
    """
    @classmethod
    def generate_common_freq_arr(cls, dict, common_words):
        new_dict = []
        for word in dict:
            if word.lower() in common_words:
                new_dict.append(word)
        return state_handler.generate_freq_arr(new_dict)



