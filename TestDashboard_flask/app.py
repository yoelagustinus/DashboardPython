from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# Contoh data Anda
data = {
    'Date': ['01 Jan 2023', '02 Jan 2023', '03 Jan 2023', '01 Jan 2023', '02 Jan 2023', '03 Jan 2023', '01 Jan 2023', '02 Jan 2023', '03 Jan 2023', '01 Jan 2023', '02 Jan 2023', '03 Jan 2023'],
    'Netsales': [10000, 20000, 25000, 5000, 10000, 15000, 70000, 30000, 35000, 20000, 10000, 45000],
    'Brand': ['Brand A', 'Brand A', 'Brand A', 'Brand B', 'Brand B', 'Brand B', 'Brand A', 'Brand A', 'Brand A','Brand B', 'Brand B', 'Brand B'],
    'Store': ['Store 1', 'Store 1', 'Store 1', 'Store 1', 'Store 1', 'Store 1', 'Store 2', 'Store 2', 'Store 2','Store 2', 'Store 2', 'Store 2']
}

# Ubah data menjadi DataFrame
df = pd.DataFrame(data)

@app.route('/')
def index():
    # Mengubah format tanggal ke datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Membuat line chart dengan Plotly Express
    fig = px.line(df, x='Date', y='Netsales', color='Brand', facet_col='Store', markers=True, title='Line Chart Netsales per Brand per Store')
    fig.update_traces(line=dict(dash="dot"))  # Menambahkan pola garis (dapat disesuaikan)

    # Menambahkan judul sumbu X dan Y
    fig.update_layout(xaxis_title='Date', yaxis_title='Netsales')

    # Menampilkan legenda di luar grafik
    fig.update_layout(legend=dict(x=1.05, y=0.5))

    # Menyesuaikan tampilan subplot
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    
    # Ubah plot menjadi JSON
    chart_json = fig.to_json()

    return render_template('index.html', chart_json=chart_json)

if __name__ == '__main__':
    app.run(debug=True)
