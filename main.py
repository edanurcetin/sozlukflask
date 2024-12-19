from flask import Flask, render_template, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

# XML dosyasını oku ve veriyi bir sözlükte tut
def load_students():
    tree = ET.parse('students.xml')  # XML dosyasının yolu
    root = tree.getroot()

    students = {}
    for student in root.findall('student'):
        student_id = student.get('id')
        name = student.find('name').text
        age = student.find('age').text
        department = student.find('department').text
        
        students[student_id] = {
            'name': name,
            'age': age,
            'department': department
        }
    
    return students

@app.route("/", methods=["GET", "POST"])
def index():
    students = load_students()  # Öğrencileri yükle
    student_info = None

    if request.method == "POST":
        student_id = request.form.get('student_id')
        student_info = students.get(student_id)  # ID'ye göre öğrenci bilgisi al

    return render_template('index.html', student_info=student_info)

if __name__ == "__main__":
    app.run(debug=True)
