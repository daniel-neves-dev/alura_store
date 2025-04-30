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

# ✏️ Conclusion
## 1. Revenue analysis
* Store 1 leads in both gross and net revenue.  
* Store 4 shows **the worst performance** in both respects.

## 2. Sales analysis by category and product
* Category with the highest number of sales: <strong>furniture</strong>, with Store 3 standing out.  
* Category with the worst sales performance: <strong>housewares</strong> in Stores 1 and 2 and <strong>musical instruments</strong> in Stores 3 and 4—Store 4 showing **the poorest performance** overall.

## 3. Customer experience analysis
* Store 3 ranks highest in customer satisfaction.  
* Store 1 has the lowest rating; however, it yields the greatest profit, indicating that improvements in logistics and after-sales service **could** raise its evaluation.

## 4. Shipping cost analysis
* Store 4 has the lowest shipping cost, but this is not reflected in higher profit or greater customer satisfaction.  
* Store 1 has the highest shipping cost, yet **is** the store that generates the most profit.

## SUMMARY
* **Store 1** – <strong>strengths:</strong> highest revenue. <strong>weaknesses:</strong> most expensive shipping and lowest customer-satisfaction score.  
* **Store 2** – <strong>strengths:</strong> good rating and solid revenue. <strong>weaknesses:</strong> slow inventory turnover of the “board game” item.  
* **Store 3** – <strong>strengths:</strong> best rating and good revenue. <strong>weaknesses:</strong> revenue slightly below Stores 1 and 2.  
* **Store 4** – <strong>strengths:</strong> cheapest shipping. <strong>weaknesses:</strong> lowest revenue, slow sales of musical instruments, and average rating.

## Sales recommendation
### <em>Store 4</em>
Store 4 displays **inferior** financial performance compared with the others, slow inventory turnover in musical instruments, and—despite its lower shipping cost—this **does not translate** into greater customer satisfaction.



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

