<template>
<div id="app" class="md-layout">
  <md-toolbar>
    <h3 class="md-title" style="flex: 1">Bioconductor Workshop Builder</h3>
    <md-menu md-direction="top-start">
      <md-button md-menu-trigger class="md-icon-button">
	<md-icon>more_vert</md-icon>      
      </md-button>
      <md-menu-content>
	<md-menu-item><a href="/jobs">List Jobs</a></md-menu-item>
	<md-menu-item><a href="/new_job">New Job</a></md-menu-item>
      </md-menu-content>
    </md-menu>
  </md-toolbar>
  <div class="md-layout-item">
    <router-view/>
  </div>
</div>
</template>

<script>

export default {
  name: 'app',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
