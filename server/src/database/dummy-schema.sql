-- PostgreSQL Schema for LLM-Based Dungeon Crawler Game
-- Based on the architecture in Project-brain-storm.md

-- Create extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Game Levels
CREATE TABLE levels (
    level_id SERIAL PRIMARY KEY,
    level_number INT NOT NULL,
    difficulty VARCHAR(20) CHECK (difficulty IN ('Easy', 'Medium', 'Hard', 'Expert')),
    theme TEXT NOT NULL,
    theme_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    map_data JSONB NOT NULL -- 2D matrix representation of the map
);

-- Room Types
CREATE TABLE room_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE CHECK (type_name IN ('Start', 'End', 'Wall', 'Quest', 'Event', 'Normal')),
    description TEXT
);

-- Rooms within Levels
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    level_id INT REFERENCES levels(level_id) ON DELETE CASCADE,
    room_type_id INT REFERENCES room_types(type_id),
    x_coord INT NOT NULL,
    y_coord INT NOT NULL,
    description TEXT,
    is_explored BOOLEAN DEFAULT FALSE,
    special_properties JSONB,
    UNIQUE(level_id, x_coord, y_coord)
);

-- Players
CREATE TABLE players (
    player_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) NOT NULL UNIQUE,
    current_level_id INT REFERENCES levels(level_id),
    current_x_coord INT,
    current_y_coord INT,
    health INT NOT NULL DEFAULT 100,
    mana INT NOT NULL DEFAULT 100,
    strength INT NOT NULL DEFAULT 10,
    carrying_capacity INT NOT NULL DEFAULT 50,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (current_level_id, current_x_coord, current_y_coord) 
        REFERENCES rooms(level_id, x_coord, y_coord) ON DELETE SET NULL
);

-- Item Types
CREATE TABLE item_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    can_be_equipped BOOLEAN DEFAULT FALSE
);

-- Items
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    item_type_id INT REFERENCES item_types(type_id),
    weight INT NOT NULL DEFAULT 1,
    stats_effect JSONB, -- Effects on player stats when used/equipped
    special_properties JSONB,
    theme_tags VARCHAR[] -- For thematic grouping of items
);

-- Item Instances (actual items in the game world)
CREATE TABLE item_instances (
    instance_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    item_id INT REFERENCES items(item_id),
    level_id INT,
    x_coord INT,
    y_coord INT,
    player_id UUID REFERENCES players(player_id),
    is_equipped BOOLEAN DEFAULT FALSE,
    durability INT,
    properties_override JSONB, -- For unique properties of this instance
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (level_id, x_coord, y_coord) 
        REFERENCES rooms(level_id, x_coord, y_coord) ON DELETE SET NULL,
    -- Item either belongs to a player OR is in a room
    CHECK ((player_id IS NULL AND level_id IS NOT NULL AND x_coord IS NOT NULL AND y_coord IS NOT NULL) 
        OR (player_id IS NOT NULL AND level_id IS NULL AND x_coord IS NULL AND y_coord IS NULL))
);

-- NPCs
CREATE TABLE npcs (
    npc_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    level_id INT,
    x_coord INT,
    y_coord INT,
    health INT DEFAULT 100,
    is_hostile BOOLEAN DEFAULT FALSE,
    dialogue_options JSONB, -- Structured dialogue choices
    special_properties JSONB,
    theme_tags VARCHAR[], -- For thematic grouping of NPCs
    FOREIGN KEY (level_id, x_coord, y_coord) 
        REFERENCES rooms(level_id, x_coord, y_coord) ON DELETE SET NULL
);

