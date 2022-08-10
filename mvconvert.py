import os
from os.path import isfile, join
from PIL import Image

class PortraitConversion:
    def __init__(self):
        self.file_extensions = ('.jpg', '.png', '.jpeg')
        self.in_directory = f"{os.path.dirname(os.path.abspath(__file__))}\\{'pre_photos'}"
        self.out_directory = f"{os.path.dirname(os.path.abspath(__file__))}\\{'post_photos'}"
        self.sprite = Image.open('Template.png') #Name of file you want to add sprites too
        self.rpg_height = 144
        self.rpg_width = 144

    def run (self):
        pictures = self.get_files_from_in_directory()
        self.put_each_file_on_tilesheet(pictures)

    def get_files_from_in_directory(self):
        onlyfiles = [f for f in os.listdir(self.in_directory) if isfile(join(self.in_directory, f))]
        return [f for f in onlyfiles if f.endswith(self.file_extensions)]

    def put_each_file_on_tilesheet(self, pictures):
        name = input("What would you like to call these portraits: ")
        portrait_current_height = 0
        portrait_current_width = 0
        count = 0
        count2 = 0
        for picture in pictures:
            if(count == 8):
                self.sprite.save(self.out_directory + '/' + name + str(count2) + '.png')
                self.sprite = Image.open('Template.png')
                portrait_current_height = 0
                portrait_current_width = 0
                count = 0
                count2 = count2 + 1
            elif(count == 4):
                portrait_current_height = self.rpg_height
                portrait_current_width = 0
            portrait = Image.open(self.in_directory + '/' + picture)
            portrait = portrait.resize((144,144), 0)
            portrait_paste = (portrait_current_width, portrait_current_height, portrait_current_width + self.rpg_height, portrait_current_height + self.rpg_height)
            self.sprite.paste(portrait, portrait_paste)
            portrait_current_width = portrait_current_width + self.rpg_width
            count = count + 1
        print("Ok Done")
            


def main():
    portraitConverstion = PortraitConversion()
    portraitConverstion.run()

if __name__ == '__main__':
    main()