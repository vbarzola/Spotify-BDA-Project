
<template>

<div id="table-container">
    <h1>Lista de artistas</h1>
    <table id="main-table" cellspacing="0">
      <thead>
        
        <tr>
            <th>Numero</th>
            <th>Nombre</th>
            <th>Accion</th>
        </tr>
      </thead>
      <tbody class="tableplaylist">
        <tr v-for="(ar, index)  in artist" :key="ar" class="playlist">
          
            <td>{{ index+1 }}</td>
            <td>{{ ar }}</td>
            <td>
            <router-link tag="td" :to="{ name: 'CancionArtista', params: { id: ar }}">
            <button href="" ><i class="far fa-play-circle"></i></button>
            </router-link>
            <!-- <button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal"><i class="fas fa-edit"></i></button>-->
            </td>
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
      playlists: [],
      artist: []
    }
  },

  mounted(){
    fetch("http://35.208.193.188/playlists")
    .then(response => response.json())
    .then(data => {
      this.playlists = data;
      if(this.playlists.length>0){
            for(let play of this.playlists){
              for(let track of play.tracks){
              if(!this.artist.includes(track.artist_name)){
                this.artist.push(track.artist_name);
              }
            }
            }
          }
    })
    .catch(err => console.log(err.message));
    
  }
}

</script>