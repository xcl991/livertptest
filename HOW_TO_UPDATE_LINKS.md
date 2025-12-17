# 🔗 Cara Update Semua CTA Links

## ⚡ Quick Start - Update Link di 1 Tempat Saja!

Untuk mengubah **SEMUA** link CTA button di website (header, mobile menu, floating buttons, game hover), cukup edit **1 BARIS** saja di file `index.html`.

---

## 📍 Lokasi Update

Buka file `index.html` dan cari section ini (sekitar line **3386-3400**):

```javascript
// ============================================
// 🔗 CENTRALIZED LINKS - UPDATE HERE ONLY!
// ============================================
// Semua CTA button akan menggunakan link dari sini.
// Cukup update sekali di bawah ini untuk mengubah semua link di website.

const ASSETS = {
    linkUtama: "https://t.ly/Yae-P7",        // 👈 UPDATE LINK UTAMA DI SINI
    linkLivechat: "https://t.ly/PG77_LC",    // 👈 UPDATE LINK LIVECHAT DI SINI
    banners: [...]
};
```

---

## 🎯 Link Yang Ter-Centralized

### 1. **LINK UTAMA** (`linkUtama`)
Digunakan oleh semua button berikut:

**Desktop Header:**
- ✅ Logo
- ✅ SERVER THAILAND
- ✅ SERVER SINGAPORE
- ✅ SERVER JEPANG
- ✅ LOGIN
- ✅ DAFTAR AKUN

**Mobile Menu:**
- ✅ SERVER THAILAND
- ✅ SERVER SINGAPORE
- ✅ SERVER JEPANG
- ✅ LOGIN
- ✅ DAFTAR AKUN

**Floating Buttons:**
- ✅ JOIN NOW (floating bottom right)
- ✅ HOT button (bottom nav)

**Game Cards:**
- ✅ Tombol "MAIN" saat hover di setiap game

**Total:** ~2,997+ games × 1 button + ~15 header/menu buttons = **3,000+ links!**

### 2. **LINK LIVECHAT** (`linkLivechat`)
Digunakan oleh:
- ✅ LIVECHAT button (bottom nav)

---

## 📝 Contoh Update

### Scenario 1: Ganti Link Utama
```javascript
// SEBELUM
linkUtama: "https://t.ly/Yae-P7",

// SESUDAH - ganti dengan link baru
linkUtama: "https://newlink.com/register",
```

✅ **Hasil:** Semua 3,000+ links otomatis berubah!

### Scenario 2: Ganti Link Livechat
```javascript
// SEBELUM
linkLivechat: "https://t.ly/PG77_LC",

// SESUDAH
linkLivechat: "https://wa.me/628123456789",
```

✅ **Hasil:** Link livechat berubah ke WhatsApp

---

## 🔧 Cara Kerja Sistem

### Automatic Link Update
File `index.html` memiliki function `updateAllLinks()` yang berjalan saat page load:

```javascript
const updateAllLinks = () => {
    // Update all main CTA links
    document.querySelectorAll('a[href="https://t.ly/Yae-P7"]').forEach(link => {
        link.href = ASSETS.linkUtama;
    });

    // Update livechat link
    document.querySelectorAll('a[href="https://t.ly/PG77_LC"]').forEach(link => {
        link.href = ASSETS.linkLivechat;
    });
};
```

Function ini:
1. ✅ Mencari semua `<a>` tags dengan href lama
2. ✅ Replace dengan link dari `ASSETS` object
3. ✅ Berjalan otomatis saat page load
4. ✅ Console log konfirmasi: `✅ All CTA links updated`

---

## 🎨 Links Yang Di-Update Otomatis

### Header (Desktop)
```html
<a href="UPDATE_OTOMATIS">Logo</a>
<a href="UPDATE_OTOMATIS">SERVER THAILAND</a>
<a href="UPDATE_OTOMATIS">SERVER SINGAPORE</a>
<a href="UPDATE_OTOMATIS">SERVER JEPANG</a>
<a href="UPDATE_OTOMATIS">LOGIN</a>
<a href="UPDATE_OTOMATIS">DAFTAR AKUN</a>
```

### Mobile Menu
```html
<a href="UPDATE_OTOMATIS">SERVER THAILAND</a>
<a href="UPDATE_OTOMATIS">SERVER SINGAPORE</a>
<a href="UPDATE_OTOMATIS">SERVER JEPANG</a>
<a href="UPDATE_OTOMATIS">LOGIN</a>
<a href="UPDATE_OTOMATIS">DAFTAR AKUN</a>
```

### Game Cards (Dynamic)
```javascript
<a href="${ASSETS.linkUtama}">MAIN</a>  // ✅ Sudah pakai variable
```

### Floating Buttons
```html
<a href="UPDATE_OTOMATIS">JOIN NOW</a>
<a href="UPDATE_OTOMATIS">HOT</a>
<a href="UPDATE_OTOMATIS_LIVECHAT">LIVECHAT</a>
```

---

## ✅ Testing

Setelah update link, test dengan cara:

1. **Save file `index.html`**
2. **Refresh browser** (Ctrl+F5 / Cmd+Shift+R)
3. **Check console log** - harus muncul: `✅ All CTA links updated`
4. **Test click beberapa button:**
   - Logo di header
   - SERVER THAILAND
   - Tombol "MAIN" di game card
   - JOIN NOW floating button
   - LIVECHAT button

---

## 🚀 Workflow Update Link

```bash
1. Edit index.html
   │
   ├─→ Cari: "CENTRALIZED LINKS - UPDATE HERE ONLY!"
   │
   ├─→ Ubah: linkUtama atau linkLivechat
   │
   └─→ Save file

2. Test di browser
   │
   ├─→ Refresh page
   │
   ├─→ Check console: "✅ All CTA links updated"
   │
   └─→ Click test beberapa button

3. Done! ✅
```

---

## 💡 Tips

### Multiple Environments
Jika ada link berbeda untuk staging/production:

```javascript
const ASSETS = {
    // Production
    linkUtama: "https://production-link.com/register",

    // Staging (comment out production, uncomment staging)
    // linkUtama: "https://staging-link.com/register",

    linkLivechat: "https://t.ly/PG77_LC",
};
```

### Tracking Links
Gunakan UTM parameters untuk tracking:

```javascript
const ASSETS = {
    linkUtama: "https://t.ly/Yae-P7?utm_source=website&utm_medium=cta",
    linkLivechat: "https://t.ly/PG77_LC?utm_source=website&utm_medium=livechat",
};
```

---

## 🎉 Keuntungan Sistem Ini

✅ **Centralized** - Update 1 tempat, semua berubah
✅ **Fast** - Tidak perlu find & replace manual
✅ **Safe** - Tidak ada link yang terlewat
✅ **Maintainable** - Mudah di-maintain
✅ **Scalable** - Tambah link baru tinggal tambah di ASSETS
✅ **Clear** - Comment yang jelas untuk developer

---

## 📞 Support

Jika ada pertanyaan atau masalah:
1. Check console browser untuk error log
2. Pastikan syntax JavaScript benar (no typo)
3. Test di browser yang berbeda

---

**Happy Updating! 🚀**
