from flask_restful import Api
from app import app
from .watsonSpeechToText import WatsonSpeechToText
from .azureSpeechToText import AzureSpeechToText
from .videoUtils import VideoUitls
from .watsonNLUTa import WatsonNLUTA
import os
env = os.environ.get("PROVIDER")
restServer = Api(app)

if(env == "ibm"):
    restServer.add_resource(WatsonSpeechToText, "/api/v1.0/transcribe/<string:model>")
else:
    restServer.add_resource(AzureSpeechToText, "/api/v1.0/transcribe/<string:model>")

restServer.add_resource(VideoUitls, "/api/v1.0/uploadVideo")
restServer.add_resource(WatsonNLUTA, "/api/v1.0/analyseText")