# importing required modules
from IPython.display import clear_output
from zipfile import ZipFile
import os

def get_all_file_paths(directory):

    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths       

def main():
    # path to folder which needs to be zipped
    directory = input("Folder Location:- ")

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    print(file_paths[0].split("/")[-1]+"\nto...\n"+file_paths[-1].split("/")[-1])
    print("Total:-",len(file_paths),"files.")

    # writing files to a zipfile
    savehere=input("Save Location:- ")
    nameofzip=input("File name:- ")
    if savehere[-1]!="/":
        savehere=savehere+"/"
    if os.path.isdir(savehere)==False:
        os.mkdir(savehere)
    fullname="/content/drive/MyDrive/"+savehere+nameofzip+".zip"
    fc=0
    with ZipFile(fullname,'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)
            os.system('clear')
            clear_output()
            print(nameofzip+".zip")
            print("Total:-",len(file_paths),"files.")
            print("Zipping in progress...")
            fc+=1
            print("["+("-"*fc)+">"+(" "*(len(file_paths)-fc))+"]\n"+str(fc)+"/"+str(len(file_paths)))
            
            if file==file_paths[-1]:
            	print ("Zipping Finished.")
            else:
            	print(file.split("/")[-1])

            

    print('All files zipped successfully!')     


if __name__ == "__main__":
    main()
