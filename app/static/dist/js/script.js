const galleryContainer = document.querySelector('.gallery.container');
const galleryControlsContainer = document.querySelector('.gallery.controls');
const galleryControls = ['previus','next'];
const galleryItems = document.querySelectorAll('.gallery.item');

class Carousel {
    constructor(container, items, controls){
        this.carouselContainer = container;
        this.carouselControls = controls;
        this.carouselArray = [...items];
    }

    updateGallery(){
        this.carouselArray.forEach(el => {
            el.classList.remove('gallery-item-1');
            el.classList.remove('gallery-item-2');
            el.classList.remove('gallery-item-3');
            el.classList.remove('gallery-item-4');
            el.classList.remove('gallery-item-5');
        });
        this.carouselArray.slice(0,5).forEach((el , i) => {
            el.classList.add(`gallery-items-${i+1}`);
        });
    }
    setCurrentState(direction){
        if(direction.className == 'gallery-controls-previous'){
            
        }
    }
}