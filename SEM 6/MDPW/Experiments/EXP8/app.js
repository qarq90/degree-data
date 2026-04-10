const products = [
    {
        id: 1,
        name: "Resident Evil 7",
        price: 1499,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202206/0207/V6IViuKogBMRtajqjnYrcj0e.png",
        category: "horror",
    },
    {
        id: 2,
        name: "Resident Evil 8",
        price: 1999,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202101/0812/FkzwjnJknkrFlozkTdeQBMub.png",
        category: "horror",
    },
    {
        id: 3,
        name: "Resident Evil 9",
        price: 2499,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202512/1205/79661d7a2bdb9784749b4e57e1456ca89f7ac7bed8615aee.png",
        category: "horror",
    },

    {
        id: 7,
        name: "GTA V",
        price: 1499,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202202/2816/K6mmm89oNII1iI1aqaClO0wh.png",
        category: "action",
    },
    {
        id: 8,
        name: "Red Dead Redemption 2",
        price: 1999,
        poster: "https://image.api.playstation.com/gs2-sec/appkgo/prod/CUSA08519_00/12/i_3da1cf7c41dc7652f9b639e1680d96436773658668c7dc3930c441291095713b/i/icon0.png",
        category: "action",
    },
    {
        id: 9,
        name: "DOOM 2016",
        price: 999,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202009/2814/GGyEnCkIXoyiVlN9sRHkzUPo.png",
        category: "shooter",
    },
    {
        id: 16,
        name: "DOOM Eternal",
        price: 1999,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202010/0114/ERNPc4gFqeRDG1tYQIfOKQtM.png",
        category: "shooter",
    },
    {
        id: 10,
        name: "Ghost of Tsushima",
        price: 2499,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202010/0222/niMUubpU9y1PxNvYmDfb8QFD.png",
        category: "action",
    },
    {
        id: 11,
        name: "Ghost of Yotei",
        price: 2999,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202504/2116/050bb77f895515e0b0e906b0b9d75b6174b37eece097b462.png",
        category: "action",
    },
    {
        id: 12,
        name: "Horizon Zero Dawn",
        price: 1499,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202010/0221/vC7trMorHJgbImp8PCQvpI0p.png",
        category: "rpg",
    },
    {
        id: 13,
        name: "Horizon Forbidden West",
        price: 2499,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202010/2915/kifM3lnke5lExwRd96mIDojQ.png",
        category: "rpg",
    },
    {
        id: 14,
        name: "Outlast Trials",
        price: 1199,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202603/1014/686d2f759e42d2a5b85140203dcf3e439b37ff6244b9ce23.png",
        category: "horror",
    },
    {
        id: 15,
        name: "Outlast 2",
        price: 1099,
        poster: "https://image.api.playstation.com/gs2-sec/appkgo/prod/CUSA06633_00/3/i_d608871643e7c4aa9b73ee8114ae527eff3548be4ac24e0053e3ceed1b903ff0/i/icon0.png",
        category: "horror",
    },
    {
        id: 4,
        name: "Black Ops 3",
        price: 999,
        poster: "https://image.api.playstation.com/gs2-sec/appkgo/prod/CUSA02624_00/6/i_c215706b64aaf3a61d26f8496a19ff5e4151fa30f504c8510ff66c7561965ec3/i/icon0.png",
        category: "shooter",
    },
    {
        id: 5,
        name: "Modern Warfare 2019",
        price: 1299,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202212/1917/OS18LBxAVpQ1iPeGWAqSnxem.png",
        category: "shooter",
    },
    {
        id: 6,
        name: "Modern Warfare 2022",
        price: 1799,
        poster: "https://image.api.playstation.com/vulcan/ap/rnd/202205/2800/W5uSEsW7yefCNTHatS03v5q7.png",
        category: "shooter",
    },
];

let cart = [];
let deferredPrompt = null;

function loadCart() {
    const savedCart = localStorage.getItem("ecommerce_cart");
    if (savedCart) {
        cart = JSON.parse(savedCart);
        updateCartUI();
    }
}

function saveCart() {
    localStorage.setItem("ecommerce_cart", JSON.stringify(cart));
    updateCartUI();
}

function updateCartUI() {
    const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    document.getElementById("cart-count").innerText = cartCount;

    const cartTotal = cart.reduce(
        (sum, item) => sum + item.price * item.quantity,
        0,
    );
    document.getElementById("cart-total").innerText = cartTotal;

    renderCartItems();
}

