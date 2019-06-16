<template>
<div>
    <h3 class="md-title" style="flex: 1">Results for Job: {{ id }}</h3>
    <ul id="job-files">
      <li v-for="f in files" v-bind:key="type">
	<a v-bind:href="f.url" target="_blank">{{ f.name }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios';
  
  export default {
      name: 'Job',
      data: () => ({
	  files: [],
	  id: ""
      }),
      methods: {
	  getMessage() {
	      const path = 'http://localhost:7000/job/'+this.id;
	      axios.get(path)
		  .then((res) => {
		      this.files = res.data;
		  })
		  .catch((error) => {
		      // eslint-disable-next-line
		      console.error(error);
		  });
	  },
      },
      created() {
	  this.id = this.$route.params.id;
	  this.getMessage();
      },
  }
</script>
