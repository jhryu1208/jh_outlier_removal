# IQR FOR BOXFLOT
# 하나의 데이터프레임에서 그룹이 2개 이상 존재할 경우 사용

def removeOutlier(df, column):
    df_list = []
    
    for i in set(df['col']):
        X = df[df['col']==i]
        
        q1 = X[column].quantile(0.25)
        q3 = X[column].quantile(0.75)
        
        iqt = 1.5*(q3-q1)
        X[column][(X[column]>(q3+iqt)) | (X[column]<(q1-iqt))] = None
        
        X = X.dropna(axis = 0)
    
        df_list.append(X)
    
    Y = pd.concat(df_list, ignore_index=True)
    
    return (Y)
