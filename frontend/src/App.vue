<script setup lang="ts">
import { ref } from 'vue';
import HealthBar from './components/HealthBar.vue';
import GameWindow from './components/GameWindow.vue';

const health = ref("100");
</script>

<template>
<body>
    <div class="flex-window topic">
        <h1>Escape the Dungeon</h1>
    </div>
    <HealthBar :health="health"></HealthBar>
    <GameWindow class="onethird">
        <textarea class="fullscreen" disabled=true></textarea>
    </GameWindow>
</body>
</template>
