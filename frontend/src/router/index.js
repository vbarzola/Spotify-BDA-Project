import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Artista from '../views/Artista.vue'
import Playlist from '../views/Playlist.vue'
import DetallePlaylist from '../views/DetallePlaylist.vue'
import CancionArtista from '../views/CancionArtista.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/artista',
        name: 'Artista',
        component: Artista
    },
    {
        path: '/playlist',
        name: 'Playlist',
        component: Playlist
    },
    {
        path: '/detallePlaylist',
        name: 'DetallePlaylist',
        component: DetallePlaylist
    },
    {
        path: '/cancionArtista',
        name: 'CancionArtista',
        component: CancionArtista
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router