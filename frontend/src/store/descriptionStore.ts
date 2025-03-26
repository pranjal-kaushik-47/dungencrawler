import { defineStore } from "pinia";
import { ref } from "vue";

export const useDescription = defineStore("description", () => {
        const description = ref("");

        function updateDescription(desc: string){
            description.value = desc;
        }

        return {description, updateDescription}
    }
)