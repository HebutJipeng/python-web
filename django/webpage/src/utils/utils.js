export function formatMap(data) {
    // const entity = data.triple.entity
    // const answer = data.triple.answer
    let link = data.triple.link
    const ans = data.hasOwnProperty('answer')
    const nodes = formatNodes(link, ans)
    const links = formatLinks(link, nodes)
    return {
        nodes: nodes, 
        links: links
    }
}

function formatNodes(link, ans=false) {
    let s = new Set()
    let nodes = []
    link.forEach(item => {
        const arr = item.split(',')
        s.add(arr[0])
        s.add(arr[2])
    })
    Array.from(s).forEach((se, key) => {
        if (key == 0) {
           nodes.push(nodeTemplate(key, se, 60)) 
        } else if(ans && key == 1) {
           nodes.push(nodeTemplate(key, se, 50)) 
        } else {
           nodes.push(nodeTemplate(key, se, 25)) 
        }
    })
    return nodes
}

function nodeTemplate(idx, name, size) {
   return {
        "id": idx,
        "name": name,
       "itemStyle": {
           "normal": {
               "color": "rgb(235,81,72)"
           }
       },
       "symbolSize": size,
       "attributes": {
           "modularity_class": idx
       }
   } 
}

function formatLinks(link) {
    let s = new Set()
    let links = []
    link.forEach(item => {
        const arr = item.split(',')
        s.add(arr[0])
        s.add(arr[2])
    }) 
    const arrset = Array.from(s)
    link.forEach(item => {
        const arr = item.split(',')
        links.push(linkTemplate(arr[1], arrset.indexOf(arr[0]), arrset.indexOf(arr[2])))
    })
    return links
}

function linkTemplate(id, source, target) {
   return {
       "id": id,
       "name": null,
       "source": source.toString(),
       "target": target.toString(),
       "lineStyle": {
           "normal": {}
       }
   } 
}