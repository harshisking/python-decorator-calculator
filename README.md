## 🚀 Secure Calculator with Python Decorators 🧮🔐  
This is a simple CLI-based calculator practice project written in Python that demonstrates the power of **decorators**. The calculator supports basic arithmetic operations but includes multiple layers of functionality using custom decorators.  
 
---  
 
### 🧠 Features  
- **Login System**: Only registered users can access the calculator.  
- **Input Validation**: Checks if inputs are valid numbers.  
- **Execution Timer**: Measures how long each operation takes.  
- **Logging**: All operations are logged in `logs.txt` with user details.  
  
---  
  
### 🔁 Decorators Used  
| Decorator Name | Purpose |  
|----------------|---------|  
| `@loginReq`    | Ensures user is logged in before performing any operation |  
| `@Validate`    | Validates input types (checks if numbers are valid) |  
| `@timer`       | Measures time taken by each operation |  
| `@logtofile`   | Logs the operation details and result to `logs.txt` |  
  
---  
 
### 🧪 Example Flow  
```  
Enter username: admin  
Enter password: 12345678  
Login successful!  
  
Choose operation:  
1. Add  
2. Subtract  
3. Multiply  
4. Divide  
Enter choice: 1  
Enter first number: 5  
Enter second number: 7  
Result: 12  
(Time taken: 0.0001s)  
```  
  
---  
  
### 🛠 How to Run  
```bash  
python3 calculator.py  
```  
  
Make sure Python 3 is installed on your system.  
  
---  
  
### 📁 Notes  
- `logs.txt` is auto-generated and records every calculation.    
 ```  
 logs.txt  
 ```  
 
---  
 
### 📜 License  
This project is free to use and modify.  
 
---  
 
Made with ❤️ by Harsh Barot
