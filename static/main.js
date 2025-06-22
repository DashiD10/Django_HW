// Основной JavaScript файл для барбершопа

document.addEventListener('DOMContentLoaded', function() {
    console.log('Барбершоп загружен!');
    
    // Инициализация всех функций
    initScrollToServices();
    initFormValidation();
    initOrdersTable();
    initStatusBadges();
});

// Можно добавить обработку ошибок
function scrollToServices() {
    const servicesSection = document.getElementById('services');
    if (servicesSection) {
        servicesSection.scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    } else {
        console.warn('Секция услуг не найдена');
    }
}

// Инициализация прокрутки к услугам
function initScrollToServices() {
    const scrollButton = document.querySelector('.btn[onclick="scrollToServices()"]');
    if (scrollButton) {
        scrollButton.addEventListener('click', function(e) {
            e.preventDefault();
            scrollToServices();
        });
    }
}

// Валидация формы записи
function initFormValidation() {
    const bookingForm = document.querySelector('.booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            const clientName = document.getElementById('client_name');
            const service = document.getElementById('service');
            const master = document.getElementById('master');
            const date = document.getElementById('date');
            
            let isValid = true;
            let errorMessage = '';
            
            // Проверка имени клиента
            if (!clientName.value.trim()) {
                errorMessage += 'Пожалуйста, введите ваше имя.\n';
                isValid = false;
            }
            
            // Проверка выбора услуги
            if (!service.value) {
                errorMessage += 'Пожалуйста, выберите услугу.\n';
                isValid = false;
            }
            
            // Проверка выбора мастера
            if (!master.value) {
                errorMessage += 'Пожалуйста, выберите мастера.\n';
                isValid = false;
            }
            
            // Проверка даты
            if (!date.value) {
                errorMessage += 'Пожалуйста, выберите дату записи.\n';
                isValid = false;
            } else {
                const selectedDate = new Date(date.value);
                const today = new Date();
                today.setHours(0, 0, 0, 0);
                
                if (selectedDate < today) {
                    errorMessage += 'Дата записи не может быть в прошлом.\n';
                    isValid = false;
                }
            }
            
            if (!isValid) {
                e.preventDefault();
                alert(errorMessage);
                return false;
            }
            
            // Показываем сообщение об отправке
            const submitButton = bookingForm.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.textContent = 'Отправляем...';
                submitButton.disabled = true;
            }
        });
        
        // Установка минимальной даты на сегодня
        const dateInput = document.getElementById('date');
        if (dateInput) {
            const today = new Date().toISOString().split('T')[0];
            dateInput.setAttribute('min', today);
        }
    }
}

// Функциональность для таблицы заявок
function initOrdersTable() {
    const orderRows = document.querySelectorAll('.order-row');
    
    orderRows.forEach(row => {
        // Добавляем hover эффект
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f8f9fa';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
        
        // Клик по строке для перехода к деталям
        row.addEventListener('click', function(e) {
            if (e.target.tagName !== 'A' && e.target.tagName !== 'BUTTON') {
                const detailLink = this.querySelector('a[href*="order_detail"]');
                if (detailLink) {
                    window.location.href = detailLink.href;
                }
            }
        });
    });
}

// Анимация для статусных бейджей
function initStatusBadges() {
    const statusBadges = document.querySelectorAll('.status-badge');
    
    statusBadges.forEach(badge => {
        // Добавляем пульсацию для новых заявок
        if (badge.classList.contains('status-новая')) {
            badge.style.animation = 'pulse 2s infinite';
        }
        
        // Добавляем tooltip с описанием статуса
        badge.addEventListener('mouseenter', function() {
            const status = this.textContent.trim().toLowerCase();
            let description = '';
            
            switch(status) {
                case 'новая':
                    description = 'Заявка принята и ожидает подтверждения';
                    break;
                case 'подтвержденная':
                    description = 'Заявка подтверждена';
                    break;
                case 'отмененная':
                    description = 'Заявка отменена';
                    break;
                case 'выполненная':
                    description = 'Услуги оказаны';
                    break;
            }
            
            if (description) {
                this.setAttribute('title', description);
            }
        });
    });
}

// Функция для фильтрации заявок по статусу (если понадобится)
function filterOrdersByStatus(status) {
    const orderRows = document.querySelectorAll('.order-row');
    
    orderRows.forEach(row => {
        if (status === 'all' || row.classList.contains(`status-${status}`)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Функция для поиска заявок по имени клиента (если понадобится)
function searchOrders(searchTerm) {
    const orderRows = document.querySelectorAll('.order-row');
    const term = searchTerm.toLowerCase();
    
    orderRows.forEach(row => {
        const clientName = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
        if (clientName.includes(term)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Утилитарные функции
function showNotification(message, type = 'info') {
    // Создаем уведомление
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Стили для уведомления
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        z-index: 1000;
        opacity: 0;
        transition: opacity 0.3s ease;
    `;
    
    // Цвета в зависимости от типа
    switch(type) {
        case 'success':
            notification.style.backgroundColor = '#27ae60';
            break;
        case 'error':
            notification.style.backgroundColor = '#e74c3c';
            break;
        case 'warning':
            notification.style.backgroundColor = '#f39c12';
            break;
        default:
            notification.style.backgroundColor = '#3498db';
    }
    
    document.body.appendChild(notification);
    
    // Показываем уведомление
    setTimeout(() => {
        notification.style.opacity = '1';
    }, 100);
    
    // Скрываем через 3 секунды
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Добавляем CSS анимации через JavaScript
const style = document.createElement('style');
style.textContent = `
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .order-row {
        cursor: pointer;
        transition: background-color 0.2s ease;
    }
    
    .notification {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
`;
document.head.appendChild(style);

// Экспортируем функции для использования в других местах
window.barbershop = {
    scrollToServices,
    filterOrdersByStatus,
    searchOrders,
    showNotification
};
