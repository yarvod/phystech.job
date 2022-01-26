<template>
    <li>
        <span v-bind:class="{done: post.completed}">
            <input v-if="post.completed" checked type="checkbox" 
                v-on:change="post.completed = !post.completed">
            <input v-else type="checkbox" 
                v-on:change="post.completed = !post.completed">
            <strong> {{ index + 1 }} </strong>
            {{ post.title }}
        </span>
        <button class="rm"
            v-on:click="$emit('remove-post', post.id)"
        >&times;</button>
    </li>
</template>


<script>
export default {
    props: {
        post: {
            type: Object,
            required: true
        },
        index: Number
    },
    filters: {
        uppercase(val) {
            return val.toUpperCase()
        }
    }
}
</script>


<style scoped>
    li {
        border: 1px solid #ccc;
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 2rem;
        margin-bottom: 1rem;
    }

    input {
        margin-right: 1rem;
    }

    .rm {
        background: red;
        color: #fff;
        border-radius: 20%;
        font-weight: bold;
    }

    .done {
        text-decoration: line-through;
    }
</style>