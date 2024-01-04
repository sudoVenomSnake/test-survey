import streamlit as st

st.set_page_config(layout = "wide")

st.title("Alcohol Consumer Survey")

st.radio("How often do you come across new whiskey brands?", options = ["Rarely", "Sometimes", "Often", "Always"])
st.multiselect(label = "What are the primary sources of discovering new whiskey brands? (Rank them according to order)", options = ["Word of mouth", "Social Media", "Internet searches", "Events/Tastings", "Point-of-Sale displays"])
st.multiselect(label = "What factors influence you to consider trying a new whiskey brand? (Rank them according to order)", options = ["Price", "Brand reputation", "Flavor profile", "Packaging/Label design", "Recommendations/reviews"])
st.radio(label = "Where do you usually buy new whiskey brands you're trying out?", options = ["Store", "Online", "Duty Free Shops"])
st.radio(label = "How often do you purchase new whiskey brands for trial?", options = ["Monthly", "Quarterly", "Semi-annually", "Annually"])
st.multiselect(label = "What factors enhance your enjoyment of a whiskey? (Rank them according to order)", options = ["Taste", "Price", "Brand reputation", "Accompanying food", "Atmosphere/company"])
st.multiselect(label = "What would make you become a loyal customer of a whiskey brand? (Rank them according to order)", options = ["Consistent quality", "Price", "Wide availability", "Variety of flavors/styles", "Company values"])
st.radio(label = "Would you recommend a new whiskey brand you particularly enjoyed to others?", options = ["Yes", "No"])
st.multiselect(label = "What channels would you use to recommend this brand? (Rank them according to order)", options = ["Word of mouth", "Social Media", "Writing a review", "Gifting the whiskey"])