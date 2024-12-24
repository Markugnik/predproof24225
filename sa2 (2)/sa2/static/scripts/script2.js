
let add_btn = document.querySelector("#add_item_zav");add_btn.addEventListener("click", () => {
    let new_text = document.querySelector("#add_zav").value;
    document.querySelector("#add_zav").value = "";
    let item_list = document.querySelector("#item_list");
    let new_item = document.createElement("div");
    new_item.setAttribute("class", "item");
    let item_info = document.createElement("p");
    item_info.setAttribute("class", "item_info");
    item_info.innerHTML = `${new_text}`;
    let item_btn_delete = document.createElement("button");
    item_btn_delete.setAttribute("id", "item_btn");
    item_btn_delete.innerHTML = "Удалить";
    new_item.appendChild(item_info);
    new_item.appendChild(item_btn_delete);
    item_list.appendChild(new_item);
    item_btn_delete.addEventListener("click", () => {
        let parent = item_btn_delete.parentNode;
        parent.parentNode.removeChild(parent);
    });

    });
