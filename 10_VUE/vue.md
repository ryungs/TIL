# VueJS

## directives(v - MAGIC)

1. v-on

   1. EventListner 를 달 때 사용
   2. 줄여서 @
   3. 체이닝 가능. `v-on:keyup.enter`
   4. = 콜백함수 `v-on:keyup.enter="someFunction()"`

2. v-for

   1. `v-for` vs `v-if`=> `v-for`한테 우선순위가 있음

3. v-if / v-else-if/ v-else

   1. ```js
      <template v-if="completed"> ... </template> // template 안에 넣어주면 completed일 때만 ...을 동작하게 한다.
      ```

      

   2. 아래 v-show와 비교해서 `<h1 v-if="false">안녕</h1>` => 브라우저에서 사라짐

4. v-show

   1. `<h1 v-show="completed">` => `<h1 display="none">`
   2. `<h1 v-show="false">안녕</h1>` => `<h1 display="none">안녕</h1>`

   

5. v-bind

   1. HTML 태그에서 attribute 의 값에 Vue의 data, methods, ...etc를 쓰고 싶을 때.
   2. `<a href='url'> `xxx / `<a v-bind:href='url'>` 이건 가능
   3. 줄여서, :

6. v-model

   1. 사용자 입력과 관련있는(`<form>`태그 안의) 태그들의 입력 값 <=쌍방향 Bind => Vue Data app.$data

7. v-once

   1. data 에서 처음 받고 나면 안바뀜
   2. `<h1 v-once>{{ greeting }} </h1>` => 아무리 앱이 동작하면서 greeting이 바뀌어도, 처음 그 값 그대로!

8. v-html

   1. { test: '<img src="asdsdf">'}
   2. `<div>{{ text }}</div>` => div 안에 문자로 <img src...> 이렇게 나온다.
   3. `<div v-html=text></div>` => 실제 HTML 처럼 동작함 

## KEY

```js
const app = new Vue({
    key1: {},
    key2: {},
})
```

1. el : ''
2. data: { key: str, number, array, object }
3. methods: { keyVerb: function } => 함수들의 집합
4. computed: { keyNoun: function } => 접근할 때, 함수실행 안됨. function 안의 값들 중 data 들이 바뀌면 알아서 실행 => 캐싱(저장) 됨, 접근하면, 저장된 값이 나옴
5. watch: { key: function } => data에서 key 값이 변하면 자동 실행됨. 실행시점 못 정함