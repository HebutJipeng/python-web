<template>
    <el-row>
        <el-col :span="24">
            <el-card class="box-card">
                <div style="margin-top: 15px; max-width: 550px;">
                    <el-input placeholder="请输入内容" v-model="search" class="input-with-select">
                        <el-select v-model="select" slot="prepend" placeholder="请选择">
                            <el-option label="实体识别" value="1"></el-option>
                            <el-option label="答案搜索" value="2"></el-option>
                        </el-select>
                        <el-button slot="append" icon="el-icon-search"></el-button>
                    </el-input>
                </div>
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
                search: '',
                select: '1'
            }
        },
        method: {
            onSubmit() {
                console.log(1)
            }
        }
    }
</script>

<style>
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
