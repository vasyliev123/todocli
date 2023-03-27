def rearange_items(df):
    res = {}
    for i, (key, item) in enumerate(df.items()):
        new_key = str(i)
        res[new_key]= item
    return res

def print_dictionary(df, max_length=60):
    print("\tYour tasks:\t")
    for task in df:
        if df[task]["due_date"] == None:
            print(f"\t{task} - {break_into_lines(df[task]['description'])}\t")
        else:
            print(f"\t{task} - {break_into_lines(df[task]['description'])} - {df[task]['due_date']}\t")
def break_into_lines(str, max_length=60):
    new_item = ""
    j = 0
    s = 0
    for i, ch in enumerate(str):
        if s >= max_length and ch == " ":
            new_item = new_item + str[j:i] + "\n\t"
            j = i
            s = 0
        s = s + 1
    new_item = new_item + str[j:]
    if new_item == "":
        new_item = str
    return new_item
