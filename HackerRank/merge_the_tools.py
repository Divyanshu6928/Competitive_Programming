import textwrap     # it is used in formatting and wrapping text

def merge_the_tools(string, k):
    mylist = textwrap.wrap(string, k)
    mylist = [list(dict.fromkeys(item)) for item in mylist]
    new_list = []
    for item in mylist:
        item= "".join(item)
        print(item)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)