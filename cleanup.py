#!/usr/bin/env python3
import os
import os.path
import re

class filetype_defs:
  image = '.JPG,.JPEG,.JFIF,.PNG,.BMP,.GIF,.TIFF'.split(",")
  video = '.3GP,.3G2,.AVI,.MPG,.MPEG,.M2V,.MP4,.M4V,.MKV,.WEBM,.FLV,.WMV,.MOV,.QT,.OGV'.split(",")
  audio = '.OGG,.OGA,.MOGG,.OPUS,.MP3,.WAV,.AAC,.FLAC,.M4A,.M4B,.RA,.WMA'.split(",")

dirPic = os.getcwd() + "/" #os.path.expanduser("~/Dropbox/Camera Uploads/")

class Media:
  def __init__(self,f):
    self.file = f
    self.filetype = os.path.splitext(f)[1]
    if(f.startswith("Screenshot")):
      self.year = f[11:15]
      self.month = f[16:18]
    else:
      self.year = f[0:4]
      self.month = f[5:7]

def unarchivedFiles():
  pattern = re.compile("^(Screenshot )?\d{4}-\d{2}-\d{2}.*")
  files = [
    Media(f) for f in os.listdir(dirPic) if os.path.isfile(dirPic+f)
    and (
      os.path.splitext(f)[1].upper() in filetype_defs.image or 
      os.path.splitext(f)[1].upper() in filetype_defs.video or
      os.path.splitext(f)[1].upper() in filetype_defs.audio 
    ) and (
      pattern.match(os.path.splitext(f)[0])
    )
  ]
  return files;
  
if __name__ == "__main__":
  for f in unarchivedFiles(): 
    newpath = dirPic + f.year + "/" + f.month + "/"
    if(not os.path.exists(newpath)):
      os.makedirs(newpath)
    os.rename(dirPic + f.file, newpath + f.file)
