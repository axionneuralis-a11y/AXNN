// sw.js - Service Worker untuk Push Notifications
// NoteMint File Manager v2.0 - SVG Version

const CACHE_NAME = 'notemint-v2';
const ASSETS = [
    '/',
    '/index.html',
    '/manifest.json',
    '/icon.svg',
    '/folder.svg',
    '/folder-open.svg',
    '/file.svg',
    '/file-plus.svg',
    '/home.svg',
    '/settings.svg',
    '/search.svg',
    '/plus.svg',
    '/trash.svg',
    '/edit.svg',
    '/move.svg',
    '/bell.svg',
    '/moon.svg',
    '/sun.svg',
    '/download.svg',
    '/upload.svg',
    '/more-vertical.svg',
    '/check.svg',
    '/x.svg'
];

// Install Service Worker
self.addEventListener('install', (event) => {
    event.waitUntil(
        Promise.all([
            self.skipWaiting(),
            caches.open(CACHE_NAME).then((cache) => {
                return cache.addAll(ASSETS);
            })
        ])
    );
});

// Activate Service Worker
self.addEventListener('activate', (event) => {
    event.waitUntil(
        Promise.all([
            self.clients.claim(),
            caches.keys().then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== CACHE_NAME) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
        ])
    );
});

// Fetch dengan cache-first strategy
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((cached) => {
            if (cached) {
                return cached;
            }
            return fetch(event.request).then((response) => {
                if (response && response.status === 200) {
                    const clone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, clone);
                    });
                }
                return response;
            });
        }).catch(() => {
            // Fallback offline dengan SVG icons
            return new Response(`
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Offline - NoteMint</title>
                    <style>
                        body {
                            font-family: 'Segoe UI', system-ui, sans-serif;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            min-height: 100vh;
                            margin: 0;
                            background: #f0f2f5;
                            color: #1a1a2e;
                            padding: 20px;
                            text-align: center;
                        }
                        .offline-box {
                            background: white;
                            padding: 40px;
                            border-radius: 16px;
                            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                            max-width: 400px;
                        }
                        .offline-box svg {
                            width: 64px;
                            height: 64px;
                            stroke: #6c5ce7;
                            fill: none;
                            margin-bottom: 16px;
                        }
                        .offline-box h1 {
                            color: #6c5ce7;
                            margin-bottom: 8px;
                        }
                        .offline-box p {
                            color: #4a4a6a;
                            margin-bottom: 20px;
                        }
                        .offline-box .btn {
                            display: inline-block;
                            padding: 10px 24px;
                            background: #6c5ce7;
                            color: white;
                            border: none;
                            border-radius: 10px;
                            text-decoration: none;
                            font-weight: 600;
                            cursor: pointer;
                        }
                        .offline-box .btn:hover { background: #5a4bd1; }
                    </style>
                </head>
                <body>
                    <div class="offline-box">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
                            <path d="M2 11h20"/>
                            <path d="M4 15h16"/>
                            <path d="M6 19h12"/>
                        </svg>
                        <h1>Offline</h1>
                        <p>Koneksi internet terputus. Silakan cek koneksi Anda.</p>
                        <button class="btn" onclick="location.reload()">🔄 Coba Lagi</button>
                    </div>
                </body>
                </html>
            `, {
                status: 503,
                statusText: 'Service Unavailable',
                headers: { 'Content-Type': 'text/html' }
            });
        })
    );
});

// Push Notification
self.addEventListener('push', (event) => {
    let data = {
        title: '📂 NoteMint',
        body: 'Ada notifikasi baru dari aplikasi NoteMint',
        icon: '/icon.svg',
        badge: '/icon.svg',
        url: '/',
        type: 'info',
        tag: Date.now().toString()
    };

    if (event.data) {
        try {
            const parsed = event.data.json();
            data = { ...data, ...parsed };
        } catch (e) {
            const text = event.data.text();
            if (text) {
                data.body = text;
            }
        }
    }

    const options = {
        body: data.body,
        icon: data.icon || '/icon.svg',
        badge: data.badge || '/icon.svg',
        vibrate: [200, 100, 200],
        data: {
            url: data.url || '/',
            type: data.type || 'info'
        },
        actions: [
            { 
                action: 'open', 
                title: '📂 Buka Aplikasi',
                icon: '/folder-open.svg'
            },
            { 
                action: 'close', 
                title: 'Tutup',
                icon: '/x.svg'
            }
        ],
        tag: data.tag,
        requireInteraction: true,
        silent: false,
        timestamp: Date.now()
    };

    event.waitUntil(
        self.registration.showNotification(data.title || '📂 NoteMint', options)
    );
});

// Notification Click Handler
self.addEventListener('notificationclick', (event) => {
    event.notification.close();

    const url = event.notification.data?.url || '/';
    const action = event.action;

    if (action === 'open' || !action) {
        event.waitUntil(
            clients.matchAll({
                type: 'window',
                includeUncontrolled: true
            }).then((clientList) => {
                for (const client of clientList) {
                    if (client.url === url && 'focus' in client) {
                        return client.focus();
                    }
                }
                if (clients.openWindow) {
                    return clients.openWindow(url);
                }
            })
        );
    }
});

// Handle message dari main thread
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SHOW_NOTIFICATION') {
        event.waitUntil(
            self.registration.showNotification(
                event.data.title || '📂 NoteMint',
                {
                    body: event.data.body || '',
                    icon: event.data.icon || '/icon.svg',
                    badge: '/icon.svg',
                    vibrate: [200, 100, 200],
                    data: { url: '/' },
                    requireInteraction: false,
                    actions: [
                        {
                            action: 'open',
                            title: '📂 Buka Aplikasi',
                            icon: '/folder-open.svg'
                        }
                    ]
                }
            )
        );
    }
});

// Background sync untuk operasi offline
self.addEventListener('sync', (event) => {
    if (event.tag === 'sync-notes') {
        event.waitUntil(syncNotes());
    }
});

async function syncNotes() {
    try {
        const pending = await getPendingData();
        if (pending && pending.length > 0) {
            const response = await fetch('/api/sync', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ data: pending })
            });
            if (response.ok) {
                await clearPendingData();
                self.registration.showNotification('✅ Sinkronisasi Berhasil', {
                    body: `${pending.length} item berhasil disinkronkan`,
                    icon: '/icon.svg',
                    badge: '/icon.svg'
                });
            }
        }
    } catch (e) {
        console.warn('Sync failed:', e);
    }
}

async function getPendingData() {
    // Implementasi untuk mendapatkan data pending dari IndexedDB
    return [];
}

async function clearPendingData() {
    // Implementasi untuk membersihkan data pending
    return;
}

// Periodic sync untuk update rutin
self.addEventListener('periodicsync', (event) => {
    if (event.tag === 'update-notes') {
        event.waitUntil(updateNotes());
    }
});

async function updateNotes() {
    try {
        const response = await fetch('/api/notes/latest');
        if (response.ok) {
            const data = await response.json();
            const clients = await self.clients.matchAll();
            clients.forEach(client => {
                client.postMessage({
                    type: 'UPDATE_NOTES',
                    data: data
                });
            });
        }
    } catch (e) {
        console.warn('Periodic update failed:', e);
    }
});

// Handle unhandled rejections
self.addEventListener('unhandledrejection', (event) => {
    console.warn('Unhandled rejection in SW:', event.reason);
});

// Handle error
self.addEventListener('error', (event) => {
    console.warn('Error in SW:', event.message);
});