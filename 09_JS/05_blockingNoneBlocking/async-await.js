const getUser = id => {
    const users = [
        { id: 1, githubID: 'ryungs' },
        { id: 2, githubID: 'ss3' },
    ];

    return new Promise((resolve, reject) =>{
        setTimeout(()=>{
            const user = users.find(user => user.id === id);
            if (user) {
                resolve(user);
            } else {
                reject (new Error(`Can not find user with id ${id}`));
            }
        }, 2000)
    });
};


const getRepos = user => {
    const repos = ['TIL', 'Workshop_HW', 'Python', 'JS'];

    return new Promise((resolve, reject) =>{
        setTimeout(()=>{
            if (repos) resolve(repos);
            else reject(new Error('No REPOs'))
        }, 1000);
    });
};


const getCommits = repo =>  {
    const commits = ['Init repo', 'Make index.html'];

    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERRRRRRORRR'));
            }
        }, 2000)
    });
};


// async 는 비동기적 요소(non-block 요소)가 있는 함수 안에서만 쓰는 거고 Promise 로 return 할 때만 쓸 수 있다.
// await 는 나 함수 안에 기다려야 하는 요소 있는데? 라고 했을 때 써야 다음 함수를 실행한다.

async function main() {
    // 성공했을 때 try
    try {
        // getUser를 가져오는 것을 성공했다면 => getCommits를 가져오고 => 또 성공했다면 commits의 길이를 return 해줘
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commit = await getCommits(repos[0]);
        console.log(commit.length);
    // 실패했을 때 catch
    } catch (e) {
        // error 메세지를 보여줘
        console.error(e);
    }
}

main();

// python 에서 쓰는 코드
// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])
// time = getTimeFromCommit(commits[0])
