<template>
    <div class="answer">
        <el-card
            class="box-card main-wrapper" 
            style="padding: 10px 0;">
            <h2 style="text-align: center;">实体识别</h2>
            <el-row>
                <el-col :span="18" :offset="3">
                    <el-form 
                        ref="form" 
                        label-width="115px" 
                        v-loading="loading">
                        <el-row>
                            <el-col :span="24">
                                <el-form-item label="问句:  " :class="['no-margin']">
                                   {{ inputquestion }} 
                                </el-form-item>
                            </el-col>
                        </el-row>

                        <el-row v-if="type=='a'">
                            <el-col :span="24">
                                <el-form-item label="最佳:  " :class="['no-margin']">
                                    {{ bestentityName }}-{{ entity }}
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row v-if="midlist.length>0&&type=='a'">
                            <el-col :span="24">
                                <el-form-item label="候选:  ">
                                    <el-radio v-for="(item, key) in midlist" v-model="radio" :label="item" v-bind:key="item">{{ midlistName[key] }}-{{ item }}</el-radio>
                                </el-form-item>
                            </el-col>
                        </el-row>

                        <el-row v-if="type=='b'">
                            <el-col :span="24">
                                <el-form-item label="最佳:  " :class="['no-margin']">
                                    <span v-for="(item, id) in bestentityName" v-bind:key="id">{{ item }}-{{ entity[id] }} ; </span>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row v-if="midlist.length>0&&type=='b'">
                            <el-col :span="24">
                                <el-form-item label="候选:  " v-for="(it, idx) in midlist" :key="idx">
                                    <el-radio v-for="(item, key) in it" v-model="radio[idx]" :label="item" v-bind:key="item">{{ midlistName[idx][key] }}-{{ item }}</el-radio>
                                </el-form-item>
                            </el-col>
                        </el-row>

                        <el-row>
                            <el-col :span="24">
                                <el-form-item label="反馈:  ">
                                    <el-input type="textarea" v-model="feedback"></el-input>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-form-item>
                            <el-button type="primary" @click="onSubmit" :loading="flag">提交并查看答案</el-button>
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
            baseURL: '',
            version: 'v1',
            feedback: '',
            radio: '',
            inputquestion: '',
            bestentityName: '',
            entity: '',
            midlist: [],
            midlistName: [],
            entityName: '',
            flag: false,
            loading: true,
            type: 'a'
        }
    },
    components: {},
    methods: {
        onSubmit() {
            this.flag = true
            let e
            let en
            if(this.type == 'a') {
                e = this.radio == ''? this.entity : this.radio
                en = this.entityName
            } else {
                e = []
                e.push(this.radio[0] == ''? this.entity[0] : this.radio[0])
                e.push(this.radio[1] == ''? this.entity[1] : this.radio[1])
                e = JSON.stringify(e)
                en = JSON.stringify(this.entityName)
            }
            this.$axios.post(`${this.baseURL}/api/EntityRecognization`, {
                bestentity: e,
                inputquestion: this.inputquestion,
                entityName: en,
                feedback: this.feedback,
                type: this.type
            })
            .then(res => {
                this.flag = false
                sessionStorage.answerStore = JSON.stringify(res.data)
                this.$router.push({ path: '/page/graph', query: { hasRes: 'reco' }})
            })
        },
        viewAnswer() {

        }
    },
    mounted() {
        const _this = this
        const search = this.$route.query.search
        this.baseURL = (sessionStorage.model == 'simple'? this.baseSimple: this.baseWeb)
        // const type = this.$route.query.type
        if(search) {
            this.$axios.put(`${this.baseURL}/api/EntityRecognization`, {
                inputquestion: search
            })
            .then(res => {
                if(res.status == 200) {
                    const result = res.data
                    _this.inputquestion = result.inputquestion
                    _this.entity = result.bestentity
                    _this.bestentityName = result.bestentity_name
                    _this.midlist = result.midlist
                    _this.midlistName = result.midlist_name
                    _this.entityName = result.entityName
                    if(typeof result.bestentity == 'string') {
                        _this.type = 'a'
                    } else {
                        _this.type = 'b'
                        _this.radio = ['', '']
                    }
                    _this.loading = false
                } else {
                    this.$message({
                        message: res.data,
                        type: 'error'
                    })
                    this.$router.push({ path: '/page/search' })
                }
            })
        } else {
            this.$message({
                message: '请填写搜索信息',
                type: 'warning'
            });
            this.$router.push({ path: '/page/search' })
        }
        
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