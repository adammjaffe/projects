----
--
-- homePage.lua
--
----

-- Build home screen

local widget = require( "widget" )
local storyboard = require( "storyboard" )
local homeScene = storyboard.newScene( "homeScene" )

function homeScene:createScene( e )

	local sceneGroup = self.view

	-- Create Logo
	local logoHome = display.newImage( sceneGroup, "assets/finishedAssets/homeScene/Logo/UltimateTTTLogo.png", display.contentWidth, display.contentHeight )
	logoHome.x, logoHome.y = centerX, _H * 0.38
	logoHome.xScale, logoHome.yScale = .85, .85

	local btnShell = display.newRect( centerX, _H * 0.75, _W * 0.8, _H * 0.2 )
	btnShell.strokeWidth = 3
	btnShell:setFillColor( 0,0,0,0 )
	btnShell:setStrokeColor( 111/255,55/255,50/255 )

	-- Create buttons

	-- Produce sound toggle
	local soundContainer = display.newContainer( _W * 0.1, _W * 0.1 )
	soundContainer:translate( _W * 0.88, _W * 0.15 )

	local btnSoundOn = display.newImageRect( "assets/finishedAssets/soundOn.png", _W * 0.08, _W * 0.08 )
	local btnSoundOff = display.newImageRect( "assets/finishedAssets/soundOff.png", _W * 0.08, _W * 0.08 )
	soundContainer:insert( btnSoundOn, true )
	btnSoundOn:addEventListener( "tap", btnSoundOn )

	if( isSoundOn ) == true then
		btnSoundOff.isVisible = false
	else 
		btnSoundOn.isVisible = false
		btnSoundOff.isVisible = true
	end

	function btnSoundOn:tap( e )
		if(isSoundOn == true) then
			audio.pause( 1 )
			isSoundOn = false
			btnSoundOn.isVisible = false
			btnSoundOff.isVisible = true
		end
	end

	soundContainer:insert( btnSoundOff, true )

	function btnSoundOff:tap( e )
		if(isSoundOn == false) then
			audio.resume( 1 )
			isSoundOn = true
			btnSoundOff.isVisible = false
			btnSoundOn.isVisible = true
		end
	end

	btnSoundOff:addEventListener( "tap", btnSoundOff )

	local btnNewGame = widget.newButton({
		id = "Button_Back",
		x = centerX,
		y =  _H * 0.7,
		label = "New Game",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 80
		})

	function btnNewGame:tap( e )
		storyboard.gotoScene( "gameplayScene",{
			effect = "slideLeft",
			time = 250
			})
	end

	btnNewGame:addEventListener( "tap", btnNewGame )

	local btnRules = widget.newButton({
		id = "Button_Back",
		x = centerX,
		y = _H * 0.79,
		label = "Rules",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 80
		})

	function btnRules:tap( e )
		storyboard.gotoScene( "rulesScene1",{
			effect = "slideLeft",
			time = 250
			})
	end

	btnRules:addEventListener( "tap", btnRules)

	sceneGroup:insert(soundContainer)
	sceneGroup:insert(btnShell)
	sceneGroup:insert(logoHome)
	sceneGroup:insert(soundContainer)
	sceneGroup:insert(btnNewGame)
	sceneGroup:insert(btnRules)
end

function homeScene:exitScene( e )
	storyboard.purgeScene("homeScene")
end

homeScene:addEventListener("createScene", homeScene)
homeScene:addEventListener("exitScene", homeScene)

return homeScene


