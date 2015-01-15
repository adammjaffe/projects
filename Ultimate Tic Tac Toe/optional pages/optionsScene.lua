----
--
-- optionsScene.lua
--
----

local widget = require( "widget" )
local storyboard = require( "storyboard" )
local optionsScene = storyboard.newScene( "optionsScene" )

function optionsScene:createScene( e )

	local sceneGroup = self.view

	local titleOptions = display.newText( "Options", centerX,_H * 0.08, font, 40)
	titleOptions:setFillColor( 111/255,55/255,50/255 )

	local textShell = display.newRect( centerX, centerY, _W * 0.82, _H * 0.77 )
	textShell.strokeWidth = 3
	textShell:setFillColor( 0,0,0,0 )
	textShell:setStrokeColor( 111/255,55/255,50/255 )

	local txtMusicSwitch = display.newText( "Music", _W * 0.25,_H * 0.2, font, 36, "right")
	txtMusicSwitch:setFillColor( 111/255,55/255,50/255 )

	local musicSwitch = widget.newSwitch({
		id = "musicSwtich",
		x = _W * 0.8,
		y = _H * 0.2,
		initialSwitchState = true
		})

	local isChannel1Playing = audio.isChannelPlaying( 1 )

	function musicSwitch:tap( e )
		if(isChannel1Playing == true) then
			audio.pause( 1 )
			isChannel1Playing = false
		elseif(isChannel1Playing == false) then
			audio.resume( 1 )
			isChannel1Playing = true
		end
	end

	musicSwitch:addEventListener( "tap", musicSwitch)

	--[[

	local txtFXSwitch = display.newText( "Sound FX", _W * 0.25,_H * 0.25, font, 36, "right")
	txtFXSwitch:setFillColor( 111/255,55/255,50/255 )

	local fXSwitch = widget.newSwitch({
		id = "musicSwtich",
		x = _W * 0.8,
		y = _H * 0.25,
		initialSwitchState = true
		})

	local isChannel2Playing = audio.isChannelPlaying( 2 )

	]]

	local btnHome = widget.newButton({
		id = "Button_Home",
		x = centerX,
		y = _H - 80,
		label = "Home",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 36
		})

	function btnHome:tap( e )
		storyboard.gotoScene( "homeScene",{
			effect = "slideRight",
			time = 250
			})
	end

	btnHome:addEventListener( "tap" , btnHome )

	sceneGroup:insert(titleOptions)
	sceneGroup:insert(textShell)
	sceneGroup:insert(txtMusicSwitch)
	--sceneGroup:insert(txtFXSwitch)
	--sceneGroup:insert(fXSwitch)
	sceneGroup:insert(musicSwitch)
	sceneGroup:insert(btnHome)

end

function optionsScene:exitScene( e )
	storyboard.purgeScene( "optionsScene" )
end

optionsScene:addEventListener( "createScene", optionsScene)
optionsScene:addEventListener( "exitScene", optionsScene)

return optionsScene