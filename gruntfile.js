module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: 'gm',
          sizes: [{
            width: 1000,
            quality: 40
          }]
        },
        
        files: [{
          expand: true,
          src: ['*.jpg'],
          cwd: 'media/source/',
          dest: 'media/dest/'
        }]
      }
    },
  });
  
  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.registerTask('default', ['responsive_images']);

};
