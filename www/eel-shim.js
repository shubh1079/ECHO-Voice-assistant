(function () {
    if (window.eel) {
        return;
    }

    function returner() {
        return Promise.resolve();
    }

    function callable() {
        return returner;
    }

    var shim = new Proxy({}, {
        get: function (_target, prop) {
            if (prop === "expose") {
                return function () { };
            }
            if (prop === "playAssistantSound") {
                return function () { };
            }
            if (prop === "allCommands") {
                return function () {
                    try {
                        var msg = arguments && arguments[0] ? String(arguments[0]) : "";
                        var evt = new CustomEvent("eel-demo-message", { detail: msg });
                        window.dispatchEvent(evt);
                    } catch (e) { }
                    return returner;
                };
            }
            return callable;
        }
    });

    window.eel = shim;
})();


