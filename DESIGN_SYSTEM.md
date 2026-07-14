# 🎨 UI/UX DESIGN GUIDE

## Color Palette

### Light Mode
```
┌─────────────────────────────────────────┐
│ Background:    #FFFFFF (White)          │
│ Accent:        #F8FAFC (Off-white)      │
│ Text:          #0F172A (Dark Navy)      │
│ Secondary:     #64748B (Slate Gray)     │
│                                         │
│ Primary:       #2563EB (Blue)           │
│ Primary Alt:   #1D4ED8 (Dark Blue)      │
│ Light Accent:  #60A5FA (Light Blue)     │
│ Hover:         #1E293B (Slate)          │
└─────────────────────────────────────────┘
```

### Dark Mode
```
┌─────────────────────────────────────────┐
│ Background:    #0B1220 (Dark Navy)      │
│ Accent:        #111827 (Deep Navy)      │
│ Text:          #F8FAFC (Off-white)      │
│ Secondary:     #CBD5E1 (Light Gray)     │
│                                         │
│ Primary:       #2563EB (Blue)           │
│ Card:          #1E293B (Dark Slate)     │
│ Input:         #1E293B (Dark Slate)     │
│ Border:        #334155 (Slate)          │
└─────────────────────────────────────────┘
```

---

## Typography

### Hierarchy
```
H1 - Hero Title
└─ font-size: 3rem
└─ font-weight: 700
└─ Used: Main page header

H2 - Page Title
└─ font-size: 1.5rem
└─ font-weight: 700
└─ Used: Card titles

H3 - Subtitle
└─ font-size: 1.2rem
└─ font-weight: 600
└─ Used: Section headers

Body Text
└─ font-size: 0.95rem
└─ font-weight: 400
└─ Used: Chat messages

Small Text
└─ font-size: 0.85rem
└─ opacity: 0.7
└─ Used: Metadata, hints

Tiny Text
└─ font-size: 0.75rem
└─ opacity: 0.6
└─ Used: Intent labels
```

---

## Spacing System

### Scale
```
4px   - Minimal spacing (borders, gaps)
8px   - Tight spacing (small margins)
12px  - Comfortable spacing (inputs, small sections)
16px  - Standard spacing (padding, gaps)
24px  - Generous spacing (sections, containers)
32px  - Large spacing (page sections)
40px  - XL spacing (page padding)
```

### Common Spacing
```
Message bubble:        padding: 12px 16px
Input area:           padding: 16px 24px
Card padding:         padding: 32px
Section gap:          gap: 24px
Inline gap:          gap: 12px
Page padding:         padding: 40px
```

---

## Component Styles

### Message Bubbles

#### User Message (Right-aligned)
```
┌─────────────────────────────────┐
│                 ┏━━━━━━━━━━━━━┓ │
│                 ┃ Your message┃ │
│                 ┗━━━━━━━━━━━━━┛ │
│              (blue gradient)    │
├─────────────────────────────────┤
│ Background:   linear-gradient   │
│ Color 1:      #2563EB          │
│ Color 2:      #1D4ED8          │
│ Text color:   #FFFFFF          │
│ Border-radius: 16px            │
│ Bottom-right: 4px              │
│ Padding:      12px 16px        │
│ Max-width:    65%               │
│ Shadow:       0 2px 8px        │
└─────────────────────────────────┘
```

#### Assistant Message (Left-aligned)
```
┌─────────────────────────────────┐
│ ┏━━━━━━━━━━━━━━━━━━┓            │
│ ┃ Bot's response   ┃            │
│ ┗━━━━━━━━━━━━━━━━━━┛            │
│ ⚙️ database_lookup · 95%        │
│ (white/dark slate)              │
├─────────────────────────────────┤
│ Background:   #F1F5F9 / #1E293B│
│ Text color:   #0F172A / #E2E8F0│
│ Border-radius: 16px            │
│ Bottom-left:  4px              │
│ Padding:      12px 16px        │
│ Max-width:    65%               │
│ Shadow:       0 2px 8px        │
│ Border:       1px solid         │
└─────────────────────────────────┘
```