function renderCartItems() {
    const cartItemsDiv = document.getElementById("cart-items");
    if (!cartItemsDiv) return;

    if (cart.length === 0) {
        cartItemsDiv.innerHTML = "<p>Your cart is empty</p>";
        return;
    }

    cartItemsDiv.innerHTML = cart
        .map(
            (item) => `
        <div class="cart-item">
            <span>${item.name} x${item.quantity}</span>
            <div>
                <span>₹${item.price * item.quantity}</span>
                <button class="remove-item" data-id="${item.id}" style="margin-left: 15px; background: #dc2626; color: white; border: none; border-radius: 4px; padding: 4px 10px; cursor: pointer;">Remove</button>
            </div>
        </div>
    `,
        )
        .join("");

    document.querySelectorAll(".remove-item").forEach((btn) => {
        btn.addEventListener("click", (e) => {
            const id = parseInt(btn.dataset.id);
            removeFromCart(id);
        });
    });
}

function removeFromCart(productId) {
    const existing = cart.find((item) => item.id === productId);
    if (existing) {
        if (existing.quantity > 1) {
            existing.quantity--;
        } else {
            cart = cart.filter((item) => item.id !== productId);
        }
    }
    saveCart();
    showToast(`🗑️ Item removed from cart!`);
}

function addToCart(product) {
    const existing = cart.find((item) => item.id === product.id);
    if (existing) {
        existing.quantity++;
    } else {
        cart.push({ ...product, quantity: 1 });
    }
    saveCart();
    showToast(`🎮 Added ${product.name} to cart!`);
}

