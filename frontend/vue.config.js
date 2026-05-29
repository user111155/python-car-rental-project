module.exports = {
  productionSourceMap: false,
  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true
      },
      '/static': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true
      }
    }
  },
  configureWebpack: {
    performance: {
      maxEntrypointSize: 512000,
      maxAssetSize: 512000
    }
  }
}
