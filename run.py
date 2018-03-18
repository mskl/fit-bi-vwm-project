from source.topktreshold import app
from source.tests.MyHeapTest import run_test
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "DEBUG":
            app.run(debug=True)
    app.run()
