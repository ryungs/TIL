
function makeArticle(id, title, content) {
    return {
        id: id,
        title: title,
        content: content,
        makeONE: function () {
            return `${this.id} 번 글: ${this.title} => ${this.content}`
        }
    }
}

function makeArticle(id, title, content) {
    return {
        id,
        title,
        content,
        makeONE () {
            return `${this.id} 번 글: ${this.title} => ${this.content}`
        },
    }
}
