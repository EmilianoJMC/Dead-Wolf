<template>
  <div class="albums">
    <h1>Álbuns</h1>
    <ul>
      <li v-for="album in albums" :key="album.id" @click="selectAlbum(album)">
        {{ album.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MusicAlbums',
  data() {
    return {
      albums: [],
    };
  },
created() {
  axios.get('http://localhost:8000/api/albums/')
    .then(response => {
      this.albums = response.data;
    })
    .catch(error => {
      console.error("There was an error fetching the albums:", error);
    });
},
  methods: {
    selectAlbum(album) {
      this.$router.push(`/albums/${album.id}`);
    }
  }
};
</script>

<style scoped>
.albums {
  padding: 20px;
}

h1 {
  font-size: 2em;
  color: #333;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  background: #f4f4f4;
  margin: 10px 0;
  padding: 10px;
  cursor: pointer;
  transition: background 0.3s;
}

li:hover {
  background: #e1e1e1;
}
</style>
