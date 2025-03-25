import { defineStore } from "pinia";
import { ref } from "vue";

export const useStoryUpdate = defineStore("story", () => {
        const text = ref("");

        function update(newText: string){
            text.value = ""
            let index = 0;
            const typeCharacter = () => {
                if (index<newText.length){
                    text.value += newText[index];
                    index++;
                    setTimeout(typeCharacter, 45)
                }
            };
            typeCharacter()
        }

        return {text, update}
    }
)