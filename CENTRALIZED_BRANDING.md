# 🎨 Centralized Branding & Links System

## ✅ Update Completed!

All branding elements (logo, title, marquee, links) are now **centralized** and can be updated from **ONE LOCATION** only!

---

## 📍 Where to Update Everything

### **Main Website** (`index.html`)

Find this section around **line 3386-3413**:

```javascript
// ============================================
// 🎨 CENTRALIZED BRANDING & LINKS - UPDATE HERE ONLY!
// ============================================

const ASSETS = {
    // 🔗 Links
    linkUtama: "https://t.ly/Yae-P7",        // 👈 UPDATE LINK UTAMA DI SINI (3,000+ CTAs)
    linkLivechat: "https://t.ly/PG77_LC",    // 👈 UPDATE LINK LIVECHAT DI SINI

    // 🏷️ Branding
    siteName: "PEGASUSPLAY77",               // 👈 UPDATE NAMA WEBSITE DI SINI
    siteTitle: "PEGASUSPLAY77 | Sumber Slot RTP Nomor 1 Indonesia Maju",  // 👈 UPDATE TITLE TAB BROWSER
    logoUrl: "https://cdn.databerjalan.com/...",  // 👈 UPDATE LOGO DI SINI
    faviconUrl: "https://cdn.databerjalan.com/...",  // 👈 UPDATE FAVICON DI SINI

    // 📢 Marquee Text (Text Berjalan)
    marqueeText1: "✨ LIVE RTP PEGASUSPLAY77 HARI INI ✨ RAIH MAXWIN BESAR ✨",
    marqueeText2: "✨ CARI DI GOOGLE : PEGASUSPLAY77 ✨ JACKPOT MENANTI ANDA ✨",

    // 🎴 Banners
    banners: [...]
};
```

### **Prediksi Togel Page** (`prediksi_togel/index.html`)

Find this section around **line 97-107**:

```javascript
// ============================================
// 🎨 CENTRALIZED BRANDING & LINKS - UPDATE HERE ONLY!
// ============================================

const ASSETS = {
    // 🔗 Links
    linkUtama: "https://t.ly/Yae-P7",        // 👈 UPDATE LINK UTAMA DI SINI (4 CTAs)
    linkRtpPage: "../",                       // 👈 UPDATE LINK RTP PAGE DI SINI (1 CTA)

    // 🏷️ Branding
    siteName: "PEGASUSPLAY77",               // 👈 UPDATE NAMA WEBSITE DI SINI
    siteTitle: "PEGASUSPLAY77 | Prediksi Togel Akurat Terbaru Hari Ini",
    logoUrl: "https://cdn.databerjalan.com/...",
    faviconUrl: "https://cdn.databerjalan.com/..."
};
```

---

## 🎯 What Gets Updated Automatically

### **Main Website**

When you edit the ASSETS object, these elements update automatically:

| Element | Property | Count |
|---------|----------|-------|
| Browser Tab Title | `siteTitle` | 1 |
| Favicon | `faviconUrl` | 1 |
| Main Logo | `logoUrl` | 1 |
| Marquee Text | `marqueeText1`, `marqueeText2` | 2 texts |
| Header CTA Links | `linkUtama` | 7 buttons |
| Mobile Menu CTAs | `linkUtama` | 5 buttons |
| Game Cards "MAIN" | `linkUtama` | ~2,997 buttons |
| Floating Buttons | `linkUtama` | 2 buttons |
| Livechat Button | `linkLivechat` | 1 button |

**Total Links Updated:** 3,000+ CTAs from 1 line!

### **Prediksi Togel Page**

When you edit the ASSETS object:

| Element | Property | Count |
|---------|----------|-------|
| Browser Tab Title | `siteTitle` | 1 |
| Favicon | `faviconUrl` | 1 |
| Main Logo | `logoUrl` | 1 |
| Top "PASANG SEKARANG" | `linkUtama` | 1 button |
| Cards "PASANG SEKARANG" | `linkUtama` | 3 buttons (HK, SG, SYD) |
| "RTP SLOT" Button | `linkRtpPage` | 1 button |

**Total Links Updated:** 5 CTAs from 2 lines!

---

## 🔴 Red Theme Applied

Both pages now use **consistent red theme**:

### Color Transformation

| Element | Before (Purple) | After (Red) |
|---------|----------------|-------------|
| **Background Dark** | `#0f0520` | `#200f0f` |
| **Background Mid** | `#1a0a33` | `#331a1a` |
| **Card Background** | `#2c144b`, `#3e2060` | `#4b1414`, `#602020` |
| **Border** | `#6b21a8`, `purple-500` | `#dc2626`, `red-500` |
| **Text** | `text-purple-300` | `text-red-300` |

---

## 📝 Example: How to Update

### Scenario 1: Ganti Logo Website

**Edit `index.html` line ~3400:**
```javascript
logoUrl: "https://your-new-logo.com/logo.gif",
```

**Edit `prediksi_togel/index.html` line ~105:**
```javascript
logoUrl: "https://your-new-logo.com/logo.gif",
```

✅ **Result:** Logo berubah di seluruh website!

### Scenario 2: Ganti Semua Link CTA

