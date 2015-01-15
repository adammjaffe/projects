----
--
-- rulesScene1.lua
--
----

local widget = require( "widget" )
local storyboard = require( "storyboard" )
local rulesScene1 = storyboard.newScene( "rulesScene1" )

function rulesScene1:createScene( e )

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
	t.text = "Each turn, you mark a square \nin one of the small boards. \nWhich square you choose \ndetermines which board your" .. 
				"\nopponent plays in next. \n\nFor example, if you mark the \nmiddle square of one of \nthe small boards, then your" .. 
				"\nopponent must mark a square \nin the middle board. \n\nIf you get three in a \nrow in any of the small boards," .. 
				"\nyou win that board. \n\nWin three small boards in \na row and you win the game."

	local fillCircle = display.newCircle( centerX - 15, _H - 150, 10)
	fillCircle:setFillColor( 111/255,55/255,50/255 )

	local emptyCircle = display.newCircle( centerX + 15, _H - 150, 10)
	emptyCircle.strokeWidth = 2
	emptyCircle:setStrokeColor( 111/255,55/255,50/255 )
	emptyCircle:setFillColor( 0,0,0,0 )

	local btnHome = widget.newButton({
		id = "Button_Home",
		x = _W * 0.2,
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

	local btnNext = widget.newButton({
		id = "Button_Next",
		x = _W * 0.8,
		y = _H - 80,
		label = "Next",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 36
		})

	function btnNext:tap( e )
		storyboard.gotoScene( "rulesScene2",{
			effect = "slideLeft",
			time = 250
			})
	end

	btnNext:addEventListener( "tap" , btnNext )

	sceneGroup:insert(soundContainer)
	sceneGroup:insert(titleRules)
	sceneGroup:insert(textShell)
	sceneGroup:insert(t)
	sceneGroup:insert(fillCircle)
	sceneGroup:insert(emptyCircle)
	sceneGroup:insert(btnHome)
	sceneGroup:insert(btnNext)

end

function rulesScene1:exitScene( e )
	t = nil
	storyboard.purgeScene( "rulesScene1" )
end

rulesScene1:addEventListener( "createScene", rulesScene )
rulesScene1:addEventListener( "exitScene", rulesScene )

return rulesScene1