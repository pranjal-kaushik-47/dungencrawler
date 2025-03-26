<template>
    <GameWindow class="full-border twocol" title="NEARBY">
        <GameButton class="small-button" @click="addtoInventory(1, '🍗', 'chicken leg')" description="chicken leg">🍗</GameButton>
        <GameButton class="small-button" @click="addtoInventory(2, '🎲', 'dice')" description="dice">🎲</GameButton>
        <GameButton class="small-button" @click="addtoInventory(3, '🐀', 'cute mouse')" description="cute mouse">🐀</GameButton>
        <GameButton class="small-button" @click="addtoInventory(3, '🐀', 'cute mouse')" description="cute mouse">🐀</GameButton>
    </GameWindow>
</template>
<script>
import { useInventory } from '@/store/inventoryStore';
import GameButton from './GameButton.vue';
import GameWindow from './GameWindow.vue';

export default {
    components: {
        GameWindow,
        GameButton
    },
    methods: {
        addtoInventory(itemId, icon, description){
            const itemStore = useInventory();
            itemStore.addToInventory(
                {
                    id: itemId,
                    name: icon,
                    weight: 5,
                    description: description
                }
            )
        }
    }
}
</script>