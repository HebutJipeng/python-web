<template>
  <div class="wrapper">
      <!-- <image src=""> -->
      <h2>基于freebase的英文问答系统</h2>
      <el-row type="flex" class="row-bg" justify="center">
        <el-button type="primary" plain round @click="chooseModel('web')">Web</el-button>
        <el-button type="primary" plain round @click="chooseModel('simple')">Simple</el-button>
      </el-row>
  </div>
</template>

<script>
  // @ is an alias to /src
  
  export default {
    name: 'Index',
    methods: {
      chooseModel(type) {
        sessionStorage.model = type
        this.$router.push('/page/search')
      }
    }
  }
</script>

<style scoped>
  .wrapper {
    margin: 0 auto;
    width: 780px;
    height: 600px;
    overflow: hidden;
    text-align: center;
    color: #fff;
    background-size: cover;
    background-position: 50% 50%;
    background-repeat: no-repeat;
    background-image: url('../assets/bg.png');
  }
  h2 {
    text-align: center;
    color: #40549c;
    font-size: 2.5rem;
    margin-left: 5rem;
    margin-top: 13rem;
  }
  .el-button--primary.is-plain {
    width: 9.5rem;
  }
</style>
