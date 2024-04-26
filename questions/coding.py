"""Review Functions and Classes."""

def compute_square_while(n) -> int:
    return


def compute_square_for(n) -> int:
    return


def primality_test_exhaustive(n) -> bool:
    return


def primality_test_efficient(n) -> bool:
    return


def compute_square_root_exhaustive(n) -> Tuple[float, bool]:
    """Use exhaustive method to compute square root."""
    return


def compute_square_root_efficient(n) -> float:
    return


def compute_intersection(tuple_one: Tuple[Any, ...], tuple_two: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return


def apply_to_each(values_list: List[int], function: Callable) -> None:


def human_readable_boolean(answer: bool) -> str:
    return


def fill_random_container(
    size: int, maximum: int, make_tuple: bool = False
) -> Union[List[int], Tuple[int, ...]]:
    return


def compute_intersection_list_double(
    input_one: List[Any], input_two: List[Any]
) -> List[Any]:
    """Compute the intersection of two provided lists."""
    return []


def compute_intersection_list_single(
    input_one: List[Any], input_two: List[Any]
) -> List[Any]:
    """Compute the intersection of two provided lists."""
    return []


def compute_intersection_tuple_double(
    input_one: Tuple[Any, ...], input_two: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    return


def compute_intersection_tuple_single(
    input_one: Tuple[Any, ...], input_two: Tuple[Any, ...]
) -> Tuple[Any, ...]:
    return


class IntersectionApproach(str, Enum):


def fibonacci_recursivelist(number: int) -> List[int]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""


def fibonacci_recursivetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""


def fibonacci_iterativetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using iteration and a tuple."""


def fibonacci_iterativelist(number: int) -> List[int]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using a list."""


def remove_duplicates(list_one: List[Any], list_two: List[Any]) -> Tuple[List[Any], List[Any]]:
    """Remove from both lists the duplicate elements that are found in both of the lists."""


def is_palindrome_reverse(word: str) -> bool:


def is_palindrome_recursive(word: str) -> bool:


def to_chars(word: str) -> str:


class Person:
    """Define a Person class."""


def is_matching_person(
    attribute: str, match: str, search_person: person.Person
) -> bool:
    """Determine if the person's specified attribute contains the search term in match."""


def find_matching_people(
    attribute: str, match: str, person_data: List[person.Person]
) -> List[person.Person]:
    """Find people who have matching data for a specified attribute."""


def generate_random_number(maximum: int, exceed: bool = False) -> int:
    """Generate a random int defined by maximum."""


def containment_check_list(thelist: List[int], number: int) -> bool:
    """Determine if a value is contained in the list."""


def containment_check_tuple(thetuple: Tuple[int], number: int) -> bool:
    """Determine if a value is contained in the tuple."""


def containment_check_set(thelist: List[int], number: int) -> bool:
    """Determine if a value is contained in the list."""


def calculate_average_values(data_list: List[float], data_count: int) -> List[float]:
    """Calculate the average values for the data in the provided list."""


def bubble_sort(array: List[int]) -> List[int]:
    """Sort an input list called array using bubble sort."""


def insertion_sort(array: List[int]) -> List[int]:
    """Run an insertion sort on the provided array."""


def merge(left: List[int], right: List[int]) -> List[int]:
    """Define a convenience method that supports the merging of lists."""


def merge_sort(array: List[int]) -> List[int]:
    """Sort the provided list called array with the merge sort algorithm."""


def quick_sort(array: List[int]) -> List[int]:
    """Sort the provided list called array with the quick sort algorithm."""


def insertion_sort_tim(array: List[int], left: int = 0, right=None):
    """Use an internal sorting algorithm for the timsort algorithm."""


def tim_sort(array: List[int]) -> List[int]:
    """Sort the list called array with the tim sort algorithm using a special insertion sort."""


def confirm_valid_file(file: Path) -> bool:


def count_negatives_in_matrix(matrix: List[List[int]]) -> int:


class Item(object):

    def __init__(self, n, v, w):
        """Construct an instance of the Item class."""
        # TODO: Add this source code segment by consulting the book and course web site

    def get_name(self) -> str:
        """Access the name of an Item."""
        # TODO: Add this source code segment by consulting the book and course web site

    def get_value(self) -> int:
        """Access the value of an Item."""
        # TODO: Add this source code segment by consulting the book and course web site

    def get_weight(self) -> int:
        """Access the weight of an Item."""
        # TODO: Add this source code segment by consulting the book and course web site

    def __repr__(self) -> str:
        """Produce a textual representation of the Item."""
        # TODO: Add this source code segment by consulting the book and course web site


def value(item: Item) -> int:
    """Return the value for a specific item."""
    # TODO: Add this source code segment by consulting the book and course web site


def weight_inverse(item: Item) -> float:
    """Return the inverse of the weight for a specific item."""
    # TODO: Add this source code segment by consulting the book and course web site


def density(item: Item) -> float:
    """Return the density of the item."""


def greedy(items: List[Item], max_weight: int, key_function) -> Tuple[List[Item], float]:
    """Perform the greedy algorithm for items, a maximum weight of a knapsack, and an objective function."""


def build_items(n: List[str], v: List[int], w: List[int]) -> List[Item]:
    """Create an instance of a 0/1 knapsack using instances of the Item class."""


def exhaustive_enumeration(pset, max_weight, get_value, get_weight):
    """Run an exhaustive enumeration algorithm to find best combination."""


def run_exhaustive_enumeration(items: List[Items], max_weight=20):
    """Use the exhaustive enumeration algorithm for a problem instance."""


def run_one_greedy(items: List[Item], max_weight: int, key_function) -> None:
    """Run the greedy algorithm and display the result."""


def run_all_greedy(items: List[Item], max_weight=20) -> None:
    """Run all greedy algorithm with all possible objective functions."""
