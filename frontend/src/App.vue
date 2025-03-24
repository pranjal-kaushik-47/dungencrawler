<script setup lang="ts">
import { ref } from 'vue';
import HealthBar from './components/HealthBar.vue';
import GameWindow from './components/GameWindow.vue';
import StoryTextArea from './components/StoryTextArea.vue';

var health = ref(100);
function testhealth(){
    health.value -= 10;
    console.log("----");
}
</script>

<template>
<body>
    <div class="topic">
        <h1>Escape the Dungeon</h1>
    </div>
    <GameWindow class="no-border">
        <HealthBar :health="health"></HealthBar>
    </GameWindow>
    <GameWindow class="bottom-border">
        <StoryTextArea style="height: 300px;"></StoryTextArea>
        <div class="flex-window">
            <GameWindow class="full-border twocol" title="ACTIONS">
                <button class="small-button">⬆</button>
                <button class="small-button">⬇</button>
                <button class="small-button">⬅</button>
                <button class="small-button">➡</button>
                <button class="small-button">👁</button>
                <button class="small-button" @click="testhealth">🖑</button>
            </GameWindow>
            <GameWindow class="full-border twocol" title="SURROUNDINGS">
                <button>Apple</button>
                <button>Knife</button>
                <button style="color: brown;">Guard(NPC)</button>
                <button>Coin</button>
            </GameWindow>
        </div>
    </GameWindow>
</body>
</template>
