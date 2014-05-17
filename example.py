#!/usr/bin/env python

"""An optparse_mooi example - options are a combination of rsync and git-annex."""


from optparse import *
from optparse import OptionParser, OptionGroup, Option
from optparse_mooi import CompactHelpFormatter, CompactColorHelpFormatter


description = '''\
Rsync is a file transfer program capable of efficient remote update
via a fast differencing algorithm.\
'''

parser = OptionParser(
    # formatter       = CompactHelpFormatter(
    #     align_long_opts=True,
    #     width = 80,
    #     metavar_column = 17,
    # ),

    formatter       = CompactColorHelpFormatter(
        align_long_opts = True,
        metavar_column  = 17,
        shopt_color   = 'white-bold',
        lopt_color    = 'white-bold',
        metavar_color = 'green-bold',
        help_color    = 'red-bold',
        option_colormap = {
            ('--force', ): (None, None, None, 'red'),
        }
    ),
    description     = description,
    add_help_option = False
)

general_options = OptionGroup(parser, 'General options')
remote_options  = OptionGroup(parser, 'Remote options')
command_options = OptionGroup(parser, 'Command options')
log_options     = OptionGroup(parser, 'Logging options')

o = general_options.add_option
o('-h', '--help',      action='help',       help='show this help message and exit'),
o('-F', '--fast',      action='store_true', help='avoid slow operations'),
o('-a', '--auto',      action='store_true', help='automatic mode'),
o('-q', '--quiet',     action='store_true', help='avoid verbose output'),
o('-v', '--verbose',   action='store_true', help='allow verbose output'),
o('-j', '--json',      action='store_true', help='enable json output'),
o('-d', '--debug',     action='store_true', help='show debug messages'),
o('-b', '--backend',   action='store',      help='specify key-value backend to use'),
o('-c', '--config',    action='store',      help='override git configuration setting'),
o('',   '--force',     action='store_true', help='allow actions that may lose annexed data'),

o = remote_options.add_option
o('-n', '--numcopies', action='store',      help='override default number of copies')
o('',   '--trust',     action='store',      help='override trust setting')
o('',   '--semitrust', action='store',      help='override trust setting back to default')
o('',   '--untrust',   action='store',      help='override trust setting to untrusted')
o('-i', '--in',        action='store',      help='skip files not present in remote')
o('-x', '--exclude',   action='store',      help='skip files matching glob pattern')
o('-I', '--include',   action='store',      help='don\'t skip files matching glob pattern')
o('-C', '--copies',    action='store',      help='skip files with fewer copies')
o('-B', '--inbackend', action='store',      help='skip files not using a key-value backend')

o = command_options.add_option
o('-f', '--from',      action='store',      help='source remote')
o('-t', '--to',        action='store',      help='destination remote')

o = log_options.add_option
o('',   '--since',     action='store',      help='show log since date')
o('',   '--after',     action='store',      help='show log after date')
o('',   '--until',     action='store',      help='show log until date')
o('',   '--before',    action='store',      help='show log before date')
o('-m', '--max-count', action='store',      help='limit number of logs displayed')
o('',   '--gource',    action='store',      help='format output for gource')

parser.add_option_group(general_options)
parser.add_option_group(remote_options)
parser.add_option_group(command_options)
parser.add_option_group(log_options)

parser.print_help()
