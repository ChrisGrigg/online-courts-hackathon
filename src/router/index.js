import Vue from 'vue'
import Router from 'vue-router'

// Containers
import Full from 'containers/Full'

// Views
import Claim from 'views/Claim'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      redirect: '/claim',
      name: 'Home',
      component: Full,
      children: [
        {
          path: 'claim',
          name: 'Claim',
          component: Claim
        }

      ]
    }
  ]
})
