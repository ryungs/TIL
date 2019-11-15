
function getUser(id, callback) {
    setTimeout(()=>{
        const users = [
            { id: 1, githubID: 'ryungs' },
            { id: 2, githubID: 'ss3' },
        ];
        const user = users.find(user => user.id === id);
        console.log('Data Loaded!');
        console.log(user);
        callback(user);
    }, 2000)
}

const getRepos = (user, callback) => {
    setTimeout(()=>{
        const repos = [
            'TIL',
            'Workshop_HW',
            'Python',
            'JS'
        ];
        console.log('Data Loaded');
        console.log(repos);
        callback(repos)
    }, 2000)
};

function getCommits (repo, callback) {
    setTimeout(()=>{
        const commits = [
            'Init repo',
            'Make index.html',
        ];
        console.log('Data Loaded!');
        console.log(commits);
        callback(commits);
    }, 2000)
}

getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(`${commits.length} 개 커밋을 했네요!`)
        })
    })
});

// python 에서 쓰는 코드
// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])
// time = getTimeFromCommit(commits[0])
