from scipy import stats
from sympy import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import geopandas as gpd
import warnings
import haversine as hs
import shapely
from sklearn.preprocessing import normalize
import datetime
from pandasql import sqldf
import math

def convert_datatype(df, lista_columnas):
    for column in lista_columnas:
        df[column] = df[column].str.replace(",", ".").astype(float)
    return df

def mapear_vacios(row, column):
    if pd.isna(row[column])==True:
        return 'Sin información'
    else:
        return row[column]

def normalize_rows(df):
    return df.pipe(lambda x: pd.DataFrame(normalize(df, axis=1, norm='l1'), columns=df.columns, index=df.index))

def age_cohorts(row, age_column):
    if row[age_column] < 18:
        return '<18'
    elif row[age_column] <=29 and row[age_column] > 18:
        return '18-29'
    elif row[age_column] <=60 and row[age_column] > 29:
        return '30-60'
    elif row[age_column] > 60 and row[age_column] < 100:
        return '>60'
    else:
        return 'No declarado'

def publico_privado(row, column, publico, privado):
    if row[column] in (publico):
        return 'Público'
    elif row[column] in (privado):
        return 'Privado'
    else:
        return 'Otro'

def manhattan_distance(a, b):
    return np.abs(a - b).sum()

def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

def weighted_mean(df, value_column, weighs_column):
    weighted_sum = (df[value_column] * df[weighs_column]).sum()
    return weighted_sum / df[weighs_column].sum()

def weighted_median(df, val, weight):
    df_sorted = df.sort_values(val)
    cumsum = df_sorted[weight].cumsum()
    cutoff = df_sorted[weight].sum() / 2.
    return df_sorted[cumsum >= cutoff][val].iloc[0]

from pandasql import sqldf
def calculate_n_viajes_per_capita(df, df_str, agg_columns_str, agg_columns_lst, id_person, person_weight, trip_weight=None):
    q = "SELECT DISTINCT {}, {}, {} FROM {}".format(id_person, agg_columns_str, person_weight, df_str)
    persons = sqldf(q, globals())
    n_personas = persons.groupby(agg_columns_lst).sum()[[person_weight]].reset_index()
    n_personas[agg_columns_lst[0]] = n_personas[agg_columns_lst[0]].astype(str)
    n_viajes = df.groupby(agg_columns_lst).sum()[[trip_weight]].reset_index()
    n_viajes[agg_columns_lst[0]] = n_viajes[agg_columns_lst[0]].astype(str)
    merged = pd.merge(n_personas, n_viajes, on=agg_columns_lst, how='left')
    merged['viajes_per_capita'] = merged[trip_weight] / merged[person_weight]
    return merged

x, y = symbols('x y')
def plot_lmplot(df, hue=None, col=None, col_wrap=None, col_order=None,filename=None):
    
    ax = sns.lmplot(data=df, x="n_viajes", y="tiempo_total", hue=hue, 
                    col=col, col_wrap=col_wrap, col_order=col_order, 
                    aspect=1.5, height=4,  line_kws={'color': 'blue'},
                    scatter_kws={'color': 'grey', 'alpha':0.2}, sharex=False)
    
    
    
    def annotate(data, **kws):
        ax = plt.gca()
        slope, intercept, r_value, p_value, std_err = stats.linregress(data['n_viajes'],data['tiempo_total'])
        median = data.tiempo_total.median()
        max_value_x= data.n_viajes.max()
        max_value_y= data.tiempo_total.max()
        plt.axhline(y=median, c='red')
    
        interception = linsolve([slope*x+intercept-y, median-y ], (x, y))
        (x0, y0) = next(iter(interception))
        plt.axvline(x=x0, c='green')
        #ax.map(plt.vlines, x=x0, ymin=median, ymax=max_value_y, color='black', marker='-')
        
        ax.text(0.7, .9, 'slope={:.6f}, intercept={:.6g}'.format(slope, intercept, r_value, p_value, std_err),
            transform=ax.transAxes)
        ax.text(13,median+4,'Median', color='red')
        
    ax.map_dataframe(annotate)
    ax.set(xlim=(0,15))
    ax.set_titles("{col_name}")
    #ax.fig.suptitle(hue)
    #ax.fig.subplots_adjust(top=0.9)
    ax.set_axis_labels(x_var="# de Viajes", y_var="Tiempo promedio de viaje")
    if filename:
        ax.savefig(filename)
    sns.despine()


