# bibref
BibTeX reference formatter

Given a file with BibTeX style refernces that inculde `author`, `title` and `year` e.g. from Google Scholar:

```
@inproceedings{nair2010rectified,
  title={Rectified linear units improve restricted boltzmann machines},
  author={Nair, Vinod and Hinton, Geoffrey E},
  booktitle={Proceedings of the 27th international conference on machine learning (ICML-10)},
  pages={807--814},
  year={2010}
}
```

this script  will reformat to the more verbose title for easier lookup:

```
@inproceedings{nair-2010-rectified-linear-units-improve-restricted-boltzmann-machines,
title={Rectified linear units improve restricted boltzmann machines},
author={Nair, Vinod and Hinton, Geoffrey E},
booktitle={Proceedings of the 27th international conference on machine learning (ICML-10)},
pages={807--814},
year={2010}
}
```

## Usage

```
python reformat.py ref.bib
```

To copy output to clipboard on Unix, use:

```
python reformat.py ref.bib | xclip -selection c
```