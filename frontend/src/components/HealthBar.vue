<template>
    <div class="health" id="health">
        <div class="healthbar" id="healthbar" :style="{width: healthLeft + '%'}"></div>
        <div class="health-details">{{ Math.floor(healthLeft) }}/100</div>
    </div>
</template>

<script>
export default {
    props: {
        health: {
            type: Number
        }
    },
    computed: {
        healthLeft() {
            return this.health
        }
    }
}
</script>