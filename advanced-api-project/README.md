
## Testing Strategy
The API utilizes `rest_framework.test.APITestCase` to ensure data integrity and security.

### How to Run Tests
1. Ensure all dependencies are installed (`pip install django djangorestframework django-filter`).
2. Run the command: `python manage.py test api`.

### Test Coverage
- **CRUD Operations**: Verified for creation, retrieval, updates, and deletion.
- **Permissions**: Confirmed that only authenticated users can modify data.
- **Filtering & Search**: Validated query parameters for `title`, `author`, and `search`.