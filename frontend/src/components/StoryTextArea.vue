<template>
    <textarea ref="storyTextarea" class="fullscreen" Locks=true :value="storyText()" readonly></textarea>
</template>
<script>
import { useStoryUpdate } from '@/store/storyPointStore';


export default {
    mounted() {
        const story = useStoryUpdate()
        story.registerCallBack(this.scrollToBottom);
        story.update("Every step could lead to salvation or something far worse. The dungeon waits. What will you do?")
    },
    methods: {
        scrollToBottom(){
            const textarea = this.$refs.storyTextarea;
            if (textarea && textarea.value){
                textarea.scrollTop = textarea.scrollHeight;
            }
        },
        storyText(){
            const story = useStoryUpdate()
            return story.text
        }
    }
}
</script>