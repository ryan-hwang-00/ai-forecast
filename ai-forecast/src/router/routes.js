const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),

    children: [
      // { path: '', component: () => import('pages/Index.vue') },
      { path: "", component: () => import("pages/home.vue") },
      { path: 'login', component: () => import('pages/login.vue') },
      { path: "register", component: () => import("pages/register.vue") },

      // { path: "map", component: () => import("pages/map.vue") },
      // { path: 'predict_variables', component: () => import('pages/predict_variables.vue') },
      // { path: "Predict", component: () => import("pages/Predict.vue") },

      { path: "store", component: () => import("pages/store.vue") },
      { path: "item", component: () => import("pages/item.vue") },
      { path: "chart", component: () => import("pages/chart.vue") },
      { path: "sample", component: () => import("pages/sample.vue") }
    ]
  },

  {
    path: "/",
    component: () => import("layouts/NavigatorLayout.vue"),

    children: [
      { path: "map", component: () => import("pages/map.vue") },
      { path: 'predict_variables', component: () => import('pages/predict_variables.vue') },
      { path: "Predict", component: () => import("pages/Predict.vue") },
    ]
  },

  {
    path: "*",
    component: () => import("pages/Error404.vue")
  },
];

export default routes;
