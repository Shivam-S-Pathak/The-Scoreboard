window.onload = function() {
    let components = document.querySelectorAll('.container');
    components.forEach((container, index) => {
      setTimeout(() => {
        container.style.opacity = '1';
      }, index * 200);
    });
  };