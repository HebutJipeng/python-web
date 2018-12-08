<template>
    <div class="answer">
        <!--  <el-form :inline="true" :model="formInline" class="demo-form-inline">
            <el-form-item :label="title">
                <el-input v-model="formInline.user" :placeholder="title" style="width: 500px;"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit" plain>查询</el-button>
            </el-form-item>
        </el-form> -->
        <el-card class="box-card main-wrapper" style="padding: 10px 0;">
            <h2 style="text-align: center;">实体识别</h2>
            <el-row>
                <el-col :span="18" :offset="3">
                    <el-form ref="form" label-width="115px">
                        <el-row>
                            <el-col :span="24">
                                <el-form-item label="问句:  " :class="['no-margin']">
                                   {{ inputquestion }} 
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-form-item label="最佳:  " :class="['no-margin']">
                                    {{ entitylist[0] }}
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24">
                                <el-form-item label="候选:  ">
                                    <el-radio v-for="item in entitylist" v-model="radio" :label="item" v-bind:key="item">{{item}}</el-radio>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col :span="24   ">
                                <el-form-item label="反馈:  ">
                                    <el-input type="textarea" v-model="feedback"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-form-item>
                            <el-button type="primary" @click="onSubmit">提交</el-button>
                            <el-button type="primary" @click="viewAnswer">查看答案</el-button>
                        </el-form-item>
                    </el-form>
                </el-col>
            </el-row>
        </el-card>
    </div>
</template>
<script>
// @ is an alias to /src

export default {
    name: 'answer',
    data: function() {
        return {
            feedback: '',
            radio: '',
            inputquestion: '',
            IOBlist: [],
            entitylist: [],
            midlist: []
        }
    },
    components: {},
    methods: {
        onSubmit() {
            this.$axios.post(`EntityRecognization`, {})
            .then(res => {
                if (res.data.isOk) {
                    console.log(res)
                }
            })
        },
        viewAnswer() {

        }
    },
    mounted() {
        const _this = this
        // const search = this.$route.query.search
        // const type = this.$route.query.type
        this.$axios.get(`/EntityRecognization`)
        .then(res => {
            if (res.data.isOk) {
                console.log(res.data.data)
                const result = res.data.data
                _this.inputquestion = result.inputquestion
                _this.IOBlist = result.inputquestion
                _this.entitylist = result.entitylist
                _this.midlist = result.midlist
            }
        })
    },
}
</script>
<style>
.el-form-item {
    margin-bottom: 16px;
}

.no-margin {
    margin: 0 0 10px;
}
</style>