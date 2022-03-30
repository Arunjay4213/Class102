import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BEw1Sq2UTWuQ7rkdQs3xccsj1n-0v3dzdCxEln5xwRITE4nYZuQ7rTkhUPf4lqjzx8FMmYmG9Xa53k5K9ExMAdbmL_aKGqehPdT2Nd-KWjBysp4ajkGOUcjk9C-qwZiGFX8bHW0'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to input to dropbox: ")
    transferData.upload_file(file_from, file_to)

    print("file has been moved")
main()


