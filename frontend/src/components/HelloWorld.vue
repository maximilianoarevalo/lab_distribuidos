<template>
<div>
  <b-card title="Permiso generado exitosamenteXD">
    <b-card-text>
      <!-- Consumo el JSON -->
      Valor predecido: {{predict}}
    </b-card-text>

    <b-button class="mt-3" variant="success" href="/">Solicitar nueva predicción</b-button>
  </b-card>
</div>
</template>


<script>
import axios from 'axios'
  export default {
    data() {
      return {
        dialog: false,
        predict: ''
      }
    },
    methods:{
      setInfo: function(Result){
        this.dialog = false;
        console.log(Result)
        this.predict = Result.predict
      }
    },
    mounted(){
      //axios.get('http://localhost:8080/app/pass')
      axios.get('http://35.232.177.132:5000/model/')
      .then(response => (this.info = response))
    }
  }
</script>

<style>

</style>