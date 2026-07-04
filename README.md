# AI Code Auditor

An automated local pipeline utility that parses C++ source directories, constructs structured code manifests, and streams real-time static code reviews utilizing the Google Gemini API.


## System Architecture

The application handles source code auditing through a synchronized multi-stage pipeline:

1. **Directory Traversal Loop:** Scans the designated assignment folders using Python's native `os` subsystem to filter out and target active `.cpp` resource files.
2. **Structural Manifest Assembly:** Ingests raw code file streams and constructs an in-memory key-value dictionary mapping filenames directly to their string codebuffers.
3. **Token Pacer Control:** Integrates a `time.sleep` execution throttle to smoothly pace web requests, keeping the process safely under the 20 Requests Per Minute developer threshold to avoid network quota blocks.
4. **ANSI Interface Rendering:** Renders localized audit panels dynamically inside the PowerShell terminal window using the `rich` UI library.


## Setup & Installation

### 1. Install Project Dependencies
Run the execution command within your active terminal window:
```bash
pip install google-genai rich
```

### 2. Environmental Security
The script securely queries authentication tokens straight from the host OS environment block. Configure your terminal environment variable securely:
```powershell
$env:GEMINI_API_KEY="YOUR_SECURE_DEVELOPER_KEY_HERE"
```


## Usage & Execution

To fire up the automated scanning pipeline across your targeted C++ source sheets, run the main production engine file:
```bash
python 09_code_auditor_2.0.py
```


## Project Progression & Milestone Log

**Milestone 1:** Completed core C++ programming workspace analysis.
**Milestone 2:** Built local in-memory folder scanner and dictionary manifest constructor.
**Milestone 3:** Developed live Gemini network API integration and fixed authentication gateway protocols.
**Milestone 4:** Engineered the time module token pacer loop to handle 429 rate limits and wrapped data output inside stylized rich console panels.