from django.db import migrations

def create_sample_tasks(apps, schema_editor):
    """
    Add sample tasks to the database
    """
    Task = apps.get_model('contrib', 'Task')
    
    # Create sample tasks
    sample_tasks = [
        {
            'title': 'Complete project setup',
            'description': 'Set up Django backend with SQLite database and API endpoints',
            'completed': False
        },
        {
            'title': 'Implement GET /tasks endpoint',
            'description': 'Create API endpoint to return all tasks as JSON list',
            'completed': True
        },
        {
            'title': 'Add CORS support',
            'description': 'Configure CORS headers for frontend-backend communication',
            'completed': True
        },
        {
            'title': 'Create React UserCard component',
            'description': 'Build frontend component to display user information',
            'completed': False
        },
        {
            'title': 'Test API integration',
            'description': 'Verify that frontend can successfully call backend APIs',
            'completed': False
        },
        {
            'title': 'Write documentation',
            'description': 'Document the API endpoints and setup process',
            'completed': False
        },
        {
            'title': 'Deploy to production',
            'description': 'Set up production environment and deploy the application',
            'completed': False
        }
    ]
    
    # Create tasks in the database
    for task_data in sample_tasks:
        Task.objects.create(**task_data)

def remove_sample_tasks(apps, schema_editor):
    """
    Remove sample tasks (reverse migration)
    """
    Task = apps.get_model('contrib', 'Task')
    Task.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('contrib', '0001_initial'),  # Depends on the Task model creation
    ]

    operations = [
        migrations.RunPython(create_sample_tasks, remove_sample_tasks),
    ]