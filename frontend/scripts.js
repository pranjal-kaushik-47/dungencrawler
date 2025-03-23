let items = {}
async function loadItems() {
    try {
        const res = await fetch('http://127.0.0.1:5500/data/items.json');
        items = await res.json();
    } catch (error) {
        console.error("----", error)
    }
}
loadItems()
let availableActions = {}
function message(message) {
    document.getElementById("outcome-ta").value = message + "\n";
}
function pickItem(item) {
    console.log(availableActions, availableActions[item.id] || 0);
    if (item.maxEquipable === undefined || (availableActions[item.id] || 0) < item.maxEquipable)
    {
        const table = document.getElementById("invTable")
        const row = document.createElement("tr")
        const name = document.createElement("td")
        const description = document.createElement("td")
        const use = document.createElement("td")
        name.innerText = item.name
        description.innerText = item.description
        const useButton = document.createElement("button")
        useButton.innerText = "Use"
        useButton.id = "action-" + item.id
        useButton.addEventListener("click", function(event) {
            useItem(item);
        })
        use.appendChild(useButton)
        row.appendChild(name)
        row.appendChild(description)
        row.appendChild(use)
        let added = false
        for (let i = 0; i < table.rows.length; i++) {
            if (table.rows[i].innerText[0] === '-'){
                table.rows[i].replaceWith(row);
                added = true
                break;
            }
        }
        if (!added){
            table.appendChild(row)
        }
        message(item.outcome);
        availableActions[item.id] = (availableActions[item.id] || 0) + 1;
        document.getElementById("action-"+item.id).remove();   
    } else {
        message("Sorry cant have more of that...I'm talking it back.");
        document.getElementById("action-"+item.id).remove(); 
    }
}
function hurt(amount) {
    const totalHealth = document.getElementById("health").offsetWidth;
    const currentHealth = document.getElementById("healthbar").offsetWidth;
    const updatedHealth = Math.min(currentHealth - (amount * totalHealth), totalHealth);
    document.getElementById("healthbar").style.width = updatedHealth + "px";

}
function useItem(item) {
    console.log(item.id);
    message(item.actionComment);
    if (item.id === "selfHarm")
    {
        document.getElementById("action-"+item.id).remove();
        hurt(item.damage*-1);
    }
    else if (item.id === "legs")
    {
        document.getElementById("move-forward").disabled = false;
        document.getElementById("move-backward").disabled = false;
        document.getElementById("move-left").disabled = false;
        document.getElementById("move-right").disabled = false;
        document.getElementById("action-" + item.id).disabled = true;
    }

    if (availableActions[item.id] !== undefined && availableActions[item.id] > 0)
    {
        availableActions[item.id] = availableActions[item.id] - 1;
    }
}
document.getElementById("all-actions").addEventListener("click", function(event) {
    if (event.target.matches("[id^='action-']")) {
        document.getElementById("outcome-ta").value = '';
        const action = event.target.id.split("-")[1];
        if (action === "spawn"){
            console.log(availableActions);
            const allItems = document.getElementById("all-actions");
            const newItem = Object.keys(items)[Math.floor(Math.random() * Object.keys(items).length)];
            const item = items[newItem];
            const newButton = document.createElement("button");
            newButton.id = "action-" + item.id;
            newButton.className = "item-button";
            newButton.innerHTML = item.name;
            allItems.appendChild(newButton);
            message("You spawn a " + item.name);
        } else {
            const item = items[action];
            if (item.trigger){
                useItem(item);
            } else {
                pickItem(item);
            }
            
        }
    }
});
document.getElementById("move-forward").addEventListener("click", function(event) {
    message("You move forward.");
});
document.getElementById("move-backward").addEventListener("click", function(event) {
    message("You move backward.");
});
document.getElementById("move-left").addEventListener("click", function(event) {
    message("You move left.");
});
document.getElementById("move-right").addEventListener("click", function(event) {
    message("You move right.");
});