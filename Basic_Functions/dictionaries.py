def example():
    '''
    This example function demonstrates how to use dictionaries
    and their multiple functionalities 

    They are very similar to json and a useful way to store data structures. 
    '''

    mydict = {
        "Name": "Chris",
        "age": 22,
        "message" : "hello :) ✔"
    }

    print("Basic format of dictionary: ")
    print(mydict)

    print("\n This is how you can loop through and access each value")
    for x in mydict:
        print(x, ": ", mydict[x])

    print("\n You can also add and remove items from a dictionary")
    mydict.pop("message")
    mydict["hair_color"] = "Black"
    for x in mydict:
        print(x, ": ", mydict[x])

if __name__ == "__main__":
    example()