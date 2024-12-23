# 🔄 Data Processor Tool

> 📝 **Recent Updates**
> - Added streaming data support
> - Enhanced validation rules
> - Improved error handling

## 🎯 Features
- 📊 Multi-format processing (CSV/JSON/XML)
- ✅ Advanced validation rules
- 🔄 Streaming transformations
- 💾 Efficient memory handling

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python data_processor.py --input data.csv --output processed.json --format json
```

## Configuration

Create a `processor_config.yaml` file:

```yaml
input_format: csv
output_format: json
validation_rules:
  - type: regex
    field: email
    pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
```

## ⚙️ Processing Pipeline
1. 📥 Data Loading
2. ✨ Validation
3. 🔄 Transformation
4. 📤 Output Generation

## 📈 Performance Tips
- Use streaming for large files
- Enable batch processing
- Configure memory limits
- Implement data chunking
