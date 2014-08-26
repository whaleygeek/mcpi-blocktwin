# blocks.py  26/08/2014  D.J.Whale
#
# Taken from:
# http://www.stuffaboutcode.com/p/minecraft-api-reference.html
#
# This link above is the most complete reference about the Minecraft API
# and the block types.

PLATFORM = "RaspberryPi"
# GLOWING_OBSIDIAN is on Pi only
# there are other changes in Bukkit, see Martin's big list

class BLOCK_IDS:
  # This is the number of unique blockid's, excluding aliases
  # you might want to take off AIR if you want the block to be
  # visible. At the moment this does not include variances for
  # extra data, but it will later on in a later release.
  
  AIR                 = 0
  STONE               = 1
  GRASS               = 2
  DIRT                = 3
  COBBLESTONE         = 4
  WOOD_PLANKS         = 5
  #WOOD_PLANKS (Not on Pi:
  #0: Oak
  #1: Spruce
  #2: Birch
  #3: Jungle
 
  SAPLING             = 6
  #SAPLING:
  #0: Oak
  #1: Spruce
  #2: Birch
  #3: Jungle (Not on Pi
  
  BEDROCK             = 7
  WATER_FLOWING       = 8
  WATER               = WATER_FLOWING #alias
  WATER_STATIONARY    = 9
  #[WATER, LAVA]_STATIONARY:
  #0-7: Level of the water, 0 being the highest, 7 the lowest

  LAVA_FLOWING        = 10
  LAVA                = LAVA_FLOWING #alias
  LAVA_STATIONARY     = 11
  #[WATER, LAVA]_STATIONARY:
  #0-7: Level of the water, 0 being the highest, 7 the lowest
  
  SAND                = 12
  GRAVEL              = 13
  GOLD_ORE            = 14
  IRON_ORE            = 15
  COAL_ORE            = 16
  WOOD                = 17
  #WOOD
  #(below not on Pi
  #3: Jungle (up/down
  #4: Oak (east/west
  #5: Spruce (east/west
  #6: Birch (east/west
  #7: Jungle (east/west
  #8: Oak (north/south
  #9: Spruce (north/south
  #10: Birch (north/south
  #11: Jungle (north/south
  #12: Oak (only bark
  #13: Spruce (only bark
  #14: Birch (only bark
  #15: Jungle (only bark 
  
  LEAVES              = 18
  #LEAVES:
  #1: Oak leaves
  #2: Spruce leaves
  #3: Birch leaves
 
  GLASS               = 20
  LAPIS_LAZULI_ORE    = 21
  LAPIS_LAZULI_BLOCK  = 22
  SANDSTONE           = 24
  #SANDSTONE:
  #0: Sandstone
  #1: Chiseled sandstone
  #2: Smooth sandstone
  
  BED                 = 26
  COBWEB              = 30
  GRASS_TALL          = 31
  #GRASS_TALL:
  #0: Shrub
  #1: Grass
  #2: Fern
  #3: Grass (color affected by biome (Not on Pi
  
  WOOL                = 35
  WOOL_WHITE = 0
  WOOL_ORANGE = 1
  WOOL_MAGENTA = 2
  WOOL_LIGHTBLUE = 3
  WOOL_YELLOW = 4
  WOOL_LIME = 5
  WOOL_PINK = 6
  WOOL_GREY = 7
  WOOL_LIGHTGREY = 8
  WOOL_CYAN = 9
  WOOL_PURPLE = 10
  WOOL_BLUE = 11
  WOOL_BROWN = 12
  WOOL_GREEN = 13
  WOOL_RED = 14
  WOOL_BLACK = 15
    
  FLOWER_YELLOW       = 37
  FLOWER_CYAN         = 38
  MUSHROOM_BROWN      = 39
  MUSHROOM_RED        = 40
  GOLD_BLOCK          = 41
  IRON_BLOCK          = 42
  STONE_SLAB_DOUBLE   = 43
  #STONE_SLAB / STONE_SLAB_DOUBLE:
  #0: Stone
  #1: Sandstone
  #2: Wooden
  #3: Cobblestone
  #4: Brick
  #5: Stone Brick
  #Below - not on Pi
  #6: Nether Brick
  #7: Quartz
  
  STONE_SLAB          = 44
  #STONE_SLAB / STONE_SLAB_DOUBLE:
  #0: Stone
  #1: Sandstone
  #2: Wooden
  #3: Cobblestone
  #4: Brick
  #5: Stone Brick
  #Below - not on Pi
  #6: Nether Brick
  #7: Quartz
  
  BRICK_BLOCK         = 45
  TNT                 = 46
  #TNT:
  #0: Inactive
  #1: Ready to explode
  
  BOOKSHELF           = 47
  MOSS_STONE          = 48
  OBSIDIAN            = 49
  TORCH               = 50
  #TORCH:
  #0: Standing on the floor
  #1: Pointing east
  #2: Pointing west
  #3: Pointing south
  #4: Pointing north
  
  FIRE                = 51
  STAIRS_WOOD         = 53
  #STAIRS_[COBBLESTONE, WOOD]:
  #0: Ascending east
  #1: Ascending west
  #2: Ascending south
  #3: Ascending north
  #4: Ascending east (upside down
  #5: Ascending west (upside down
  #6: Ascending south (upside down
  #7: Ascending north (upside down
  
  CHEST               = 54
  #LADDERS, CHESTS, FURNACES:
  #2: Facing north
  #3: Facing south
  #4: Facing west
  #5: Facing east
  
  DIAMOND_ORE         = 56
  DIAMOND_BLOCK       = 57
  CRAFTING_TABLE      = 58
  FARMLAND            = 60
  FURNACE_INACTIVE    = 61
  #LADDERS, CHESTS, FURNACES:
  #2: Facing north
  #3: Facing south
  #4: Facing west
  #5: Facing east
  
  FURNACE_ACTIVE      = 62
  #LADDERS, CHESTS, FURNACES:
  #2: Facing north
  #3: Facing south
  #4: Facing west
  #5: Facing east
  
  DOOR_WOOD           = 64
  LADDER              = 65
  #LADDERS, CHESTS, FURNACES:
  #2: Facing north
  #3: Facing south
  #4: Facing west
  #5: Facing east
  
  STAIRS_COBBLESTONE  = 67
  #STAIRS_[COBBLESTONE, WOOD]:
  #0: Ascending east
  #1: Ascending west
  #2: Ascending south
  #3: Ascending north
  #4: Ascending east (upside down
  #5: Ascending west (upside down
  #6: Ascending south (upside down
  #7: Ascending north (upside down
  
  DOOR_IRON           = 71
  REDSTONE_ORE        = 73
  SNOW                = 78
  #Not on Pi
  #SNOW:
  #0-7: Height of snow, 0 being the lowest, 7 being the highest.
  
  ICE                 = 79
  SNOW_BLOCK          = 80
  CACTUS              = 81
  CLAY                = 82
  SUGAR_CANE          = 83
  FENCE               = 85
  GLOWSTONE_BLOCK     = 89
  BEDROCK_INVISIBLE   = 95
  STONE_BRICK         = 98
  #STONE_BRICK:
  #0: Stone brick
  #1: Mossy stone brick
  #2: Cracked stone brick
  #3: Chiseled stone brick
  
  GLASS_PANE          = 102
  MELON               = 103
  FENCE_GATE          = 107
  GLOWING_OBSIDIAN    = 246 # pi only
  NETHER_REACTOR_CORE = 247
  #NETHER_REACTOR_CORE:
  #0: Unused
  #1: Active
  #2: Stopped / used up
  
  
  # The index is a way of getting a unique blockid without gaps
  index = [
  AIR,
  STONE,
  GRASS,
  DIRT,
  COBBLESTONE,
  WOOD_PLANKS,
  SAPLING,
  BEDROCK,
  WATER_FLOWING,
  WATER_STATIONARY,
  LAVA_FLOWING,
  LAVA_STATIONARY,
  SAND,
  GRAVEL,
  GOLD_ORE,
  IRON_ORE,
  COAL_ORE,
  WOOD,
  LEAVES,
  GLASS,
  LAPIS_LAZULI_ORE,
  LAPIS_LAZULI_BLOCK,
  SANDSTONE,
  BED,
  COBWEB,
  GRASS_TALL,
  WOOL,
  FLOWER_YELLOW,
  FLOWER_CYAN,
  MUSHROOM_BROWN,
  MUSHROOM_RED,
  GOLD_BLOCK,
  IRON_BLOCK,
  STONE_SLAB_DOUBLE,
  STONE_SLAB,
  BRICK_BLOCK,
  TNT,
  BOOKSHELF,
  MOSS_STONE,
  OBSIDIAN,
  TORCH,
  FIRE,
  STAIRS_WOOD,
  CHEST,
  DIAMOND_ORE,
  DIAMOND_BLOCK,
  CRAFTING_TABLE,
  FARMLAND,
  FURNACE_INACTIVE,
  FURNACE_ACTIVE,
  DOOR_WOOD,
  LADDER,
  STAIRS_COBBLESTONE,
  DOOR_IRON,
  REDSTONE_ORE,
  SNOW,
  ICE,
  SNOW_BLOCK,
  CACTUS,
  CLAY,
  SUGAR_CANE,
  FENCE,
  GLOWSTONE_BLOCK,
  BEDROCK_INVISIBLE,
  STONE_BRICK,
  GLASS_PANE,
  MELON,
  FENCE_GATE,
  GLOWING_OBSIDIAN,
  NETHER_REACTOR_CORE
  ]
  
# END
