<template>
    <GameWindow class="full-border twocol" title="ACTIONS">
        <GameButton class="small-button" @click="testMovement('front')" description="move forward">⬆</GameButton>
        <GameButton class="small-button" @click="testMovement('back')" description="move backward">⬇</GameButton>
        <GameButton class="small-button" @click="testMovement('left')" description="move left">⬅</GameButton>
        <GameButton class="small-button" @click="testMovement('right')" description="move right">➡</GameButton>
        <GameButton class="small-button" @click="testDamageu(10)" description="check your environment">👁</GameButton>
        <GameButton class="small-button" @click="testDamaged(10)" description="slap">🖑</GameButton>
    </GameWindow>
</template>
<script>
import { useStoryUpdate } from '@/store/storyPointStore';
import { useHealthStore } from '@/store/playerHealthStore';
import GameWindow from './GameWindow.vue';
import GameButton from './GameButton.vue';

export default {
    components: {
        GameWindow,
        GameButton
    },
    methods: {
        testDamaged(damage){
            const story = useStoryUpdate();
            const health = useHealthStore();
            health.decHealthBy(damage);
            story.update("you swing you arm... you hit a wall and take 20 damage(ouch)!!")
        },
        testDamageu(damage){
            const story = useStoryUpdate();
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