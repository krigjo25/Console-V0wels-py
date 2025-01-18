def main():
        print(shorten(input("Type a text with vowels:").lower()))

        return

def shorten(arg):

    #   Initializing variables
    string = ''

    #   Initializing a list with vowels
    x = [
            'a','e','i',
            'o','u', 'y',
            'æ', 'ø', 'å']

    for i in str(arg).lower():

        if i not in x:
            string += i

    return string

if __name__ == '__main__':
    main()
