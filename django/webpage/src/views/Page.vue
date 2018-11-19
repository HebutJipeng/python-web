<template>
  <div class="page">
    <el-container>
      <el-header>
        <router-link to="/">
          <h1><i class="el-icon-date"></i> 问答系统</h1>
        </router-link>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
            <el-menu :default-openeds="['1']">
              <router-link to="/page/search">
                <el-menu-item index="1-1">输入问句</el-menu-item>
              </router-link>
              <router-link to="/page/answer">
                <el-menu-item index="1-2">实体识别</el-menu-item>
              </router-link>
              <router-link to="/page/graph">
                <el-menu-item index="1-3">答案搜索</el-menu-item>
              </router-link>

            </el-menu>
          </el-aside>
        </el-aside>
        <el-main>
          <transition name="slide-fade">
            <router-view/>
          </transition>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
}
</script>
