import { defineStore } from "pinia";
import { ref } from "vue";

export const useHealthStore = defineStore(
    "health", () => {
        const life = ref(100);

        function decHealthBy(value: number){
            life.value = Math.max(0, life.value-value);
        };

        function incHealthBy(value: number){
            life.value = Math.min(100, life.value+value);
        };

        function changeHealthto(value: number){
            life.value = value;
        };
        
        return {life, decHealthBy, incHealthBy, changeHealthto}
    }
)