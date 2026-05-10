module.exports = {
  content: [
    "./*.html",
    "./**/*.html",
    "./**/*.js",
  ],

  theme: {
    container: {
      center: true,
    },

    extend: {
      colors: {
        primary: {
          // DEFAULT: "#D12329",
          DEFAULT: "#E7000B",
          50: "#fff1f2",
          100: "#ffe0e2",
          200: "#ffc7cb",
          300: "#ff9ea5",
          400: "#ff6570",
          500: "#E7000B",
          600: "#c40009",
          700: "#a30008",
          800: "#88010a",
          900: "#73030b",
        },
        secondary: {
          DEFAULT: "#0EA5E9",
          50: "#f0f9ff",
          100: "#e0f2fe",
          200: "#bae6fd",
          300: "#7dd3fc",
          400: "#38bdf8",
          500: "#0EA5E9",
          600: "#0284c7",
          700: "#0369a1",
          800: "#075985",
          900: "#0c4a6e",
        },
        accent: {
          DEFAULT: "#FACC15",
          50: "#fefce8",
          100: "#fef9c3",
          200: "#fef08a",
          300: "#fde047",
          400: "#facc15",
          500: "#eab308",
          600: "#ca8a04",
          700: "#a16207",
          800: "#854d0e",
          900: "#713f12",
        },
      },
    },
  },

  plugins: [],
}