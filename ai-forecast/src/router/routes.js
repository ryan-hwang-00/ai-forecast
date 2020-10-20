
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),

    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'store', component: () => import('pages/store.vue') },
      { path: 'login', component: () => import('pages/login.vue') },
      { path: 'test1', component: () => import('pages/test1.vue') },
      { path: 'main_test', component: () => import('pages/main_test.vue') },
      { path: 'test2', component: () => import('pages/test2.vue') },
      { path: 'register', component: () => import('pages/register.vue') }
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
