<template>
  <div>
    <ul id="job-files">
      <li v-for="f in files">
	<a v-bind:href="f.url">{{ f.name }}</a>
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
