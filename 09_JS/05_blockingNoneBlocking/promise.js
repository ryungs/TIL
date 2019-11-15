const getUser = id => {
    const users = [
        { id: 1, githubID: 'ryungs' },
        { id: 2, githubID: 'ss3' },
    ];

    return new Promise((resolve, reject) => {
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

    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            if (repos) resolve(repos);
            else reject(new Error('No REPOs'))
        }, 1000);
    });
};


const getCommits = repo =>  {
    const commits = ['Init repo', 'Make index.html'];

    return new Promise((resolve, reject) => {
        setTimeout(()=>{
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERRRRRRORRR'));
            }
        }, 2000)
    });
};

getUser(1)

    .then(user => getRepos(user))
    .then(repos => getCommits(repos[0]))
    .then(commits => console.log(commits.length))
    // getUser를 가져오는 것을 실패했다면
    .catch(err => console.log(err));



// python 에서 쓰는 코드
// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])
// time = getTimeFromCommit(commits[0])
