# recommendations/views.py
from django.shortcuts import render
import pandas as pd
import sys
from sklearn.metrics.pairwise import euclidean_distances
from .models import Tshirt
from .forms import RecommendForm
print(sys.executable)
def recommend_tshirts(request):
    if request.method == 'POST':
        form = RecommendForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            
            # Get all Tshirt data
            df = pd.read_excel(r'S:\21CS62\recommender_project\dataset.xlsx')

            
            # Calculate distances
            df['distance'] = euclidean_distances(df[['height', 'weight']], [[height, weight]])
            
            # Sort by distance and get top 5 recommendations
            recommendations = df.sort_values(by='distance').head(5)
            
            return render(request, 'recommendations/recommend_tshirts.html', {'form': form, 'recommendations': recommendations.to_dict('records')})
    else:
        form = RecommendForm()
    
    return render(request, 'recommendations/recommend_tshirts.html', {'form': form})
