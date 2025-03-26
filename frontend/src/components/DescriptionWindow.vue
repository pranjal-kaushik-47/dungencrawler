<template>
    <GameWindow class="threecol full-border" style="height: 200px;" title="DESCRIPTION">
        {{ description }}
    </GameWindow>
</template>
<script>
import { useDescription } from '@/store/descriptionStore';
import GameWindow from './GameWindow.vue';

export default {
    components: {
        GameWindow
    },
    computed: {
        description: function(){
            const descArea = useDescription();
            return descArea.description
        }
    }
}
</script>