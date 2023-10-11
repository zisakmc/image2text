import easyocr

class TextFromImage:
    
    """
    The extract func take the image and feed into easyocr,
    and store the predicted value in the output variable

    """
    def extract(self,img):
        self.reader = easyocr.Reader(lang_list=['en'])
        self.text = self.reader.readtext(img)
        self.output=''

        for i in range(len(self.text)):
            # take only above 50% conf value
            if self.text[i][2] > 0.5:
                """
                the easyocr output:
                [
                ([[x1,y1],[x2,y2]],'some string', confident value]),
                ([[x1,y1],[x2,y2]],'some string', confident value]),
                ]

                so we take text[something][2]

                """
                self.output += ' ' + self.text[i][1]
        
        return self.output
