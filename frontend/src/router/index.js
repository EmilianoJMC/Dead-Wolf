import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import MusicAlbums from '@/components/MusicAlbums.vue';
import MusicPlayer from '@/components/MusicPlayer.vue';

const routes = [
    { path: '/', component: HomePage },
    { path: '/albums', component: MusicAlbums },
    { path: '/player', component: MusicPlayer },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
