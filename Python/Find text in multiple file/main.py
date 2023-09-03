import os

def isVinod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

    # Detect all forms of vinod like ViNod
    if "vinod" in fileContent.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    # Listing the cntents of this folder
    dir_contents = os.listdir()

    nVinod = 0
    # For each text file, run isVinod for them
    for item in dir_contents:
        if item.endswith('txt'):
            # print(f"Detecting Vinod in {item}")
            flag = isVinod(item)
            if(flag):
                print(f"**** Vinod found in {item}!!!!!")
                nVinod+=1
            else:
                print(f"Vinod not found in {item}")

    print(f"{nVinod} files found with Vinod hidden into them")
