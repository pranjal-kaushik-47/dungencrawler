- dungen crawler
- escape
- floors/level
- level : door -> next level
- easy : 10lv, medium: 20lv ...


Mechanics:
Actions:
- move (f b l r)
- inspect
- attack
- pickup
- equip
- view
- Chat with npc using N options, no keybord chat

- some items will be predefined that are importent for the quest
- llm will generate misc. items + items with (events + quests)
- Each item genrated from LLM will have a probibilty of event or quest being triggered

Stats:
- Health
- Mana (magic)
- Strength
- Carring Capacity


Quest: 

- To genrate quest we need to give LLM the set of actions that we have, so that the quest is possible and within the relm
- N number of quest in each level

Map:
Room types:
- Start
- End
- Wall
- Quest
- Event

- Each level will have a map
- A algo will genrate a 2D matrix, using this LLM will create the stroy line for the Level





----------------
Steps for each Level Genration: 
- Genrate a map using Algo
- Map the room types
- Use LLM to create a theme for the level 
    - environment, 
    - side quest, 
    - events, 
    - NPC, 
    - items
    - predefined items

-----------------

When an event will be triggered:
- Each button will have a probability assigned to it, that will trigger an event
    - NOTE: Map events will have a 100% prob
- Once an event is triggered LLM will update the story, environment, and map

Type of events:
    - Inventory Update
    - Stats update
    - Map update
    - Quest update

------------------


How will LLM genrate event sinario after an event is triggered:
- IT will use:
    - Level theme information
    - Event inforation
    - Past evnet infomation
    - All equiped items information

- Will will genrate the outcome of the event

-------------------
