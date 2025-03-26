import { defineStore } from "pinia";
import { ref } from "vue";
import { useActionDisable } from "./actionLockStore";

export const useHealthStore = defineStore(
    "health", () => {
        const life = ref(100);
        const smoothness = 0.5;
        const framerate = 40
        const disabledState = useActionDisable();

        function decHealthBy(value: number){
            disabledState.disable();
            const finalValue = Math.max(0, life.value-value);
            const updateHealth = () => {
                if (life.value == finalValue){
                    disabledState.enable();
                };
                if (life.value > finalValue){
                    life.value -= smoothness;
                    setTimeout(updateHealth, framerate)
                }
            }
            updateHealth();
        };

        function incHealthBy(value: number){
            disabledState.disable();
            const finalValue = Math.min(100, life.value+value);
            const updateHealth = () => {
                if (life.value == finalValue){
                    disabledState.enable();
                };
                if (life.value < finalValue){
                    life.value += smoothness;
                    setTimeout(updateHealth, framerate)
                }
            }
            updateHealth();
        };

        function changeHealthto(value: number){
            console.log(disabledState.Locks);
            disabledState.disable();
            const finalValue = value;
            const updateHealth = () => {
                if (life.value == finalValue){
                    disabledState.enable();
                };
                if (finalValue > life.value){
                    if (life.value < finalValue){
                        life.value += smoothness;
                        setTimeout(updateHealth, framerate)
                    }
                } else {
                    if (life.value > finalValue){
                        life.value -= smoothness;
                        setTimeout(updateHealth, framerate)
                    }
                }
                
            }
            updateHealth();
        };
        
        return {life, decHealthBy, incHealthBy, changeHealthto}
    }
)