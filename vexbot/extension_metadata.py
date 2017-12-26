extensions = {'pip_install': {'path': 'vexbot.extensions.admin:install',
                              'short': 'Install packages using pip',},
              'pip_uninstall': {'path': 'vexbot.extensions.admin:uninstall',
                                'short': 'Uninstall packages using pip'},
              'pip_update': {'path': 'vexbot.extensions.admin:update',
                             'short': 'Update packages using pip'},
              'get_commands': {'path': 'vexbot.extensions.admin:get_commands',
                               'short': 'Get commands from command observer'},
              'get_command_modules': {'path': 'vexbot.extensions.admin:get_command_modules',
                                      'short': 'Get all the module names for the commands that are available'},
              'get_disabled': {'path': 'vexbot.extensions.admin:get_disabled',
                                'short': 'Get all disabled commands from command observer'},
              'disable': {'path': 'vexbot.extensions.admin:disable',
                          'short': 'Remove a command from the commands'},
              'get_cache': {'path': 'vexbot.extensions.admin:get_cache',
                            'short': 'Get the values of the configuration cache'},
              'delete_cache': {'path': 'vexbot.extensions.admin:delete_cache',
                               'short': 'Remove the values from the configuration cache'},
              'get_code': {'path': 'vexbot.extensions.develop:get_code',
                           'short': 'Get the source code from a method using the inspect module'},
              'get_method_names': {'path': 'vexbot.extensions.develop:get_members',
                                   'short': 'Get all the method names from a class using inspect module'},
              'get_size': {'path': 'vexbot.extensions.digitalocean:get_size',
                           'short': 'Get the size of a digital ocean droplet',
                           'extras': ['digitalocean',]},
              'power_off': {'path': 'vexbot.extensions.digitalocean:power_off',
                            'short': 'Power off a digital ocean droplet',
                           'extras': ['digitalocean',]},
              'power_on': {'path': 'vexbot.extensions.digitalocean:power_on',
                           'short': 'Power on a digital ocean droplet',
                           'extras': ['digitalocean',]},
              'log_level': {'path': 'vexbot.extensions.log:log_level',
                            'short': 'Set or get the root logger to a level'},
              'set_debug': {'path': 'vexbot.extensions.log:set_debug',
                            'short': 'Set the root logger to `logging.DEBUG'},
              'set_info': {'path': 'vexbot.extensions.log:set_info',
                           'short': 'Set the root logger to `logging.INFO'},
              'set_default': {'path': 'vexbot.extensions.log:set_default',
                              'short': 'Set the root logger to `logging.WARNING'},
              'filter_logs': {'path': 'vexbot.extensions.log:filter_logs',
                              'short': 'Filter logs'},
              'anti_filter': {'path': 'vexbot.extensions.log:anti_filter',
                              'short': 'Filter anything that is not this'},
              'get_all_droplets': {'path': 'vexbot.extensions.digitalocean:get_all_droplets',
                                   'short': 'Get all droplets from digital ocean',
                                   'extras': ['digitalocean',]},
              'add_extensions': {'path': 'vexbot.extensions.extensions:add_extensions',
                                 'short': 'Add an extension to a command observer'},
              'get_extensions': {'path': 'vexbot.extensions.extensions:get_extensions',
                                 'short': 'Get all the extensions from an observer instance'},
              'remove_extension': {'path': 'vexbot.extensions.extensions:remove_extension',
                                    'short': 'Remove an extension from an observer instance'},
              'get_installed_extensions': {'path': 'vexbot.extensions.extensions:get_installed_extensions',
                                           'short': 'See all installed extensions for Vexbot'},
              'get_installed_modules': {'path': 'vexbot.extensions.extensions:get_installed_modules',
                                        'short': 'See all installed modules for Vexbot'},
              'add_extensions_from_dict': {'path': 'vexbot.extensions.extensions:add_extensions_from_dict',
                                           'short': 'Used to intialize command observers efficient'},
              'help': {'path': 'vexbot.extensions.help:help',
                       'short': 'Get the help from a method'},
              'hidden': {'path': 'vexbot.extensions.hidden:hidden',
                         'short': 'Get all hidden method methods'},
              'bot_intents': {'path': 'vexbot.extensions.intents:get_intents',
                              'short': 'Get the intents from the bot'},
              'bot_intent': {'path': 'vexbot.extensions.intents:get_intent'},
              'get_google_trends': {'path': 'vexbot.extensions.news:get_hot_trends',
                                    'short': 'Get the google trends',
                                    'extras': ['summarization']},
              'get_news_urls': {'path': 'vexbot.extensions.news:get_popular_urls',
                                'extras': ['summarization']},
              'summarize_news_url': {'path': 'vexbot.extensions.news:summarize_article',
                                     'extras': ['summarization']},
              'start_process': {'path': 'vexbot.extensions.subprocess:start',
                                'extras': ['process_manager'],
                                'short': 'Start a process'},
              'stop_process': {'path': 'vexbot.extensions.subprocess:stop',
                                'extras': ['process_manager'],
                                'short': "Stop a process"},
              'restart_process': {'path': 'vexbot.extensions.subprocess:restart',
                                  'extras': ['process_manager'],
                                  'short': "Restart a process"},
              'status_process': {'path': 'vexbot.extensions.subprocess:status',
                                 'extras': ['process_manager'],
                                 'short': 'Get the status of a process'},
              'process_uptime': {'path': 'vexbot.extensions.subprocess:uptime',
                                 'extras': ['process_manager'],
                                 'short': 'Get the uptime of a process'},
              'cpu_count': {'path': 'vexbot.extensions.system:cpu_count',
                            'short': 'Show the total number of CPU\'s',
                            'extras': ['system']},
              'cpu_frequency': {'path': 'vexbot.extensions.system:cpu_frequency',
                                'extras': ['system']},
              'virtual_memory_percent': {'path': 'vexbot.extensions.system:virtual_memory_percent',
                                         'extras': ['system']},
              'virtual_memory_total': {'path': 'vexbot.extensions.system:virtual_memory_total',
                                       'short': 'Show the total amoun of virtual memory available in Mb\'s',
                                       'extras': ['system']},
              'virtual_memory_used': {'path': 'vexbot.extensions.system:virtual_memory_used',
                                      'short': 'Show the total amount of virtual memory in use in MBs',
                                      'extras': ['system']},
              'swap': {'path': 'vexbot.extensions.system:swap',
                       'short': 'Show the total amount of swap used in MB',
                       'extras': ['system']}}