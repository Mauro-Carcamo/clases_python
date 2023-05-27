class CustomHtttpException(Exception):
    def __init__(self, code = 500, _messege="Internal Server Error"):
        self.code = code
        self.message = _messege

try:
    raise CustomHtttpException
except Exception as error:
    print(error.args)

try:
    raise CustomHtttpException
except Exception as error:
    print(error.code)
    print(error._mesagge)

    