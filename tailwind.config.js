/*@type {import('tailwindcss').Config}*/
module.exports = {
  content: ["./static/scripts/*.js",
            "./templates/*.html"],
  theme: {
    extend: {
        dropShadow: {
            glow: [
              "0 0px 20px rgba(255,192, 203, 0.35)",
              "0 0px 65px rgba(255, 192,203, 0.2)"
            ]
          },
        screens: {
            'widescreen': { 'raw': '(min-aspect-ratio: 3/2)' },
            'tallscreen': { 'raw': '(max-aspect-ratio: 13/20)' },
        },
        keyframes: {
            'open-menu': {
                '0%': {transform: 'scaleY(0)'},
                '80%': {transform: 'scaleY(1.2)'},
                '100%': {transform: 'scaleY(1)'},
            },
        },
        animation: {
            'open-menu': 'open-menu 0.5s ease-in-out forwards',

        }
    },
  },
  plugins: [],
}
