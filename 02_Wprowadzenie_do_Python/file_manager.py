
class FileManager:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        handle = open(self.file_name, 'r', encoding='utf-8')
        data = handle.read()
        handle.close()
        return data

    def update_file(self, text_data):
        handle = open(self.file_name, 'a', encoding='utf-8')
        handle.write(text_data)
        handle.close()


