# SLDV False Positive Predictor

This application is a full-stack MVVM-based desktop tool that imports SLDV results and processes them using a Python end-to-end pipeline. It applies machine learning models (Random Forest and MLP) to predict false positives in the SLDV results and exports a new file with a prediction attribute.

## Features
- Import SLDV results, Simulink models, and slice files.
- Select a preferred machine learning model (Random Forest or MLP).
- Run an analysis to predict false positives.
- Export results with a new prediction attribute.

## Technologies Used
- **C#** (MVVM Framework for Desktop UI)
- **Python** (Data processing & ML pipeline)
- **MongoDB** (Database for storing results)
- **GitHub** (Version control & collaboration)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/HadiAtwi/AI-QA-predictor.git
   ```
2. Navigate to the project directory:
   ```sh
   cd sldv-false-positive-predictor
   ```
3. Set up the Python environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Build and run the C# application in Visual Studio.

## Usage
1. Open the application.
2. Import SLDV results and Simulink model slices.
3. Select the machine learning model for prediction.
4. Run the analysis.
5. Export the results with predicted false positives.

## Folder Structure
```
sldv-false-positive-predictor/
│── src/                     # C# application source code
│── python_pipeline/         # Python ML pipeline
│── models/                  # Trained ML models (Random Forest, MLP)
│── data/                    # Input & output files
│── README.md                # Project documentation
│── requirements.txt         # Python dependencies
│── .gitignore               # Git ignore file
```

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push to GitHub:
   ```sh
   git push origin feature-branch
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

