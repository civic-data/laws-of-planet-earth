importScripts('bower_components/sw-toolbox/sw-toolbox.js'); 

// Set up routes from URL patterns to request handlers
//toolbox.router.get('/myapp/index.html', someHandler);

// For some common cases Service Worker Toolbox provides a built-in handler
toolbox.router.get('/(.*)', toolbox.networkFirst, {origin: 'http://open.senate.gov'});
//toolbox.router.get('/', toolbox.networkFirst);

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
toolbox.precache(['/getdata1_swtoolkit.html']);
