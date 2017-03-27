# cProfileContextManager_snippet

Normally cProfile prints out time usage in an unstructured way.

To just print out the total time during the process, you could do

        with CProfileContextManager():
            dosomething()

without patching the package.