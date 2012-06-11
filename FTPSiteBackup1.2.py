from ftplib import FTP
import ftputil
import os
import datetime


def create_local_folder():
    now = datetime.datetime.now()
    folder_name = str(now.month) + '.' + str(now.day) + '.' + str(now.year)
    str(folder_name)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print 'Creating Backup Folder ' + folder_name
        return folder_name
    else:
        print 'Backup for ' + folder_name + ' already exists'
        return folder_name

def grab_files(folders): #function to download folders, if not a file it adds the file to the directory dictionary to be downloaded later
    directory_dic = {}
    names = azure.listdir(azure.curdir)
    for i in names:
        if azure.path.isfile(i):
                azure.download(i, i, 'b')  # remote, local, binary mode
                print 'Currently Downloading: ' + i + '...'
        else:
            directory_dic[i] = str(azure.getcwd() + '/' + i)
        return directories
    
def grab_directories(directory_dic,cfl):
    cfl = cfl
    if not directory_dic:
        print 'no directories left'
    else:
        for directory in directory_dic:
            azure.chdir(directory_dic[directory]) #change remote directory using the directory_dic
            local_sync(directory_dic[directory],cfl) #create corresponding local directory and change local working directory to it
            directory = {}
            ls = list_files(directory)
            grab_directories(ls,cfl)

def local_sync(directorypath,cfl):
    directorypathfixed = directorypath[32:]
    root_path = '/Users/Dylan/Documents/WebsiteBackups/'
    current_root_path = root_path + cfl + directorypathfixed
    os.mkdir(current_root_path) #create local directory, corresponding to the remote directory
    os.chdir(current_root_path)
           

def list_files(directories): #list files in remote directory
    names = azure.listdir(azure.curdir)
    for name in names:
        if azure.path.isfile(name):
            progress = 0
            print 'downloading ' + name + ' from ' + azure.getcwd()
            azure.download(name, name, 'b', callback = progress) #remote, local, binary mode
            print progress
            print 'downloaded ' + name
        else:
            working_directory = str(azure.getcwd() + '/' + name)
            directories[name] = working_directory
            print 'added directory ' + name + ' at ' + azure.getcwd()
    return directories


#start of program

directories = {} #dictonary of directories that grab_files finds    
azure = ftputil.FTPHost('azure.feralhosting.com','dylanpierce','uC04rSmfonvJ0XhI')
azure.chdir('www')
azure.getcwd()
print 'Listing files...'
print azure.listdir(azure.curdir)
os.chdir('/Users/Dylan/Documents/WebsiteBackups/')
pwd_local = os.getcwd()  #finding current working directory to append the date value to
cwd = str(os.getcwd())
print 'Current Local Directory: ' + str(cwd)
cfl = create_local_folder() #create local folder makes a local directory named after the current date
os.chdir('/Users/Dylan/Documents/WebsiteBackups/' + cfl)
directories = list_files(directories)
grab_directories(directories,cfl)

print 'Backup Complete!'


    

