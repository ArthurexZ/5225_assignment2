<template>
  <div class="register">
    <register-Mainbody></register-Mainbody>
  </div>
</template>

<script>
  import RegisterMainbody from './component/mainbody.vue'

export default {
  name: 'Register',
  components: {
    RegisterMainbody : RegisterMainbody,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
