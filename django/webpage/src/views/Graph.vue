<template>
    <el-row>
        <el-col :span="24">
            <el-card class="box-card main-wrapper">
                <h2 style="text-align: center; margin-bottom: 0;">实体搜索</h2>
                <el-row>
                    <el-col :span="12">
                        <div id="main" style="width: 100%;min-height: 500px;"></div>
                    </el-col>
                    <el-col :span="10" :offset="1">
                        <h4 style="margin-bottom:0">description:</h4>
                        <el-card shadow="always" style="font-size: 12px; width: 100%; margin-top: 10px;">The 1973 NBA World Championship Series pitted the New York Knicks of the Eastern Conference against the Los Angeles Lakers of the Western Conference for the NBA championship. The series was an exact reversal of the prior year, with the Lakers winning Game 1 and the Knicks taking the next four games
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
                visible: false,
                formInline: {
                    user: '',
                    region: ''
                }
            }
        },
        methods: {
            draw: function() {
                var myChart = this.$echarts.init(document.getElementById('main'));
                this.$axios.get(`/EntityAnswer`)
                .then(res => {

                    // var graph = echarts.dataTool.gexf.parse(res);
                    var graph = formatMap(res.data.data)
                    // var graph = res

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
                })

            }
        },
        mounted() {
            this.draw()
        },
    }
</script>
