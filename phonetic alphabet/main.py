import pandas


temp_data = pandas.read_csv("./day_26_spelling/nato_phonetic_alphabet.csv")
data = {row.letter:row.code for (index, row) in temp_data.iterrows()}


def spell():
    name = input("Enter a name: ").upper()
    try:
        code_list = [data[letter] for letter in name]
    except KeyError:
        print("Invalid input")
        spell()
    else:
        print(code_list)
spell()