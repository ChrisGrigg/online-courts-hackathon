<template>
  <header class="app-header navbar">
    <slot></slot>
    <div class="row">
      <div class="ml-1"><img id="hmcts" src="static/img/HMCTS.png" alt=""></div>
    </div>
  </header>
</template>
<script>
export default {
  name: 'navbar',
  created () {
    this._navbar = true
  }
}
</script>
<style lang="css">

  #hmcts {
    height: 60px;
  }

</style>
