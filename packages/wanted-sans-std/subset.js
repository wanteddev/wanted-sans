const { FONTFAMILY, getFontList, subsets } = require("subset-utils");

const fontList = getFontList(FONTFAMILY.WantedSansStd);
const variable = getFontList(FONTFAMILY.WantedSansStd, { variable: true });

subsets(
    // Wanted Sans Std woff2
    ["complete", "woff2", fontList],
    ["split", "woff2", fontList],

    // Wanted Sans Std Variable
    ["complete", "woff2", variable],
    ["split", "woff2", variable]
);
