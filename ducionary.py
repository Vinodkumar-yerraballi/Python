def sort_dict():
    key_values={}
    key_values[2]=123
    key_values[3]=44
    key_values[1]=55
    key_values[5]=999
    key_values[4]=58
    print("key_value",key_values)
    for i in sorted(key_values.keys()):
        print(i,end="")
 
def main():
    # function calling
    sort_dict()
 
 
# Main function calling
if __name__ == "__main__":
    main()
