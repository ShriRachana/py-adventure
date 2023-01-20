prompt = input("Do you need the same odd/even ?")
#multi line explanantion for input prompting is not possible with int/number --> need to check why the error occurs though
#prompt += "\nCan I ad a line"
prompt = int(prompt)

if prompt % 2 ==0 :
    print("even")

else:
    print("odd")