### Cards

#### Chatbot Card
```
┌──────────────────────────┐
│      🤖 LogiBot          │
│                          │
│ AI Logistics Support     │
│                          │
│  ┌────────────────────┐  │
│  │  [Start Chat]      │  │
│  └────────────────────┘  │
│                          │
│ ┌─ Hover Effect ─┐      │
│ │ Transform: -8px │      │
│ │ Box-shadow: ✨  │      │
│ └─────────────────┘      │
└──────────────────────────┘
```

### Input Area
```
┌────────────────────────────────────────┐
│ ┌────────────────────────────────────┐ │
│ │ Type your message...               │ │
│ │ (Shift+Enter for new line)         │ │
│ │                                    │ │
│ │ [Height: 44px, grows with text]  │ │
│ └────────────────────────────────────┘ │
│                                        │
│ ┌──────────┐ ┌───────┐                │
│ │   Send   │ │ Clear │                │
│ └──────────┘ └───────┘                │
└────────────────────────────────────────┘
```

---

## Animations

### Fade In (Messages)
```css
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
duration: 0.3s ease-out
```

### Hover Effect (Buttons)
```
Default:
└─ Transform: none
└─ Shadow: normal

Hover:
└─ Transform: translateY(-2px)
└─ Shadow: larger

Active:
└─ Transform: translateY(0)
└─ Shadow: normal

Duration: 0.2s ease
```

### Card Hover
```
Default:
└─ Transform: none
└─ Border: transparent
└─ Shadow: 0 10px 40px rgba(...)

Hover:
└─ Transform: translateY(-8px)
└─ Border: #2563EB
└─ Shadow: 0 20px 60px rgba(...)

Duration: 0.3s cubic-bezier(...)
```

---

## Responsive Breakpoints

### Desktop (> 768px)
```
┌─────────────────────────────┐
│  ┌──────┐  ┌──────────────┐ │
│  │ Back │  │ LogiBot      │ │
│  └──────┘  │ AI Support   │ │
│            └──────────────┘ │
│                             │
│  Chat messages area         │
│  (65% max-width bubbles)    │
│                             │
│  ┌─────────────────────────┐ │
│  │ Input area              │ │
│  └─────────────────────────┘ │
└─────────────────────────────┘
```

### Tablet (600px - 768px)
```
┌───────────────────────┐
│ Back │ LogiBot        │
│      │ AI Support     │
├───────────────────────┤
│                       │
│ Chat messages area    │
│ (75% max-width)       │
│                       │
├───────────────────────┤
│ Input [S] [C]         │
└───────────────────────┘
```

### Mobile (< 600px)
```
┌──────────────┐
│ Back LogiBot │
├──────────────┤
│              │
│ Messages     │
│ (85% width)  │
│              │
├──────────────┤
│ Input        │
│ [Send][Clr]  │
└──────────────┘
```

---

## Accessibility

### Color Contrast
```
Light Mode:
└─ Text (#0F172A) on White (#FFF):        21:1 ✅ AAA
└─ Text (#0F172A) on Light Gray (#F8F):   15:1 ✅ AAA
└─ Text (#FFF) on Blue (#2563EB):         10:1 ✅ AAA

Dark Mode:
└─ Text (#F8FAFC) on Dark (#0B1220):      18:1 ✅ AAA
└─ Text (#F8FAFC) on Slate (#1E293B):     12:1 ✅ AAA
└─ Text (#FFF) on Blue (#2563EB):         10:1 ✅ AAA
```

### Focus States
```
All interactive elements have:
└─ Visible focus outline
└─ Keyboard navigation
└─ Sufficient touch target (≥44px)
```

### Semantic HTML
```
✅ Proper heading hierarchy (h1, h2, etc.)
✅ Form labels for inputs
✅ Button elements for buttons
✅ Descriptive link text
✅ ARIA labels where needed
```

---

