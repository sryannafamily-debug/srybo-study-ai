from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os


class SryboHandler(SimpleHTTPRequestHandler):

    def do_POST(self):

        if self.path != "/ask":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)

        try:
            request = json.loads(data.decode("utf-8"))
            question = request.get("question", "").strip()
            q = question.lower()

            if "c programming" in q or "what is c" in q or "explain c" in q:
                answer = """C Programming

C is a general-purpose programming language developed by Dennis Ritchie.

Important C topics include:

1. Variables and data types
2. Operators
3. If statements
4. Loops
5. Functions
6. Arrays
7. Pointers
8. Structures
9. File handling
10. Dynamic memory allocation"""

            elif "python" in q or "what is python" in q or "explain python" in q:
                answer = """Python

Python is a high-level programming language known for its simple and readable syntax.

Python is commonly used for:

1. Web development
2. Artificial intelligence
3. Data science
4. Automation
5. Software development
6. Machine learning"""

            elif "hardware" in q:
                answer = """Computer Hardware

Computer hardware refers to the physical parts of a computer that can be seen and touched.

Examples include:

1. CPU
2. RAM
3. Hard drive or SSD
4. Keyboard
5. Mouse
6. Monitor
7. Motherboard
8. Printer"""

            elif "software" in q:
                answer = """Computer Software

Computer software is a collection of programs and instructions that tell computer hardware what to do.

Two major types are:

1. System software
   Example: Operating systems

2. Application software
   Example: Web browsers and word processors"""

            elif "network" in q or "networking" in q:
                answer = """Computer Networks

A computer network is a group of computers and devices connected together so they can communicate and share resources.

Types include:

1. LAN - Local Area Network
2. WAN - Wide Area Network
3. MAN - Metropolitan Area Network
4. PAN - Personal Area Network"""

            elif "database" in q or "databases" in q or "dbms" in q:
                answer = """Database Systems

A database is an organized collection of data that can be stored, accessed, managed and updated.

DBMS means Database Management System.

Examples include:

1. MySQL
2. PostgreSQL
3. Microsoft SQL Server
4. Oracle Database"""

            elif "operating system" in q or "operating systems" in q:
                answer = """Operating Systems

An operating system is system software that manages computer hardware and provides services for application programs.

Examples include:

1. Windows
2. Linux
3. Android
4. macOS

Main functions include:

1. Memory management
2. File management
3. Process management
4. Device management
5. Security management"""

            elif "web development" in q or "website" in q or "websites" in q:
                answer = """Web Development

Web development is the process of creating websites and web applications.

The main technologies are:

1. HTML - creates structure
2. CSS - controls design
3. JavaScript - adds interaction

Backend technologies include Python, PHP and Node.js."""

            elif "cybersecurity" in q or "cyber security" in q:
                answer = """Cybersecurity

Cybersecurity is the practice of protecting computers, networks, applications and data from unauthorized access and attacks.

Important areas include:

1. Password security
2. Network security
3. Malware protection
4. Encryption
5. Access control
6. Data protection"""

            elif "mathematics" in q or "math" in q or "mathematical" in q:
                answer = """Mathematics in Computer Science

Mathematics is an important part of Computer Science.

It is used in:

1. Algorithms
2. Programming
3. Computer graphics
4. Cryptography
5. Artificial intelligence
6. Data analysis"""

            elif "entrepreneurship" in q or "entrepreneur" in q:
                answer = """Entrepreneurship

Entrepreneurship is the process of identifying an opportunity, creating a business idea and organizing resources to create value.

Important concepts include:

1. Business ideas
2. Innovation
3. Market research
4. Business planning
5. Risk management
6. Customer needs"""

            elif "programming" in q or "programming language" in q:
                answer = """Programming

Programming is the process of writing instructions that a computer can execute.

Examples of programming languages include:

1. C
2. Python
3. Java
4. JavaScript
5. C++"""

            elif "hello" in q or "hi" in q or "hey" in q:
                answer = """Hello! 👋

I'm Srybo Study AI. 🤖

I can help you study:

• C Programming
• Python
• Computer Hardware
• Computer Software
• Computer Networks
• Database Systems
• Operating Systems
• Web Development
• Cybersecurity
• Mathematics
• Entrepreneurship
• Programming"""

            else:
                answer = """I'm Srybo Study AI. 🤖

I don't know that topic yet.

Try asking me:

• What is C programming?
• What is Python?
• What is computer hardware?
• What is computer software?
• What is a computer network?
• What is a database?
• What is an operating system?
• What is web development?
• What is cybersecurity?
• What is mathematics?
• What is entrepreneurship?
• What is programming?"""

            response = json.dumps({
                "answer": answer
            }).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(response)

        except Exception as e:

            response = json.dumps({
                "error": str(e)
            }).encode("utf-8")

            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()

            self.wfile.write(response)


port = int(os.environ.get("PORT", 8000))

server = HTTPServer(
    ("0.0.0.0", port),
    SryboHandler
)

print(f"Srybo Study AI running on port {port}")

server.serve_forever()
