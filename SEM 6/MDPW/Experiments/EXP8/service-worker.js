const CACHE_NAME = "ecommerce-pwa-v1";
const ASSETS_TO_CACHE = [
    "/",
    "/index.html",
    "/styles.css",
    "/app.js",
    "/manifest.json",
    "/icons/icon-192.png",
    "/icons/icon-512.png",
];

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches
            .open(CACHE_NAME)
            .then((cache) => {
                console.log("Caching assets");
                return cache.addAll(ASSETS_TO_CACHE);
            })
            .then(() => self.skipWaiting()),
    );
});

self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches
            .keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== CACHE_NAME) {
                            console.log("Deleting old cache:", cacheName);
                            return caches.delete(cacheName);
                        }
                    }),
                );
            })
            .then(() => self.clients.claim()),
    );
});

self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                return cachedResponse;
            }
            return fetch(event.request)
                .then((response) => {
                    if (!event.request.url.startsWith(self.location.origin)) {
                        return response;
                    }
                    if (event.request.method !== "GET") {
                        return response;
                    }

                    return caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, response.clone());
                        return response;
                    });
                })
                .catch(() => {
                    if (
                        event.request.headers
                            .get("accept")
                            .includes("text/html")
                    ) {
                        return caches.match("/index.html");
                    }
                    return new Response("Offline - content not available");
                });
        }),
    );
});
