name = ["moskov","claude","grange","karrie"]

userdata = input("Do you want to remove any element in this list? : ")

if userdata == "yes":
    userdata = input("what name you want to remove?")

name.remove(userdata)

print(name)
