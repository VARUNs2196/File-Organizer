# File-Organizer
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Organizer User Manual</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        header {
            background-color: #0044cc;
            color: white;
            text-align: center;
            padding: 20px;
        }

        .container {
            padding: 20px;
        }

        h2 {
            color: #0044cc;
        }

        .feature {
            background-color: #ffffff;
            border: 1px solid #ddd;
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 5px;
        }

        .screenshot {
            width: 100%;
            max-width: 600px;
            display: block;
            margin: 20px auto;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .requirements, .steps, .features {
            margin-top: 20px;
        }

        .requirements ul, .steps ul, .features ul {
            list-style-type: none;
            padding: 0;
        }

        .requirements li, .steps li, .features li {
            background-color: #ffffff;
            margin: 5px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        footer {
            text-align: center;
            padding: 10px;
            background-color: #0044cc;
            color: white;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>

<header>
    <h1>File Organizer Application - User Manual</h1>
</header>

<div class="container">
    <section class="requirements">
        <h2>Prerequisites & Requirements</h2>
        <p>Before using the File Organizer application, make sure you have the following installed:</p>
        <ul>
            <li>Python 3.x or higher</li>
            <li>Libraries: 
                <pre>tkinter, pillow</pre>
            </li>
        </ul>
    </section>

    <section class="steps">
        <h2>Installation Steps</h2>
        <p>Follow these steps to get the File Organizer application running:</p>
        <ol>
            <li>Clone or download the project to your local machine.</li>
            <li>Navigate to the project directory.</li>
            <li>Create a virtual environment (optional but recommended):
                <pre>python -m venv venv</pre>
            </li>
            <li>Activate the virtual environment:
                <pre>venv\Scripts\activate (Windows)</pre>
                <pre>source venv/bin/activate (Linux/macOS)</pre>
            </li>
            <li>Install required dependencies:
                <pre>pip install -r requirements.txt</pre>
            </li>
            <li>Run the application:
                <pre>python file_organizer.py</pre>
            </li>
        </ol>
    </section>

    <section class="usage">
        <h2>How to Use the File Organizer</h2>
        <p>Follow these steps to organize your files:</p>
        <ol>
            <li>Open the application by running the Python script.</li>
            <li>In the application window, enter the directory path where the files are located.</li>
            <li>Select the file categories you want to organize (Videos, Audios, Documents, etc.).</li>
            <li>Click the "Organize Files" button to move files into appropriate folders based on their type.</li>
        </ol>
    </section>

    <section class="features">
        <h2>Features</h2>
        <ul>
            <li class="feature">
                <strong>Automatic File Sorting</strong> – Sorts files based on types like Videos, Audios, Documents, etc.
            </li>
            <li class="feature">
                <strong>Customizable Folder Creation</strong> – Automatically creates folders for each file type in the specified directory.
            </li>
            <li class="feature">
                <strong>Supports Multiple File Formats</strong> – Supports common file extensions for videos, audios, and documents.
            </li>
            <li class="feature">
                <strong>Cross-Platform Support</strong> – Works on both Windows and Linux operating systems.
            </li>
        </ul>
    </section>

    <section class="screenshots">
        <h2>Screenshots</h2>
        <p>Here are some screenshots of the File Organizer in action:</p>
        <img src="screenshot1.png" alt="File Organizer Screenshot 1" class="screenshot">
        <img src="screenshot2.png" alt="File Organizer Screenshot 2" class="screenshot">
    </section>
</div>

<footer>
    <p>&copy; 2024 File Organizer Application</p>
</footer>

</body>
</html>
