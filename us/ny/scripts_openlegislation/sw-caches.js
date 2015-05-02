console.log('Service Worker!!!');
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.open('mysite-dynamic').then(function(cache) {
      return fetch(event.request).then(function(response) {
console.log('putting: ' + event.request);
        cache.put(event.request, response.clone());
        return response;
      });
    })
  );
});
console.log('...done Service Worker!!!');
