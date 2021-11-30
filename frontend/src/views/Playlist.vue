<template>
  <div id="table-container">
    <h1>Playlist completa</h1>
    <table id="main-table" cellspacing="0">
      <thead>
        <tr>
          <th>Numero</th>
          <th>Nombre</th>
          <th>Accion</th>
        </tr>
      </thead>
      <tbody class="tableplaylist">
        <tr class="playlist" v-if="loading">
          <td colspan="3">Cargando...</td>
        </tr>
        <tr
          v-for="(playlist, index) in playlists"
          :key="playlist._id.$oid"
          class="playlist"
        >
          <td>{{ index + 1 }}</td>
          <td>{{ playlist.name }}</td>
          <td>
            <router-link
              :to="{
                name: 'DetallePlaylist',
                params: { id: playlist._id.$oid, nombre: playlist.name },
              }"
            >
              <button href=""><i class="far fa-play-circle"></i></button>
            </router-link>
            <button @click="deletePlaylist(playlist._id.$oid)">
              <i class="fas fa-trash"></i>
            </button>
            <button
              @click="guardarDatoPlaylist(playlist._id.$oid, playlist.name)"
              type="button"
              class="btn btn-info btn-lg"
              data-toggle="modal"
              data-target="#myModal"
            >
              <i class="fas fa-edit"></i>
            </button>
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
            <button type="button" class="close" data-dismiss="modal">
              &times;
            </button>
            <h4 class="modal-title">{{ nombrePlaylist.name }}</h4>
          </div>
          <div class="modal-body">
            <p>Actualice el nombre de la Playlist {{ nombrePlaylist.name }}.</p>
            <input v-model="nuevo" />
          </div>
          <div class="modal-footer">
            <button
              @click="save()"
              type="button"
              class="btn btn-default"
              data-dismiss="modal"
              style="margin-right: 5px"
            >
              Actualizar
            </button>
            <button type="button" class="btn btn-default" data-dismiss="modal">
              Cerrar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
  methods: {
    async deletePlaylist(idplaylist) {
      const r = await fetch("http://35.208.193.188/playlists/" + idplaylist, {
        method: "DELETE",
      });
      this.playlists = this.playlists.filter((playlist) => {
        return playlist._id.$oid !== idplaylist;
      });
    },
    guardarDatoPlaylist(id, nombre) {
      this.nombrePlaylist.name = nombre;
      this.idplaylist = id;
    },
    async save() {
      if (!this.nuevo == "" || !this.nuevo == null) {
        this.nombrePlaylist.name = this.nuevo;
      }
      const payload = JSON.stringify(this.nombrePlaylist);
      const url = "http://35.208.193.188/playlists/" + this.idplaylist;
      const r = await fetch(url, {
        method: "PUT",
        body: payload,
        headers: {
          "Content-type": "application/json",
        },
      });
      //const response = await r.json();
      location.reload();
    },
  },
  mounted() {
    this.loading = true;
    fetch("http://35.208.193.188/playlists")
      .then((response) => response.json())
      .then((data) => {
        this.playlists = data;
        this.loading = false;
      })
      .catch((err) => console.log(err.message));
  },
};
</script>

<style>
#table-container {
  max-width: 400px;
  padding: 5px;
  margin: 0 auto;
}
#main-table {
  width: 100%;
  color: white;
}
#main-table th {
  background: #27afd8;
  padding: 7px;
}
#main-table td {
  background: #4a9eb8;
  text-align: center;
  padding: 7px;
}

#table-container button {
  float: right;
  border: none;
  padding: 5px 12px;
  margin: 10px 0;
  background-color: #4a9eb8;
  color: white;
  cursor: pointer;
}
h1 {
  color: white;
}
</style>
