const { FONTFAMILY, getFontList, subsets } = require("subset-utils");

const fontList = getFontList(FONTFAMILY.WantedSans);
const variable = getFontList(FONTFAMILY.WantedSans, { variable: true });

subsets(
    // Wanted Sans woff2
    ["complete", "woff2", fontList],
    ["split", "woff2", fontList],

    // Wanted Sans Variable
    ["complete", "woff2", variable],
    ["split", "woff2", variable]
);
