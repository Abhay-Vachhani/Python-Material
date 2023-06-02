from builtins import print as pyPrint, input as pyInput
from ast import literal_eval
from io import BytesIO
import pip
import os


os.system('title Exercise - 1 by Abhay M. Vachhani')


def install(package):
    pip.main(['install', package])


try:
    import pygetwindow as pyWindow
    import pyautogui
    import win32clipboard
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError:
    os.system('title Exercise - 1 by Abhay M. Vachhani - Installing Modules')
    try:
        install('PyGetWindow')
        install('pillow')
        install('pyautogui')
        install('pywin32')
    except:
        print()
        print('Make sure you are connected to internet')
        exit()


    print()
    print('All required modules are installed. Run the program again.')
    exit()

imagess = [[]]
def generateImages():
    imgWidth = 0
    imgHeight = 0
    imgMaxHeight = 0

    preI = 0
    for j, images in zip(range(len(imagess)), imagess):
        if len(images) > 0:
            imgWidth = 0
            imgHeight = 0
            imgMaxHeight = 0
            for im in images: 
                imgWidth = im.width if im.width > imgWidth else imgWidth
                imgMaxHeight = im.height if im.height > imgMaxHeight else imgMaxHeight
                imgHeight += im.height
            img = Image.new('RGB', (imgWidth * 2 + 15, (len(images) / 2).__ceil__() * 5 + 5 + ((len(images) / 2).__ceil__() * imgMaxHeight)), color=(180, 180, 180))
            preI = 0
            for i, image in zip(range(len(images)), images):
                x = 0 if i % 2 == 0 else imgWidth + 5
                y = preI
                img.paste(image, (x + 5, y + 5))
                if i % 2 == 1:
                    preI = y + imgMaxHeight + 5

            os.makedirs('images', exist_ok=True)
            img.save(f'images/output_{j}.png')

def saveImage(outputId):
    window = pyWindow.getActiveWindow()
    img = pyautogui.screenshot(region=(window.left + 9, window.top + 1, window.width - 18, window.height - 10))
    image = Image.new(img.mode, (img.width, img.height + 90), color=(255, 255, 255))
    image.paste(img, (0, image.height - img.height))
   
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), 'Name: Abhay Vachhani', (0, 0, 0), font=ImageFont.truetype('calibri', 30))
    draw.text((10, 50), f'Output: {outputId}', (0, 0, 0), font=ImageFont.truetype('calibri', 30))
    img = image
    
    global imagess
    im = img.convert('RGB')
    imagess[-1].append(im)
    if len(imagess[-1]) == 4:
        imagess.append([])


def print(*args, **kwargs):
    pyPrint('\t\t\t', *args, **kwargs, sep='')


def input(__prompt = '', getNumber = False):
    input = pyInput(f'\t\t\t{__prompt}: ')
    if getNumber:
        try:
            return literal_eval(input) if type(literal_eval(input)) in [int, float] else None
        except:
            return None
    return input


def printT(*args, **kwargs):
    pyPrint('\t\t', *args, **kwargs, sep='')


