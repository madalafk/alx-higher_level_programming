#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p) {
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AS_STRING(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        if (string[i] >= 0)
            printf(" %02x", string[i]);
        else
            printf(" %02x", 256 + string[i]);

    printf("\n");
}

void print_python_list(PyObject *p) {
    long int size, i;
    Py_ssize_t allocated;
    PyObject *obj;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++) {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
