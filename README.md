# Pandas_as_pd
So, a girl gotta know Python and its libraries, right? That’s why this repo is all about practicing and learning Pandas. I really wanted to name it import pandas as pd because that was the first thing I ever learned—and hey, right from the name itself, I’m already dropping what I know! So let’s gooo!!!


Also, understand that saving Pandas DataFrames is different than saving Python scripts! When I make DataFrames in a .py file, that's just the code - like a recipe. But to actually save the cooked data (my DataFrame), I need .csv, .pkl, or .parquet files. So my script.py generates the data, then boom - df.to_csv() saves it separately. Pro move: .pkl saves everything perfectly for next time I need it, no rerunning needed! That's the real power move right there. 🔥


Common Ways to Save a DataFrame:

                  1. Save as CSV (.csv)
                  
                  myvar.to_csv('data.csv', index=False)  # Prevents saving row indices
                  File: data.csv (Comma-separated values, good for Excel/importing)

                  2. Save as Excel (.xlsx)
                  
                  myvar.to_excel('data.xlsx', index=False)  
                  File: data.xlsx (Excel format)

                  3. Save as JSON (.json)
                  
                  myvar.to_json('data.json')  
                  File: data.json (Structured data format)

                  4. Save as Pickle (.pkl)
                  
                  myvar.to_pickle('data.pkl')  
                  File: data.pkl (Preserves DataFrame structure, Python-specific)

If You Want to Save the Python Code (.py file)
If you meant saving the script that generates the DataFrame (not the data itself), you would save it as a .py file (e.g., my_script.py), but that's different from saving the DataFrame.

                      
                      # my_script.py, the Python file name
                      import pandas as pd
                      
                      mydataset = {
                          "Cars": ["BMW", "Volvo", "Ford"],
                          "Passings": [3, 7, 2]
                      }
                      
                      myvar = pd.DataFrame(mydataset)
                      myvar.to_csv('data.csv', index=False)  # Save DataFrame to CSV
                      print("Data saved successfully!")
Then run it with:

                                  "in gitbash or something"
                                  python my_script.py

                                  
Which One Should You Use?

    CSV/Excel     →   Best for sharing with non-Python users.
    Pickle (.pkl) →   Best for Python-only use (preserves data types).
    JSON          →   Good for web applications.
    .py file      →   Only if you want to save the code, not the DataFrame itself.
