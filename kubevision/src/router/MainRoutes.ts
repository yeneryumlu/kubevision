const MainRoutes = {
    path: '/main',
    meta: {
        requiresAuth: true
    },
    redirect: '/main',
    component: () => import('@/layouts/full/FullLayout.vue'),
    children: [
        {
            name: 'Dashboard',
            path: '/',
            component: () => import('@/views/dashboard/index.vue')
        },
        {
            name: 'Clusters',
            path: '/ui/clusters',
            component: () => import('@/views/components/Clusters.vue')
        },
        {
            name: 'Cluster',
            path: '/ui/cluster/:name',
            component: () => import('@/views/components/Cluster.vue'),
            props: true
        },
        {
            name: 'ClusterAdd',
            path: '/ui/addcluster/',
            component: () => import('@/views/components/ClusterAdd.vue'),
            props: true
        },
        {
            name: 'Node',
            path: '/ui/nodes',
            component: () => import('@/views/components/Nodes.vue'),
            props: true
        },
        {
            name: 'Namespace',
            path: '/ui/namespaces',
            component: () => import('@/views/components/Namespaces.vue'),
            props: true
        },
        {
            name: 'Starter',
            path: '/sample-page',
            component: () => import('@/views/pages/SamplePage.vue')
        },
    ]
};

export default MainRoutes;
