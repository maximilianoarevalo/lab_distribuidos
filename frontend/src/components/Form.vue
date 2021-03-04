<template>
<div class="content">
  <div class="head">
    <h1>Predicción de datos</h1>
    <hr>
  </div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group" label="Dato:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.original"
          required
          placeholder="Ingrese el valor"
        ></b-form-input>
      </b-form-group>
     
    <b-container class="bv-example-row">
      <b-row>
        <b-col>
        <b-button class="a" type="submit" variant="success" @click="showDismissibleAlert=true" >Generar predicción</b-button>
        </b-col>
        <b-col>
        <b-button class="b" type="reset" variant="primary" @click="showDismissibleAlert=false">Solicitar nueva predicción</b-button>
        </b-col>
      </b-row>
    </b-container>    
    </b-form>
    <div class="alert">
    <b-alert v-model="showDismissibleAlert" variant="success" dismissible>
      <h1>
        Predicción generada exitosamente
      </h1>
      Valor predecido: {{this.predict}} <br/> 
    </b-alert>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    data() {
      return {
        form: {
          original: '',
        },
        show: true,
        showDismissibleAlert: false,
        predict: ''
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        console.log(this.form)
        let parameters = {
          original: this.form.original,
        };
        //axios.post('http://localhost:8080/app/newPass',parameters)
        console.log(parameters.original)
        axios.get('http://35.232.177.132:5000/model/'+parameters.original.toString())
        .then((response) => {
          this.predict = response.data
          
        })
        .catch((error)=> console.log(error))
        //alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.original = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
    }
  }
</script>

<style>
#input-group{
  margin-left:  25%;
  margin-right: 25%;
}
.head{
  padding: 10px; 
}

.content{
  margin-bottom: 15px;
}
.alert{
  margin-top: 5px;
  margin-left:  50px;
  margin-right: 50px;
}
.a{
  margin-left:  200px;
  width: 200px;

}
.b{
  margin-right: 200px;
  width: 200px;
}

</style>