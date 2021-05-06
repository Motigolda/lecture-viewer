import requests
import tempfile

URL_LECTURE_VIEWER   = "https://motigolda.github.io/lecture-viewer/"
TEMPLATE_FILE_NAME    = "template.html"
LOCAL_LECTURE_VIEWER_DIR = ""
VIDEO_FILE_FULL_PATH = tempfile.gettempdir() + "\\video_file.html"
class Template():
    def _get_template(self, template_dir=LOCAL_LECTURE_VIEWER_DIR):
        self._template_text = "" # todo

    def set_tags(self, video_path, title="lecture", description=""):
        self._template_text = self._template_text.replace("{$!title!$}", title)
        self._template_text = self._template_text.replace("{$!description!$}", description)
        self._template_text = self._template_text.replace("{$!video!$}", video_path)
    def save(self, path=VIDEO_FILE_FULL_PATH):
        with open(path, 'w+', encoding="utf8") as video_file:
            video_file.write(self._template_text)
    
    def launch(self):
        pass
    
    def get_video(self):
        return VIDEO_FILE_FULL_PATH
        
    @staticmethod
    def local_exists(self):
        pass

class LocalTemplate(Template):
    def __init__(self):
        self._get_template()

    def _get_template(self, source_dir=LOCAL_LECTURE_VIEWER_DIR):
        try:
            with open(source_dir + TEMPLATE_FILE_NAME, 'r', encoding="utf8") as template_source:
                self._template_text = template_source.read()
        except (FileNotFoundError ,IOError) as err:
            print("Error with finding template at %s" % source_dir)
            exit()


class RemoteTemplate(Template):
    def __init__(self):
        if self._connection_works():
            self._get_template()
        else:
            print("No internet connection")
            exit()
    def _get_template(self, source_dir=URL_LECTURE_VIEWER):
        self._template_text = requests.get(source_dir + TEMPLATE_FILE_NAME).text

    def _connection_works(self):
        url = "http://www.google.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
        except (requests.ConnectionError, requests.Timeout) as exception:
            return False

        return True

def main():
    template = RemoteTemplate()
    template.set_tags(r"C:\Users\motig\OneDrive\ראשי\ז. לימודים כלליים\ב. מכללה\שנה א\סמסטר ב\חדוא 1\חומר\הרצאות\hedva_har_27.4.mp4")
    template.save()

if __name__ == '__main__':
    main()