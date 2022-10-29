/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/app/**/*.{vue,js}",
    "./src/components/**/*.{vue,js}",
    "./src/layouts/**/*.{vue,js}",
    "./src/pages/**/*.{vue,js}",
  ],
  theme: {
    fontFamily: {
      sans: ["Roboto"],
      mono: ["Roboto Mono"],
      serif: ["Roboto Slab"],
    },
    extend: {},
  },
  plugins: [],
}
