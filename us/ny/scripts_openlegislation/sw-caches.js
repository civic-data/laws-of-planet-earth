CACHENAMEDYNAMIC="civic-data-dynamic"
CACHENAMEFILES="civic-data-static-v1"
console.log('Service Worker!!!');
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.open(CACHENAMEDYNAMIC).then(function(cache) {
      return fetch(event.request).then(function(response) {
console.log('putting: ' + event.request);
        cache.put(event.request, response.clone());
        return response;
      });
    })
  );
});

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHENAMEFILES).then(function(cache) {
    console.log('QQQ:CACHE:');
    console.log(cache);
    cache.add('/getdata1_caches.html');
    /*
      return cache.addAll([
        //'/',
        // '/getdata1_caches.html'
        // etc
      ]);
      */
    })
  );
});
console.log('...done Service Worker!!!');
