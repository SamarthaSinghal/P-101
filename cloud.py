import dropbox 
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'q2vzry6jFoIAAAAAAAAAAf8QnH5mEU1E1DuyTSxEQgqaCUVu3R9MvFy_ATSVdgKT'
    transferData = TransferData(access_token)

    file_from = input ("Enter File Path")
    file_to = input ("Enter File Path") 
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
