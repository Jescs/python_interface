class Config:
    """
    Access to configuration values, pluginmanager and plugin hooks.

    :ivar PytestPluginManager pluginmanager: the plugin manager handles plugin registration and hook invocation.

    :ivar argparse.Namespace option: access to command line option as attributes.

    :ivar InvocationParams invocation_params:

        Object containing the parameters regarding the ``pytest.main``
        invocation.

        Contains the following read-only attributes:

        * ``args``: tuple of command-line arguments as passed to ``pytest.main()``.
        * ``plugins``: list of extra plugins, might be None.
        * ``dir``: directory where ``pytest.main()`` was invoked from.
    """

