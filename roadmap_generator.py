def generate_roadmap(missing_skills):

    # Learning recommendations for known skills
    roadmap_data = {
        "python": "Learn Python fundamentals, syntax, functions, OOP, and practice coding problems.",

        "sql": "Learn SQL queries, filtering, joins, aggregation, subqueries, and database operations.",

        "pandas": "Learn data manipulation, cleaning, transformation, and analysis using Pandas.",

        "numpy": "Learn numerical computing, arrays, matrices, and mathematical operations using NumPy.",

        "machine learning": "Learn supervised and unsupervised learning, model training, evaluation, and feature engineering.",

        "deep learning": "Learn neural networks, backpropagation, optimization, and deep learning fundamentals.",

        "scikit-learn": "Practice building machine learning models using Scikit-learn.",

        "tensorflow": "Learn how to build, train, and deploy deep learning models using TensorFlow.",

        "pytorch": "Learn PyTorch tensors, neural networks, training loops, and deep learning model development.",

        "nlp": "Learn Natural Language Processing fundamentals including text preprocessing and text representation.",

        "natural language processing": "Study NLP techniques such as tokenization, stemming, embeddings, and text classification.",

        "transformers": "Learn Transformer architecture, attention mechanisms, and modern NLP models.",

        "hugging face": "Learn how to use Hugging Face models, tokenizers, datasets, and Transformers.",

        "fastapi": "Learn how to build APIs using FastAPI and deploy machine learning applications.",

        "docker": "Learn containerization, Docker images, containers, and application deployment.",

        "mlflow": "Learn experiment tracking, model versioning, and machine learning lifecycle management.",

        "opencv": "Learn image processing and computer vision using OpenCV.",

        "cnn": "Learn Convolutional Neural Networks and image classification techniques.",

        "yolo": "Learn object detection concepts and implement object detection using YOLO.",

        "power bi": "Learn data visualization, dashboard creation, DAX, and reporting using Power BI.",

        "excel": "Improve spreadsheet analysis, formulas, pivot tables, and data visualization skills.",

        "rag": "Learn Retrieval-Augmented Generation, vector databases, embeddings, and document retrieval.",

        "llm": "Learn Large Language Model fundamentals, prompting, fine-tuning, and applications.",

        "data structures": "Learn arrays, linked lists, stacks, queues, trees, graphs, and hash tables.",

        "algorithms": "Learn searching, sorting, recursion, dynamic programming, and algorithm problem solving."
    }


    roadmap = []


    # Create one roadmap step for EVERY missing skill
    for skill in missing_skills:

        # Clean skill name
        clean_skill = str(skill).strip()

        # Convert to lowercase for dictionary matching
        skill_key = clean_skill.lower()


        # Get recommendation
        if skill_key in roadmap_data:

            topic = roadmap_data[skill_key]

        else:

            topic = (
                f"Learn the fundamentals and practical applications "
                f"of {clean_skill}."
            )


        # Add roadmap step
        roadmap.append({
            "skill": clean_skill,
            "topic": topic
        })


    return roadmap