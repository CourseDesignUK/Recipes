# Easy Meal Planner

A zero-dependency, mobile-first web application designed for rapid meal planning using gesture-based recipe triage, automatic ingredient aggregation, and print/calendar export capabilities.

---

## Overview

Easy Meal Planner reduces decision fatigue by presenting curated recipes through a single-card interface. Users filter meals by prep time, category, and target days, then swipe to accept, reject, or bookmark options. Upon completing the quota, the application scales ingredient portions, categorizes raw items by grocery aisle, and outputs structured plans for physical print or calendar sync.

Built as a self-contained client-side application using standard HTML5, CSS3, and vanilla JavaScript (ES6+).

---

## Key Features

- **Gesture & Keyboard Triage:** Swipe right to accept into the weekly plan, left to dismiss, or up to save to favorites. Full desktop parity via arrow keys and hotkeys.
- **Portion Scaling Engine:** Dynamically parses fractional ingredient quantities (e.g., `½`, `1 1/4`, `2 tbsp`) and scales values based on selected portion multipliers (1x to 3x).
- **Aisle Classification:** Regex-based categorization engine sorts aggregated shopping list items across 6 supermarket departments: Produce, Meat & Seafood, Dairy & Chilled, Bakery, Spices & Seasonings, and Pantry & Dry Goods.
- **Screen Wake Lock API:** Integrated display retention prevents mobile screen timeout while consulting ingredients and step-by-step methods during cooking.
- **A4 Print Engine:** Dedicated `@media print` stylesheet generates a clean, two-column black-and-white layout containing the meal agenda and organized shopping list.
- **iCalendar Export:** Client-side generation of `.ics` calendar files containing automated daily dinner schedules, prep times, scaled ingredient checklists, and cooking instructions.
- **Local Persistence:** Retains favorite meals and historical meal plans across browser sessions using the `localStorage` API.

---

## Keyboard Controls

| Key | Context | Action |
| :--- | :--- | :--- |
| `→` (Right Arrow) | Card Screen | Accept / Save recipe |
| `←` (Left Arrow) | Card Screen | Dismiss / Reject recipe |
| `↑` (Up Arrow) | Card Screen | Bookmark to Favorites |
| `Backspace` / `Z` | Card Screen | Undo last card decision |
| `Space` | Card / Modal | Toggle Recipe Info Modal |
| `Escape` | Modal Active | Close Recipe Info Modal |

---

## File Structure & Requirements

The application runs directly in the browser via any static file server:

```text
.
├── index.html              # Main single-file application
├── intro.mp4               # Optional video splash screen (auto-dismisses on end)
└── Cards/
    ├── cards.json          # Manifest indexing all recipe JSON files
    ├── recipe-01.json      # Individual recipe data
    └── recipe-02.json