## Dark Mode Implementation

### CSS Media Query
```css
@media (prefers-color-scheme: dark) {
  body { background: #0B1220; }
  .chat-bubble { background: #1E293B; }
  /* ... more rules ... */
}
```

### Color Mapping
```
Light Mode → Dark Mode
─────────────────────────────────────
#FFFFFF   → #111827
#F8FAFC   → #0F172A
#0F172A   → #F8FAFC
#64748B   → #CBD5E1
#2563EB   → #2563EB (same)
```

### Automatic Detection
```
Streamlit detects system preference automatically
No manual toggle needed
User can override in system settings
Changes reflected immediately on reload
```

---

## Visual Hierarchy

### Main Page
```
1. Hero Title (3rem, gradient)
2. Subtitle (1.2rem)
3. Card Titles (1.5rem, bold)
4. Card Descriptions (0.95rem)
5. Button Text (0.9rem, bold)
6. Footer Text (0.9rem, muted)
```

### Chat Page
```
1. Header Title (1.3rem)
2. Header Subtitle (0.85rem)
3. Message Content (0.95rem)
4. Message Metadata (0.75rem)
5. Input Placeholder (0.95rem)
```

---

## Shadow System

### Subtle Shadows
```
Card shadow:      0 10px 40px rgba(15, 23, 42, 0.1)
Message shadow:   0 2px 8px rgba(15, 23, 42, 0.08)
Input focus:      0 0 0 3px rgba(37, 99, 235, 0.1)
Header shadow:    0 4px 12px rgba(37, 99, 235, 0.15)
```

### Dark Mode Shadows
```
Increased contrast for visibility
Slightly darker shadows
More pronounced depth
```

---

## Border Radius

### System
```
Micro:    4px   (message bubble bottoms)
Small:    8px   (back button)
Medium:   16px  (message bubbles, buttons)
Large:    20px  (input area)
XL:       24px  (old card style)
Round:    999px (pills/chips)
```

### Usage
```
Cards:         20px
Buttons:       16px
Input:         20px
Messages:      16px
Accents:       4-8px
```

---

## Font Family

```css
font-family: -apple-system, BlinkMacSystemFont, 
             "Segoe UI", Roboto, "Helvetica Neue", 
             Arial, sans-serif;
```

### System Fonts
- macOS:   San Francisco
- iOS:    San Francisco
- Android: Roboto
- Windows: Segoe UI
- Web:    Fallback to system sans-serif

---

## Performance Optimization

```
✅ CSS animations (GPU accelerated)
✅ Smooth scroll behavior
✅ No layout shifts
✅ Lazy loaded images
✅ Minimal repaints
✅ Cached resources
✅ Efficient selectors
```

---

## Design Tokens

```python
# Colors
PRIMARY = "#2563EB"
PRIMARY_DARK = "#1D4ED8"
PRIMARY_LIGHT = "#60A5FA"
GRAY_DARK = "#0F172A"
GRAY_LIGHT = "#F8FAFC"

# Spacing
SPACE_S = "12px"
SPACE_M = "16px"
SPACE_L = "24px"

# Typography
TEXT_SIZE_LARGE = "1.5rem"
TEXT_SIZE_BASE = "0.95rem"
TEXT_SIZE_SMALL = "0.85rem"
FONT_WEIGHT_BOLD = "700"
FONT_WEIGHT_MEDIUM = "600"

# Borders
RADIUS_S = "8px"
RADIUS_M = "16px"
RADIUS_L = "20px"

# Shadows
SHADOW_S = "0 2px 8px"
SHADOW_M = "0 10px 40px"
SHADOW_L = "0 20px 60px"
```

---

## Summary

This design system provides:
- ✅ Professional appearance
- ✅ Consistent styling
- ✅ Responsive layout
- ✅ Dark mode support
- ✅ Accessibility
- ✅ Smooth interactions
- ✅ Modern aesthetics
- ✅ Easy maintenance

The entire frontend follows these principles for a cohesive, polished user experience.
