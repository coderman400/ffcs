/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        'charcoal':'#264653',
        'persian':'#2A9D8F',
        'saffron':'#E9C46A',
        'sandy':'#F4A261',
        'sienna':'#E76F51'
      },
      screens:{
        'sm': '320px'
      }
    },
  },
  plugins: [],
}