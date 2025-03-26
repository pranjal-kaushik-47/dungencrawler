<template>
    <GameWindow class="full-border twocol" title="NEARBY">
        <GameButton class="small-button" @click="addtoInventory(1, '🍗', 'The only drumstick that never plays music but always hits the spot!')" description="The only drumstick that never plays music but always hits the spot!">🍗</GameButton>
        <GameButton class="small-button" @click="addtoInventory(2, '🎲', 'Dice: The original RNGesus—now in pocket size!')" description="Dice: The original RNGesus—now in pocket size!">🎲</GameButton>
        <GameButton class="small-button" @click="addtoInventory(3, '🐀', 'A tiny cheese-powered ninja with big dreams!')" description="A tiny cheese-powered ninja with big dreams!">🐀</GameButton>
        <GameButton class="small-button" @click="addtoInventory(3, '🐀', 'A tiny cheese-powered ninja with big dreams!')" description="A tiny cheese-powered ninja with big dreams!">🐀</GameButton>
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