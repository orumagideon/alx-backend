
Simple Helper Function
This repository contains Python scripts implementing simple pagination and hypermedia pagination functionalities for a dataset of popular baby names.

Files
0-simple_helper_function.py
This script contains a simple helper function index_range that takes two integer arguments page and page_size. It returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

1-simple_pagination.py
This script includes a class Server designed to paginate a database of popular baby names. It implements a method get_page that returns the appropriate page of the dataset based on the provided pagination parameters. It also validates input arguments and ensures correct pagination.

2-hypermedia_pagination.py
Replicating the functionality from the previous task, this script extends the Server class to include a method get_hyper which returns pagination details in a dictionary format, including information about the current page, page size, next page, previous page, and total pages.

3-hypermedia_del_pagination.py
This script enhances pagination resilience by providing a method get_hyper_index within the Server class. It ensures that if certain rows are removed from the dataset between two queries, the pagination remains accurate and the user does not miss items from the dataset when changing pages. The method returns pagination details similar to get_hyper, but with additional handling for deleted items.

Usage
Each script can be run independently to demonstrate the functionality. Example usage and expected outputs are provided in the corresponding main.py files for each task.

Repository Details
GitHub repository: alx-backend
Directory: 0x00-pagination
Files: 0-simple_helper_function.py, 1-simple_pagination.py, 2-hypermedia_pagination.py, 3-hypermedia_del_pagination.py
