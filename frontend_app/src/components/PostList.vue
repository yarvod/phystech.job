<template>
	<div>
		<ul>
			<PostItem
				v-for="(post, i) of posts"
				v-bind:post="post"
				v-bind:index="i"
				:key="post.id"
				v-on:remove-post="removePost"
			/>
		</ul>
	</div>
</template>


<script>
import PostItem from '@/components/PostItem'
export default {
		props: ['posts'],
    components: {
        PostItem: PostItem
    },
		methods: {
			removePost(id) {
				this.$emit('remove-post', id)
			}
		}
}
</script>


<style scoped>
	ul {
		list-style: none;
		margin: 0;
		padding: 0;
	}
</style>