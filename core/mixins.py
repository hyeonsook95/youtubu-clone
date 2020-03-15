
class UploadPathMixin:

    def data_upload_to(instance, filename):
        
        """ 미디어 파일의 이름을 hex 값으로 변경한다. """

        uuid_name = uuid4().hex[:20]
        extension = os.path.splitext(filename)[-1].lower()
        print(instance)
        return f'{uuid_name}{extension}'