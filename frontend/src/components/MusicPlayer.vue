<template>
  <div class="player">
    <h1>Player de Música</h1>
    <audio controls>
      <source :src="currentTrack" type="audio/mpeg">
      Seu navegador não suporta o elemento de áudio.
    </audio>
  </div>
</template>

<script>
export default {
  name: 'MusicPlayer',
  data() {
    return {
      currentTrack: '',
    };
  },
  created() {
    // Defina a URL do arquivo de música aqui
    this.currentTrack = 'http://localhost:8000/path/to/music/file.mp3';
  }
};
</script>

<style scoped>
.player {
  text-align: center;
  margin-top: 50px;
}

h1 {
  font-size: 2em;
  color: #333;
}

audio {
  width: 100%;
  max-width: 600px;
}
</style>
