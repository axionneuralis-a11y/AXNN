
folder & files structure:
AXNN/
│
├── .gitignore
├── README.md
├── buildozer.spec
├── requirements.txt
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── note_model.py
│   ├── todo_model.py
│   ├── folder_model.py
│   ├── calculator_model.py
│   ├── notification_model.py
│   ├── file_model.py
│   └── setting_model.py
│
├── controllers/
│   ├── __init__.py
│   ├── note_controller.py
│   ├── todo_controller.py
│   ├── folder_controller.py
│   ├── calculator_controller.py
│   ├── notification_controller.py
│   ├── settings_controller.py
│   ├── stats_controller.py
│   └── editor_controller.py
│
├── screens/
│   ├── __init__.py
│   ├── home_screen.py
│   ├── notes_screen.py
│   ├── todos_screen.py
│   ├── calculator_screen.py
│   ├── calendar_screen.py
│   ├── settings_screen.py
│   ├── folder_screen.py
│   ├── note_detail_screen.py
│   ├── todo_detail_screen.py
│   ├── notification_screen.py
│   ├── backup_screen.py
│   └── editor_screen.py
│
├── kv_files/
│   ├── __init__.py
│   ├── main.kv
│   ├── home_screen.kv
│   ├── notes_screen.kv
│   ├── todos_screen.kv
│   ├── calculator_screen.kv
│   ├── calendar_screen.kv
│   ├── settings_screen.kv
│   ├── folder_screen.kv
│   ├── note_detail_screen.kv
│   ├── todo_detail_screen.kv
│   ├── notification_screen.kv
│   ├── backup_screen.kv
│   ├── editor_screen.kv
│   └── code_editor.kv
│
├── components/
│   ├── __init__.py
│   ├── bottom_nav.py
│   ├── note_card.py
│   ├── todo_item.py
│   ├── calendar_widget.py
│   ├── badge_notification.py
│   ├── export_dialog.py
│   ├── create_folder_dialog.py
│   ├── create_file_dialog.py
│   ├── search_bar.py
│   ├── confirmation_dialog.py
│   └── code_editor.py
│
├── utils/
│   ├── __init__.py
│   ├── database.py
│   ├── helpers.py
│   ├── constants.py
│   ├── file_picker.py
│   ├── theme.py
│   ├── syntax_highlighter.py
│   ├── autocomplete.py
│   ├── permissions.py
│   ├── notification_helper.py
│   ├── backup_restore.py
│   └── export_manager.py
│
├── assets/
│   ├── icon.png
│   └── splash.png
│
├── data/
│   ├── code_templates.json
│   └── sample_data.json
│
├── docs/
│   ├── PROJECT_BIBLE.md
│   ├── proposal.md
│   ├── changelog.md
│   ├── user_guide.md
│   ├── developer_guide.md
│   ├── test_case_checklist.md
│   ├── bug_tracker.md
│   └── wireframe_editor.md
│
├── notebooks/
│   └── build_axnn_colab.ipynb
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── bin/
