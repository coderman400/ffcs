/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        'theory':'#8b635c',
        'lab':'#DCBF85',
      },
    },
  },
  plugins: [],
}