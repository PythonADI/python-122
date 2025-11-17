# Final Project: Django Web Application

## Overview
Build a small Django web application that demonstrates the workflows we practiced together: setting up a project, creating models, wiring views, and rendering templates. Focus on a clear user story, clean presentation, and documentation that lets a classmate run the project without surprises.

## Core Requirements (Workshop Skills)
- Start a fresh Django project and app using `django-admin startproject` and `python manage.py startapp` (see `workshop_13/web` for reference).
- Define at least two related models (e.g., `Category` → `Product`) and apply the migrations.
- Register your models in the Django admin and load enough sample records so pages have real data.
- Build one list view and one detail view (function-based or class-based) that return context data to templates.
- Create templates that render those views, reuse shared navigation, and display meaningful empty states when no records exist.
- Link pages together (e.g., list → detail → back to list) so the user can move through the app smoothly.

## Technical Checklist (Workshop Skills)
- Work inside a virtual environment and track dependencies with `requirements.txt`.
- Keep project code inside a dedicated Django app (`core`, `tracker`, etc.) with models, views, templates, and `urls.py` grouped logically.
- Document the commands to install dependencies, run migrations, create a superuser, and start the development server.

## Milestones
1. **Proposal**: Submit a short design brief describing the problem, target users, core models (fields/relationships), and key pages.
2. **Prototype**: Implement the data models, migrations, and admin site registration. Share screenshots or admin URLs.
3. **Beta**: Finish your list/detail views, templates, and sample data. Request peer feedback on usability.
4. **Launch**: Polish styling, finalize documentation, and demo the application running locally.

## Deliverables
- Django project folder tracked in Git with clear commit history.
- `README.md` at the project root explaining setup, usage, and known limitations.
- `requirements.txt` for replicating the environment.
- Screenshots or a short screencast showing the core user flow.
- Optional: Deployed version on Render, Railway, or PythonAnywhere (link in README).

## Optional Enhancements (Research & Explore)
- Add create/update forms with `ModelForm` to manage content directly in the app: https://docs.djangoproject.com/en/5.0/topics/forms/
- Implement search or filtering to narrow results: https://docs.djangoproject.com/en/5.0/topics/db/queries/#retrieving-specific-objects-with-filters
- Introduce template inheritance with a shared base layout: https://docs.djangoproject.com/en/5.0/ref/templates/language/#template-inheritance
- Move secrets (e.g., `SECRET_KEY`) into environment variables using `python-dotenv` or similar: https://djangostars.com/blog/configuring-django-settings-best-practices/
- Seed the database with fixtures or a management command for quick demos: https://docs.djangoproject.com/en/5.0/howto/initial-data/
- Explore deployment to a hosted service such as Render or PythonAnywhere: https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
- Experiment with automated tests if you want extra coverage: https://docs.djangoproject.com/en/5.0/topics/testing/overview/

## Research Links
- Official Django tutorial: https://docs.djangoproject.com/en/5.0/intro/tutorial01/
- Django Girls step-by-step guide: https://tutorial.djangogirls.org/en/
- Mozilla Django Local Library walkthrough: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
- Template language reference: https://docs.djangoproject.com/en/5.0/ref/templates/language/
- Working with class-based views: https://docs.djangoproject.com/en/5.0/topics/class-based-views/
- Static files and styling: https://docs.djangoproject.com/en/5.0/howto/static-files/
