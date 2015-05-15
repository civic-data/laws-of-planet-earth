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
    cache.add('/spinner.gif');
    //cache.add('https://code.jquery.com/jquery-2.1.3.min.js');
    //cache.add('https://ajax.googleapis.com/ajax/static/modules/gviz/1.1/core/tooltip.css');
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
