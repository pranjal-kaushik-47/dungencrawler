<template>
    <GameWindow class="full-border twocol" title="ACTIONS">
        <GameButton class="small-button" @click="testMovement('front')">⬆</GameButton>
        <GameButton class="small-button" @click="testMovement('back')">⬇</GameButton>
        <GameButton class="small-button" @click="testMovement('left')">⬅</GameButton>
        <GameButton class="small-button" @click="testupdateHealth(10)">➡</GameButton>
        <GameButton class="small-button" @click="testDamageu(10)">👁</GameButton>
        <GameButton class="small-button" @click="testDamaged(10)">🖑</GameButton>
    </GameWindow>
</template>
<script>
import { useStoryUpdate } from '@/store/storyUpdate';
import GameWindow from './GameWindow.vue';
import { useHealthStore } from '@/store/playerHealth';
import GameButton from './GameButton.vue';

export default {
    components: {
        GameWindow,
        GameButton
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