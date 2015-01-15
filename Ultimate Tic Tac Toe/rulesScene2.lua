----
--
-- rulesScene2.lua
--
----

local widget = require( "widget" )
local storyboard = require( "storyboard" )
local rulesScene2 = storyboard.newScene( "rulesScene2" )

function rulesScene2:createScene( e )

	local sceneGroup = self.view

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

	local titleRules = display.newText( "Rules", centerX,_H * 0.08, font, 40)
	titleRules:setFillColor( 111/255,55/255,50/255 )

	local textShell = display.newRect( centerX, centerY, _W * 0.82, _H * 0.77 )
	textShell.strokeWidth = 3
	textShell:setFillColor( 0,0,0,0 )
	textShell:setStrokeColor( 111/255,55/255,50/255 )

	local t = native.newTextField( centerX,centerY, _W * 0.8, _H * 0.75 )
	t.font = native.newFont( font, 18 )
	t:setTextColor( 111/255,55/255,50/255 )
	t.hasBackground = false
	t.isEditable = false
	t.text = "A few odds and ends: \nyou are allowed to play in a \nboard even if it has already \nbeen won. \n\nAlso, if your opponent sends" .. 
				"\nyou to a board that is already \nfull, then you get to play in \nany of the remaining boards." .. 
				"\n\nAnd last, if a board finishes in \na tie, it counts as neither \nan X nor an O.\n\nThat's all, enjoy!"

	local emptyCircle = display.newCircle( centerX - 15, _H - 150, 10)
	emptyCircle.strokeWidth = 2
	emptyCircle:setStrokeColor( 111/255,55/255,50/255 )
	emptyCircle:setFillColor( 0,0,0,0 )

	local fillCircle = display.newCircle( centerX + 15, _H - 150, 10)
	fillCircle:setFillColor( 111/255,55/255,50/255 )

	local btnBack = widget.newButton({
		id = "Button_Back",
		x = _W * 0.2,
		y = _H - 80,
		label = "Back",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 36
		})

	function btnBack:tap( e )
		storyboard.gotoScene( "rulesScene1",{
			effect = "slideRight",
			time = 250
			})
	end

	btnBack:addEventListener( "tap" , btnBack )

	local btnPlay = widget.newButton({
		id = "Button_Play",
		x = _W * 0.8,
		y = _H - 80,
		label = "Play",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 36
		})

	function btnPlay:tap( e )
		storyboard.gotoScene( "gameplayScene",{
			effect = "slideLeft",
			time = 250
			})
	end

	btnPlay:addEventListener( "tap" , btnPlay )

	sceneGroup:insert(soundContainer)
	sceneGroup:insert(titleRules)
	sceneGroup:insert(textShell)
	sceneGroup:insert(t)
	sceneGroup:insert(emptyCircle)
	sceneGroup:insert(fillCircle)
	sceneGroup:insert(btnBack)
	sceneGroup:insert(btnPlay)

end

function rulesScene2:exitScene( e )
	t = nil
	storyboard.purgeScene( "rulesScene2" )
end

rulesScene2:addEventListener( "createScene", rulesScene)
rulesScene2:addEventListener( "exitScene", rulesScene)

return rulesScene2