import { defineStore } from "pinia";
import { ref } from "vue";
import { useActionDisable } from "./gameStore";

export const useStoryUpdate = defineStore("story", () => {
        const text = ref("");
        const disabledState = useActionDisable();

        function update(newText: string){
            disabledState.disable();
            text.value = ""
            let index = 0;
            const typeCharacter = () => {
                if (index < newText.length){
                    text.value += newText[index];
                    index++;
                    setTimeout(typeCharacter, 45)
                } else {
                    disabledState.enable();
                }
            };
            typeCharacter()
        }

        return {text, update}
    }
)