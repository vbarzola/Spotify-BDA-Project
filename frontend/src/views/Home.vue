<template>
  <div class="home">
    <img
      alt="Vue logo"
      width="300px"
      height="300px"
      src="../assets/logo3.png"
    />
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <div id="table-container">
      <h1>Canción más escuchada</h1>
      <table id="main-table" cellspacing="0">
        <thead>
          <tr>
            <th>Canción</th>
            <th>Frecuencia</th>
            <th>Cantante</th>
          </tr>
        </thead>
        <tbody class="tableplaylist">
          <tr class="playlist" v-if="loading">
            <td colspan="3">Cargando...</td>
          </tr>
          <tr class="playlist">
            <td>{{ playlists.song }}</td>
            <td>{{ playlists.frecuency }}</td>
            <td>
              <router-link
                :to="{ name: 'Artista', params: { id: playlists.artist } }"
              >
                {{ playlists.artist }}
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
a {
  color: white;
}
</style>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Navegacion from "@/views/Navegacion.vue";

export default {
  name: "Home",
  components: {
    HelloWorld,
    Navegacion,
  },
  data() {
    return {
      playlists: [],
      idplaylist: "",
      nombrePlaylist: {
        name: "",
      },
      nuevo: "",
      blog: [],
      loading: true,
    };
  },
  mounted() {
    this.loading = true;
    fetch("http://35.208.193.188/mapReduce")
      .then((response) => response.json())
      .then((data) => {
        this.playlists = data;
        this.loading = false;
      })
      .catch((err) => console.log(err.message));
  },
};
</script>
