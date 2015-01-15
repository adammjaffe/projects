----
--
-- newGameScene.lua
--
----

local widget = require( "widget" )
local storyboard = require( "storyboard" )
local newGameScene = storyboard.newScene( "newGameScene" )

function newGameScene:createScene( e )

	local sceneGroup = self.view

	local txtGameModes = display.newText( "New Game", centerX, _H * 0.08, font, 40, "center")
	txtGameModes:setFillColor( (111/255),(55/255),(50/255) )

	local btnShell = display.newRect( centerX, centerY, _W * 0.85, _H * 0.3 )
	btnShell.strokeWidth = 3
	btnShell:setFillColor( 0,0,0,0 )
	btnShell:setStrokeColor( 111/255,55/255,50/255 )

	local btnVsHuman = widget.newButton({
		id = "Button_VsHuman",
		x = centerX,
		y = centerY - 100,
		label = "Pass and Play",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 80
		})

	function btnVsHuman:tap( e )
		storyboard.gotoScene( "practice", {
			effect = "slideLeft",
			time = 250
			})
	end

	btnVsHuman:addEventListener( "tap", btnVsHuman )

	local btnVsComputer = widget.newButton({
		id = "Button_VsComputer",
		x = centerX,
		y = centerY,
		label = "vs. Computer",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 80
		})

	function btnVsComputer:tap( e )
		storyboard.gotoScene( "gameplayScene",{
			effect = "slideLeft",
			time = 250
			})
	end

	btnVsComputer:addEventListener( "tap", btnVsComputer )

	local btnVsOnline = widget.newButton({
		id = "Button_VsOnline",
		x = centerX,
		y = centerY + 100,
		label = "Online",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 80
		})

	function btnVsOnline:tap( e )
		storyboard.gotoScene( "gameplayScene",{
			effect = "slideLeft",
			time = 250
			})
	end

	btnVsOnline:addEventListener( "tap", btnVsOnline )

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

	btnHome:addEventListener( "tap", btnHome )

	sceneGroup:insert(txtGameModes)
	sceneGroup:insert(btnShell)
	sceneGroup:insert(btnVsHuman)
	sceneGroup:insert(btnVsComputer)
	sceneGroup:insert(btnVsOnline)
	sceneGroup:insert(btnHome)

end

function newGameScene:exitScene( e )
	storyboard.purgeScene( "newGameScene" )
end

newGameScene:addEventListener( "createScene", newGameScene)
newGameScene:addEventListener( "exitScene", newGameScene)

return newGameScene