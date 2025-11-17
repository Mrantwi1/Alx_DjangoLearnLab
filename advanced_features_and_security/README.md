# Managing Permissions and Groups in Django

This project utilizes Django's built-in authentication system to manage user access via custom permissions and groups.

## 1. Custom Permissions Setup
Custom permissions are defined in the `relationship_app/models.py` file on the **Book** model under the `Meta` class.

- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## 2. Group Configuration (Manual Admin Step)
The following groups must be created manually in the Django Admin interface:

| Group | Assigned Permissions |
| :--- | :--- |
| **Admins** | All permissions for all models (including all Book CRUD). |
| **Editors** | `can_view`, `can_create`, `can_edit`. |
| **Viewers** | `can_view`. |

## 3. Permission Enforcement in Views
Access control is enforced using the `@permission_required` decorator in `relationship_app/views.py`.

- `add_book` is protected by: `relationship_app.can_create`
- `change_book` is protected by: `relationship_app.can_edit`
- `delete_book` is protected by: `relationship_app.can_delete`# Introduction to Django
This folder contains the LibraryProject Django starter project for the ALX Django lab.
