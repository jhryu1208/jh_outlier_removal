# zscore outlier 제거 함수
# 하나의 데이터프레임에서 그룹이 2개 이상 존재할 경우 사용

def zscoreOutlier(df, column):
    df_list = []
    
    for i in set(df['col']):
        X = df[df['col']==i]
        
        X['zscore'] = np.abs(stats.zscore(X[column]))
        X = X[X['zscore'] < 3]
        
        df_list.append(X)
    
    Y = pd.concat(df_list, ignore_index=True)
    
    return (Y)
