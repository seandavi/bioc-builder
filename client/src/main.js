import Vue from 'vue';
import App from './App.vue';
import router from './router';

// Material design https://github.com/vuematerial/vue-material
import VueMaterial from 'vue-material'
import { MdButton,
	 MdContent,
	 MdTabs,
	 MdTable,
	 MdLayout
       } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default-dark.css'

Vue.use(VueMaterial)

Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(MdTable)

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
