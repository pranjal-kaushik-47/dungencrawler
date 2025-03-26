<template>
    <button :disabled="isDisabled"><slot></slot></button>
</template>
<script>
import { useActionDisable } from '@/store/gameStore';

export default {
    computed: {
        isDisabled: function(){
            const action = useActionDisable();
            return action.Locks != 0
        }
    }
}
</script>