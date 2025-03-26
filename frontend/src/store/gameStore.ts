import { defineStore } from "pinia";
import { ref } from "vue";

export const useActionDisable = defineStore("actionDisable", () => {
        const Locks = ref(0);

        function disable(){
            console.log("made disable");
            Locks.value += 1
        }

        function enable(){
            console.log("made enable");
            Locks.value -= 1
        }

        function status(){
            return Locks.value
        }

        return {Locks, disable, enable, status}
    }
)