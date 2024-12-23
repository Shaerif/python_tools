# 📄 Documentation Checker

> 📝 **Recent Updates**
> - Added style checking
> - Enhanced link validation
> - Improved formatting rules

## 🔍 Validation Rules
- 📚 Structure validation
- 🔗 Link checking
- 🎨 Style consistency
- ✅ Format verification

## Usage

```bash
python src/tools/doc_checker.py --directory ./docs
```

## Configuration

Create a `doc_checker_config.yaml` file:

```yaml
validation_rules:
  - type: structure
  - type: links
  - type: style
  - type: format
```

## Example

```python
from src.tools.doc_checker import check_docs

# Check documentation files
issues = check_docs(directory="./docs")
