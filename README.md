# Augmented reality (AR) visualization pipeline
This repo has been forked from [Soft Tissue Biomechanics Lab](https://github.com/SoftTissueBiomechanicsLab/AR_Pipeline/)

## Software Requirements
* To create augmented reality (AR) models you will require the following packages:
  * [ParaView 5.10](https://www.paraview.org/download/)
  * [Blender 2.83](https://download.blender.org/release/)
  * [BlenderUSDZ addon](https://github.com/robmcrosby/BlenderUSDZ/tree/e8a002849b85df3daba339912f4cc91fb042fe6d) 
  * [MacOS users: Apple Reality Converter](https://developer.apple.com/augmented-reality/tools/)
  * [Windows/Unix users: Apple usdzconvert utility](https://github.com/tappi287/usdzconvert_windows)
* To host and render the AR models you will need to include  the [model-viewer](https://modelviewer.dev/) API within your webpage. 

## File Description
We provide '.ply' files of results from Fluent simulations. The '.ply', '.glb' and '.usdz' files are located within this repo and essential for the AR models corresponding to these results. 

## References
If you find this repository useful for your research, please cite the following work:
```
@article{Mathur2023AR,
author = {Mathur, Mrudang and Brozovich, Josef M. and Rausch, Manuel K.},
doi = {10.1016/j.finel.2022.103851},
issn = {0168874X},
journal = {Finite Elements in Analysis and Design},
number = {September 2022},
publisher = {Elsevier B.V.},
title = {{A brief note on building augmented reality models for scientific visualization}},
volume = {213},
year = {2023}
}

```

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg