let add_btn = document.querySelector("#add_item_btn");add_btn.addEventListener("click", () => {
    let new_text = document.querySelector("#add_item_name").value;
    document.querySelector("#add_item_name").value = "";
    let new_kol = document.querySelector("#add_item_kol").value;
    document.querySelector("#add_item_kol").value = "";
    let item_list = document.querySelector("#item_list");
    let quality = document.createElement('div');
    quality.setAttribute("class", "quality");
    let new_item = document.createElement("div");
    new_item.setAttribute("class", "item");
    let item_info = document.createElement("p");
    item_info.setAttribute("class", "item_info");
    item_info.innerHTML = `${new_text} , ${new_kol}`;
    let item_btn_delete = document.createElement("button");
    item_btn_delete.setAttribute("id", "item_btn");
    item_btn_delete.innerHTML = "Удалить";
    item_btn_delete.innerHTML = "Удалить";
    let item_btn_edit = document.createElement("button");
    item_btn_edit.innerHTML = "Редактировать";
    new_item.appendChild(item_info);
    new_item.appendChild(item_btn_edit);
    new_item.appendChild(item_btn_delete);
    item_list.appendChild(new_item);
    item_btn_delete.addEventListener("click", () => {
        let parent = item_btn_delete.parentNode;
        parent.parentNode.removeChild(parent);
    });
    item_btn_edit.addEventListener("click", () => {
        quality.style.display = "flex";
        let new_name = prompt("Введите новое название:", new_text);
        let new_koli = prompt("Введите новое количество:", new_kol);
        let new_quality = prompt("Введите новое состояние:", quality);


        if (new_name !== null && new_koli !== null && new_quality !== null) {
            new_text = new_name;
            new_kol = new_koli;
            quality = new_quality;
            item_info.innerHTML = `${new_text}, ${new_kol}, ${new_quality}`;
        };
    });
});