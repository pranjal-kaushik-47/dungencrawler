<template>
    <button :disabled="isDisabled" @mouseover="displayDescription()"><slot></slot></button>
</template>
<script>
import { useActionDisable } from '@/store/actionLockStore';
import { useDescription } from '@/store/descriptionStore';

export default {
    props: {
        description: String,
        canBeDisabled: {
            type: Boolean,
            default: true
        }
    },
    computed: {
        isDisabled: function(){
            if(this.canBeDisabled){
                const action = useActionDisable();
                return action.Locks != 0
            } else {
                return false
            }
        }
    },
    methods: {
        displayDescription: function(){
            const descArea = useDescription();
            descArea.updateDescription(this.description)
        }
    }
}
</script>