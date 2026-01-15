
# Dictionary of preservation techniques and their descriptions
PRESERVATION_TECHNIQUES = {
    "Drying": {
        "Description": "Removes moisture from food to inhibit the growth of bacteria, yeast, and mold.",
        "Methods": ["Sun drying", "Oven drying", "Dehydrator"],
        "Best For": ["Fruits", "Vegetables", "Herbs", "Meats (Jerky)"]
    },
    "Freezing": {
        "Description": "Lowers temperature to slow down enzyme activity and microbial growth. Does not kill sterilization.",
        "Methods": ["Blast freezing", "Home freezing"],
        "Best For": ["Fruits", "Vegetables", "Meats", "Prepared meals"]
    },
    "Fermentation": {
        "Description": "Uses beneficial microorganisms (bacteria, yeast) to convert carbohydrates into alcohol or organic acids.",
        "Methods": ["Lacto-fermentation", "Alcoholic fermentation"],
        "Best For": ["Vegetables (Sauerkraut, Kimchi)", "Dairy (Yogurt)", "Beverages"]
    },
    "Canning": {
        "Description": "Seals food in sterilzed containers and applies heat to destroy spoilage organisms.",
        "Methods": ["Water bath canning (High acid)", "Pressure canning (Low acid)"],
        "Best For": ["Fruits", "Vegetables", "Meats"]
    },
    "High-Pressure Processing (HPP)": {
        "Description": "A non-thermal method that uses extremely high pressure to inactivate pathogens while maintaining freshness.",
        "Methods": ["Industrial HPP chambers"],
        "Best For": ["Juices", "Dips", "Meats", "Seafood"]
    },
    "Cold Plasma": {
        "Description": "Uses ionized gas to decontaminate food surfaces without heat.",
        "Methods": ["Dielectric barrier discharge"],
        "Best For": ["Fresh produce surface sterilization"]
    },
    "Vacuum Packaging": {
        "Description": "Removes air from the package prior to sealing to reduce atmospheric oxygen, limiting the growth of aerobic bacteria or fungi.",
        "Methods": ["Vacuum sealer"],
        "Best For": ["Meats", "Fish", "Cheese", "Vegetables (to be frozen)"]
    }
}

def get_knowledge_context():
    """Returns a string representation of the knowledge base for LLM context."""
    context = "Food Preservation Techniques Knowledge Base:\n\n"
    for tech, details in PRESERVATION_TECHNIQUES.items():
        context += f"## {tech}\n"
        context += f"- **Principle**: {details['Description']}\n"
        context += f"- **Methods**: {', '.join(details['Methods'])}\n"
        context += f"- **Suitable For**: {', '.join(details['Best For'])}\n\n"
    return context
