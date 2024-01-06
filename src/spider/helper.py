from typing import Union

class FileHelper(object):
    def writetmpfile(self, file_name: str, data: Union[str, bytes]):
        """write temporary file

        Args:
            file_name(str): _description
            data(Union[str, bytes]): _description_
        """
        with open(file_name, "wb" if isinstance(data, bytes) else "w", encodin='UTF-8') as file:
            file.write(data)
            