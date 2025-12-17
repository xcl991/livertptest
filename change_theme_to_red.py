#!/usr/bin/env python3
"""
Script untuk mengubah theme dari purple ke red
"""
import re

def change_theme_to_red():
    print("🎨 Mengubah theme dari purple ke red...")

    # Read HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Color replacements
    replacements = [
        # Purple shades to Red shades
        ('purple-900', 'red-900'),
        ('purple-800', 'red-800'),
        ('purple-700', 'red-700'),
        ('purple-600', 'red-600'),
        ('purple-500', 'red-500'),
        ('purple-400', 'red-400'),
        ('purple-300', 'red-300'),
        ('purple-200', 'red-200'),
        ('purple-100', 'red-100'),
        ('purple-50', 'red-50'),

        # Gradients
        ('from-purple-', 'from-red-'),
        ('to-purple-', 'to-red-'),
        ('via-purple-', 'via-red-'),

        # RGBA shadows (purple glow to red glow)
        ('rgba(168,85,247,', 'rgba(239,68,68,'),
        ('rgba(168, 85, 247,', 'rgba(239, 68, 68,'),

        # Specific gradient backgrounds
        ('#1a0033', '#330000'),  # Dark purple to dark red
        ('#2d0052', '#520000'),  # Purple to red
        ('#3d0066', '#660000'),  # Purple to red
        ('#1a0a33', '#331a1a'),  # Purple bg to red bg
        ('#0f0520', '#200f0f'),  # Very dark purple to very dark red

        # Hex colors in linear gradients
        ('0f0520', '200f0f'),
        ('1a0a33', '331a1a'),
    ]

    # Apply replacements
    for old, new in replacements:
        content = content.replace(old, new)

    # Count changes
    changes_count = sum(1 for old, new in replacements if old in original_content)

    # Write updated HTML
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Theme berhasil diubah!")
    print(f"📊 Total color replacements: {changes_count}")
    print(f"📁 File updated: index.html")
    print(f"\n🎨 Theme colors:")
    print(f"   Purple → Red")
    print(f"   Purple shadows → Red shadows")
    print(f"   Purple gradients → Red gradients")
    print(f"\n🌟 New theme: RED THEME ACTIVATED!")

if __name__ == "__main__":
    change_theme_to_red()
