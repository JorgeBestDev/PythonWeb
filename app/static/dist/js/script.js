const galleryContainer = document.querySelector('.gallery-container');
const galleryItems = document.querySelectorAll('.gallery-item');



class Carousel {
    constructor(container, items) {
        this.carouselContainer = container;
        this.carouselArray = [...items];
        this.currentIndex = 0;
        this.totalItems = this.carouselArray.length;
        this.autoAdvanceInterval = null;
    }

    updateGallery() {
        this.carouselArray.forEach(el => {
            el.classList.remove('gallery-item-1');
            el.classList.remove('gallery-item-2');
            el.classList.remove('gallery-item-3');
            el.classList.remove('gallery-item-4');
            el.classList.remove('gallery-item-5');
            el.classList.remove('gallery-item-6');
            el.classList.remove('gallery-item-7');
            el.classList.remove('gallery-item-8');
        });
        this.carouselArray.slice(0, 8).forEach((el, i) => {
            el.classList.add(`gallery-item-${i + 1}`);
        });
    }

    setCurrentState(direction) {
        if (direction === 'previus') {
            this.carouselArray.push(this.carouselArray.shift());
        } else {
            this.carouselArray.unshift(this.carouselArray.pop());
        }
        this.updateGallery();
    }
    
    autoAdvance() {
        const time=2000;
        this.autoAdvanceInterval = setInterval(() => {
            this.setCurrentState('next');
        }, time); // Cambia de slide cada 2 segundos
    }
}

const exampleCarousel = new Carousel(galleryContainer, galleryItems);
exampleCarousel.autoAdvance(); // Inicia el avance automático de los slides