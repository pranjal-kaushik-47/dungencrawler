import { defineStore } from "pinia";
import { reactive } from "vue";
import { type Item } from "@/types/items"

export const useInventory = defineStore("inventory", () => {
    const inventoryItems = reactive<Array<Item>>([]);

    function addToInventory(item: Item){
        inventoryItems.push(item);
    }

    function removeFromInventory(itemId: Number){
        const index = inventoryItems.findIndex(item => {item.id === itemId})
        if (index !== -1){
            inventoryItems.splice(index, 1)
        }
    }

    return {
        inventoryItems,
        addToInventory,
        removeFromInventory
    }
})