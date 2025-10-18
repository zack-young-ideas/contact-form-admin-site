import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  build: {
    outDir: 'static/css',
    emptyOutDir: false,
    assetsDir: '',
    rollupOptions: {
      input: {
        styles: path.resolve(__dirname, 'assets/scss/styles.scss'),
      },
      output: {
        assetFileNames: '[name][extname]',
      },
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        includePaths: ['assets/scss'],
      },
    },
  },
});