function showToast(message) {
    const toast = document.createElement("div");
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        bottom: 80px;
        left: 50%;
        transform: translateX(-50%);
        background: #333;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        z-index: 1002;
        animation: fadeOut 2s ease;
    `;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}

function handleImageError(img) {
    img.onerror = null;
    img.src = "https://placehold.co/300x400/1a1a2e/white?text=No+Image";
}

function renderProducts() {
    const grid = document.getElementById("products-grid");
    if (!grid) return;

    grid.innerHTML = products
        .map(
            (product) => `
        <div class="product-card">
            <div class="product-image">
                <img src="${product.poster}" 
                     alt="${product.name}" 
                     loading="lazy"
                     onerror="this.onerror=null; this.src='https://placehold.co/300x400/1a1a2e/white?text=${encodeURIComponent(product.name)}'"
                >
            </div>
            <div class="product-info">
                <div class="product-title">${product.name}</div>
                <div class="product-price">₹${product.price}</div>
                <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
            </div>
        </div>
    `,
        )
        .join("");

    document.querySelectorAll(".add-to-cart").forEach((btn) => {
        btn.addEventListener("click", (e) => {
            const id = parseInt(btn.dataset.id);
            const product = products.find((p) => p.id === id);
            if (product) addToCart(product);
        });
    });
}

function initCartModal() {
    const modal = document.getElementById("cart-modal");
    const cartIcon = document.querySelector(".cart-icon");
    const closeBtn = document.querySelector(".close");
    const checkoutBtn = document.getElementById("checkout-btn");

    cartIcon?.addEventListener("click", () => {
        modal.style.display = "flex";
    });

    closeBtn?.addEventListener("click", () => {
        modal.style.display = "none";
    });

    checkoutBtn?.addEventListener("click", () => {
        if (cart.length === 0) {
            showToast("Cart is empty!");
        } else {
            const totalItems = cart.reduce(
                (sum, item) => sum + item.quantity,
                0,
            );
            alert(
                `🎉 Order placed successfully!\n📦 Total Items: ${totalItems}\n💰 Total Amount: ₹${document.getElementById("cart-total").innerText}\n\nThank you for shopping at GameStore!`,
            );
            cart = [];
            saveCart();
            modal.style.display = "none";
        }
    });

    window.addEventListener("click", (e) => {
        if (e.target === modal) modal.style.display = "none";
    });
}

window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferredPrompt = e;
    const installPrompt = document.getElementById("install-prompt");
    if (installPrompt) installPrompt.style.display = "flex";

    document
        .getElementById("install-btn")
        ?.addEventListener("click", async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const { outcome } = await deferredPrompt.userChoice;
                if (outcome === "accepted") {
                    console.log("User accepted install");
                }
                deferredPrompt = null;
                installPrompt.style.display = "none";
            }
        });

    document.getElementById("close-install")?.addEventListener("click", () => {
        installPrompt.style.display = "none";
    });
});

function initOfflineDetection() {
    function updateOfflineStatus() {
        if (!navigator.onLine) {
            let indicator = document.getElementById("offline-indicator");
            if (!indicator) {
                indicator = document.createElement("div");
                indicator.id = "offline-indicator";
                indicator.className = "offline-indicator";
                indicator.innerHTML =
                    "⚠️ You are offline. Games will be available from cache.";
                document.body.insertBefore(indicator, document.body.firstChild);
            }
        } else {
            const indicator = document.getElementById("offline-indicator");
            if (indicator) indicator.remove();
        }
    }

    window.addEventListener("online", updateOfflineStatus);
    window.addEventListener("offline", updateOfflineStatus);
    updateOfflineStatus();
}

if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
        navigator.serviceWorker
            .register("/service-worker.js")
            .then((reg) => console.log("Service Worker registered:", reg))
            .catch((err) =>
                console.log("Service Worker registration failed:", err),
            );
    });
}

function updatePageTitle() {
    const headerTitle = document.querySelector("header h1");
    if (headerTitle) {
        headerTitle.innerHTML = "DAWG";
    }
}

const applyTheme = (darkMode) => {
    if (darkMode) {
        document.documentElement.style.setProperty("--background", "#0a0a0a");
        document.documentElement.style.setProperty("--foreground", "#e0e0e0");
        document.documentElement.style.setProperty("--card-bg", "#111111");
        document.documentElement.style.setProperty("--card-border", "#2a2a2a");
        document.documentElement.style.setProperty(
            "--header-bg",
            "linear-gradient(135deg, #1a1a1a, #000000)",
        );
        document.documentElement.style.setProperty("--header-border", "#333");
        document.documentElement.style.setProperty("--button-bg", "#1a1a1a");
        document.documentElement.style.setProperty("--button-border", "#333");
        document.documentElement.style.setProperty("--button-hover", "#2a2a2a");
        document.documentElement.style.setProperty(
            "--cart-icon-bg",
            "rgba(255, 255, 255, 0.1)",
        );
        document.documentElement.style.setProperty("--modal-bg", "#111111");
        document.documentElement.style.setProperty("--modal-border", "#333");
        document.documentElement.style.setProperty("--border-light", "#2a2a2a");
        document.documentElement.style.setProperty("--text-muted", "#888");
        document.documentElement.style.setProperty("--offline-bg", "#1a1a1a");
        document.documentElement.style.setProperty("--offline-text", "#cccccc");
        document.documentElement.style.setProperty(
            "--scrollbar-track",
            "#0a0a0a",
        );
        document.documentElement.style.setProperty("--scrollbar-thumb", "#333");
        document.documentElement.style.setProperty(
            "--scrollbar-thumb-hover",
            "#444",
        );
    } else {
        document.documentElement.style.setProperty("--background", "#f5f5f7");
        document.documentElement.style.setProperty("--foreground", "#1d1d1f");
        document.documentElement.style.setProperty("--card-bg", "#ffffff");
        document.documentElement.style.setProperty("--card-border", "#e5e5e7");
        document.documentElement.style.setProperty(
            "--header-bg",
            "linear-gradient(135deg, #ffffff, #f5f5f7)",
        );
        document.documentElement.style.setProperty(
            "--header-border",
            "#d2d2d6",
        );
        document.documentElement.style.setProperty("--button-bg", "#ffffff");
        document.documentElement.style.setProperty(
            "--button-border",
            "#d2d2d6",
        );
        document.documentElement.style.setProperty("--button-hover", "#f5f5f7");
        document.documentElement.style.setProperty(
            "--cart-icon-bg",
            "rgba(0, 0, 0, 0.05)",
        );
        document.documentElement.style.setProperty("--modal-bg", "#ffffff");
        document.documentElement.style.setProperty("--modal-border", "#e5e5e7");
        document.documentElement.style.setProperty("--border-light", "#e5e5e7");
        document.documentElement.style.setProperty("--text-muted", "#8e8e93");
        document.documentElement.style.setProperty("--offline-bg", "#fee2e2");
        document.documentElement.style.setProperty("--offline-text", "#991b1b");
        document.documentElement.style.setProperty(
            "--scrollbar-track",
            "#f5f5f7",
        );
        document.documentElement.style.setProperty(
            "--scrollbar-thumb",
            "#c6c6c8",
        );
        document.documentElement.style.setProperty(
            "--scrollbar-thumb-hover",
            "#8e8e93",
        );
    }
};

function initThemeSwitcher() {
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = document.getElementById("theme-icon");

    const savedTheme = localStorage.getItem("theme");
    const isDarkMode = savedTheme !== "light";

    applyTheme(isDarkMode);

    if (themeIcon) {
        themeIcon.textContent = isDarkMode ? "🌙" : "☀️";
    }

    themeToggle?.addEventListener("click", () => {
        const isCurrentlyDark =
            document.documentElement.style.getPropertyValue("--background") ===
                "#0a0a0a" || localStorage.getItem("theme") !== "light";
        const newDarkMode = !isCurrentlyDark;

        applyTheme(newDarkMode);
        localStorage.setItem("theme", newDarkMode ? "dark" : "light");

        if (themeIcon) {
            themeIcon.textContent = newDarkMode ? "🌙" : "☀️";
        }
    });
}

function init() {
    updatePageTitle();
    initThemeSwitcher();
    loadCart();
    renderProducts();
    initCartModal();
    initOfflineDetection();
}

init();
