types-labgrid
=============

This is a `PEP 561 <https://peps.python.org/pep-0561/>`_ stub-only distribution for the `labgrid <https://github.com/labgrid-project/labgrid>`_ library.

Install alongside ``labgrid`` so type checkers (for example mypy or pyright) can resolve annotations for the ``labgrid`` package::

    pip install labgrid types-labgrid

The stubs are generated with mypy's ``stubgen`` in ``--no-import --parse-only`` mode and are intended as a starting point for human refinement.

Protobuf/gRPC modules under ``labgrid.remote.generated`` ship ``.pyi`` files with ``labgrid`` itself; this package does not duplicate them.

Development
-----------

From the ``labgrid-stubs`` directory::

    pip install -e ".[dev]"
    ruff check src
    ruff format --check src
    mypy --install-types --non-interactive src/labgrid
