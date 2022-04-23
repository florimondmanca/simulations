# wfa

Procedural generation of a bitmap terrain from a set of tiles and connection rules (_palette_) using the [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) algorithm.

The palette is:

```
🌳 🌿 🐚 🌊
```

Which reads as:

* Trees may be next to grass
* Grass may be next to trees, or sand (represented by a shell - there's no sand emoji!)
* Sand may be next to grass, or sea.
* Sea may be next to sand.

## Requirements

- Python 3.10+

## Quickstart

```
python main.py
```

## Example output

_Output changes at every run._

```
🌿 🐚 🌊 🌊 🐚 🐚 🐚 🐚 🌿 🌿 🌿 🐚 🌊 🐚 🐚 🌊 🐚 🌿 🐚 🐚 🐚 🐚 🌊 🌊 🐚 
🐚 🐚 🐚 🐚 🌿 🐚 🌿 🌿 🌳 🌿 🐚 🌊 🐚 🌿 🐚 🌊 🐚 🌿 🐚 🐚 🌊 🌊 🌊 🐚 🐚 
🐚 🐚 🌿 🌿 🌿 🌿 🌳 🌿 🌿 🐚 🐚 🐚 🌿 🐚 🌿 🐚 🐚 🐚 🌿 🐚 🌊 🌊 🌊 🐚 🌿 
🐚 🌿 🌿 🌳 🌿 🌳 🌳 🌳 🌿 🌿 🌿 🌿 🌿 🐚 🐚 🌊 🐚 🐚 🐚 🌿 🐚 🐚 🐚 🌿 🌿 
🌿 🐚 🌿 🌳 🌿 🌳 🌿 🌳 🌳 🌳 🌳 🌿 🌳 🌿 🐚 🐚 🐚 🌊 🐚 🐚 🌊 🌊 🐚 🌿 🌿 
🌿 🌿 🐚 🌿 🌿 🌳 🌳 🌳 🌿 🌳 🌳 🌳 🌳 🌿 🐚 🌊 🌊 🌊 🐚 🐚 🌊 🌊 🐚 🌿 🌳 
🌿 🌳 🌿 🌳 🌳 🌳 🌳 🌳 🌿 🌿 🌳 🌳 🌳 🌳 🌿 🐚 🐚 🐚 🌊 🐚 🌊 🐚 🌿 🌿 🌳 
🌳 🌳 🌳 🌿 🌳 🌿 🌳 🌿 🌿 🐚 🌿 🌳 🌳 🌿 🌿 🐚 🌊 🐚 🌊 🌊 🐚 🌊 🐚 🌿 🌳 
🌿 🌳 🌿 🌳 🌳 🌳 🌿 🐚 🌿 🐚 🌿 🌿 🌿 🌿 🐚 🐚 🌊 🌊 🐚 🐚 🌊 🌊 🐚 🌿 🌳 
🌳 🌳 🌳 🌳 🌿 🌳 🌳 🌿 🌿 🐚 🐚 🐚 🐚 🐚 🐚 🌊 🌊 🐚 🐚 🌊 🐚 🌊 🐚 🌿 🌳 
🌳 🌳 🌿 🌿 🌿 🌳 🌿 🐚 🐚 🐚 🐚 🌿 🐚 🌊 🌊 🌊 🌊 🐚 🌊 🐚 🐚 🐚 🌿 🌿 🌳 
🌳 🌿 🌳 🌳 🌿 🌳 🌿 🐚 🌿 🌿 🐚 🐚 🌿 🐚 🐚 🌊 🐚 🐚 🐚 🌊 🌊 🐚 🌿 🌿 🌳 
🌿 🌿 🌳 🌳 🌳 🌿 🌿 🐚 🌿 🌿 🌿 🌿 🐚 🐚 🌿 🐚 🌊 🐚 🌊 🐚 🌊 🐚 🐚 🌿 🌳 
🌳 🌳 🌳 🌳 🌿 🐚 🐚 🐚 🌿 🌿 🌿 🐚 🌿 🐚 🌿 🐚 🌊 🌊 🌊 🐚 🐚 🌊 🐚 🌿 🌿 
🌳 🌳 🌳 🌿 🌿 🌿 🐚 🌊 🐚 🐚 🐚 🌿 🌳 🌿 🌿 🌿 🐚 🌊 🐚 🌿 🐚 🐚 🐚 🐚 🐚 
🌳 🌿 🌿 🐚 🐚 🐚 🌊 🌊 🌊 🐚 🐚 🌿 🌿 🐚 🐚 🐚 🐚 🌊 🌊 🐚 🌊 🌊 🌊 🌊 🌊 
🌿 🐚 🌿 🌿 🐚 🐚 🌊 🐚 🐚 🐚 🌿 🌿 🐚 🌊 🌊 🐚 🌊 🌊 🐚 🐚 🐚 🐚 🌊 🐚 🐚 
🌿 🐚 🐚 🌿 🌿 🐚 🐚 🌿 🐚 🐚 🌿 🐚 🌿 🐚 🌊 🌊 🌊 🌊 🌊 🐚 🐚 🌊 🌊 🌊 🌊 
🐚 🐚 🌊 🐚 🌿 🌿 🐚 🐚 🐚 🌿 🌿 🐚 🐚 🐚 🌊 🌊 🐚 🐚 🐚 🌿 🌿 🐚 🌊 🐚 🐚 
🌊 🌊 🌊 🐚 🌿 🐚 🐚 🌿 🌿 🌿 🐚 🌊 🌊 🌊 🌊 🐚 🌿 🌿 🌿 🌳 🌿 🌿 🐚 🌿 🐚 
🌊 🌊 🐚 🐚 🐚 🌿 🐚 🌿 🌳 🌿 🐚 🌊 🌊 🐚 🐚 🌿 🌳 🌳 🌿 🌿 🌳 🌿 🐚 🌿 🌿 
🐚 🌊 🐚 🌿 🌿 🌿 🌿 🌿 🌳 🌳 🌿 🐚 🐚 🐚 🐚 🐚 🌿 🌿 🌿 🌿 🌿 🌿 🐚 🌿 🌳 
🐚 🌊 🌊 🐚 🌿 🌳 🌿 🌳 🌿 🌿 🐚 🐚 🌿 🐚 🌊 🐚 🌿 🐚 🌿 🌿 🌳 🌿 🐚 🐚 🌿 
🐚 🌊 🐚 🌿 🌳 🌿 🌿 🌿 🌳 🌳 🌿 🌿 🐚 🐚 🌊 🐚 🌿 🐚 🐚 🌿 🌿 🌳 🌿 🌿 🐚 
🐚 🐚 🐚 🌿 🌳 🌿 🌳 🌳 🌿 🌳 🌳 🌳 🌿 🌿 🐚 🌊 🐚 🌿 🐚 🌿 🌳 🌳 🌿 🐚 🌊
```

## Possible improvements

- Make width and height configurable via the command line
- Add weights to adjust proportions of sea and land
- Make palette configurable using a text file of emojis
- Move from emojis to NxN pixel tiles

## Credits

- [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse), mxgmn, visited 2022-04-23
- [Why I'm Using Wave Function Collapse for Procedural Terrain](https://www.youtube.com/watch?v=20KHNA9jTsE), DV Gen, 2022-04-10
- [Superpositions, Sudoku, the Wave Functions Collapse algorithm](https://www.youtube.com/watch?v=2SuvO4Gi7uY), Martin Donald, 2020-07-31
