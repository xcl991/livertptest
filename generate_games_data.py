#!/usr/bin/env python3
"""
Script untuk menghasilkan data provider dan game dari CSV files
"""
import csv
import os
import json

CSV_DIR = r"F:\NukeRTPScrapingCDN\output_csv"

def read_providers_info():
    """Membaca informasi provider dari _providers_info.csv"""
    providers_file = os.path.join(CSV_DIR, "_providers_info.csv")
    providers = []

    with open(providers_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            provider_name = row['Provider Name'].strip()
            provider_logo = row['Provider Logo CDN'].strip()
            total_games = row['Total Games'].strip()

            # Map provider filename to key
            provider_key = provider_name.replace('-', '')

            providers.append({
                'key': provider_key,
                'name': provider_name,
                'logo': provider_logo,
                'total_games': total_games,
                'csv_file': f"{provider_name}.csv"
            })

    return providers

def read_games_from_csv(csv_filename):
    """Membaca game dari file CSV"""
    csv_path = os.path.join(CSV_DIR, csv_filename)
    games = []

    if not os.path.exists(csv_path):
        print(f"Warning: {csv_filename} tidak ditemukan")
        return games

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            game_name = row['Game Name'].strip()
            image_cdn = row['Image CDN'].strip()

            games.append({
                'name': game_name,
                'image': image_cdn
            })

    return games

def generate_provider_array():
    """Generate array PROVIDERS untuk JavaScript"""
    providers = read_providers_info()

    js_code = "const PROVIDERS = [\n"
    for provider in providers:
        # Buat display name yang lebih bagus
        display_name = provider['name'].upper().replace('-SLOT', '').replace('-SLOTS', '')

        js_code += f"    {{ key: '{provider['key']}', name: '{display_name}', logo: '{provider['logo']}' }},\n"

    js_code += "];\n"

    return js_code, providers

def generate_raw_html_for_provider(provider_key, games):
    """Generate RAW_HTML variable untuk satu provider"""
    html = f"const RAW_HTML_{provider_key.upper()} = `\n"

    for idx, game in enumerate(games, 1):
        html += f'    <div class="grid-item"><img alt="{game["name"]}" src="{game["image"]}" /></div>\n'

    html += "`;\n"

    return html

def generate_allgames_assignment(providers):
    """Generate allGames assignment"""
    js_code = "\n// Load all games data\n"
    for provider in providers:
        js_code += f"allGames['{provider['key']}'] = parseHTMLToGames(RAW_HTML_{provider['key'].upper()}, '{provider['key']}');\n"

    return js_code

def main():
    print("🚀 Memulai proses generate data...")

    # Generate provider array
    print("\n📋 Membaca provider info...")
    provider_array, providers = generate_provider_array()

    # Generate RAW_HTML untuk setiap provider
    print("\n🎮 Membaca games data...")
    all_raw_html = ""

    for provider in providers:
        print(f"   - Processing {provider['name']}...")
        games = read_games_from_csv(provider['csv_file'])

        if games:
            raw_html = generate_raw_html_for_provider(provider['key'], games)
            all_raw_html += "\n" + raw_html
            print(f"     ✅ {len(games)} games loaded")
        else:
            print(f"     ⚠️  No games found")

    # Generate allGames assignment
    allgames_code = generate_allgames_assignment(providers)

    # Combine semua code
    output = f"""
// ============================================
// GENERATED CODE - Provider dan Games Data
// ============================================

{provider_array}

// ============================================
// RAW HTML DATA untuk setiap provider
// ============================================
{all_raw_html}

// ============================================
// Load semua games ke allGames object
// ============================================
{allgames_code}
"""

    # Simpan ke file
    output_file = "generated_games_data.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n✅ Code berhasil di-generate ke: {output_file}")
    print(f"📊 Total providers: {len(providers)}")
    print("\n🎉 Selesai!")

    # Juga simpan summary
    summary = {
        'total_providers': len(providers),
        'providers': [
            {
                'key': p['key'],
                'name': p['name'],
                'total_games': p['total_games']
            } for p in providers
        ]
    }

    with open('providers_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"📄 Summary saved to: providers_summary.json")

if __name__ == "__main__":
    main()
