let fs = require('fs')
let lines = fs.readFileSync('./final-rank.txt', 'utf-8').split('\n')

let l = ''

// lines.forEach((item, index)=> {
//    let a = item.split('\t') 
//    if(a[0].match(/\d/)) {
//        console.log(index, '--', item)
//        l += `${index+1}\t${item}\n`
//    }
// });



// let temp = ''
// let i = 0

// lines.forEach((item, index)=> {
//    let a = item.split('\t') 
//    if (temp != a[0]) {
//        i++
//    }
//    l += `${i}\t${item}\n`
//    temp = a[0]
// });


lines.forEach((item, index)=> {
   let a = item.split('\t') 
   console.log(a)
   console.log(a[1])
   if(a[1].match(/\d/)) {
       console.log(index, '--', item)
       l += `${item}\n`
   }
});

fs.writeFile('./final-rank-list.txt', l, function (err) {
   if (err) {
      return console.error(err) 
   } 
})