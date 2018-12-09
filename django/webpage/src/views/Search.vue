<template>
    <el-row>
        <el-col :span="24">
            <el-card class="box-card main-wrapper" style="text-align: center;">
                <h2>面向知识库的英文问答系统</h2>
                <div style="margin-top: 15px; max-width: 550px; margin: 15px auto">
                    <el-input placeholder="请输入内容" v-model="search" class="input-with-select" >
                        <el-select v-model="select" slot="prepend" placeholder="请选择" style="width: 120px;">
                            <el-option label="实体识别" value="1"></el-option>
                            <el-option label="答案搜索" value="2"></el-option>
                            <el-option label="实体搜索" value="3"></el-option>
                        </el-select>
                        <el-button slot="append" icon="el-icon-search" @click="onSubmit" :loading="flag"></el-button>
                    </el-input>
                </div>
                <img src="../assets/img_2.png" style="width:550px; margin: 30px auto 0 ;">
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
    // @ is an alias to /src
    export default {
        name: 'search',
        data: function() {
            return {
                baseURL: '',
                version: 'v1',
                search: '',
                select: '1',
                flag: false
            }
        },
        methods: {
            onSubmit() {
                if(!this.search) {
                    this.$message({
                        message: '请填写搜索信息',
                        type: 'warning'
                    });
                    return false
                }
                switch(this.select) {
                    case '1':
                        this.$router.push({ path: '/page/answer', query:{ search: this.search, type: this.select }})
                        break;
                    case '2':
                        this.flag = true
                        this.$axios.post(`${this.baseURL}/api/AnswerSearchFirst`, {
                            question: this.search,
                        })
                        .then(res => {
                            console.log(res)
                            this.flag = false
                            sessionStorage.answerStore = JSON.stringify(res.data)
                            this.$router.push({ path: '/page/graph', query: { hasRes: 'reco' }})
                        })
                        break;
                    default:
                        this.$router.push({ path: '/page/graph', query: { search: this.search, hasRes: 'sear' }})
                }
            }
        },
        mounted() {
            this.baseURL = (sessionStorage.model == 'simple'? this.baseSimple: this.baseWeb)
        }
    }
</script>

<style scoped>
  .el-card {
      min-height: 550px;
  }
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
