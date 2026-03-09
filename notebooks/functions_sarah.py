def clean_hhi(df_hhi):
     #make all column names lower case
    df_hhi.columns = df_hhi.columns.str.lower()




def clean_hhi2(df_hhi2):
    #make all column names lower case
    df_hhi2.columns = df_hhi2.columns.str.lower()
    #drop columns
    df_hhi2 = df_hhi2.drop(['ref_area', '2012', '2013'], axis=1)
    #filter GBR countries
    filtered_ref_area_label = df_hhi2.loc[df_hhi2['ref_area_label'].isin(['Australia', 'Papua New Guinea'])]
    df_hhi2_gbr = filtered_ref_area_label
    return df_hhi2_gbr

df_hhi2_gbr = clean_hhi2(df_hhi2)

def plot_line_chart(df, title='Scores by Area and Year'):
    # Extract unique areas and years (assuming consistent DataFrame structure)
    areas = df['ref_area_label'].unique()
    categories = df.columns[1:].tolist()  # Years from 2014 to 2024

    # Create a plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot each area
    for area in areas:
        # Extract values for the current area
        values = df[df['ref_area_label'] == area].iloc[0, 1:].values.astype(float)
        x = np.arange(len(categories))
        
        # Plot the line
        ax.plot(x, values, marker='o', label=area)
        
        # Annotate each point with its value
        for i, val in enumerate(values):
            ax.text(i, val, f'{val:.2f}', ha='center', va='bottom')

    # Label plot
    ax.set_xlabel('Year')
    ax.set_ylabel('Scores')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.grid(True)

    # Adjust layout to fit
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Call the function using df_hhi2_gbr
plot_line_chart(df_hhi2_gbr)