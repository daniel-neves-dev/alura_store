# 📊 Retail Stores Sales Analysis

> Data‑driven recommendation on which of four stores should be divested

---

## 1 – Project Overview
This repository contains the complete workflow used to analyse the performance of four retail stores (Loja 1 – Loja 4) and to recommend which outlet the owner (Sr. João) should sell. The analysis integrates **Python**, **Pandas**, **Matplotlib**, **Geopandas** and Google **Colab** notebooks to evaluate sales, freight, customer ratings and product mix.

## 2 – Objectives
* Consolidate raw CSV sales data for all stores
* Calculate key metrics: revenue, net margin, average freight, customer rating
* Identify best/worst‑selling products and categories per store
* Visualise insights with at least three chart types (bar, pie, scatter/geo‑map)
* Produce a written report recommending the store to be sold (Loja 4)



## 5 – Environment & Installation
```bash
# Clone the repo
$ git clone https://github.com/<user>/retail‑stores‑analysis.git
$ cd retail‑stores‑analysis

# (Option A) Conda – recommended
$ conda env create -f environment.yml
$ conda activate retail‑stores

# (Option B) pip
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
```

### Running the notebooks
* **Locally:** `jupyter lab` then open files in `/notebooks`.
* **Google Colab:** click the badge below to launch in Colab with all dependencies pre‑installed.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<user>/retail‑stores‑analysis/blob/main/notebooks/01_data_clean.ipynb)

## 6 – Key Results
| Metric | Best | Worst |
|--------|------|-------|
| **Revenue** | Loja 1 (R$ 1.53 M) | Loja 4 (R$ 1.38 M) |
| **Net Margin (avg.)** | Loja 1 (R$ 615) | Loja 4 (R$ 556) |
| **Customer Rating** | Loja 3 (4.05★) | Loja 1 (3.98★) |
| **Freight Cost** | Loja 4 (R$ 31) | Loja 1 (R$ 35) |

*Loja 4* under‑performs on revenue and margin despite the lowest freight cost, and shows weak sales in **instrumentos musicais**. Consequently, the final report recommends selling Loja 4.

## 7 – Visualisations
All charts are generated programmatically and saved under `report/figures/`:
* `revenue_by_store.png` – bar chart of gross revenue
* `top_products_per_store.png` – grouped bar chart
* `categories_heatmap.png` – category performance heat‑map
* `stores_map.html` – interactive geo‑map via Geopandas/Folium

## 8 – Reproducibility
The notebook `03_final_report.ipynb` orchestrates the entire pipeline from raw data to PDF. Execute all cells (⯈ Run All) to reproduce numbers and figures.

## 9 – Contributing
Pull requests are welcome! Please open an issue first to discuss major changes.

1. Fork the project
2. Create your feature branch (`git checkout -b feat/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to the branch (`git push origin feat/my-feature`)
5. Open a pull request

## 10 – License
Distributed under the **MIT License** — see `LICENSE` for full text.

