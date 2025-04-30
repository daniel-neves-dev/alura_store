<div  style="display: flex;">
    <img alt="Logo da empresa Alura" src="https://www.cuponation.com.br/images/fit-in/256x/images/a/alura_logo.png", style = "width:100px;">
    <img class="company-logo__img" src="https://cdn2.gnarususercontent.com.br/1/1221562/b6256fa6-5fde-4cdd-a4a3-d33ebc90bb6c.png" alt="Logo da empresa - Oracle ONE - Br Geral 8">
    <h1>Turma 8</h1>
</div>

# 📈 Stores Sales Analysis

## 🎯 Main goal: data‑driven recommendation on which of four stores should be shold

## 💻 Project Overview
This repository contains the complete workflow used to analyse the performance of four retail stores (Loja 1 – Loja 4) and to recommend which outlet the owner (Sr. João) should sell. The analysis integrates **Python**, **Pandas**, **Matplotlib**, 
**Prettytable** and Google **Colab** otebooks to evaluate sales, revenue, customer ratings and product mix.

## 📋 Objectives
* Consolidate raw CSV sales data for all stores
* Calculate key metrics: revenue, net margin, average freight, customer rating
* Identify best/worst‑selling products and categories per store
* Visualise insights with at least three chart types (bar, pie, scatter/geo‑map)
* Produce a written report recommending the store to be sold (Loja 4)

## 📊 Visualisations
<table>
  <tr>
    <td valign="top"><img src="https://github.com/user-attachments/assets/0bb01e2e-18bb-45b7-988f-6b448a2fdfff"></td>
    <td valign="top"><img src="https://github.com/user-attachments/assets/68791cd7-7345-451a-b211-801d47d3454e"></td>
  </tr>
</table>

<table>
  <tr>
    <td valign="top"><img src="https://github.com/user-attachments/assets/5bae4c9a-bc13-4871-b504-aef4f2496cbd"></td>
    <td valign="top"><img src="https://github.com/user-attachments/assets/24356bc7-8e3d-4dab-b9f3-3d378c089379"></td>
  </tr>
</table>

<table>
  <tr>
    <td valign="top"><img src="https://github.com/user-attachments/assets/590c2fbd-745e-4256-9ad7-6d7ba5100467"></td>
    <td valign="top"><img src="https://github.com/user-attachments/assets/16b857e1-3fae-4f76-a0b8-c4b2fab62485"></td>
  </tr>
</table>



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

[![Open In Colab])]

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

