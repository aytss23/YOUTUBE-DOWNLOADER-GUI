import pytubefix

DOWNLOAD_PATH = "..\\downloads\\"

class YoutubeDownloaderProcces:
    
    @staticmethod
    def getOnlyAudioStreams(streamObject) -> pytubefix.StreamQuery: return streamObject.streams.filter(only_audio = True)

    @staticmethod
    def getOnlyVideoStreams(streamObject) -> pytubefix.StreamQuery: return streamObject.streams.filter(only_video = True)

    @staticmethod
    def getProgressiveStreams(streamObject) -> pytubefix.StreamQuery: return streamObject.streams.filter(progressive = True)

    @staticmethod
    def getStreamData(youtubeLink) -> pytubefix.YouTube:
        streamObject = pytubefix.YouTube(youtubeLink)
        return streamObject
    
    @staticmethod
    def downloadStream(streamObject, downloadPath = DOWNLOAD_PATH) -> pytubefix.Stream: return streamObject.download(downloadPath)