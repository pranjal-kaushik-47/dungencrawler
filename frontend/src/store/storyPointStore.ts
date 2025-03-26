import { defineStore } from "pinia";
import { ref, nextTick } from "vue";
import { useActionDisable } from "./actionLockStore";

export const useStoryUpdate = defineStore("story", () => {
        const text = ref("");
        const disabledState = useActionDisable();

        let onUpdateCallBack: (() => void) | null = null

        function registerCallBack(callable: ()=>{}){
            onUpdateCallBack = callable
        }

        function update(newText: string){
            disabledState.disable();
            text.value = ""
            let index = 0;
            const typeCharacter = () => {
                if (index < newText.length){
                    text.value += newText[index];
                    nextTick(() => {
                        if (onUpdateCallBack){
                            onUpdateCallBack();
                        }
                      });
                    index++;
                    setTimeout(typeCharacter, 45)
                } else {
                    disabledState.enable();
                }
            };
            typeCharacter()
        }

        return {text, update, registerCallBack}
    }
)