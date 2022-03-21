module.exports = {
  mode: 'jit',
  content: ['./public/**/*.html', './src/**/*.{js,jsx,ts,tsx,vue}'],
  media: false, // or 'media' or 'class'

  theme: {
    fontfamily: {
      sans: ['roboto'],
    },
    extend: {
      animation: {
        'spin-slow': 'spin 3s linear infinite',
        'spin-reverse': 'spin reverse 3s linear infinite',
        'ping-slow': 'ping 3s linear infinite',
        'ping-medium': 'ping 2s linear infinite',
        'ping-fast': 'ping 1s linear infinite',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
