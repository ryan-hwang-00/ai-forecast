
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),

    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'store', component: () => import('pages/store.vue') },
      { path: 'login', component: () => import('pages/login.vue') },

      { path: 'item', component: () => import('pages/item.vue') },
      { path: 'main_test', component: () => import('pages/main_test.vue') },

      { path: 'register', component: () => import('pages/register.vue') },
      { path: 'predict_variables', component: () => import('pages/predict_variables.vue') }
    ]
  },


  
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  },

  {
    path: '/login',
    component: () => import('pages/register.vue')
  },

]

export default routes
