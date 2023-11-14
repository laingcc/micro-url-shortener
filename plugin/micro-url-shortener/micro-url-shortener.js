//Add the context menu item

browser.contextMenus.create({
    id: "micro-url-shortener",
    title: "Shorten URL",
    contexts: ["all"]
}, () => {console.log("lmao")});