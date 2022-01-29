<template>
  <div class="posts">
    <div class="container">
      <div class="posts__h postsname">
        <h2>Post List</h2>
      </div>
      <div class="posts__h postslink">
        <router-link to="/">Home</router-link>
      </div>
      <hr>
      <AddPost 
        v-on:add-post="addPost"
      />
      <select v-model="filter">
        <option value="all">All</option>
        <option value="completed">Completed</option>
        <option value="not-completed">Not completed</option>
      </select>
      <hr>
      <br>
      <Loader v-if="loading" />
      <PostList
        v-else-if="filteredPosts.length" 
       v-bind:posts="filteredPosts"
        v-on:remove-post="removePost"
      />
      <p v-else>No posts!</p>
    </div>
  </div>
</template>


<script>
import PostList from '@/components/PostList'
import AddPost from '@/components/AddPost'
import Loader from '@/components/Loader'

export default {
  name: 'App',
	data() {
		return {
			posts: [],
            loading: true,
            filter: 'all'
		}
	},
	mounted() {
		fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
			.then(response => response.json())
			.then(json => {
        this.posts = json
        this.loading = false
      })

  },
	methods: {
		removePost(id) {
			this.posts = this.posts.filter(p => p.id !== id)
		},
		addPost(newPost) {
			this.posts.push(newPost)
		} 
	},
  components: {
		PostList: PostList,
		AddPost: AddPost,
        Loader
  },
  computed: {
    filteredPosts() {
      if (this.filter === 'all') {
        return this.posts;
      }

      if (this.filter === 'completed') {
        return this.posts.filter(t => t.completed)
      }

      if (this.filter === 'not-completed') {
        return this.posts.filter(t => !t.completed)
      }
    }
  }
//   watch: {
//       filter(val) {
//           console.log(val)
//       }
//   }
}
</script>