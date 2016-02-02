from __future__ import division
from string_manipulation.string_handler import state_handler

__author__ = 'ana'


prob = { 'a' : 8.167, 'b':1.492, 'c':2.782, 'd': 4.253, 'e':12.702, 'f' :2.228,'g':2.015,'h':6.094, 'i'	: 6.966, 'j':0.153,
'k'	:0.772, 'l':4.025, 'm':2.406, 'n': 6.749, 'o':7.507, 'p':1.929 , 'q': 0.095, 'r':5.987,'s'	:6.327,
't':9.056, 'u':2.758, 'v':0.978, 'w': 2.361, 'x':0.150, 'y'	:1.974, 'z'	:0.074}


class Game:
    def __init__(self, token, state, guess_num):
        self.status_dict = {'ALIVE' :0, 'DEAD' : 1, 'FREE': 2}
        self.token = token
        self.state = state.split()
        self.guess_num = guess_num
        self.status = 0;
        self.seen = []
        self.dict = []
        with open('./4000-most-common-english-words-csv.csv')as common_words:
            for common_word in common_words:
                self.dict.append(common_word.rstrip())

    def next_guess(self):
        #generate current template for each word
        #generate new dictionary for each word
        current_dicts = []
        for word in self.state:
            new_dict = state_handler.get_matching_dict(word)
            current_dicts.append(new_dict)


        #generate frequency arrays
        freq_arrys = []
        com_freq_arrys = []
        for dict in current_dicts:
            freq_arr = state_handler.generate_freq_arr(dict)
            common_freq_arr = state_handler.generate_common_freq_arr(dict, self.dict)

            self.apply_common(common_freq_arr, freq_arr)
            freq_arrys.append(freq_arr)



        return self.get_best_char(freq_arrys)

    """
    applies the effect of being a frequent word to the generated frequency array
    """
    def apply_common (self, common_freq_arry, freq_array):
        for ind, freq in enumerate(freq_array):
            freq_array[ind] = (freq_array[ind] * 5 + common_freq_arry[ind] * 5) / 10
        return freq_array


    """
    applies general frequency of each character (from wikipedia) to tune  computed frequency
    """
    def apply_preprob(self, freq_array):
        for ind, freq in enumerate(freq_array):
            freq_array[ind] = (freq_array[ind] * 8 + prob[chr(ord('a') + ind)] * 2) / 10
        return freq_array

    def percent_found(self,str):
        count = 0
        for i in str:
            if i == '_':
                count = count + 1
        return (len(str) - count)/ len(str)

    def get_best_char(self,freq_arrays):

        #normalize all frequency arrays
        for ind, raw in enumerate(freq_arrays) :
            if max(raw) == 0:
                pass
            else:
                freq_arrays[ind] = [float(i)/max(raw) for i in raw]
                raw = freq_arrays[ind]
                freq_arrays[ind] = [float(i)/max(raw) for i in raw]


        #merge results for different words
        final_weights = [0] * 26
        for ind, arr in enumerate(freq_arrays):
            coof = self.percent_found(self.state[ind]) / len(self.state[ind])
            for i in range(26):

                #shorter words and more complete words have greater weights
                final_weights[i] = final_weights[i] + (arr[i]*0.8 + (coof)*0.2) * (1 / len(self.state[ind]))

        self.apply_preprob(final_weights)


        ###################### find  new max #######################
        max_value = max(final_weights)
        max_index = final_weights.index(max_value)
        g_char  = max_index + ord('A')

        while g_char in self.seen:
            final_weights = final_weights[:max_index] + final_weights[max_index+1 :]
            max_value = max(final_weights)
            max_index = final_weights.index(max_value)
            g_char  = max_index + ord('A')

        self.seen.append(g_char)
        return chr(g_char)



    def if_lost(self):
        if self.guess_num == 0:
            return True
        return False

    def update(self, res):
        self.state = res['state'].split()
        self.guess_num = res['remaining_guesses']
        self.status =self.status_dict[res['status']]



