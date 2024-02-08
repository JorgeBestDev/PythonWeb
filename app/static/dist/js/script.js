const galleryContainer = document.querySelector('.gallery-container');
const galleryControlContainer = document.querySelector('.gallery-control');
const galleryControl = ['previus','next'];
const galleryItems = document.querySelectorAll('.gallery-item');

class Carousel {
    constructor(container, items, control) {
        this.carouselContainer = container;
        this.carouselControl = control;
        this.carouselArray = [...items];
    }

    updateGallery() {
        this.carouselArray.forEach(el => {
            el.classList.remove('gallery-item-1');
            el.classList.remove('gallery-item-2');
            el.classList.remove('gallery-item-3');
            el.classList.remove('gallery-item-4');
            el.classList.remove('gallery-item-5');
        });
        this.carouselArray.slice(0, 5).forEach((el, i) => {
            el.classList.add(`gallery-item-${i + 1}`);
        });
    }

    setCurrentState(direction) {
        if (direction.className == 'gallery-control-previus') {
            this.carouselArray.push(this.carouselArray.shift());
        } else {
            this.carouselArray.unshift(this.carouselArray.pop());
        }
        this.updateGallery();
    }

    setControl() {
        this.carouselControl.forEach(control => {
            galleryControlContainer.appendChild(document.createElement('button')).className = `gallery-control-${control}`;
            document.querySelector(`.gallery-control-${control}`).innerText=control;
        });
    }

    useControl() {
        const triggers = [...galleryControlContainer.childNodes];
        triggers.forEach(control => {
            control.addEventListener('click', e => {
                e.preventDefault();
                this.setCurrentState(control);
            });
        });
    }
}

const exampleCarousel = new Carousel(galleryContainer, galleryItems, galleryControl);
exampleCarousel.setControl();
exampleCarousel.useControl();