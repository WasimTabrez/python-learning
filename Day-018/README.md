# 📅 Day 18 - Multithreading & Multiprocessing

## 🎯 Objective

Learn how to execute tasks concurrently and in parallel using Python's **threading** and **multiprocessing** modules. Understand thread synchronization, inter-thread communication, and the differences between multithreading and multiprocessing.

---

## 📚 Concepts Learned

- Introduction to Concurrency
- Process vs Thread
- Global Interpreter Lock (GIL)
- The `threading` Module
- Creating Threads
- Thread Lifecycle
- `start()` and `join()`
- Daemon Threads
- Thread Names
- Thread Synchronization
- `Lock`
- `RLock`
- `Semaphore`
- `Event`
- `Queue`
- Producer-Consumer Pattern
- The `multiprocessing` Module
- Creating Processes
- Process Pool
- CPU-bound vs I/O-bound Tasks
- Shared Resources
- Thread Safety

---

## 💻 Programs Implemented

| File | Description |
|------|-------------|
| `thread_demo.py` | Create and run a simple thread |
| `multiple_threads.py` | Run multiple threads simultaneously |
| `join_demo.py` | Demonstrate `join()` |
| `daemon_thread.py` | Demonstrate daemon threads |
| `thread_name.py` | Display thread names |
| `lock_demo.py` | Synchronize threads using `Lock` |
| `rlock_demo.py` | Demonstrate `RLock` |
| `semaphore_demo.py` | Demonstrate `Semaphore` |
| `event_demo.py` | Synchronize threads using `Event` |
| `queue_demo.py` | Thread-safe communication using `Queue` |
| `producer_consumer.py` | Implement the Producer-Consumer pattern |
| `process_demo.py` | Create a process |
| `multiple_processes.py` | Run multiple processes |
| `process_pool.py` | Demonstrate a process pool |
| `cpu_bound.py` | Solve a CPU-bound task using multiprocessing |
| `io_bound.py` | Solve an I/O-bound task using multithreading |
| `thread_vs_process.py` | Compare threads and processes |
| `shared_counter.py` | Shared counter with synchronization |
| `file_downloader.py` | Simulate concurrent file downloads |
| `image_processor.py` | Simulate parallel image processing |

---

## 🧠 Key Takeaways

- Learned the difference between concurrency and parallelism.
- Understood the difference between processes and threads.
- Created and managed multiple threads.
- Used `join()` to wait for thread completion.
- Worked with daemon threads.
- Synchronized shared resources using locks.
- Used semaphores and events for thread coordination.
- Implemented producer-consumer communication using queues.
- Created and managed multiple processes.
- Used multiprocessing for CPU-intensive tasks.
- Compared multithreading and multiprocessing for different workloads.

---

## 💡 Challenges Faced

- Understanding the Global Interpreter Lock (GIL).
- Preventing race conditions.
- Synchronizing multiple threads safely.
- Deciding when to use threads versus processes.
- Sharing data safely between concurrent tasks.

---

## 📂 Folder Structure

```text
Day-018/
│
├── README.md
├── thread_demo.py
├── multiple_threads.py
├── join_demo.py
├── daemon_thread.py
├── thread_name.py
├── lock_demo.py
├── rlock_demo.py
├── semaphore_demo.py
├── event_demo.py
├── queue_demo.py
├── producer_consumer.py
├── process_demo.py
├── multiple_processes.py
├── process_pool.py
├── cpu_bound.py
├── io_bound.py
├── thread_vs_process.py
├── shared_counter.py
├── file_downloader.py
├── image_processor.py
├── concurrent_file_downloader.py
└── parallel_data_processing.py
```

---

## 🏆 Mini Project

### Concurrent File Downloader

**Features**

- Download Multiple Files Simultaneously (Simulation)
- Display Download Progress
- Thread per Download
- Wait for All Threads
- Show Download Status
- Exit

**Concepts Used**

- Multithreading
- `Thread`
- `Lock`
- `join()`
- Functions
- Loops
- Time Module

---

## ⭐ Bonus Project

### Parallel Data Processing System

**Features**

- Generate Large Dataset
- Split Data Across Processes
- Calculate Sum
- Calculate Average
- Find Maximum
- Find Minimum
- Display Processing Time
- Exit

**Concepts Used**

- Multiprocessing
- Process Pool
- CPU-bound Processing
- Time Measurement
- Lists
- Functions

---

## 📖 Real-World Applications

Python Multithreading and Multiprocessing are commonly used for:

- Web Servers
- REST APIs
- Download Managers
- Image Processing
- Video Processing
- Data Analytics
- Scientific Computing
- Machine Learning
- ETL Pipelines
- Background Task Processing

---

## 🚀 Next Topic

**Day 19 – Database Programming with SQLite**

Topics:

- SQLite Database
- Connecting to a Database
- Creating Tables
- CRUD Operations
- SQL Queries
- Parameterized Queries
- Transactions
- Exception Handling
- Database Projects

---

## ✅ Status

**Completed ✔️**
