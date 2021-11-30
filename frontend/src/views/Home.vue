<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <div id="table-container">
    <h1>Canción más escuchada</h1>
    <table id="main-table" cellspacing="0">
      <thead>
        <th colspan="3">Playlist
           
        </th>
        <tr>
            <th>Canción</th>
            <th>Frecuencia</th>
            <th>Cantante</th>
        </tr>
      </thead>
      <tbody class="tableplaylist">
        <tr class="playlist">
          
            <th>{{ playlists.song }}</th>
            <th>{{ playlists.frecuency }}</th>
            <th>
            <router-link :to="{ name: 'Artista', params: { id: playlists.artist }}">
            {{ playlists.artist }}
            </router-link>
            </th>
          </tr>
        </tbody>
       
    </table>
  

   
      
  

</div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Navegacion from '@/views/Navegacion.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Navegacion
  },
  data (){
    return{
      playlists: [],
      idplaylist: "",
      nombrePlaylist: {
        name: ""
      },
      nuevo: "",
      blog: []
    }

  },
  mounted(){
    fetch("http://35.208.193.188/mapReduce")
    .then(response => response.json())
    .then(data => this.playlists = data)
    .catch(err => console.log(err.message));
  }
}

</script>
