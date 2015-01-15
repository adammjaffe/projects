local storyboard = require( "storyboard" )
local practice = storyboard.newScene( "practice" )

function practice:createScene( event )
	a = 1
	b = 1
	c = 1


	if(a==b and a==d) then
		print("a = b")
	elseif(a==c) then
		print("a = c")
	elseif(b==c) then
		print("b = c")
	end



	--[[
	container = display.newContainer( 100,200 )

	function containerBuild( hostContainer )

		local w = hostContainer.contentWidth
		local h = hostContainer.contentHeight
		local n = 0
		inputTable = {}
		inputTable.subTables = {}
		local z = 1

		for i = -1,1 do
			for j = -1,1 do

				local subTable = {}
				local name = (n) .. (i+2) .. (j+2)
				subTable.name = name
				local loc = {i+2,j+2}
				subTable.loc = loc
				subTable.fill = nil
				table.insert( inputTable.subTables,subTable )

				print(inputTable.subTables[z].loc[1])

				z = z+1
				--print(subTable.name,subTable.loc[1],subTable.loc[2],subTable.fill,subTable[1][1])
			end
		end
	end

	containerBuild(container)
	]]

	--[[

	masterTable = { 
		{name = "011", loc = {1,1}, fill = nil, subTables = {
			{name = "111", loc = {1,1}, fill = nil, subTables = {}},
			{name = "112", loc = {1,2}, fill = nil, subTables = {}},
			...
			{name = "333", loc = {3,3}, fill = nil, subTables = {}}
		},
		{name = "012", loc = {1,2}, fill = nil, subTables = {
			{name = "111", loc = {1,1}, fill = nil, subTables = {}},
			{name = "112", loc = {1,2}, fill = nil, subTables = {}},
			...
			{name = "333", loc = {3,3}, fill = nil, subTables = {}}
		},
		...
		{name = "033", loc = {3,3}, fill = nil, subTables = {
			{name = "111", loc = {1,1}, fill = nil, subTables = {}},
			{name = "112", loc = {1,2}, fill = nil, subTables = {}},
			...
			{name = "333", loc = {3,3}, fill = nil, subTables = {}}
		}
	}

	]]
end

function practice:enterScene( event )
end

function practice:exitScene( event )
end

function practice:destroyScene( event )
end

practice:addEventListener( "createScene", practice )
practice:addEventListener( "enterScene", practice )
practice:addEventListener( "exitScene", practice )
practice:addEventListener( "destroyScene", practice )

return practice


