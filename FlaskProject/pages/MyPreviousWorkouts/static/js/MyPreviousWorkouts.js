document.addEventListener("DOMContentLoaded", function() {

    const lessons = [
        { date: "2024-02-10", time: "17:00", Branch: "Studio Tel-Aviv", lesson: "Zumba", difficulty: "Easy" },
        { date: "2024-02-12", time: "18:30", Branch: "Studio Life", lesson: "Pilates", difficulty: "Medium" },
        { date: "2024-02-14", time: "16:00", Branch: "Studio Tel-Aviv", lesson: "Yoga", difficulty: "Medium" },
        { date: "2024-02-16", time: "19:00", Branch: "Studio Life", lesson: "CrossFit", difficulty: "Hard" },
        { date: "2024-02-18", time: "20:00", Branch: "Studio Tel-Aviv", lesson: "Spinning", difficulty: "Medium" }

    ];

    const tbody = document.querySelector("tbody");

    lessons.forEach(lesson => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${formatDate(lesson.date)}</td>
            <td>${lesson.time}</td>
            <td>${lesson.Branch}</td>
            <td>${lesson.lesson}</td>
            <td class="difficulty" data-value="${lesson.difficulty}">
                <div class="filter-container">
                    <button class="filter-button">SELECT</button>
                    <div class="filter-options-container"></div>
                </div>
            </td>
        `;
        tbody.appendChild(row);
    });

    const filterOptions = ["Easy", "Medium", "Hard"];

    tbody.addEventListener("click", function(event) {
        if (event.target.classList.contains("filter-option")) {
            const option = event.target.textContent.toUpperCase();
            const difficultyCell = event.target.closest("td");
            const filterButton = difficultyCell.querySelector(".filter-button");

            console.log('Filter by difficulty: ${option}');
            filterButton.textContent = option;
            difficultyCell.dataset.value = option;


            difficultyCell.querySelector(".filter-options-container").innerHTML = "";
        } else if (event.target.classList.contains("filter-button")) {
            const difficultyCell = event.target.closest("td");
            renderFilterOptions(difficultyCell);
        }
    });

    function renderFilterOptions(difficultyCell) {
        const optionsContainer = difficultyCell.querySelector(".filter-options-container");
        optionsContainer.innerHTML = createOptionsHTML(filterOptions, difficultyCell.dataset.value);
    }

    function createOptionsHTML(options, selectedOption) {
        return options.map(option => `
            <button class="filter-option ${option === selectedOption ? 'selected' : ''}">${option}</button>
        `).join('');
    }



function changeSelectColor(event, option) {
    const selectButton = event.target.closest(".filter-button");
    selectButton.style.backgroundColor = getButtonColor(option);
}

function createOptionsHTML(options, selectedOption) {
    return options.map(option => `
        <button class="filter-option ${option === selectedOption ? 'selected' : ''}" onclick="changeSelectColor(event, '${option}')" style="background-color: ${getButtonColor(option)}">${option}</button>
    `).join('');
}

function changeSelectColor(event, option) {
    const selectButton = event.target.closest(".filter-button");
    selectButton.style.backgroundColor = getButtonColor(option);

    if (option === 'Hard') {
        selectButton.style.backgroundColor = '#FF6347'; // Change background color to red for "hard"
    }
}

function getButtonColor(option) {
    switch(option) {
        case 'Easy':
            return '#6BB56D'; // Light green
        case 'Medium':
            return '#FFA500'; // Orange
        case 'Hard':
            return '#FF6347'; // Red
        default:
            return '#4CAF50'; // Default green
    }
}


    function formatDate(dateString) {
        const options = { year: "numeric", month: "2-digit", day: "2-digit" };
        const date = new Date(dateString);
        return date.toLocaleDateString("en-US", options);
    }
});
