<script setup lang="ts">
import HealthBar from './components/HealthBar.vue';
import GameWindow from './components/GameWindow.vue';
import StoryTextArea from './components/StoryTextArea.vue';
import Nearby from './components/Nearby.vue';
import ActionArea from './components/ActionArea.vue';
import InventoryWindow from './components/InventoryWindow.vue';
import EquipmentWindow from './components/EquipmentWindow.vue';
import DescriptionWindow from './components/DescriptionWindow.vue';

import {useHealthStore} from '@/store/playerHealthStore'
import GameButton from './components/GameButton.vue';

const health = useHealthStore()
</script>

<template>
<body>
    <div class="topic flex-window">
        <h1>--- ☠ Escape the Dungeon ☠ ---</h1>
        <GameButton style="width: 5%; margin: 94%; position: absolute;" :canBeDisabled="false">⟳</GameButton>
    </div>
    <GameWindow class="no-border">
        <HealthBar :health="health.life"></HealthBar>
    </GameWindow>
    <GameWindow class="no-border">
        <StoryTextArea style="height: 130px;"></StoryTextArea>
    </GameWindow>
    <div style="display: flex;">
        <ActionArea></ActionArea>
        <Nearby></Nearby>
    </div>
    <div style="display: flex;">
        <InventoryWindow></InventoryWindow>
        <EquipmentWindow></EquipmentWindow>
        <DescriptionWindow></DescriptionWindow>
    </div>
</body>
</template>
