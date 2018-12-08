let fs = require('fs');
let obj = JSON.parse(fs.readFileSync('./WebQSP.train.json', 'utf8'));

let qa = obj['Questions']
let content = ''
qa.forEach((item, key) => {
    let parse = item.Parses
    parse.forEach(it => {
        let list = it.Answers.map(item => {
            return item.AnswerArgument
        })
        console.log(item.RawQuestion, '\t', list.join(' '))
        content += `${item.RawQuestion}\t${list.join(' ')}\n`
    })
})

writeFile(content)

function writeFile(content) {
    fs.writeFile('./WebQSP.train-1.json', content, function (err) {
        if (err) {
            return console.error(err);
        }
    }); 
}
