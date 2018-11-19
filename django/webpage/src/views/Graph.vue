<template>
    <el-row>
        <el-col :span="24">
            <el-card class="box-card">
                <div id="main" style="width: 100%;height:600px;"></div>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
    // @ is an alias to /src
    
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
                var myChart = echarts.init(document.getElementById('main'));
                $.get('/data/data.json', function(res) {

                    // var graph = echarts.dataTool.gexf.parse(res);
                    var graph = res
                    console.log(graph)
                    // var graph = res

                    var categories = [];
                    for (var i = 0; i < 9; i++) {
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
                                show: node.symbolSize > 25
                            }
                        };
                        node.category = node.attributes.modularity_class;
                    });
                    let option = {
                        title: {
                            text: '实体关系图',
                            subtext: 'Default layout',
                            top: 'bottom',
                            left: 'right'
                        },
                        tooltip: {},
                        legend: [{
                            // selectedMode: 'single',
                            data: categories.map(function(a) {
                                return a.name;
                            })
                        }],
                        animationDuration: 1500,
                        animationEasingUpdate: 'quinticInOut',
                        series: [{
                            name: '实体关系图',
                            type: 'graph',
                            layout: 'circular',
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
                                    shadowColor: 'rgba(0, 0, 0, 0.3)'
                                }
                            },
                            label: {
                                position: 'right',
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
