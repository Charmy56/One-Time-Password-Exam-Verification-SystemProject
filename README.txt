

#System

The  System is a web application designed to help manage various aspects of student information, including generating OTPs, verifying OTPs, updating student records, updating fee records, and updating exam cards.

## Installation

To install and run the Student Management System, follow these steps:

1. Install Python (version 3.x) from the [official Python website](https://www.python.org/).

2. Install Django (version 3.x) by running the following command:

   ```
   pip install django faker
   ```

3. Install other dependencies using the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Student Management System:

1. Start the development server by running the following command:

   ```
   python manage.py createsuperuser

   python manage.py runserver

   ```

2. Access the system locally at `http://localhost:8000` in your web browser.

3. Use the navigation links to access different features of the system:

   - **Generate OTP**: Generate OTPs for students.
   - **Verify OTP**: Verify OTPs generated for students.
   - **Update Student Records**: Update student information such as name, department, etc.
   - **Update Fee Records**: Update fee-related records for students.
   - **Update Exam Card**: Update exam card details for students.

## Using SQLite Database

The system uses SQLite as its database. No additional setup is required for the database.

## Generating Test Data

The Faker module is used to generate test data. Test data is automatically generated when needed.

## Author

This project was created by Valeria Akinyi.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides instructions for installing, running, and using the Student Management System. It also includes information about the author, how to contribute, and the project's license.