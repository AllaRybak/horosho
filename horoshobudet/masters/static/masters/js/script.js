// Получаем элементы слайдера
    const slider = document.querySelector('.slider');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    const slides = Array.from(slider.querySelectorAll('.slide-box'));
    const slideCount = slides.length;
    let slideIndex = 0;

    // Устанавливаем обработчики событий для кнопок
    prevButton.addEventListener('click', showPreviousSlide);
    nextButton.addEventListener('click', showNextSlide);

    // Функция для показа предыдущего слайда
    function showPreviousSlide() {
      slideIndex = (slideIndex - 1 + slideCount) % slideCount;
      updateSlider();
    }

    // Функция для показа следующего слайда
    function showNextSlide() {
      slideIndex = (slideIndex + 1) % slideCount;
      updateSlider();
    }

    // Функция для обновления отображения слайдера
    function updateSlider() {
      slides.forEach((slide, index) => {
        if (index === slideIndex) {
          slide.style.display = 'block';
        } else {
          slide.style.display = 'none';
        }
      });
    }

    // Инициализация слайдера
    updateSlider();

// Скрипт для фото-клик
// Получаем элементы модального окна и изображения
    const modal = document.getElementById("modal");
    const modalImage = document.getElementById("modal-image");

    // Отображаем модальное окно и устанавливаем источник изображения
    function displayModal(img)
    {
        modal.style.display = "block";
        modalImage.src = img.src;
    }

    // Скрываем содержимое модального окна, если пользователь кликнул вне его
    function hideModal()
    {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

//var link_photo = document.getElementsByClassName("form-profile");
//
//link_photo[7].a.remove()