<script setup lang="ts">
import { ref } from 'vue';
import HealthBar from './components/HealthBar.vue';

const health = ref("100");
</script>

<template>
<body>
    <div class="game-description">
        <h1>Escape the Dungeon</h1>
    </div>
    <HealthBar :health="health"></HealthBar>
    
</body>
</template>
