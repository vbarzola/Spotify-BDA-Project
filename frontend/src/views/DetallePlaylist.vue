<template>

<div id="table-container">
    <h1>{{ this.$route.params.nombre }}</h1>
    <table id="main-table" cellspacing="0">
      <thead>
        <th colspan="4">Lista de canciones
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-plus-circle"></i></button>
        </th>
        <tr>
            <th>Canción</th>
            <th>Artista</th>
            <th>Albúm</th>
            <th>Acciones</th>
        </tr>
      </thead>
      <!--<tbody class="playlist">-->
          <tbody>
        <tr v-for="d in detalle.tracks" :key="d._id" class="detalle">
 
            <th>{{ d.track_name }}</th>
            <router-link tag="th" :to="{ name: 'CancionArtista', params: { id: d.artist_name }}">
            <th>{{ d.artist_name }}</th>
            </router-link>
            <th>{{ d.album_name }}</th>
            <th>
             <!--<button href=""><i class="far fa-play-circle"></i></button>-->
            <button @click="deleteTrack(d.track_name)" ><i class="fas fa-trash"></i></button>
             <!--<button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>-->
            </th>
          </tr>
        </tbody>
        
            
          
    </table>

   
        

    <!-- Modal -->
    <div class="modal fade" id="myModal" role="dialog">
        <div class="modal-dialog">
        
        <!-- Modal content-->
        <div class="modal-content">
            <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">Añada un nuevo track</h4>
            </div>
            <div class="modal-body">
            <p>Ingrese los siguiente datos</p>
            <div>
              <p>Nombre del artista:</p><input v-model="artista" />
              <p>Nombre de la canción:</p><input v-model="cancion" />
              <p>Nombre del album:</p><input v-model="album" />
              <p>Duración (milisegundos):</p><input v-model="duracion" />
            </div>
            </div>
            <div class="modal-footer">
            <button @click="añadirTrack()" type="button" class="btn btn-default" data-dismiss="modal">Añadir</button>
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            </div>
        </div>
        
        </div>
    </div>
  

</div>
</template>



<script>
import HelloWorld from '@/components/HelloWorld.vue'
import Navegacion from '@/views/Navegacion.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Navegacion
  },
  props: ['id'],
  data (){
    return{
      detalle: [],
      trackname: "",
      nuevoTrack: {
        artist_name: "",
        track_name: "",
        album_name: "",
        duration_ms: 0,
      },
      cancion:"",
      album:"",
      duracion:"",
      artista:""
    }
  },
  methods: {
     async deleteTrack(trackname) {
    const r = await fetch("http://35.208.193.188/playlists/" + this.$route.params.id + "/tracks/" + trackname, {
        method: "DELETE",
    });
    this.detalle.tracks=this.detalle.tracks.filter((t)=>t.track_name!=trackname)
},
async añadirTrack() {
    this.nuevoTrack.artist_name = this.artista; 
    this.nuevoTrack.track_name = this.cancion; 
    this.nuevoTrack.album_name = this.album; 
    this.nuevoTrack.duration_ms = this.duracion;  
    const payload = JSON.stringify(this.nuevoTrack);
    const url = "http://35.208.193.188/playlists/" + this.$route.params.id + "/tracks";
    const r = await fetch(url, {
        method: "POST",
        body: payload,
        headers: {
            "Content-type": "application/json",
        }
    });
    //const response = await r.json();
    //location. reload();
    //this.router.go("http://35.208.193.188/playlists/" + this.$route.params.id);
    this.detalle.tracks.push({...this.nuevoTrack});
    //console.log(this.detalle);
    }
},
  mounted(){
      console.log(this.$route.params.id);

    fetch("http://35.208.193.188/playlists/" + this.$route.params.id)
    .then(response => response.json())
    .then(data => this.detalle = data)
    .catch(err => console.log(err.message));

  }
}

</script>