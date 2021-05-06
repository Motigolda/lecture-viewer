import requests
import webbrowser
from Template import *

PATH_TEMPLATE = """sanitized """

class LectureViewer():
    def __init__(self, video_path, title="Lecture",description=""):
        self._load_template()

        self.set_video_path(video_path)
        self.set_title(title) 
        self.set_description(description)


    def set_title(self, title):
        self._video_title = title
    
    def get_title(self):
        return self._video_title

    def set_description(self, desc):
        self._video_description = desc

    def get_description(self):
        return self._video_description

    def set_video_path(self, video_path):
        self._video_path = video_path        

    def get_video_path(self):
        return self._video_path

    def _load_template(self, template_type="remote"):
        if template_type == "local":
            self._template = LocalTemplate()
        elif template_type == "remote":
            self._template = RemoteTemplate()   
        else:
            self._template = RemoteTemplate()  

    def _push_data_to_template(self):
        self._template.set_tags(self._video_path, self._video_title, self._video_description)
        self._template.save()

    def launch(self):
        self._push_data_to_template()
        webbrowser.open(self._template.get_video())

