# client

## Coding

### Add a route/component

- Add component to src/components using `Vue` style, such as `Job.vue`
- Register component in `src/router.js`
    ```
    import Job from './components/Job.vue';
	```
- Add route:
   ```
     routes: [
	 ...,
    {
      path: '/job/:id?',
      name: 'Job',
      component: Job,
    }
	],
	```
## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
