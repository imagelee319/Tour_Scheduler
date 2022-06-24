  let sliders = document.querySelectorAll(".slider")
  let innerSliders = document.querySelectorAll(".slider-inner")
  let presseds = [false,false]
  let startx = []
  let x = []
  
  sliders.forEach((slider, index) => {
      slider.addEventListener("mousedown", e => {
          presseds[index] = true
          startx[index] = e.offsetX - innerSliders[index].offsetLeft
          slider.style.cursor = "grabbing"
      })
  
      slider.addEventListener("mouseenter", () => {
          slider.style.cursor = "grab"
      })
  
      slider.addEventListener("mouseup", () => {
          slider.style.cursor = "grab"
      })
  
      window.addEventListener("mouseup", () => {
          presseds[index] = false
      })
  
      slider.addEventListener("mousemove", e => {
          if (!presseds[index]) return
          e.preventDefault()
          x[index] = e.offsetX
  
          innerSliders[index].style.left = `${x[index] - startx[index]}px`
          checkboundary(index) 
      })
  })
  
  
  function checkboundary(index) {
      let outer = sliders[index].getBoundingClientRect()
      let inner = innerSliders[index].getBoundingClientRect()
  
      if (parseInt(innerSliders[index].style.left) > 0) {
          innerSliders[index].style.left = "0px"
      } else if (inner.right < outer.right) {
          innerSliders[index].style.left = `-${inner.width - outer.width}px`
      }
  }
