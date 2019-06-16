<template>
  <div>
    <form novalidate class="md-layout" @submit="onSubmit" @reset="onReset">
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-header>
          <div class="md-title">Job</div>
        </md-card-header>

        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field >
                <label for="pkg_repo">Package Repository</label>
                <md-input name="pkg_repo" id="pkg_repo" v-model="job.pkg_repo" :disabled="sending" />
              </md-field>
            </div>
	  </div>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-primary" :disabled="sending">Submit Job</md-button>
        </md-card-actions>
      </md-card>

    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "NewJob",
    data() {
	return {
	    sending: false,
	    job: {
		pkg_repo: '',
	    },
	};
    },
    methods: {
    addJob(payload) {
	const path = 'http://localhost:7000/new_job';
	axios.post(path, payload)
            .then(() => {
		console.log(payload);
            })
            .catch((error) => {
		// eslint-disable-next-line
		console.log(error);
            });
    },
    initForm() {
	this.job.pkg_repo = '';
    },
    onSubmit(evt) {
	evt.preventDefault();
	this.sending = true;
	const payload = {
            pkg_repo: this.job.pkg_repo,
	};
	this.addJob(payload);
	this.initForm();
	this.sending=false;
    },
    onReset(evt) {
	evt.preventDefault();
	this.initForm();
    },
  },
  created() {
    console.log('created form page');
  },
};
</script>
