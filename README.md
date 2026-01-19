# Automate-File-Organizer

A Python-based desktop application to **organize files automatically** into categorized folders based on their file extensions. This version includes a **GUI interface**, logging, preview, and customizable extension mappings.

## Features

- Organizes files into categories such as:
  - **Images**: `.jpeg`, `.jpg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
  - **Documents**: `.doc`, `.docx`, `.pdf`, `.txt`, `.rtf`, `.xlsx`, `.ppt`, `.pptx`
  - **Code**: `.c`, `.cpp`, `.py`, `.java`, `.js`, `.html`, `.css`, `.php`
  - **Audio**: `.mp3`, `.wav`, `.flac`
  - **Video**: `.mp4`, `.avi`, `.mkv`
  - **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
  - **Executables**: `.exe`, `.dll`
  - **Databases**: `.sql`
  - **Applications**: `.app`
  - **Data**: `.json`, `.csv`
  - **Logs**: `.log`
  - **XML**: `.xml`
  - **Other**: All unsupported extensions go into an `other` folder.

- **GUI interface** using `Tkinter` with buttons to:
  - Select directory and organize files
  - Configure or change folder mappings for file extensions
  - Preview file organization before executing

- **Progress bar** to show file organization status.

- **Logging**: All file movements and created directories are logged in `file_organizer.log`.

- **Preview**: See how files will be organized before applying changes.