class PracticeSet():
    def print(self, programId):
        pyPrint(f'\t:: Program: {programId} ::\n')
        printT('Question:')
        exec(f'print(self._{programId}.__doc__)')
        printT('Output:')
        exec(f'self._{programId}()')
        print()
   
    def _1(self):
        '''Insert string into the variable and perform following tasks:
                            -Print the type of the variable with a message “The type of the variable is:”
                            -Print the string with a message “The string is:”
                            -Display the 3rd character of the string
                            -Display character from 4th to 6th from the string
                            -Change the 3rd character of the string replace it with 'A' '''
        string = '123456789'
        print(f'The type of the variable is: { type(string) }')
        print(f'The string is: { string }')
        print(f'Third character is: { string[2] }')
        print(f'4th to 6th: { string[3:6] }')
        print(f'Before replace: { string }')
        string = "".join([string[i] if i != 2 else "A" for i in range(len(string))])
        print(f'After replace: { string }')
    
    def _2(self):
        '''Store the integer value using int() class.
                            -Insert an Octal value in the variable and convert it to decimal.
                            -Insert the binary value in the variable and convert it to decimal.
                            -Insert the float value in the variable convert it to decimal.'''
        no = int('123456789')
        print(f'Number: { no }')
        no = 0o1001
        print(f'Octal 2 Decimal: 0o1001 -> { no }')
        no = 0b1001
        print(f'Binary 2 Decimal: 0b1001 -> { int(no) }')
        no = float(10.9)
        print(f'Float 2 Decimal: { no } -> { int(no) }')
    
    def _3(self):
        '''Create a list with variety of data and perform following tasks:
                            -Print all the element of the list.
                            -Display the class.
                            -Display the first element of the list.
                            -Display the 4th element of the list using negative index.
                            -Change the 4th element of the list.'''
        
        lst = [
            101,
            1,
            'Abhay',
            [
                1,
                101,
                'Abhay',
            ]
        ]

        print(f'List data: { lst }')
        print(f'Class of list: { type(lst) }')
        print(f'First element of list: { lst[0] }')
        print(f'4th element of list using negative index: { lst[-1] }')
        lst[-1] = {
            'name': 'Abhay',
            'Number': 100,
            10: 20
        }
        print(f'After changing 4th element: { lst }')

    def _4(self):
        '''Create a tuple using a tuple() class.
                            -Modify the 1st element of the tuple.
                            -Display the 3rd to 6th element from the tuple.
                            -Display the 3rd to 6th element from the tuple using negative index.'''

        tpl = tuple('123456789')

        print(f'Tuple: { tpl }')
        tpl = [i if i != 0 else 'Abhay' for i in range(len(tpl))]
        print(f'After changing 1st element: { tpl }')
        print(f'3rd to 6th element: { tpl[3:7] }')
        print(f'3rd to 6th element using negative index: { tpl[-6:-2] }')

    def _5(self):
        '''Create a dictionary with at least 10 values and perform the following task:
                            -Display all the elements of the dictionary.
                            -Check the class of the dictionary you made.
                            -Display the value stored in the key 7.
                            -Change the value stored in the key 7.
                            -Display all the values only.'''

        dic = {
            1 : 'A 01',
            2 : 'A 02',
            3 : 'A 03',
            4 : 'A 04',
            5 : 'A 05',
            6 : 'A 06',
            7 : 'A 07',
            8 : 'A 08',
            9 : 'A 09',
            10: 'A 10',
        }

        print(f'Dict: { dic }')
        print(f'Class of dict: { type(dic) }')
        print(f'Value at 7 in dict: { dic.get(7) }')
        dic[7] = 'B 07'
        print(f'After changing value at 7 in dict: { dic }')
        print(f'Values only: { ", ".join(dic.values()) }')

    def _6(self):
        '''Create a set containing varieties of value and perform following task:
                            -Try to insert the duplicate value.
                            -Add two values in the set.
                            -Remove two values from the set.'''

        st = set(range(5))
        print(f'Set: { st }')
        st = set(list(st) + list(range(5)))
        print(f'After adding duplicate values: { st }')
        st.update([5, 6])
        print(f'After adding two values: { st }')
        st.pop()
        st.remove(5)
        print(f'After removing two values: { st }')

    def _7(self):
        '''Create a set containing varieties of value and perform following task (the set must be not modifiable):
                            -Try to insert the duplicate value.
                            -Add two values in the set.
                            -Remove two values from the set.'''

        st = frozenset(range(5))
        print(f'Set: { st }')
        st = frozenset(list(st) + list(range(5)))
        print(f'After adding duplicate values: { st }')
        try:
            st[4] = 5
            st[5] = 6
            print(f'After adding two values: { st }')
        except Exception as e:
            print(f'Error: { e }')
        try:
            del st[2]
            del st[4]
            print(f'After removing two values: { st }')
        except Exception as e:
            print(f'Error: { e }')
        print(f'Set: {st}')

    def _8(self):
        '''Create a bytes and perform the following tasks:
                            -Display the first element using negative index.
                            -Display the last element using positive index.
                            -Add two values in to it.
                            -Modify the last element.'''

        bys = bytes(range(15, 10, -1))
        print(f'Bytes: { bys }')
        print(f'Bytes: { list(bys) }')
        print(f'First element of bytes using negative index: { bys[-5] }')
        print(f'Last element: { bys[len(bys)-1] }')
        bys = bys.__add__(bytes([10, 12]))
        print(f'After adding two  elements to bytes: { list(bys) }')
        try:
            bys[-1] = 20
            print(f'Bytes: { list(bys) }')
        except Exception as e:
            print(f'Error: { e }')
    
    def _9(self):
        '''Create a bytes array and perform the following tasks:
                            -Display the first element using negative index.
                            -Display the last element using positive index.
                            -Add two values in to it.
                            -Modify the last element.
                            -Remove the last values from the set.'''

        bys = bytearray(range(15, 10, -1))
        print(f'Bytes Array: { bys }')
        print(f'Bytes Array: { list(bys) }')
        print(f'First element of bytes array using negative index: { bys[-5] }')
        print(f'Last element: { bys[len(bys)-1] }')
        bys = bys.__add__(bytes([10, 12]))
        print(f'After adding two  elements to bytes: { list(bys) }')
        bys[-1] = 20
        print(f'After modifying last element: { list(bys) }')
        bys.remove(20)
        print(f'After removing last element: { list(bys) }')

if __name__ == '__main__':
    os.system('title Exercise - 1 by Abhay M. Vachhani')
    practiceSet = PracticeSet()
    while True:
        os.system('clear || cls')
        choice = input('''
        \b\b\b\b0       Exit
    1 - 9  Run Program
    Enter your choice''', True)


        if choice == 0:
            break
        elif choice > 9 or choice <= -10:
            print('Please enter valid program number')
            print()
            pyInput('Press any key to continue...')
            saveImage('Invalid Input')
            continue


        if choice < 0:
            choice = 10 + choice
        print()
        practiceSet.print(choice)
        pyInput('Press any key to continue...')
        saveImage(f'Program - {choice}')


    pyPrint('\nBye...')
    saveImage('Exit')
generateImages()