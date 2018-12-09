export function formatMap(data) {
    // const entity = data.triple.entity
    // const answer = data.triple.answer
    const nodes = formatNodes(data.ans, data.other)
    const links = formatLinks(data, nodes)
    return {
        nodes: nodes, 
        links: links
    }
}

function formatNodes(ans, other) {
    let s = new Set()
    let ss = new Set()
    let nodes = []
    let step = 0
    ans.forEach(item => {
        s.add(item[0])
        s.add(item[2])
    })
    const sarr = Array.from(s)
    sarr.forEach((se, key) => {
        if (key == 0) {
            nodes.push(nodeTemplate(key, se, 80)) 
        } else {
            nodes.push(nodeTemplate(key, se, 50))
        }
        step = key
    })
    if (sarr.length == 0) {
       step = -1 
    }

    other.forEach(item => {
        ss.add(item[0])
        ss.add(item[2])
    })
    let idx = 0
    Array.from(ss).forEach((se) => {
        if (sarr.indexOf(se)== -1) {
            nodes.push(nodeTemplate(idx, se, 25, step+1))
            idx++
        }
    })
    return nodes
}

function nodeTemplate(idx, name, size, step = 0) {
   return {
        "id": idx + step,
        "name": name,
       "itemStyle": {
           "normal": {
               "color": "rgb(235,81,72)"
           }
       },
       "symbolSize": size,
       "attributes": {
           "modularity_class": idx + step
       }
   } 
}

function formatLinks(data) {
    let s = new Set()
    const ans = data.ans
    const other = data.other

    let links = []
    ans.forEach(item => {
        s.add(item[0])
        s.add(item[2])
    })
    other.forEach(item => {
        s.add(item[0])
        s.add(item[2])
    })
    const arrset = Array.from(s)
    
    ans.forEach(item => {
        links.push(linkTemplate(item[1], arrset.indexOf(item[0]), arrset.indexOf(item[2])))
    })
    other.forEach(item => {
        links.push(linkTemplate(item[1], arrset.indexOf(item[0]), arrset.indexOf(item[2])))
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