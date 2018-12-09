<template>
    <el-row>
        <el-col :span="24">
            <el-card class="box-card main-wrapper">
                <h2 style="text-align: center; margin-bottom: 0;">{{ title }}</h2>
                <el-row>
                    <el-col 
                        :span="12" 
                        v-loading="loading">
                        <div id="main" style="width: 100%;min-height: 500px;"></div>
                    </el-col>
                    <el-col :span="10" :offset="1">
                        <h4 v-if="inputquestion">问句: {{ inputquestion }}</h4>
                        <el-card v-if="answers" shadow="always" style="word-break: break-all;font-size: 12px; width: 100%; margin-top: 10px;">
                            答案: {{ answers }}
                        </el-card>
                        <h4 style="margin-bottom:0">description:</h4>
                        <el-card shadow="always" style="font-size: 12px; width: 100%; margin-top: 10px;">
                            {{ desc }}
                        </el-card>
                    </el-col>
                </el-row>
            </el-card>
        </el-col>
    </el-row>

</template>

<script>
    // @ is an alias to /src
    import { formatMap } from '@/utils/utils.js'
    export default {
        name: 'graph',
        data: function() {
            return {
                baseURL: '',
                title: '答案搜索',
                visible: false,
                formInline: {
                    user: '',
                    region: ''
                },
                entityname: '',
                q_entity: '',
                parse: '',
                triplelen: '',
                ansTriple: [],
                otherTriple: [],
                desc: 'loading...',
                loading: true,
                inputquestion: '',
                answers: '',
                version: 'v1',
                parselist: []
            }
        },
        methods: {
            draw: function() {
                const _this = this
                var myChart = this.$echarts.init(document.getElementById('main'));
                this.$axios.post(`${this.baseURL}/api/AnswerShow`, {
                    entityname: _this.entityname,
                    q_entity: _this.q_entity,
                    parse: _this.parse,
                    triplelen: _this.triplelen,
                    parselist: JSON.stringify(_this.parselist)
                })
                .then(res => {
                    _this.otherTriple = res.data.otherTriple

                    var graph = formatMap({
                        ans: _this.ansTriple,
                        other: res.data.otherTriple
                    })
                    var categories = [];
                    for (var i = 0; i < 20; i++) {
                        categories[i] = {
                            name: '类目' + i
                        };
                    }
                    graph.nodes.forEach(function(node) {
                        node.itemStyle = null;
                        node.value = node.symbolSize;
                        node.symbolSize /= 1.5;
                        node.label = {
                            normal: {
                                show: true
                            }
                        };
                        node.category = node.attributes.modularity_class;
                    });
                    console.log(graph)
                    let option = {
                        tooltip: {
                            trigger: 'item',
                            formatter: function (params) {//连接线上提示文字格式化
                                return params.name;
                            }
                        },
                        // legend: [{
                        //     // selectedMode: 'single',
                        //     data: categories.map(function(a) {
                        //         return a.name;
                        //     })
                        // }],
                        animationDuration: 1500,
                        animationEasingUpdate: 'quinticInOut',
                        series: [{
                            name: '实体关系图',
                            type: 'graph',
                            layout: 'force',
                            data: graph.nodes,
                            links: graph.links,
                            categories: categories,
                            roam: true,
                            focusNodeAdjacency: true,
                            itemStyle: {
                                normal: {
                                    borderColor: '#fff',
                                    borderWidth: 1,
                                    shadowBlur: 10,
                                    shadowColor: 'rgba(0, 0, 0, 0.3)',
                                }
                            },
                            label: {
                                position: 'top',
                                formatter: '{b}'
                            },
                            lineStyle: {
                                color: 'source',
                                curveness: 0.3,
                                width: 5
                            },
                            emphasis: {
                                lineStyle: {
                                    width: 10
                                }
                            },
                            force: {
                                repulsion: 200
                            }
                        }]
                    };
                    myChart.setOption(option);
                    _this.loading = false
                })

            },
            puredraw: function(data) {
                const _this = this
                var myChart = this.$echarts.init(document.getElementById('main'));

                console.log(data)
                var graph = formatMap({
                    ans: data.ansTriple,
                    other: data.otherTriple
                })

                var categories = [];
                for (var i = 0; i < 20; i++) {
                    categories[i] = {
                        name: '类目' + i
                    };
                }
                graph.nodes.forEach(function(node) {
                    node.itemStyle = null;
                    node.value = node.symbolSize;
                    node.symbolSize /= 1.5;
                    node.label = {
                        normal: {
                            show: true
                        }
                    };
                    node.category = node.attributes.modularity_class;
                });
                console.log(graph)
                let option = {
                    tooltip: {
                        trigger: 'item',
                        formatter: function (params) {//连接线上提示文字格式化
                            return params.name;
                        }
                    },
                    // legend: [{
                    //     // selectedMode: 'single',
                    //     data: categories.map(function(a) {
                    //         return a.name;
                    //     })
                    // }],
                    animationDuration: 1500,
                    animationEasingUpdate: 'quinticInOut',
                    series: [{
                        name: '实体关系图',
                        type: 'graph',
                        layout: 'force',
                        data: graph.nodes,
                        links: graph.links,
                        categories: categories,
                        roam: true,
                        focusNodeAdjacency: true,
                        itemStyle: {
                            normal: {
                                borderColor: '#fff',
                                borderWidth: 1,
                                shadowBlur: 10,
                                shadowColor: 'rgba(0, 0, 0, 0.3)',
                            }
                        },
                        label: {
                            position: 'top',
                            formatter: '{b}'
                        },
                        lineStyle: {
                            color: 'source',
                            curveness: 0.3,
                            width: 5
                        },
                        emphasis: {
                            lineStyle: {
                                width: 10
                            }
                        },
                        force: {
                            repulsion: 200
                        }
                    }]
                };
                myChart.setOption(option);
                _this.loading = false
            }
        },
        mounted() {
            const _this = this
            this.baseURL = (sessionStorage.model == 'simple'? this.baseSimple: this.baseWeb)
            const flag = this.$route.query.hasRes
            if(flag == 'reco') {
                const res = JSON.parse(sessionStorage.answerStore)
                _this.desc = res.desc
                _this.ansTriple = res.ansTriple
                _this.entityname = res.entityname
                _this.q_entity = res.q_entity
                _this.parse = res.parse
                _this.triplelen = res.triplelen
                _this.inputquestion = res.inputquestion
                _this.parselist = res.parselist
                let l = []
                res.ansTriple.forEach(item => {
                    l.push(item[2])
                })
                _this.answers = l.join(',')
                this.draw()
            } else if(flag == 'sear') {
                this.title = '实体搜索'
                const search = this.$route.query.search
                this.$axios.post(`${this.baseURL}/api/EntityResearch`, {
                    keyword: search
                })
                .then(res => {
                    if(res.status == 200) {
                        _this.desc = res.data.description
                        _this.inputquestion = res.data.inputquestion
                        this.puredraw(res.data)
                    } else {
                        this.$message({
                            message: `查询错误, ${res.data}`,
                            type: 'error'
                        })

                        setTimeout(() => {
                            _this.$router.push({ path: '/page/search' })
                        }, 500)
                    }
                    console.log(res)
                })
            } else {
                 this.$message({
                    message: '请填写搜索信息',
                    type: 'warning'
                });
                _this.$router.push({ path: '/page/search' })
            }
        },
    }
</script>
