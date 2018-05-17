class Luhn(object):

    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def is_valid(self):
        if len(self.card_num) < 2 or not self.card_num.isdigit():
            return False

        nsum = 0        
        psum = 0
        for n in range(len(self.card_num)):
            
            temp = int(self.card_num[-1 - n]) % 10

            if n % 2 == 0:
                nsum += temp
            else:
                temp = temp * 2

                if temp > 9:
                    temp = (temp % 10) + 1
                
                psum += temp
        
        return (psum + nsum) % 10 == 0