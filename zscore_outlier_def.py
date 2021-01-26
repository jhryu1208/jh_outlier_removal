# zscore outlier 제거 함수
def zscoreOutlier(df, column):
    df_list = []
    
    for i in set(df['col']):
        X = df[df['col']==i]
        
        X['zscore'] = np.abs(stats.zscore(X[column]))
        X = X[X['zscore'] < 3]
        
        df_list.append(X)
    
    Y = pd.concat(df_list, ignore_index=True)
    
    return (Y)
