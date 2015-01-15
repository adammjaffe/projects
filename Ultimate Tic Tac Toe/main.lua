----
--
-- main.lua
--
----

-- Build home screen
display.setStatusBar( display.DefaultStatusBar )

-- Define reference points locations anchor ponts
TOP_REF = 0
BOTTOM_REF = 1
LEFT_REF = 0
RIGHT_REF = 1
CENTER_REF = 0.5

centerX = display.contentCenterX
centerY = display.contentCenterY
_W = display.contentWidth
_H = display.contentHeight

font = --[["Perpetua" or]] native.systemFont

-- Create app background

local bg = display.newImageRect( "assets/finishedAssets/background/woodTexture@320x480.png", _W, _H )
bg.x, bg.y = centerX, centerY

audioFile = audio.loadStream( "assets/finishedAssets/background/erasureAlways.mp3")
audio.play(audioFile,{
	channel = 1,
	loops = -1,
	})
audio.setVolume(0.5)

isSoundOn = audio.isChannelPlaying( 1 )

local storyboard = require("storyboard")

storyboard.gotoScene("homeScene")