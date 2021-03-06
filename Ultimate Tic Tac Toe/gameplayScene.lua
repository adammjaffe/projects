----
--
-- gameplayScene.lua
--
----

local widget = require( "widget" )
local storyboard = require( "storyboard" )
local gameplayScene = storyboard.newScene( "gameplayScene" )

function gameplayScene:createScene( e )

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

	-- This builds the # shape. In the smaller boards, the shorten parameter makes the line elements slightly smaller; for aesthetic purposes.
	local function buildBoard( container, shorten )

		local w,h = container.contentWidth,container.contentHeight

		if(shorten == true) then
			local vert1 = display.newLine( container, -w/6,-h/2.5, -w/6,h/2.5 )
			vert1.strokeWidth = 6
			vert1:setStrokeColor( 111/255,55/255,50/255 )

			local vert2 = display.newLine( container, w/6,-h/2.5, w/6,h/2.5 )
			vert2.strokeWidth = 6
			vert2:setStrokeColor( 111/255,55/255,50/255 )

			local hor1 = display.newLine( container, -w/2.5,-h/6, w/2.5,-h/6 )
			hor1.strokeWidth = 6
			hor1:setStrokeColor( 111/255,55/255,50/255 )

			local hor2 = display.newLine( container, -w/2.5,h/6, w/2.5,h/6 )
			hor2.strokeWidth = 6
			hor2:setStrokeColor( 111/255,55/255,50/255 )

		elseif(shorten == false) then
			local vert1 = display.newLine( container, -w/6,-h, -w/6,h )
			vert1.strokeWidth = 6
			vert1:setStrokeColor( 111/255,55/255,50/255 )

			local vert2 = display.newLine( container, w/6,-h, w/6,h )
			vert2.strokeWidth = 6
			vert2:setStrokeColor( 111/255,55/255,50/255 )

			local hor1 = display.newLine( container, -w,-h/6, w,-h/6 )
			hor1.strokeWidth = 6
			hor1:setStrokeColor( 111/255,55/255,50/255 )

			local hor2 = display.newLine( container, -w,h/6, w,h/6 )
			hor2.strokeWidth = 6
			hor2:setStrokeColor( 111/255,55/255,50/255 )
		end
	end

	local function isTappedCell( event )
	-- Describes reaction when cell is clicked. Most gameplay occurs here.

		local function updateMovesList( x,y )
		-- Saves the coordinates of the cell that is clicked. Used to help surface 'go here' box and 'last move' mark.	
			movesList.previousMove = {x,y}
		end

		local function isWonFunc( inputTable )
		-- Checks to see if a given board is full.

			-- Check if given board is not full to save memory and time in the case that it is full
			if(inputTable.isWon == false) then
				isWon = false

				-- Test horizontals
				for i = 1,7,3 do
					-- Prevent false positives the first time someone plays in the board, all cells are in the .fill = nil state.
					if( inputTable.subTables[i].fill ~= nil ) then
						if( inputTable.subTables[i].fill == inputTable.subTables[i+1].fill and 
							inputTable.subTables[i+1].fill == inputTable.subTables[i+2].fill ) then
							inputTable.isWon = true
							isWon = true
						end
					end
				end

				-- Test verticals
				-- Check if board is won on a horizontal or a vertical and save memory and time if that is true
				if(isWon == false) then
					for i = 1,3 do
						if( inputTable.subTables[i].fill ~= nil ) then
							if( inputTable.subTables[i].fill == inputTable.subTables[i+3].fill and
								inputTable.subTables[i].fill == inputTable.subTables[i+6].fill ) then
								inputTable.isWon = true
								isWon =  true
							end
						end
					end
				end

				-- Test diagonals
				if(isWon == false) then
					for i = 1,1 do
						if( inputTable.subTables[i].fill ~= nil ) then
							if( inputTable.subTables[i].fill == inputTable.subTables[i+4].fill and 
								inputTable.subTables[i].fill == inputTable.subTables[i+8].fill ) then
								inputTable.isWon = true
								isWon =  true
							end
						end
					end
				end

				if(isWon == false) then
					for i = 3,3 do
						if( inputTable.subTables[i].fill ~= nil ) then
							if( inputTable.subTables[i].fill == inputTable.subTables[i+2].fill and 
								inputTable.subTables[i].fill == inputTable.subTables[i+4].fill ) then
								inputTable.isWon = true
								isWon =  true
							end
						end
					end
				end

				-- If board has been won, change its .fill state to reflect the winner
				if(isWon == true) then
					inputTable.fill = whoseTurn

					-- Fill board container with mark of winner
					w = inputTable.container.contentWidth
					h = inputTable.container.contentHeight
					if(whoseTurn == "X") then
						inputTable.fill = "X"
						xMark = display.newImageRect( "assets/finishedAssets/xNew.png", w,h )
						xMark.alpha = 0.3
						inputTable.container:insert( xMark )
					elseif(whoseTurn == "O") then
						inputTable.fill = "O"
						oMark = display.newImageRect( "assets/finishedAssets/oNew.png", w,h )
						oMark.alpha = 0.3
						inputTable.container:insert( oMark )
					end

					return true
				end

			else return false
			end
		end

		local function isFull( inputTable )
		-- Checks to see if all the subtables of a given table are filled
			if( inputTable.subTables[1].fill ~= nil and
				inputTable.subTables[2].fill ~= nil and
				inputTable.subTables[3].fill ~= nil and
				inputTable.subTables[4].fill ~= nil and
				inputTable.subTables[5].fill ~= nil and
				inputTable.subTables[6].fill ~= nil and
				inputTable.subTables[7].fill ~= nil and
				inputTable.subTables[8].fill ~= nil and
				inputTable.subTables[9].fill ~= nil ) then return true
			else return false
			end
		end

		-- Shorthand for the position of the clicked cell. x gives board number, y gives cell number.
		local x,y = event.target.loc[1], event.target.loc[2]
		
		varBoard = masterTable.subTables[x]
		varCell = masterTable.subTables[x].subTables[y]

		-- If both the board and the cell are editable, procced. Otherwise, post warning at top of screen.
		if( masterTable.subTables[x].isEditable == true and varCell.isEditable == true ) then

			-- Shorthand for location of previous move, if it exists.
			if( movesList.previousMove ~= nil ) then
				prev_x = movesList.previousMove[1]
				prev_y = movesList.previousMove[2]
			end

			-- Remove old 'go here' box. Replace 'new move' mark on previous cell with 'old move' mark.
			if( movesList.previousMove ~= nil ) then
				masterTable.subTables[prev_x].subTables[prev_y].container:remove( mark )
				masterTable.subTables[prev_y].container:remove( highlight )
				if( whoseTurn == "X" ) then
					masterTable.subTables[prev_x].subTables[prev_y].container:insert( display.newImageRect( "assets/finishedAssets/oOld.png", 50,50 ) )
				elseif( whoseTurn == "O") then
					masterTable.subTables[prev_x].subTables[prev_y].container:insert( display.newImageRect( "assets/finishedAssets/xOld.png", 50,50 ) )
				end
			end

			-- Handle X's turn.
			if(whoseTurn == "X") then
				-- Communicate that since player one has just played, it is the turn of player two
				topBadge.text = "Player 2, go!"

				-- Put X in clicked cell, change the .fill property of cell and make cell uneditable
				mark = display.newImageRect( "assets/finishedAssets/xNew.png", 50,50 )
				varCell.container:insert( mark )
				masterTable.subTables[x].subTables[y].fill = "X"
				masterTable.subTables[x].subTables[y].isEditable = false

				-- Check if clicked board has been won
				isWonFunc( masterTable.subTables[x] )

				-- If the future board is not yet full ...
				if( isFull( masterTable.subTables[y] ) == false ) then
					for i = 1,9 do
						-- ... then surface a 'go here' box on the board for the next move ...
						if(i == y) then 
							nextBoard = masterTable.subTables[i]
							highlight = display.newRect( 0,0, nextBoard.container.contentWidth * 0.95, nextBoard.container.contentHeight * 0.95)
							highlight:setFillColor( 1,0,0, 0.2)
							nextBoard.container:insert( highlight )
							-- ... and ensure that only the board for the next move is editable.
							nextBoard.isEditable = true
						else masterTable.subTables[i].isEditable = false
						end
					end
				-- But if the future board is full ...
				elseif( isFull ( masterTable.subTables[y] ) == true ) then
					-- ... delete the 'go here' box in the current board ...
					masterTable.subTables[x].container:remove( highlight )
					-- ... then insert a new, invisible one so that the code above works (if I could figure out how to index 'highlight' in 
					--	'container' i would do this all in the one step above) ...
					currentBoard = masterTable.subTables[x]
					highlight = display.newRect( 0,0, currentBoard.container.contentWidth * 0.95, currentBoard.container.contentHeight * 0.95)
					highlight:setFillColor( 0,0,0, 0)
					currentBoard.container:insert( highlight )
					-- ... and make any not-full board editable.
					for i = 1,9 do
						if( isFull( masterTable.subTables[i]) == false ) then masterTable.subTables[i].isEditable = true end
					end
				end

				-- If the clicked board is now full then make sure that the full board is not editable.
				if( isFull( masterTable.subTables[x] ) == true ) then masterTable.subTables[x].isEditable = false end

				-- Check if the total board has been won and surface a congratulations if so.
				if( isWonFunc( masterTable ) == true) then topBadge.text = "Player 1 wins! New game?" end

				-- Pass the coordinates of the cell into the 'previous moves' list and change the turn to the next player.
				updateMovesList( x,y )
				whoseTurn = "O"

			elseif(whoseTurn == "O") then
				topBadge.text = "Player 1, go!"

				mark = display.newImageRect( "assets/finishedAssets/oNew.png", 50,50 )
				varCell.container:insert( mark )
				masterTable.subTables[x].subTables[y].fill = "O"
				masterTable.subTables[x].subTables[y].isEditable = false
				isWonFunc( masterTable.subTables[x] )

				if( isFull( masterTable.subTables[y] ) == false ) then
					for i = 1,9 do
						if(i == y) then
							nextBoard = masterTable.subTables[i]
							highlight = display.newRect( 0,0, nextBoard.container.contentWidth * 0.9, nextBoard.container.contentHeight * 0.95)
							highlight:setFillColor( 1,0,0, 0.2)
							nextBoard.container:insert( highlight )
							nextBoard.isEditable = true
						else masterTable.subTables[i].isEditable = false
						end
					end
				-- But if the future board is full ...
				elseif( isFull ( masterTable.subTables[y] ) == true ) then
					-- ... delete the 'go here' box in the current board
					masterTable.subTables[x].container:remove( highlight )
					-- ... then insert a new, invisible one so that the code above works (if I could figure out how to index 'highlight' in 
					--	'container' i would do this all in the one step above) ...
					currentBoard = masterTable.subTables[x]
					highlight = display.newRect( 0,0, currentBoard.container.contentWidth * 0.95, currentBoard.container.contentHeight * 0.95)
					highlight:setFillColor( 0,0,0, 0)
					currentBoard.container:insert( highlight )
					-- ... and make any not-full board editable
					for i = 1,9 do
						if( isFull( masterTable.subTables[i]) == false ) then masterTable.subTables[i].isEditable = true end
					end
				end

				-- If the clicked board is now full then make sure that the full board is not editable.
				if( isFull( masterTable.subTables[x] ) == true ) then masterTable.subTables[x].isEditable = false end

				if( isWonFunc( masterTable ) == true) then topBadge.text = "Player 2 wins! New game?" end
				
				updateMovesList( x,y )
				whoseTurn = "X"
			end

			-- Check if clicked board is full. If so, mark it as uneditable and skip to posting warning at top of screen.
			if( isFull( masterTable.subTables[x] ) == true ) then
				masterTable.subTables[x].isEditable = false 
			end
		else topBadge.text = "Oops! Can't go there!"
		end
	end

	local function buildContainerTable( hostContainer, isSmallBoard, inputTable, x, isTappedSmallBoard, isTappedCell )
		
		local w,h = hostContainer.contentWidth, hostContainer.contentHeight
		local y = 0

		inputTable.subTables = {}

		for j = -1,1 do
			for i = -1,1 do

				y = y + 1

				-- Name and build  containter
				local dummyContainer = display.newContainer( w/3,h/3 )
				local w1,h1 = dummyContainer.contentWidth, dummyContainer.contentHeight

				local dummyRect = display.newRect( 0,0, w1 * 0.75,h1 * 0.75 )
				dummyRect:setFillColor( 0,0,0,1 )
				dummyRect.isVisible = false
				if( isSmallBoard == true ) then
					dummyRect.isHitTestable = true 
					dummyRect:addEventListener( "tap", isTappedCell ) 
				end

				-- Create table, link to container

				local subTable = {}

				subTable.name = x .. y
				subTable.loc = {x,y}
				subTable.fill = nil
				subTable.isEditable = true
				subTable.isFull = false
				subTable.isWon = false

				dummyRect.name = subTable.name
				dummyRect.loc = subTable.loc
				dummyContainer:insert( dummyRect, true )
				subTable.container = dummyContainer

				table.insert( inputTable.subTables,subTable )

				hostContainer:insert( dummyContainer, true )
				dummyContainer:translate( (i/3) * w,(j/3) * h )

				-- Build containers in shape
				if(isSmallBoard == false) then
					buildBoard( dummyContainer, true)
					buildContainerTable( dummyContainer, true, subTable, x, isTappedSmallBoard, isTappedCell )
					x = x + 1
				end
			end
		end
	end

	-- Forward references
	local shorten
	local isSmallBoard
	local x = 1

	-- Globals
	masterContainer = display.newContainer( sceneGroup, _W * 0.9,_W * 0.9)
	masterContainer:translate( centerX,centerY )
	masterTable = { isWon = false, container = masterContainer }
	movesList = {}
	whoseTurn = "X"
	topBadge = display.newText( "Player 1, go!", centerX, centerY * 0.3, font, 40 )
	topBadge:setFillColor( 111/255,55/255,50/255 )

	-- Instantiate
	buildBoard( masterContainer, false )
	buildContainerTable( masterContainer, false, masterTable, x, isTappedSmallBoard, isTappedCell )

	local btnQuit = widget.newButton({
		id = "Button_Quit",
		x = _W * 0.2,
		y = _H - 100,
		label = "Quit",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 40
		})

	function btnQuit:tap( e )
		storyboard.gotoScene( "homeScene",{
			effect = "slideRight",
			time = 250
			})
	end

	btnQuit:addEventListener( "tap" , btnQuit )

	local btnNewGame = widget.newButton({
		id = "Button_NewGame",
		x = _W * 0.8,
		y = _H - 100,
		label = "New Game",
		labelColor = {
			default = { 111/255,55/255,50/255,1 },
			over = { 200/255,0/255,20/255,0.5 }
		},
		font = font,
		fontSize = 40
		})

	function btnNewGame:tap( e )
		masterContainer = nil
		masterTable = nil
		movesList = nil
		whoseTurn = nil
		topBadge = nil
		storyboard.gotoScene( "gameplayScene",{
			effect = "crossFade",
			time = 250
			})
	end

	btnNewGame:addEventListener( "tap" , btnNewGame )

	sceneGroup:insert(soundContainer)
	sceneGroup:insert(topBadge)
	sceneGroup:insert(masterContainer)
	sceneGroup:insert(btnQuit)
	sceneGroup:insert(btnNewGame)
end

function gameplayScene:exitScene( e )
	storyboard.purgeScene( "gameplayScene" )
end

gameplayScene:addEventListener( "createScene", gameplayScene)
gameplayScene:addEventListener( "exitScene", gameplayScene)

return gameplayScene