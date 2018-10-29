const rq = require('request');
var request = rq.defaults({ jar: true })
var j = request.jar()

let user = {
    nickName: 'peng1234',
    email: 'peng123457890@gmail.com',
    password: '123456'
}

// let header = {
//     'Content-Type': 'application/json',
//     'Accept': 'application/json, text/plain, */*',
//     'Accept-Encoding': 'gzip, deflate',
//     'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8,ja;q=0.7,th;q=0.6,ru;q=0.5,id;q=0.4,pt;q=0.3,zh-TW;q=0.2,de;q=0.1,en;q=0.1,en-US;q=0.1,es;q=0.1,it;q=0.1,hi;q=0.1',
//     'Connection': 'keep-alive',
//     'Content-Length': '0',
//     'Cookie': 'sid=' + cookies['sid'],
//     'Host': 'contest.farener.com',
//     'Origin': 'http://contest.farener.com',
//     'Referer': 'http://contest.farener.com/home',
//     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89;Keep/5.7.9 (iPhone; iOS 10.3.2; Scale/2.00)',
// }

function header(sid) {
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8,ja;q=0.7,th;q=0.6,ru;q=0.5,id;q=0.4,pt;q=0.3,zh-TW;q=0.2,de;q=0.1,en;q=0.1,en-US;q=0.1,es;q=0.1,it;q=0.1,hi;q=0.1',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'sid=' + sid,
        'Host': 'contest.farener.com',
        'Origin': 'http://contest.farener.com',
        'Referer': 'http://contest.farener.com/home',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89;Keep/5.7.9 (iPhone; iOS 10.3.2; Scale/2.00)',
    }
}

let data = {
    'videoID': 30
}

let URL = `http://contest.farener.com/api/user/register?nickName=${user.nickName}&email=${user.email}&password=${user.password}`
let voteURL = 'http://contest.farener.com/api/vote?videoID=30'

request.post(URL, function (error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(JSON.parse(body).data);
        request.post(
          {
            url: voteURL,
            headers: JSON.stringify(header(JSON.parse(body).data.sid))
          },
          data,
          function(error, response, body) {
            console.log(response);
          }
        );
    }
});