**Edit `index.html` line ~3394:**
```javascript
linkUtama: "https://new-link.com/register",
```

**Edit `prediksi_togel/index.html` line ~99:**
```javascript
linkUtama: "https://new-link.com/register",
```

✅ **Result:** 3,000+ links otomatis berubah!

### Scenario 3: Ganti Marquee Text

**Edit `index.html` line ~3404-3405:**
```javascript
marqueeText1: "✨ NEW PROMO BONANZA 100% ✨",
marqueeText2: "✨ JACKPOT HINGGA MILYARAN ✨",
```

✅ **Result:** Text berjalan berubah otomatis!

### Scenario 4: Ganti Browser Tab Title

**Edit `index.html` line ~3399:**
```javascript
siteTitle: "NEWSITE | Slot Gacor No 1 Indonesia",
```

**Edit `prediksi_togel/index.html` line ~104:**
```javascript
siteTitle: "NEWSITE | Prediksi Togel Akurat",
```

✅ **Result:** Title di tab browser berubah!

---

## 🔧 How It Works

### Auto-Update Function

Both pages have an `updateAllBranding()` function that runs on page load:

```javascript
const updateAllBranding = () => {
    // Update browser tab title
    document.title = ASSETS.siteTitle;

    // Update favicon
    const favicon = document.querySelector('link[rel="icon"]');
    if (favicon) favicon.href = ASSETS.faviconUrl;

    // Update logo
    const logo = document.querySelector('header img[alt]');
    if (logo) {
        logo.src = ASSETS.logoUrl;
        logo.alt = ASSETS.siteName;
    }

    // Update marquee text (main page only)
    const marqueeContainer = document.querySelector('.animate-marquee');
    if (marqueeContainer) {
        marqueeContainer.innerHTML = `
            <span>${ASSETS.marqueeText1}</span>
            <span>${ASSETS.marqueeText2}</span>
        `;
    }

    // Update all CTA links
    document.querySelectorAll('a[href="https://t.ly/Yae-P7"]').forEach(link => {
        link.href = ASSETS.linkUtama;
    });

    // ... and more
};
```

This function:
1. ✅ Runs automatically saat page load
2. ✅ Reads dari ASSETS object
3. ✅ Update semua elemen yang sesuai
4. ✅ Console log konfirmasi

---

## 🎉 Benefits

### Centralized Management
✅ **Update 1 baris → 3,000+ links berubah**
✅ **Logo di 1 tempat → berlaku semua page**
✅ **Single source of truth**

### Easy Maintenance
✅ **Tidak perlu find & replace manual**
✅ **Tidak ada link yang terlewat**
✅ **Clear documentation dengan comment**

### Scalable
✅ **Mudah tambah link baru**
✅ **Mudah tambah branding element**
✅ **Future-proof architecture**

### Safe
✅ **Backup file tersedia** (`index.html.backup`)
✅ **Git version control**
✅ **Console log untuk verification**

---

## 📊 Summary Statistics

### Main Website
- **Total lines:** 3,751
- **ASSETS location:** Line 3392-3413
- **Links centralized:** 3,000+
- **Branding elements:** 7 (title, favicon, logo, marquee x2, banners x3)

### Prediksi Togel
- **Total lines:** 344
- **ASSETS location:** Line 97-107
- **Links centralized:** 5
- **Branding elements:** 4 (title, favicon, logo, siteName)

---

## 🚀 Quick Start Workflow

```bash
1. Edit ASSETS object
   │
   ├─→ Main: index.html line ~3392
   ├─→ Togel: prediksi_togel/index.html line ~97
   │
2. Save files
   │
3. Refresh browser (Ctrl+F5)
   │
4. Check console log
   │
   └─→ Should show: "✅ All branding & CTA links updated"

5. Test beberapa links/elements
   │
6. Done! ✅
```

---

## 💡 Console Verification

When page loads, you'll see:

**Main Website:**
```
✅ All branding & CTA links updated from ASSETS configuration
   📝 Site: PEGASUSPLAY77
   🔗 Main Link: https://t.ly/Yae-P7
   💬 Livechat: https://t.ly/PG77_LC
```

**Prediksi Togel:**
```
✅ All branding & CTA links updated from ASSETS configuration
   📝 Site: PEGASUSPLAY77
   🔗 Main Link: https://t.ly/Yae-P7
   🎰 RTP Page: ../
```

---

## 📞 Support

Jika ada pertanyaan atau masalah:
1. Check console browser (F12) untuk error log
2. Pastikan syntax JavaScript benar (no typo)
3. Hard refresh browser (Ctrl+Shift+R)
4. Clear cache jika perlu

---

## 📂 Related Files

- `index.html` - Main website
- `prediksi_togel/index.html` - Prediksi togel page
- `HOW_TO_UPDATE_LINKS.md` - Link management guide
- `RED_THEME_CHANGES.md` - Theme transformation log
- `UPDATE_SUMMARY.md` - Initial data update summary

---

**🎉 Centralized branding system successfully implemented!**

**Repository:** https://github.com/xcl991/livertptest
**Latest Commit:** 79d3c3d - Centralize branding & red theme

---

Generated: 2025-12-17
Version: 2.0
