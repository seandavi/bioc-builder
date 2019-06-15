<template>
  <div>
    <md-table v-model="jobs" md-sort="name" md-sort-order="asc" md-card>
      <md-table-toolbar>
        <h1 class="md-title">Job List</h1>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-sort-by="jobId"><a v-bind:href="'/job/' +  item.jobId">{{ item.jobId }}</a></md-table-cell>
        <md-table-cell md-label="Status" md-sort-by="status">{{ item.status }}</md-table-cell>
        <md-table-cell md-label="Name" md-sort-by="jobName">{{ item.jobName }}</md-table-cell>
        <md-table-cell md-label="Started" md-sort-by="startedAt" md-table-numeric>{{ item.startedAt }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
  import axios from 'axios';
  
  export default {
      name: 'TableSort',
      data: () => ({
	  jobs: []
      }),
      methods: {
	  getMessage() {
	      const path = 'http://localhost:7000/job_list';
	      axios.get(path)
		  .then((res) => {
		      this.jobs = res.data;
		  })
		  .catch((error) => {
		      // eslint-disable-next-line
		      console.error(error);
		  });
	  },
      },
      created() {
	  this.getMessage();
      },
  }
</script>
