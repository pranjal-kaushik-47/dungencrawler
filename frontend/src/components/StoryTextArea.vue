<template>
    <textarea class="fullscreen" Locks=true :value="storyText()"></textarea>
</template>
<script>
import { useStoryUpdate } from '@/store/storyPointStore';


export default {
    methods: {
        storyText(){
            const story = useStoryUpdate()
            return story.text
        }
    }
}
</script>