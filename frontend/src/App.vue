<template>
  <div id="app">
  <div id="nav">
<router-link to="/"> Home </router-link>
                <router-link to="/playlist"> Playlist 
                </router-link>
                <router-link to="/artista"> Artista </router-link>
            
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
body{
  background-image: url("./assets/imagen1.jpg");
  background-size: 100% 125%;
}
</style>


