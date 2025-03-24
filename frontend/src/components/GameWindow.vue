<template>
    <div class="game-window">
        <div v-if="title">{{title}}</div>
        <slot></slot>
    </div>
</template>
<script>
export default {
    props:{
        title: String
    }
}
</script>