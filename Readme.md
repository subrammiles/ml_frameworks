# Learn Python data frameworks

A collection of small, runnable examples for learning NumPy, pandas, and Matplotlib, from first steps to more advanced workflows. Examples use familiar data and are intended to be read and changed.

## Setup

Use Python 3. Install the libraries used by the examples:

```bash
python -m pip install numpy pandas matplotlib
```

Run a file from the repository root, for example:

```bash
python numpy/basic/Dimensions.py
python pandas/cleaning.py
```

Matplotlib examples open a window; close it to finish the program. Some scripts print generated random data, so their output can differ each run.

## Learning path

### 1. NumPy: arrays and vectorized operations

Start with `numpy/basic/Dimensions.py`, `numpy/basic/Add1ToEachElementInAnArray.py`, and `numpy/basic/PythonVsNumpy.py`. Then continue:

- `numpy/indexing.py` — select, slice, and update array values.
- `numpy/boolean_masks.py` — filter data using conditions.
- `numpy/reshaping.py` — reshape, combine, and split arrays.
- `numpy/statistics.py` — axis-based summaries and missing values.

### 2. pandas: tabular data

Start with `pandas/basic.py` and `pandas/plot.py`. Then continue:

- `pandas/selection.py` — inspect, select, and sort rows and columns.
- `pandas/cleaning.py` — handle missing values and duplicates.
- `pandas/groupby.py` — group, aggregate, and pivot data.
- `pandas/merge.py` — join tables and parse dates.

### 3. Matplotlib: communicate results

Explore the existing scripts in `matplotlib/`, then try:

- `matplotlib/customize.py` — titles, axes, legends, and layout.
- `matplotlib/multiple_series.py` — compare groups and add error bars.

### 4. Statistics foundations

The `Statistics/mean_median_mode/` folder introduces mean, median, and mode. Try changing the sample values and predicting the result before running each script.

## Going from beginner to advanced

For every example, first run it unchanged, then change the input values and explain the output. Next, combine ideas: load or create data, clean it with pandas, calculate summaries with NumPy/pandas, and visualize those summaries with Matplotlib. Advanced practice ideas include reading a CSV file, comparing groups, handling dates, annotating a chart, and turning repeated steps into functions.

Examples are independent scripts rather than a single application. They use small inline datasets so they work without downloading data.
