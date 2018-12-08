<template>
  <div id="app">
    <!-- <sync-loader class="custom-class" :color="'#409EFF'" :loading="loading" :size="15" :sizeUnit="'px'" :margin="'2px'"></sync-loader> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "app",
  data: function () {
    return {
      loading: true
    }
  }
};
</script>

<style>
  html,
  body {
    padding: 0;
    margin: 0;
  }

  .main-wrapper {
    min-height: 550px;
  }

  h1 {
    margin: 0;
  }
  .el-header,
  .el-footer {
    background-color: #409EFF;
    color: #fff;
    line-height: 60px;
  }

  .el-header h1 {
    font-weight: bold;
    color: #fff;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    height: 100vh;
  }

  body>.el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

  a {
    text-decoration: none;
    color: #666;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .3s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }

  .slide-fade-enter-active {
    transition: all .5s ease;
  }
  .slide-fade-leave-active {
    transition: all 0s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }
  .slide-fade-enter, .slide-fade-leave-to
  /* .slide-fade-leave-active for below version 2.1.8 */ {
    transform: translateX(10px);
    opacity: 0;
  }
</style>