def generate_groups(df):
    # Generating interception points
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['n_viajes'],df['tiempo_total']) # linear equation
    median = df.tiempo_total.median() # time median
    max_value_x= df.n_viajes.max() # max trip number
    min_value_x= df.n_viajes.min() # max trip number
    max_value_y= df.tiempo_total.max() # max time
    min_value_y= df.tiempo_total.min() # max time
    interception = linsolve([slope*x+intercept-y, median-y ], (x, y))
    (x0, y0) = next(iter(interception)) # interception median time and trip number
    
    #interception points
    x_points=[]
    y_points=[]
    for x_point in range(1,max_value_x+1):
        interception_2 = linsolve([slope*x+intercept-y, x_point-x ], (x, y))
        (x1, y1) = next(iter(interception_2)) # interception points
        x_points.append(x1)
        y_points.append(y1)
    if x0 > 0:    
        #B2
        print('Generando grupo B2...')
        b2 = df[(df.tiempo_total >= y0) & (df.n_viajes >= x0)].assign(group='b2')

        #B1
        print('Generando grupo B1...')
        b1 = pd.DataFrame()
        for i in range(int(x0)+1,len(x_points)):
            temp = df[(df.tiempo_total < median) & (df.tiempo_total>=y_points[i-1]) & (df.n_viajes>=x_points[i-1]) & (df.n_viajes< x_points[i])]
            b1 = pd.concat([b1, temp], axis=0)
        b1 = b1.assign(group='b1')

        #A1
        print('Generando grupo A1...')
        a1 = pd.DataFrame()
        for i in range(int(x0)+1,len(x_points)):
            temp = df[(df.tiempo_total<y_points[i-1]) & (df.n_viajes>=x_points[i-1]) & (df.n_viajes< x_points[i])]
            a1 = pd.concat([a1, temp], axis=0)
        a1 = a1.assign(group='a1')

        #A2
        print('Generando grupo A2...')
        a2 = df[(df.n_viajes > 1) & (df.n_viajes < x0) & (df.tiempo_total < y0) & (df.tiempo_total >= 0)].assign(group='a2')

        #A3
        print('Generando grupo A3...')
        a3 = pd.DataFrame()
        for i in range(1,int(x0)+1):
            temp = df[(df.tiempo_total >= median) & (df.tiempo_total<y_points[i-1]) & (df.n_viajes>1) & (df.n_viajes>=x_points[i-1]) & (df.n_viajes< x_points[i])]
            a3 = pd.concat([a3, temp], axis=0)
        a3 = a3.assign(group='a3')

        #B3
        print('Generando grupo B3...')
        b3 = pd.DataFrame()
        for i in range(1,int(x0)+1):
            temp = df[(df.tiempo_total>=y_points[i-1]) & (df.n_viajes>1) & (df.n_viajes>=x_points[i-1]) & (df.n_viajes< x_points[i])]
            b3 = pd.concat([b3, temp], axis=0)
        b3 = b3.assign(group='b3')

        #C
        print('Generando grupo C...')
        c = df[(df.tiempo_total < y_points[0]) & (df.n_viajes == 1)].assign(group='c')

        #D
        print('Generando grupo D...')
        d = df[(df.tiempo_total >= y_points[0]) & (df.n_viajes == 1)].assign(group='d')

        return pd.concat([b2,b1,a1,a2,a3,b3,c,d], axis=0)

def calculate_size_1p(df, group_n, fe):
    return df[df['group']==group_n][fe].sum()

def calculate_indicators(df, fe):
    pop_total = df[fe].sum()
    print('Tamaño población: {}'.format(pop_total))
    m = (calculate_size_1p(df, 'a1', fe) + calculate_size_1p(df, 'a2', fe) + calculate_size_1p(df, 'a3', fe)) / pop_total
    m1 = (calculate_size_1p(df, 'a1', fe)) / pop_total
    m2 = (calculate_size_1p(df, 'a2', fe) + calculate_size_1p(df, 'a3', fe)) / pop_total
    m3 = (calculate_size_1p(df, 'b3', fe)) / pop_total
    m4 = (calculate_size_1p(df, 'b1', fe)) / pop_total
    m5 = (calculate_size_1p(df, 'b2', fe)) / pop_total
    m6 = (calculate_size_1p(df, 'c', fe)) / pop_total
    m7 = (calculate_size_1p(df, 'd', fe)) / pop_total
    m8 = (calculate_size_1p(df, 'c', fe) + calculate_size_1p(df, 'd', fe)) / pop_total
    m9 = df[df.tiempo_total <= 15][fe].sum() / pop_total
    m10 = df[df.n_viajes == 2][fe].sum() / pop_total
    
    data = {'Medida': ['(A1+A2+A3)/P', 'A1/P', '(A2+A3)/P', 'B3/P',
                       'B1/P', 'B2/P', 'C/P', 'D/P', '(C+D)/P', '<=15 min', '2 viajes diarios'],
           'Valor':[m, m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]}
    
    return pd.DataFrame(data)   