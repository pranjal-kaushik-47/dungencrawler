<template>
    <GameWindow class="full-border twocol" title="ACTIONS">
        <button class="small-button" @click="testMovement('front')">⬆</button>
        <button class="small-button" @click="testMovement('back')">⬇</button>
        <button class="small-button" @click="testMovement('left')">⬅</button>
        <button class="small-button" @click="testupdateHealth(10)">➡</button>
        <button class="small-button" @click="testDamageu(10)">👁</button>
        <button class="small-button" @click="testDamaged(10)">🖑</button>
    </GameWindow>
</template>
<script>
import { useStoryUpdate } from '@/store/storyUpdate';
import GameWindow from './GameWindow.vue';
import { useHealthStore } from '@/store/playerHealth';

export default {
    components: {
        GameWindow
    },
    methods: {
        testDamaged(damage){
            const health = useHealthStore();
            health.decHealthBy(damage);
        },
        testDamageu(damage){
            const health = useHealthStore();
            health.incHealthBy(damage);
        },
        testupdateHealth(val){
            const health = useHealthStore();
            health.changeHealthto(val);
        },
        testMovement(dir){
            const msg = `you have moved 1 step ${dir}`;
            const story = useStoryUpdate()
            story.update(msg)
        },
    }
}
</script>