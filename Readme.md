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

Start with `Statistics/mean_median_mode/` for mean, median, and mode. Continue with:

- `Statistics/descriptive_stats.py` — mean, median, range, and standard deviation; compare sample and population formulas.
- `Statistics/percentiles_outliers.py` — quartiles, IQR, and a common outlier flagging rule.
- `Statistics/probability.py` — compare a simulated probability with its theoretical value.
- `Statistics/correlation.py` — calculate a correlation matrix and discuss what correlation can and cannot tell you.

### 5. Interview practice

These examples show common array and table problems, with follow-up questions in comments:

- `numpy/interview_standardize.py` — vectorized column-wise z-scores and the constant-column edge case.
- `numpy/interview_top_k.py` — select the largest values with `argpartition`.
- `pandas/interview_deduplicate.py` — keep the latest record per user and define a tie-breaker.
- `pandas/interview_group_rank.py` — rank values within groups and handle ties at the cutoff.
- `pandas/interview_rolling.py` — calculate time-based rolling totals within each group.

For interview practice, read the prompt in each file, hide or rewrite the solution, and solve it yourself. Then explain the edge cases and trade-offs out loud. Run the example afterward to compare results.

## Going from beginner to advanced

For every example, first run it unchanged, then change the input values and explain the output. Next, combine ideas: load or create data, clean it with pandas, calculate summaries with NumPy/pandas, and visualize those summaries with Matplotlib. Advanced practice ideas include reading a CSV file, comparing groups, handling dates, annotating a chart, and turning repeated steps into functions.

Examples are independent scripts rather than a single application. They use small inline datasets so they work without downloading data.
