#!/usr/bin/env python
from PIL import Image, FontFile, ImageFont, ImageDraw
class RenderText2Image:
    
    ##Defines
    FULL_PATH_TO_FONT = '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'
    _bgcolor = None
    _fontColor = None
    _text = None
    _error, _errmsg = 1, None
    _outputFileName = None
    _img = None
    _font = None
    _draw = None
    
    def __init__(self, text, bgColor='#FFFFFF', fontColor='#000000', outputFileName="this"):
        ##Set global vars
        self._text, self._bgcolor, self._fontColor = text, bgColor, fontColor
        self._outputFileName = outputFileName
        self.makeBackground()
        
    def makeBackground(self):
        try:
            self._img = Image.new("RGB", (400, 400), self._bgcolor)
            self._draw = ImageDraw.Draw(self._img)
            self.setFontSize()
        except Exception, e:
            self._error, self._errmsg = 0, "Background could not be rendered ERR_MSG:" + e
    
    def setFontSize(self):
        print "set font size"
        fontsize = 1
        img_fraction = 1.7
        try:
            self._font = ImageFont.truetype(self.FULL_PATH_TO_FONT, fontsize)
            while self._font.getsize(self._text)[0] < img_fraction * self._img.size[0]:
                fontsize += 1
                self._font = ImageFont.truetype(self.FULL_PATH_TO_FONT, fontsize)
        except Exception, e:
            print "ERROR WITH FONT", e
            
        self.addText2Image()
    
    def parseText(self):
        import textwrap
        lines = textwrap.wrap(self._text, 50)
        return lines
    
    def addText2Image(self):
        lines = self.parseText()
        try:
            count = 0
            for line in lines:
                width, height = self._font.getsize(line)
                self._draw.text((0,(count*height)+2), line, fill=self._fontColor, font=self._font)
                count += 1
            self._img.save(self._outputFileName, "PNG")
        except Exception, e:
            print e;
            
    def getImage(self):
        return self._outputFileName if self._error else self._error