import logging
from colours import colours


PERROR_LEVEL_NUM = 45
PWARNING_LEVEL_NUM = 35
PINFO_LEVEL_NUM = 25

PERROR_FMT = colours.FAIL + '[ ERROR ]: %(message)s' + colours.ENDC
PWARNING_FMT = colours.WARNING + '[ WARNING ]: %(message)s' + colours.ENDC
PINFO_FMT = colours.INFO + '[ INFO ]: %(message)s' + colours.ENDC
STD_FMT = '%(message)s'
DEBUG_FMT = '%(levelname)7s: %(message)s'

log = logging.getLogger('suprc')


class MyFormatter(logging.Formatter):
    def __init__(self, fmt=(DEBUG_FMT)):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        format_orig = self._fmt

        if record.levelno == PERROR_LEVEL_NUM:
            self._fmt = PERROR_FMT
        elif record.levelno == PWARNING_LEVEL_NUM:
            self._fmt = PWARNING_FMT
        elif record.levelno == PINFO_LEVEL_NUM:
            self._fmt = PINFO_FMT
        elif record.levelno >= logging.WARNING:
            self._fmt = STD_FMT

        result = logging.Formatter.format(self, record)

        self._fmt = format_orig
        return result


def init_logging(verbosity):
    """ Set up core logging """
    handler = logging.StreamHandler()
    log.setLevel(verbosity)

    """ Define custom levels & formats for our plugin logging """
    logging.addLevelName(PERROR_LEVEL_NUM, "PERROR")
    logging.addLevelName(PWARNING_LEVEL_NUM, "PWARNING")
    logging.addLevelName(PINFO_LEVEL_NUM, "PINFO")

    logging.Logger.pError = _perror
    logging.Logger.pWarning = _pwarning
    logging.Logger.pInfo = _pinfo

    formatter = MyFormatter()

    handler.setFormatter(formatter)
    log.addHandler(handler)


def _perror(self, message, *args, **kwargs):
    if self.isEnabledFor(PERROR_LEVEL_NUM):
        self._log(PERROR_LEVEL_NUM, message, args, **kwargs)


def _pwarning(self, message, *args, **kwargs):
    if self.isEnabledFor(PWARNING_LEVEL_NUM):
        self._log(PWARNING_LEVEL_NUM, message, args, **kwargs)


def _pinfo(self, message, *args, **kwargs):
    if self.isEnabledFor(PINFO_LEVEL_NUM):
        self._log(PINFO_LEVEL_NUM, message, args, **kwargs)
