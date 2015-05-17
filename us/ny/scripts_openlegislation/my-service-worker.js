//globalOptions.debug=true;
importScripts('bower_components/sw-toolbox/sw-toolbox.js'); 

// Set up routes from URL patterns to request handlers
//toolbox.router.get('/myapp/index.html', someHandler);

// For some common cases Service Worker Toolbox provides a built-in handler
//toolbox.router.get('/(.*)', toolbox.networkFirst, {origin: 'http://open.senate.gov'});
//toolbox.router.get('/(.*)', toolbox.fastest, {origin: 'http://open.senate.gov'});
//toolbox.router.get('/(.*)', toolbox.fastest, {origin: 'https://origin-proxy.appspot.com'});
toolbox.router.get('/(.*)', toolbox.cacheFirst, {origin: 'https://www.google.com'});
toolbox.router.get('/(.*)', toolbox.cacheFirst, {origin: 'https://code.jquery.com'});
//https://code.jquery.com/jquery-2.1.3.min.js
toolbox.router.get('/(.*)', toolbox.cacheFirst, {origin: 'https://origin-proxy.appspot.com'});
toolbox.router.get('/', toolbox.networkFirst);

// URL patterns are the same syntax as ExpressJS routes
// (http://expressjs.com/guide/routing.html)

//toolbox.router.get(':foo/index.html', function(request, values) {
//return new Response('Handled a request for ' + request.url +
//', where foo is "' + values.foo + '");
//});

// For requests to other origins, specify the origin as an option
//toolbox.router.post('/(.*)', apiHandler, {origin: 'https://api.example.com'});

// Provide a default handler
//toolbox.router.default = myDefaultRequestHandler;

// You can provide a list of resources which will be cached at service worker install time
//toolbox.precache(['/getdata1_swtoolkit.html']);
toolbox.precache([
'/laws-of-planet-earth/us/ny/scripts_openlegislation/getdata1_swtoolkit.html',
'/laws-of-planet-earth/us/ny/scripts_openlegislation/bower_components/sw-toolbox/companion.js'
]);
