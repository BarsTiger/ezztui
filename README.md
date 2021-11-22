## Usage

```python
import ezztui
ezztui.check_curses() # check and install windows-curses, if on windows
menu = {
    'First menu':
        {'Function 1': 'ezztui_return_value',
         'Function 2': 'ezztui_return_value',
         'Function 3': 'ezztui_return_value',
         'Function 4': 'ezztui_return_value',
         'Function 5': 'ezztui_return_value',
         'Back': 'ezztui_back_value'},

    'Second menu':
        {'Submenu 1': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Function 3': 'ezztui_return_value',
            'Function 4': 'ezztui_return_value',
            'Function 5': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Submenu 2': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Function 3': 'ezztui_return_value',
            'Function 4': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Submenu 3': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Function 3': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Submenu 4': {
            'Function 1': 'ezztui_return_value',
            'Function 2': 'ezztui_return_value',
            'Back': 'ezztui_back_value'},
         'Back': 'ezztui_back_value'},

    'No submenu function': 'ezztui_return_value',

    'Third menu':
        {'Function 1': 'ezztui_return_value',
         'Function 2': 'ezztui_return_value',
         'Function 3': 'ezztui_return_value',
         'Function 4': 'ezztui_return_value',
         'Back': 'ezztui_back_value'},

    'Exit':
        {"Exit": 'ezztui_exit_value',
         "Back": 'ezztui_back_value'}
}

```

## Returns
```
['Second menu', 'Submenu 2', 'Function 3']
```