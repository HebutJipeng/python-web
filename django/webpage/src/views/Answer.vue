<template>
    <div class="answer">
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
            <el-form-item :label="title">
                <el-input v-model="formInline.user" :placeholder="title" style="width: 500px;"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit" plain>查询</el-button>
            </el-form-item>
        </el-form>
        <el-row>
            <el-col :span="22">
                <el-card class="box-card" style="padding: 10px 0; min-height: 500px;">
                    <el-form ref="form" :model="form" label-width="115px">
                        <el-row>
                            <el-col :span="14">
                                <el-form-item label="Question:  " :class="['no-margin']">
                                    问题
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="14">
                                <el-form-item label="最佳:  " :class="['no-margin']">
                                    最佳答案
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="14">
                                <el-form-item label="候选:  " >
                                    候选答案
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="18">
                                <el-form-item label="反馈:  ">
                                    <el-input type="textarea" v-model="feedback"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-form-item>
                            <el-button type="primary" @click="onSubmit">提交</el-button>
                        </el-form-item>
                    </el-form>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    // @ is an alias to /src
    
    export default {
        name: 'answer',
        data: function () {
        return {
            title: '实体识别',
            feedback: '',
            visible: false,
            formInline: {
                user: '',
            },
            form: {
                name: ''
            }
            }
        },
        components: {
        },
        methods: {
            onSubmit() {
            console.log('submit!');
            }
        }
    }
</script>

<style>
    .el-form-item {
        margin-bottom: 16px;
    }
    .no-margin {
        margin: 0;
    }
</style>
