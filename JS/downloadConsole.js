var textFile = null,
    makeTextFile = function (text) {
        var data = new Blob([text], { type: 'text/plain' });
        // If we are replacing a previously generated file we need to
        // manually revoke the object URL to avoid memory leaks.
        if (textFile !== null) {
            window.URL.revokeObjectURL(textFile);
        }
        textFile = window.URL.createObjectURL(data);
        // returns a URL you can use as a href
        return textFile;
    };

/** This function will get the textContent from all nodes 
 *  identified by queryString in the DOM and generate 
 *  a new URL with a JSON string of said the text.
 */
function getTextFromQuerySelector(queryString) {
    var textData = document.querySelectorAll(queryString);
    var jsonText = {};
    for (var i = 0; i < textData.length; ++i) {
        jsonText[i] = textData[i].textContent;
    }
    return makeTextFile(JSON.stringify(jsonText));
}