-- Quests
CREATE TABLE quests (
    quest_id SERIAL PRIMARY KEY,
    level_id INT REFERENCES levels(level_id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_main_quest BOOLEAN DEFAULT FALSE,
    prerequisite_quest_id INT REFERENCES quests(quest_id),
    reward_description TEXT,
    reward_item_id INT REFERENCES items(item_id),
    reward_stats JSONB, -- Stats changes upon completion
    start_trigger JSONB, -- What triggers this quest to become available
    completion_criteria JSONB -- Structured data defining completion requirements
);

-- Player Quest Progress
CREATE TABLE player_quests (
    player_id UUID REFERENCES players(player_id),
    quest_id INT REFERENCES quests(quest_id),
    status VARCHAR(20) CHECK (status IN ('Not Started', 'In Progress', 'Completed', 'Failed')),
    progress_data JSONB, -- Tracks multi-step quest progress
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    PRIMARY KEY (player_id, quest_id)
);

-- Event Types
CREATE TABLE event_types (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    category VARCHAR(50) CHECK (category IN ('Map', 'Item', 'NPC', 'Quest', 'Stats', 'Inventory'))
);

-- Event Triggers
CREATE TABLE event_triggers (
    trigger_id SERIAL PRIMARY KEY,
    level_id INT REFERENCES levels(level_id),
    x_coord INT,
    y_coord INT,
    trigger_type VARCHAR(50) CHECK (trigger_type IN ('Location', 'Item', 'NPC', 'Action')),
    trigger_details JSONB, -- What specifically triggers this event
    event_type_id INT REFERENCES event_types(type_id),
    probability DECIMAL(5,2) DEFAULT 100.00, -- 0-100% chance of triggering
    trigger_conditions JSONB, -- Additional conditions for triggering
    event_content JSONB, -- The specifics of what happens
    is_one_time BOOLEAN DEFAULT FALSE, -- If true, only triggers once
    FOREIGN KEY (level_id, x_coord, y_coord) 
        REFERENCES rooms(level_id, x_coord, y_coord) ON DELETE CASCADE
);

-- Event Log (records of triggered events)
CREATE TABLE event_log (
    log_id SERIAL PRIMARY KEY,
    player_id UUID REFERENCES players(player_id),
    trigger_id INT REFERENCES event_triggers(trigger_id),
    event_type_id INT REFERENCES event_types(type_id),
    level_id INT REFERENCES levels(level_id),
    x_coord INT,
    y_coord INT,
    triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_details JSONB, -- What specifically happened
    state_changes JSONB, -- How game state changed as a result
    narrative_text TEXT, -- The story text shown to the player
    FOREIGN KEY (level_id, x_coord, y_coord) 
        REFERENCES rooms(level_id, x_coord, y_coord) ON DELETE SET NULL
);

-- Game Sessions (for tracking player progress)
CREATE TABLE game_sessions (
    session_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    player_id UUID REFERENCES players(player_id),
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    last_save_point JSONB, -- Compact representation of game state
    session_summary TEXT -- Generated summary of what happened in this session
);

-- Indices for performance
CREATE INDEX idx_rooms_level ON rooms(level_id);
CREATE INDEX idx_item_instances_player ON item_instances(player_id);
CREATE INDEX idx_item_instances_location ON item_instances(level_id, x_coord, y_coord) 
    WHERE level_id IS NOT NULL;
CREATE INDEX idx_npcs_location ON npcs(level_id, x_coord, y_coord);
CREATE INDEX idx_player_quests_player ON player_quests(player_id);
CREATE INDEX idx_event_triggers_location ON event_triggers(level_id, x_coord, y_coord) 
    WHERE level_id IS NOT NULL;
CREATE INDEX idx_event_log_player ON event_log(player_id);

-- Initial data for room_types
INSERT INTO room_types (type_name, description) VALUES
('Start', 'Starting room for the level'),
('End', 'End/goal room for the level'),
('Wall', 'Impassable wall or obstacle'),
('Quest', 'Room containing a quest or quest-related content'),
('Event', 'Room with a special event trigger'),
('Normal', 'Standard traversable room');

-- Initial data for item_types
INSERT INTO item_types (type_name, description, can_be_equipped) VALUES
('Weapon', 'Items that can be used to attack', true),
('Armor', 'Items that provide protection', true),
('Consumable', 'One-time use items like potions', false),
('Quest', 'Items related to quests', false),
('Key', 'Items used to unlock areas or containers', false),
('Treasure', 'Valuable items with no direct utility', false);

-- Initial data for event_types
INSERT INTO event_types (type_name, description, category) VALUES
('Encounter', 'Random encounter with an NPC or creature', 'NPC'),
('Trap', 'Mechanical or magical trap', 'Map'),
('Discovery', 'Finding a hidden item or passage', 'Map'),
('Puzzle', 'A puzzle that must be solved', 'Map'),
('Dialogue', 'Conversation with an NPC', 'NPC'),
('Reward', 'Receiving a reward', 'Item'),
('StatusEffect', 'Change to player stats', 'Stats'),
('QuestUpdate', 'Progress in a quest', 'Quest'),
('InventoryChange', 'Addition or removal of items', 'Inventory'); 