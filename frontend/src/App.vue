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

const health = useHealthStore()
</script>

<template>
<body>
    <div class="topic">
        <h1>☠ Escape the Dungeon ☠</h1>
    </div>
    <GameWindow class="no-border">
        <HealthBar :health="health.life"></HealthBar>
    </GameWindow>
    <GameWindow class="no-border">
        <StoryTextArea style="height: 150px;"></StoryTextArea>
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
