echo "========================================"
echo "Start formatting code..."
echo "========================================"

echo "Running isort..."
python -m isort .

echo "Running black..."
python -m black .

echo "========================================"
echo "Formatting complete!"
echo "========================================"