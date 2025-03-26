<template>
    <GameWindow class="full-border twocol" title="ACTIONS">
        <GameButton class="small-button" @click="testMovement('front')">⬆</GameButton>
        <GameButton class="small-button" @click="testMovement('back')">⬇</GameButton>
        <GameButton class="small-button" @click="testMovement('left')">⬅</GameButton>
        <GameButton class="small-button" @click="testMovement('right')">➡</GameButton>
        <GameButton class="small-button" @click="testDamageu(10)">👁</GameButton>
        <GameButton class="small-button" @click="testDamaged(10)">🖑</GameButton>
    </GameWindow>
</template>
<script>
import { useStoryUpdate } from '@/store/storyUpdate';
import { useHealthStore } from '@/store/playerHealth';
import GameWindow from './GameWindow.vue';
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
            this.actionLocks.open += 1;
        },
        testDamageu(damage){
            const story = useStoryUpdate()
            const health = useHealthStore();
            health.incHealthBy(damage);
            story.update("As you inspect your surroundings, you heal 20 points")
        },
        testupdateHealth(val){
            const health = useHealthStore();
            health.changeHealthto(val);
        },
        testMovement(dir){
            const story = useStoryUpdate()
            const health = useHealthStore();
            const msg = `you have moved 1 step ${dir}, You fall and take 20 points in damage`;    
            story.update(msg)
            health.decHealthBy(20);
        },
    }
}
</script>