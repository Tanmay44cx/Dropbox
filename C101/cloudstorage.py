import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
      
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'R74iuCt-oaEAAAAAAAAAAR45el18-z31qo-PQ424jLkVoBtADG7uhU0c2-qIdk7Y'
    transferData = TransferData(access_token)

    file_from = input("Enter The Source File Path: ")
    file_to = input("Enter The Destination: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Uploaded")

main()