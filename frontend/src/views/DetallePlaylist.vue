<template>

<div id="table-container">
    <h1>Detalle de la Playlist</h1>
    <table id="main-table" cellspacing="0">
      <thead>
        <th colspan="4">Playlist
            <button href=""><i class="fas fa-plus-circle"></i></button>
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
            <th>{{ d.artist_name }}</th>
            <th>{{ d.album_name }}</th>
            <th>
            <button href=""><i class="far fa-play-circle"></i></button>
            <button href=""><i class="fas fa-trash"></i></button>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>
            </th>
          </tr>
        </tbody>
        <!--<tr>
            <th>1</th>
            <th>Playlist1</th>
            <th>
            <button href=""><i class="far fa-play-circle"></i></button>
            <button href=""><i class="fas fa-trash"></i></button>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>
            </th>
        </tr>
        <tr>
            <th>1</th>
            <th>Playlist1</th>
            <th>
            <button href=""><i class="far fa-play-circle"></i></button>
            <button href=""><i class="fas fa-trash"></i></button>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>
            </th>
        </tr>
        <tr>
            <th>1</th>
            <th>Playlist1</th>
            <th>
            <button href=""><i class="far fa-play-circle"></i></button>
            <button href=""><i class="fas fa-trash"></i></button>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>
            </th>
        </tr>
        <tr>
            <th>1</th>
            <th>Playlist1</th>
            <th>
            <button href=""><i class="far fa-play-circle"></i></button>
            <button href=""><i class="fas fa-trash"></i></button>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>
            </th>
        </tr>
        <tr>
            <th>1</th>
            <th>Playlist1</th>
            <th>
            <button href=""><i class="far fa-play-circle"></i></button>
            <button href=""><i class="fas fa-trash"></i></button>
            <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>
            </th>
        </tr>-->
      <!--</tbody>-->
    </table>
    <button id="add-row">Add Row</button>

   
        

    <!-- Modal -->
    <div class="modal fade" id="myModal" role="dialog">
        <div class="modal-dialog">
        
        <!-- Modal content-->
        <div class="modal-content">
            <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">Modal Header</h4>
            </div>
            <div class="modal-body">
            <p>Some text in the modal.</p>
            </div>
            <div class="modal-footer">
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
      detalle: []
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