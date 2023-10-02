import { basename, extname, join } from "path";
import { mkdir, access, rm } from 'fs/promises';
import { fontPipe, FontPipeI } from "font-range";

// == Types ===================================================================
export interface ISubsets<T>{
  (kinds: TSubsetKinds, format: Tformat, fontList: IFontInfo): T
}
export interface IFontInfo {
  family:   FONTFAMILY;
  fontList: string[];
  options:  TFontListOptions;
}

export type Tformat      = "woff" | "woff2"
export type TPathKinds   = "Static" | "Variable";
export type TSubsetKinds = "complete" | "subset" | "split";
export type TFontListOptions = { ext?: "ttf"; variable?: boolean };

// == Constants ===============================================================
const STATIC_PATH          = join(process.cwd(), "fonts", "ttf");
const VARIABLE_PATH        = join(process.cwd(), "fonts", "variable");
const STATIC_OUTPUT_PATH   = join(process.cwd(), "fonts", "webfonts", "static");
const VARIABLE_OUTPUT_PATH = join(process.cwd(), "fonts", "webfonts", "variable");

export enum FONTFAMILY {
  WantedSans     = "WantedSans",
  WantedSansStd  = "WantedSansStd",
};

const FONTWEIGHTS = [
  "Black",
  "Bold",
  "ExtraBlack",
  "ExtraBold",
  "Medium",
  "Regular",
  "SemiBold"
];

// == Functions ===============================================================
export async function clearDir(outDir: string) {
  try {
    await access(outDir);
    await rm(outDir, { recursive: true, force: true });
    await mkdir(outDir);
  } catch(err) {
    await mkdir(outDir, { recursive: true });
  }
}

function getOutInfo(kinds: TSubsetKinds, format: Tformat) {
  switch(kinds) {
    case "complete":   return {
      outType: format,
      outName: "{NAME}{EXT}"
    };
    case "subset":    return {
      outType: format,
      outName: "{NAME}.subset{EXT}"
    };
    case "split":  return {
      outType: format,
      outName: "{NAME}.split.{INDEX}{EXT}"
    };
  }
}

async function createOption(kinds: TSubsetKinds, format: Tformat, fontInfo: IFontInfo) {
  // Get Infos
  const { fontList, options } = fontInfo;

  const pathType = options?.variable  ? "Variable" : "Static";
  const isStatic = pathType === "Static";
  const basePath = isStatic ? STATIC_PATH         : VARIABLE_PATH;
  const fontsPath = isStatic ? STATIC_OUTPUT_PATH : VARIABLE_OUTPUT_PATH

  const { outType,  outName } = getOutInfo(kinds, format);
  const outDir = join(fontsPath, kinds, outType);

  // Clear Files
  await clearDir(outDir);

  // Create Options
  const baseLogFormat  = "Convert {ORIGIN} -> {OUTPUT}";
  const groupLogFormat = `\n== ${kinds} ${outType} ======\n` + baseLogFormat;
  const baseOption     = {
    format: format === "woff" ? "woff-zopfli" : format,
    saveDir: outDir,
    nameFormat: outName
  };
  const fontOptions = fontList.map((fontFile, i) => {
    const logFormat  = i === 0 ? groupLogFormat : baseLogFormat;
    const fontName   = basename(fontFile, extname(fontFile));
    const fontPath   = join(basePath, fontFile);
    const fontOption = {
      fontPath,
      option: {
        ...baseOption,
        logFormat
      }
    } as Required<FontPipeI>;

    if(kinds === "subset") {
      fontOption.option.textFile = join(process.cwd(), "subset_glyphs.txt");
    } 
    
    if(kinds === "split") {
      fontOption.option.cssFile  = join(fontsPath, kinds, fontName + ".css");
    }
    return fontOption;
  });
  return fontOptions;
}

// == Main ====================================================================
export function getFontList(family = FONTFAMILY.WantedSans, options?: TFontListOptions) {
  const { ext = "ttf", variable = false } = options ?? {};

  const extResult = `.${ext}`;
  const fontList  = variable
    ? [ family + "Variable" + extResult ]
    : FONTWEIGHTS.map(weight => family + "-" + weight + extResult);

  return { family, fontList, options };
}

export async function subsets<T>(...subsetList: Parameters<ISubsets<T>>[]) {
  const options = subsetList.map(async (info) => await createOption(...info));

  await fontPipe(
    (await Promise.all(options)).flat()
  );
}
