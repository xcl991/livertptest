# 🚀 QUICK START - Fully Centralized System

## ✅ SISTEM SEKARANG: 1 File untuk Semua!

```
SEBELUM (2 Files untuk Edit):
┌─────────────────────────────────────────┐
│  index.html                             │
│  ├─ ASSETS { ... }  👈 Edit di sini    │
│  └─ 3,000+ elements                     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  prediksi_togel/index.html              │
│  ├─ ASSETS { ... }  👈 Edit di sini    │
│  └─ 5+ elements                         │
└─────────────────────────────────────────┘

❌ Masalah: Update 2 tempat, inconsistent, ribet!
```

```
SEKARANG (1 File untuk Edit):
┌─────────────────────────────────────────┐
│  assets-config.js  👈 EDIT DI SINI SAJA!│
│  ├─ linkUtama                           │
│  ├─ linkLivechat                        │
│  ├─ logoUrl                             │
│  ├─ siteTitle                           │
│  ├─ marqueeText                         │
│  └─ ... semua config                    │
└─────────────────────────────────────────┘
         ↓ ↓ ↓ Auto Load ↓ ↓ ↓
    ┌─────────┴────────┐
    ↓                   ↓
┌───────────┐   ┌──────────────────┐
│ index.html│   │ prediksi_togel/  │
│           │   │   index.html     │
│ 3,000+    │   │   5+ elements    │
│ elements  │   │                  │
└───────────┘   └──────────────────┘

✅ Solusi: Update 1 file, semua page berubah!
```

---

## 🎯 CARA UPDATE (Super Simple!)

### **Step 1: Buka File `assets-config.js`**

**Lokasi:**
```
C:\Users\USER-\Downloads\LIVE RTP - NEW\LIVE RTP - NEW\PG\assets-config.js
```

### **Step 2: Edit Yang Diperlukan**

**Ganti Link CTA:**
```javascript
linkUtama: "https://LINK-BARU.com",  // 👈 Ganti di sini
```

**Ganti Logo:**
```javascript
logoUrl: "https://NEW-LOGO.com/logo.gif",  // 👈 Ganti di sini
```

**Ganti Marquee:**
```javascript
marqueeText1: "✨ TEXT BARU 1 ✨",  // 👈 Ganti di sini
marqueeText2: "✨ TEXT BARU 2 ✨",  // 👈 Ganti di sini
```

### **Step 3: Save**

Ctrl+S atau File → Save

### **Step 4: Refresh Browser**

Ctrl+Shift+R (hard refresh)

### **Step 5: Done!** ✅

Lihat perubahannya di SEMUA page!

---

## 📊 Yang Berubah Otomatis

| Yang Anda Edit | Main Page | Togel Page | Total |
|----------------|-----------|------------|-------|
| `linkUtama` | 3,011 buttons | 4 buttons | **3,015** |
| `linkLivechat` | 1 button | - | **1** |
| `logoUrl` | 1 logo | 1 logo | **2** |
| `siteTitle` / `siteTitle_Togel` | 1 title | 1 title | **2** |
| `marqueeText1` & `2` | 2 texts | - | **2** |
| `faviconUrl` | 1 favicon | 1 favicon | **2** |

**GRAND TOTAL: 3,024+ elements dari 1 file!**

---

## 💡 Contoh Real

### **Contoh 1: Ganti Semua Link**

**Buka `assets-config.js` line 13:**
```javascript
linkUtama: "https://t.ly/Yae-P7",  // 👈 GANTI INI
```

**Menjadi:**
```javascript
linkUtama: "https://newsite.com/register",
```

**Save → Refresh → Done!**

✅ **3,015 links berubah sekaligus!**

---

### **Contoh 2: Ganti Logo & Nama**

**Buka `assets-config.js` line 22-28:**
```javascript
siteName: "PEGASUSPLAY77",  // 👈 GANTI INI
logoUrl: "https://cdn.databerjalan.com/...",  // 👈 GANTI INI
```

**Menjadi:**
```javascript
siteName: "SULTANBET77",
logoUrl: "https://newcdn.com/sultanbet-logo.gif",
```

**Save → Refresh → Done!**

✅ **Logo & nama berubah di 2 pages!**

---

### **Contoh 3: Ganti Marquee**

**Buka `assets-config.js` line 35-39:**
```javascript
marqueeText1: "✨ LIVE RTP PEGASUSPLAY77 ...",  // 👈 GANTI INI
marqueeText2: "✨ CARI DI GOOGLE : ...",         // 👈 GANTI INI
```

**Menjadi:**
```javascript
marqueeText1: "✨ BONUS NEW MEMBER 200% ✨ DEPO 10RB ✨",
marqueeText2: "✨ SLOT GACOR HARI INI MAXWIN JACKPOT ✨",
```

**Save → Refresh → Done!**

✅ **Text berjalan berubah!**

---

## 🔍 Verification

**Setelah update, check console browser (F12):**

```
🎨 ASSETS Configuration Loaded
   📝 Site Name: PEGASUSPLAY77
   🔗 Main Link: https://t.ly/Yae-P7
   💬 Livechat: https://t.ly/PG77_LC
   🎰 RTP Page Link: ../
✅ Ready to update all pages
✅ All branding & CTA links updated from ASSETS configuration
```

Jika muncul message ini = **SUCCESS!** ✅

---

## ⚠️ PENTING - Yang TIDAK Boleh Dilakukan

### **❌ JANGAN Edit ASSETS di `index.html`**
File ini sudah tidak punya ASSETS object lagi.
Semua load dari `assets-config.js`.

### **❌ JANGAN Edit ASSETS di `prediksi_togel/index.html`**
File ini sudah tidak punya ASSETS object lagi.
Semua load dari `assets-config.js`.

### **❌ JANGAN Hapus Include Script**
```html
<script src="./assets-config.js"></script>  <!-- JANGAN HAPUS INI! -->
```

### **✅ HANYA Edit File `assets-config.js`**
Ini satu-satunya file yang perlu di-edit!

---

## 📂 File Structure

```
PG/
├── assets-config.js          👈 EDIT FILE INI!
│   └── const ASSETS = { ... }
│
├── index.html                 ✅ Otomatis load dari assets-config.js
│   └── <script src="./assets-config.js"></script>
│
└── prediksi_togel/
    └── index.html             ✅ Otomatis load dari assets-config.js
        └── <script src="../assets-config.js"></script>
```

---

## 🎉 Benefits

### **Sebelum:**
- 😫 Edit 2 files
- 😫 Find & replace manual
- 😫 Risk inconsistency
- 😫 10-15 minutes per update

### **Sekarang:**
- 😊 Edit 1 file only
- 😊 Auto-update semua page
- 😊 100% consistent
- 😊 30 seconds per update

---

## 📞 Need Help?

**Problem: Perubahan tidak muncul**
→ Hard refresh: Ctrl+Shift+R
→ Clear cache: Ctrl+Shift+Del

**Problem: Error di console**
→ Check file `assets-config.js` tersave
→ Check syntax JavaScript (no typo)

**Problem: Sebagian tidak berubah**
→ Hard refresh dengan cache clear
→ Check console log untuk errors

---

## 📖 Full Documentation

**Quick Start:** `QUICK_START.md` ← You are here!
**Complete Guide:** `README_CENTRALIZED.md`
**Technical Details:** `CENTRALIZED_BRANDING.md`

---

**Created:** 2025-12-17
**Version:** 3.0 - Fully Centralized
**Repository:** https://github.com/xcl991/livertptest
**Commit:** 16bc010

---

🎯 **REMEMBER: Edit `assets-config.js` ONLY!**
