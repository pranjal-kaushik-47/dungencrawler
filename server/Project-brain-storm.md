# Enhanced LLM-Based Dungeon Crawler Game Architecture

Based on your detailed specifications, here's a refined solution for your dungeon crawler game with specific mechanics, levels, and event triggering systems.

## Core Architecture Components

### Map Generation System
- **Procedural Map Generator**: Creates 2D matrix representing each level
- **Room Type Allocator**: Assigns room types (Start, End, Wall, Quest, Event) based on level difficulty
- **Connectivity Validator**: Ensures paths exist between Start and End rooms
- **Difficulty Scaler**: Adjusts map complexity based on level number (10 for Easy, 20 for Medium, etc.)

### Level Theme Synthesizer
- **LLM-Powered Theme Generator**: Creates cohesive theme for each level
- **Constraint Enforcement**: Ensures themes align with available mechanics (move, inspect, attack, pickup, equip, view, chat)
- **Asset Controller**: Maps theme elements to:
  - Environment descriptions
  - NPC characteristics
  - Item distributions
  - Predefined quest items

### Player Mechanics Manager
- **Action Processor**: Handles player's limited action set (move f/b/l/r, inspect, attack, pickup, equip, view)
- **Stats Tracker**: Monitors Health, Mana, Strength, Carrying Capacity
- **Inventory System**: Manages equipped vs. carried items, enforces carrying limits
- **NPC Dialogue System**: Presents N dialogue options without free-form chat

### Quest & Event Systems

#### Quest Engine
- **Quest Generator**: Creates quests possible within action constraints
- **Quest Validator**: Ensures quests are completable with available mechanics
- **Quest Tracker**: Monitors progress across multi-step quests
- **Quest Density Controller**: Manages N quests per level based on difficulty

#### Event Probability System
- **Trigger Probability Assigner**: Sets likelihood of events for each interaction
  - Map events: 100% probability
  - Item events: Variable probability
  - NPC events: Variable probability
- **Random Encounter Generator**: Rolls against probabilities when actions are taken
- **Event Type Classifier**: Categorizes triggered events (Inventory, Stats, Map, Quest updates)

### LLM Context Management

#### Event Context Assembler
- **Theme Context**: Current level's thematic elements
- **Event Trigger Context**: What caused the event
- **Historical Context**: Relevant past events (filtered by causal connection)
- **Equipment Context**: Currently equipped items that may affect outcomes

#### State Compression System
- **Map State Compressor**: Converts 2D map to efficient representation
- **Player Progress Summarizer**: Condenses player's journey to key milestones
- **Inventory Optimizer**: References only relevant items in context
- **Dynamic Context Window**: Adjusts context size based on event complexity

## Execution Flow

### Level Initialization Process
1. Generate map matrix via algorithm
2. Assign room types strategically
3. Use LLM to create level theme with constraints:
   - Environmental descriptions
   - Side quests (N based on difficulty)
   - Potential events
   - NPCs appropriate to theme
   - Standard and special items
   - Required quest items

### Event Triggering System
1. Every player action has probabilistic event triggers
2. Map locations have deterministic (100%) event triggers
3. When triggered, event system:
   - Assembles relevant context
   - Queries LLM with structured prompt
   - Parses response into game state changes
   - Updates appropriate systems (inventory, stats, map, quests)

### Context Management for LLM Event Generation
1. Maintain compressed world state:
   - Level theme metadata
   - Current map state (explored/unexplored)
   - Player position and stats
   - Active quests and progress
   - Recent event history (last 3-5 events with full details)
   - Important historical events (summarized)

2. For each LLM prompt, include:
   - Event trigger details (what player did)
   - Current location description
   - Equipped items that could affect outcome
   - Relevant quests that might be impacted
   - Action constraints (what outcomes are mechanically possible)
   - Required output format (structured for easy parsing)

3. After LLM response:
   - Validate changes against game rules
   - Update state databases
   - Generate player-facing narrative
   - Update probabilities for future events

### Persistence and State Management
- **Level State Repository**: Persists level information between sessions
- **Player Progress Database**: Tracks stats, inventory, quest completion
- **Event Log**: Records all triggered events for consistency checking
- **State Transition Validator**: Ensures all state changes comply with game rules

This architecture provides a scalable solution for your dungeon crawler, maintaining narrative consistency while supporting your specific game mechanics and progressive difficulty levels.