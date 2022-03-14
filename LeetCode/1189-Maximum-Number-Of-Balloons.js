// 1189. Maximum Number of Balloons
// Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
// You can use each character in text at most once. Return the maximum number of instances that can be formed.

/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    if (text.length < 7) {
        return 0;
    }

    let count = {
        "b": 0,
        "a": 0,
        "l": 0,
        "o": 0,
        "n": 0
    }
    
    for (let i = 0; i < text.length; i++) {
        if (count[text[i]] != undefined) {
            count[text[i]]++;
        }
    }
    return Math.min(count["b"], count["a"], Math.floor(count["l"]/2), Math.floor(count["o"]/2), count["n"]);
};