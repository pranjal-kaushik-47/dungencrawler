<template>
    <button :disabled="isDisabled" @mouseover="displayDescription()"><slot></slot></button>
</template>
<script>
import { useActionDisable } from '@/store/actionLockStore';
import { useDescription } from '@/store/descriptionStore';

export default {
    props: {
        description: String
    },
    computed: {
        isDisabled: function(){
            const action = useActionDisable();
            return action.Locks != 0
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