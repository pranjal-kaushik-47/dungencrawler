<template>
    <GameWindow class="threecol full-border" style="height: 200px;" title="INVENTORY">  
        <GameButton class="small-button" v-for="it in inventoryItems" :description="it.description">{{ it.name }}</GameButton>    
    </GameWindow>
</template>
<script>
import { useInventory } from '@/store/inventoryStore';
import GameWindow from './GameWindow.vue';
import GameButton from './GameButton.vue';

export default {
    components: {
        GameWindow,
        GameButton
    },
    computed:
    {
        inventoryItems: function(){
            const itemStore = useInventory();
            return itemStore.inventoryItems
        }
    }
}
</script>