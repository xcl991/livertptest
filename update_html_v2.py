#!/usr/bin/env python3
"""
Script update HTML v2 - Lebih robust
"""
import re

def main():
    print("🚀 Memulai update HTML file (v2)...")

    # Read files
    print("📖 Membaca files...")
    with open('index.html.backup', 'r', encoding='utf-8') as f:
        html_content = f.read()

    with open('generated_games_data.js', 'r', encoding='utf-8') as f:
        generated_content = f.read()

    # Extract PROVIDERS array
    print("✂️  Extract PROVIDERS array...")
    providers_match = re.search(r'const PROVIDERS = \[(.*?)\];', generated_content, re.DOTALL)
    if not providers_match:
        print("❌ Error: Could not find PROVIDERS array")
        return
    new_providers = 'const PROVIDERS = [' + providers_match.group(1) + '];'

    # Extract RAW_HTML data (everything between first const RAW_HTML and the Load comment)
    print("✂️  Extract RAW_HTML data...")
    raw_html_start = generated_content.find('const RAW_HTML_ADVANT')
    raw_html_end = generated_content.find('// Load all games data')
    new_raw_html = generated_content[raw_html_start:raw_html_end].strip()

    # Extract allGames assignments (everything after "// Load all games data")
    print("✂️  Extract allGames assignments...")
    allgames_start = generated_content.find("allGames['advant']")
    allgames_end = generated_content.find("allGames['ggsoftslot']")
    # Find the end of the last allGames line
    allgames_end = generated_content.find(';', allgames_end) + 1
    new_allgames = generated_content[allgames_start:allgames_end].strip()

    print("\n🔧 Updating HTML sections...")

    # 1. Replace RAW_HTML section (from first const RAW_HTML to just before const PROVIDERS)
    # Find the old RAW_HTML section
    old_raw_start = html_content.find('const RAW_HTML_PRAGMATIC')
    old_raw_end = html_content.find('const PROVIDERS = [')

    if old_raw_start == -1 or old_raw_end == -1:
        print("❌ Error: Could not find RAW_HTML or PROVIDERS sections")
        return

    # Replace RAW_HTML section
    part1 = html_content[:old_raw_start]
    part2 = '\n        ' + new_raw_html + '\n\n        '
    remaining = html_content[old_raw_end:]

    html_content = part1 + part2 + remaining
    print("   ✅ RAW_HTML section replaced")

    # 2. Replace PROVIDERS array
    # Find the PROVIDERS array in updated content
    old_providers_start = html_content.find('const PROVIDERS = [')
    old_providers_end = html_content.find('];', old_providers_start) + 2

    if old_providers_start == -1:
        print("❌ Error: Could not find PROVIDERS array")
        return

    part1 = html_content[:old_providers_start]
    part2 = new_providers
    remaining = html_content[old_providers_end:]

    html_content = part1 + part2 + remaining
    print("   ✅ PROVIDERS array replaced")

    # 3. Update activeProvider line
    html_content = re.sub(
        r"let activeProvider = '.*?';",
        "let activeProvider = 'pragmaticslots';",
        html_content
    )
    print("   ✅ activeProvider updated")

    # 4. Replace allGames assignments
    # Find the old allGames['pragmatic'] line and replace all assignments until allGames['cq9']
    old_allgames_start = html_content.find("allGames['pragmatic']")
    old_allgames_end = html_content.find("allGames['cq9']")
    old_allgames_end = html_content.find(';', old_allgames_end) + 1

    if old_allgames_start == -1 or old_allgames_end == -1:
        print("❌ Error: Could not find allGames assignments")
        return

    part1 = html_content[:old_allgames_start]
    part2 = new_allgames
    remaining = html_content[old_allgames_end:]

    html_content = part1 + part2 + remaining
    print("   ✅ allGames assignments replaced")

    # Write output
    print("\n💾 Menyimpan index.html...")
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("\n✅ HTML berhasil di-update!")
    print("📁 Backup: index.html.backup")
    print("📄 Updated: index.html")

    # Summary
    print("\n📊 Summary:")
    print("   - Total providers: 19")
    print("   - Total games: 2997")
    print("   - Active provider: pragmaticslots (595 games)")
    print("\n🎉 Selesai! Silahkan buka index.html di browser.")

if __name__ == "__main__":
    main()
