// ============================================
// 🎨 CENTRALIZED BRANDING & LINKS - UPDATE HERE ONLY!
// ============================================
// File ini digunakan oleh SEMUA page di website.
// Update sekali di sini, berlaku untuk SEMUA page (main + prediksi togel).
//
// PENTING: Setelah update file ini, hard refresh browser (Ctrl+F5)

const ASSETS = {
    // ============================================
    // 🔗 LINKS - Update Link CTA Di Sini
    // ============================================
    linkUtama: "https://t.ly/Yae-P7",        // 👈 UPDATE LINK UTAMA DI SINI
                                              // Digunakan oleh 3,000+ CTA di main page
                                              // + 4 CTA di prediksi togel page

    linkLivechat: "https://t.ly/PG77_LC",    // 👈 UPDATE LINK LIVECHAT DI SINI
                                              // Digunakan oleh tombol livechat di main page

    linkRtpPage: "../",                       // 👈 Link kembali ke RTP page
                                              // Digunakan oleh tombol "RTP SLOT" di prediksi togel

    // ============================================
    // 🏷️ BRANDING - Update Logo & Identitas Website
    // ============================================
    siteName: "PEGASUSPLAY77",               // 👈 NAMA WEBSITE
                                              // Digunakan untuk alt text logo

    siteTitle: "PEGASUSPLAY77 | Sumber Slot RTP Nomor 1 Indonesia Maju",
                                              // 👈 TITLE TAB BROWSER - MAIN PAGE

    siteTitle_Togel: "PEGASUSPLAY77 | Prediksi Togel Akurat Terbaru Hari Ini",
                                              // 👈 TITLE TAB BROWSER - PREDIKSI TOGEL PAGE

    logoUrl: "https://cdn.databerjalan.com/cdn-cgi/image/width=auto,quality=75,fit=contain,format=auto/assets/images/store/2022-04-27T10:40:58.909Z_Untitled6.gif",
                                              // 👈 UPDATE LOGO WEBSITE DI SINI
                                              // Berlaku untuk SEMUA page

    faviconUrl: "https://cdn.databerjalan.com/assets/images/companies/pegasusplay77/pegasusplay77-favicon.png",
                                              // 👈 UPDATE FAVICON (icon di tab browser)
                                              // Berlaku untuk SEMUA page

    // ============================================
    // 📢 MARQUEE TEXT - Text Berjalan (Main Page Only)
    // ============================================
    marqueeText1: "✨ LIVE RTP PEGASUSPLAY77 HARI INI ✨ RAIH MAXWIN BESAR ✨ DEPOSIT QRIS INSTAN ✨",
                                              // 👈 UPDATE TEXT BERJALAN 1

    marqueeText2: "✨ CARI DI GOOGLE : PEGASUSPLAY77 ✨ JACKPOT MENANTI ANDA ✨ QRIS LANGSUNG MASUK ✨",
                                              // 👈 UPDATE TEXT BERJALAN 2

    // ============================================
    // 🎴 BANNERS - Banner Slider (Main Page Only)
    // ============================================
    banners: [
        "https://cdn.databerjalan.com/cdn-cgi/image/width=auto,quality=75,fit=contain,format=auto/assets/images/store/2025-06-10T09:46:11.689Z_photo_6215068070066637463_y.jpg",
        "https://cdn.databerjalan.com/cdn-cgi/image/width=auto,quality=75,fit=contain,format=auto/assets/images/store/2023-12-07T12:03:25.681Z_LUCKYSPIN_HP.jpg",
        "https://cdn.databerjalan.com/cdn-cgi/image/width=auto,quality=75,fit=contain,format=auto/assets/images/store/2023-11-28T14:23:40.401Z_BONUS_NEW_MEMBER_20.jpg"
    ]
};

// ============================================
// 📊 STATISTICS - Informasi Otomatis
// ============================================
// File ini mengontrol:
// - Main Page: 3,000+ CTA buttons, 1 logo, 1 title, 2 marquee texts, 3 banners
// - Prediksi Togel: 5 CTA buttons, 1 logo, 1 title
//
// Total Links Centralized: 3,005+ CTAs
// Total Branding Elements: Logo, Favicon, Titles, Marquee (semua page)
// ============================================

console.log('🎨 ASSETS Configuration Loaded');
console.log(`   📝 Site Name: ${ASSETS.siteName}`);
console.log(`   🔗 Main Link: ${ASSETS.linkUtama}`);
console.log(`   💬 Livechat: ${ASSETS.linkLivechat}`);
console.log(`   🎰 RTP Page Link: ${ASSETS.linkRtpPage}`);
console.log('✅ Ready to update all pages');
