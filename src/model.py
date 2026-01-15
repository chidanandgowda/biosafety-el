import pandas as pd
import numpy as np
import os

class ShelfLifeModel:
    def __init__(self, data_path="data/food_data.csv"):
        self.data_path = data_path
        self.model = None
        # Lazy import LabelEncoder
        from sklearn.preprocessing import LabelEncoder
        self.le_category = LabelEncoder()
        self.le_item = LabelEncoder()
        
    def load_and_train(self):
        # Lazy import RandomForest
        from sklearn.ensemble import RandomForestRegressor
        
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
            
        df = pd.read_csv(self.data_path)
        
        # Preprocessing
        # Encode categorical variables
        df['Category_Encoded'] = self.le_category.fit_transform(df['Food_Category'])
        # We might not use 'Item' for general prediction to avoid overfitting to specific names, 
        # but it's useful to have. Let's stick to Category, pH, Temp for generalization.
        
        X = df[['Temperature_C', 'pH', 'Category_Encoded']]
        y = df['Shelf_Life_Days']
        
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        print("Model trained successfully.")
        
    def predict(self, temperature, ph, category_name):
        if self.model is None:
            self.load_and_train()
            
        # Handle unseen categories gracefully
        try:
            cat_encoded = self.le_category.transform([category_name])[0]
        except ValueError:
            # Fallback for unknown category: use mode or a generic average. 
            # For now, let's pick "Vegetable" or similar as a baseline if unknown, 
            # or just raise a warning. Let's map to existing or default (e.g., Vegetable index 0)
            # A better way is to list available categories.
            # print(f"Warning: Category '{category_name}' not found. using default.")
            cat_encoded = 0 # Defaulting
            
        input_data = pd.DataFrame({
            'Temperature_C': [temperature],
            'pH': [ph],
            'Category_Encoded': [cat_encoded]
        })
        
        prediction = self.model.predict(input_data)[0]
        return max(0, prediction) # Ensure non-negative

    def get_categories(self):
        if self.model is None:
            self.load_and_train()
        return list(self.le_category.classes_)

if __name__ == "__main__":
    # Test
    model = ShelfLifeModel()
    model.load_and_train()
    pred = model.predict(4, 6.0, "Vegetable")
    print(f"Prediction for Vegetable at 4C, pH 6.0: {pred:.2f} days")
