#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", (long int)(((PyListObject *)p)->allocated));
    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
