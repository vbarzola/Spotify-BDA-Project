
<template>

<div id="table-container">
    <h1>Playlist completa</h1>
    <table id="main-table" cellspacing="0">
      <thead>
        <th colspan="3">Playlist
            <button href=""><i class="fas fa-plus-circle"></i></button>
        </th>
        <tr>
            <th>Numero</th>
            <th>Nombre</th>
            <th>Accion</th>
        </tr>
      </thead>
      <tbody class="tableplaylist">
        <tr v-for="(playlist, index)  in playlists" :key="playlist._id.$oid" class="playlist">
          
            <th>{{ index }}</th>
            <th>{{ playlist.name }}</th>
            <th>
            <router-link :to="{ name: 'DetallePlaylist', params: { id: playlist._id.$oid }}">
            <button href="" ><i class="far fa-play-circle"></i></button>
            </router-link>
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
  data (){
    return{
      playlists: []
    }
  },
  mounted(){
    fetch("http://35.208.193.188/playlists")
    .then(response => response.json())
    .then(data => this.playlists = data)
    .catch(err => console.log(err.message));
  }
}

</script>