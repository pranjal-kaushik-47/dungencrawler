import { defineStore } from "pinia";
import { ref } from "vue";

export const useActionDisable = defineStore("actionDisable", () => {
        const isDisable = ref(false);

        function disable(){
            console.log("made disable");
            isDisable.value = true
        }

        function enable(){
            console.log("made enable");
            isDisable.value = false
        }

        function status(){
            return isDisable.value
        }

        return {isDisable, disable, enable, status}
    }
)