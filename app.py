from flask import Flask, request, render_template_string
import flag_checker

app = Flask(__name__)

html_form = '''
  <h2>Upload your file to get the flag</h2>
  <form method="POST" enctype="multipart/form-data">
    <input type="file" name="file" required>
    <input type="submit" value="Submit">
  </form>
  {% if flag %}
    <h3>Flag: {{ flag }}</h3>
  {% elif error %}
    <h3 style="color:red;">{{ error }}</h3>
  {% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def check_flag():
    flag = None
    error = None
    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            filepath = '/tmp/uploaded_file'
            f.save(filepath)
            try:
                flag = flag_checker.check_file(filepath)
            except Exception as e:
                error = str(e)
        else:
            error = "No file uploaded."
    return render_template_string(html_form, flag=flag, error=error)
