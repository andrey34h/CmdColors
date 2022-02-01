import colorama
import letters
import subprocess
import random
import keyboard
#By Andrey
#Discord: &Andrey#3839

#This is only a simple cmd program for return colored letters (Only Upper and Lower Letters)

colorama.init();

class COLORED_LETTERS:
    def __init__(self):
        self.BAD_COLORS:list = ["BLACK", "WHITE", "LIGHTBLACK_EX", "LIGHTWHITE_EX", "RESET"];
        self.colors:dict = vars(colorama.Fore);
        self.filtered_colors:list = self.__filter_(self.colors);  # filtered_colors: list = list(colors[x] for x in colors if x not in BAD_COLORS);
        self.WORD:str = "";
        if self.__COLOR_LETTERS():

            self.WORD_FINAL:list = list();
            for x in self.WORD:
                if x.islower():
                    self.WORD_FINAL.append((letters.LETTERS_LOWER[str(x)]));
                elif x.isupper():
                    self.WORD_FINAL.append(letters.LETTERS_UPPER[str(x)])
                elif str(x) == " ":
                    self.WORD_FINAL.append("\n");
                else:
                    #This is only for prevention // will never be execute
                    self.WORD_FINAL.append(letters.NONE_LETTER.replace("\n",""));


        self.colored_letters = "\n".join(list(random.choice(self.filtered_colors) + x for x in self.WORD_FINAL));
        print(self.colored_letters);
        keyboard.wait("enter")

    def __del__(self):
        print(colorama.Fore.BLUE + "I hope you liked it!");
        print(colorama.Style.RESET_ALL);

    def __COLOR_LETTERS(self) -> bool:
        Done:bool = not bool;
        cache:list = list();
        while not Done:
            user_input:str = str(input("Palabra a colorear: "));
            cache:bool = all(x in letters.ALLOWED_CHARS for x in user_input);
            if cache:
                subprocess.run(["cls"], shell=True);
                self.WORD:str = user_input;
                return True;
            else:
                continue;

    def __filter_(self, args: dict) -> list:
        if (type(args)) != self.__filter_.__annotations__["args"]:
            return list();
        else:
            list1: list = list();
            for x in args:
                if x not in self.BAD_COLORS:
                    list1.append(self.colors[x]);
            return list1;

if __name__ == "__main__":
    COLORED_LETTERS();

