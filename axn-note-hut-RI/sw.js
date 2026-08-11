var CACHE_NAME = 'axn-note-cache-v2.6.0-merdeka';

var ICON_PATHS = [];
for (var i = 1; i <= 23; i++) {
  ICON_PATHS.push('./assets/icons/icon-' + i + '.svg');
}

var PRECACHE_URLS = [
  './',
  './index.html',
  './manifest.json'
].concat(ICON_PATHS);

self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        return cache.addAll(PRECACHE_URLS);
      })
      .then(function () {
        return self.skipWaiting();
      })
  );
});

self.addEventListener('activate', function (event) {
  event.waitUntil(
    caches.keys()
      .then(function (keys) {
        return Promise.all(
          keys
            .filter(function (key) {
              return key !== CACHE_NAME;
            })
            .map(function (key) {
              return caches.delete(key);
            })
        );
      })
      .then(function () {
        return self.clients.claim();
      })
  );
});

self.addEventListener('fetch', function (event) {
  var request = event.request;

  if (request.method !== 'GET') {
    return;
  }

  var requestUrl;

  try {
    requestUrl = new URL(request.url);
  } catch (e) {
    return;
  }

  if (requestUrl.origin !== location.origin) {
    return;
  }

  if (request.mode === 'navigate') {
    event.respondWith(
      caches.match('./index.html')
        .then(function (cached) {
          if (cached) {
            return cached;
          }

          return fetch(request)
            .then(function (response) {
              return response;
            })
            .catch(function () {
              return caches.match('./index.html');
            });
        })
    );
    return;
  }

  event.respondWith(
    caches.match(request)
      .then(function (cached) {
        if (cached) {
          return cached;
        }

        return fetch(request)
          .then(function (response) {
            if (response && response.status === 200 && response.type === 'basic') {
              var clone = response.clone();

              caches.open(CACHE_NAME).then(function (cache) {
                cache.put(request, clone);
              });
            }

            return response;
          })
          .catch(function () {
            return cached;
          });
      })
  );
});

