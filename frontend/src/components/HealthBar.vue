<template>
    <div class="health" id="health">
        <div class="healthbar" id="healthbar" :style="{width: healthLeft + '%'}"></div>
    </div>
</template>

<script>
export default {
    props: {
        health: {
            type: String
        }
    },
    computed: {
        healthLeft() {
            return this.health
        }
    }
}
</script>