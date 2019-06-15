import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Jobs from './components/Jobs.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/jobs',
      name: 'Jobs',
      component: Jobs,
    }
  ],
});
