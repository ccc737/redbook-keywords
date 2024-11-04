# !/usr/bin/env python
# coding: utf-8

import logging
from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

custom_theme = Theme({
    "log.time": "dim blue",
    "logging.level.debug": "cyan", 
    "logging.level.info": "green",
    "logging.level.warning": "yellow", 
    "logging.level.error": "bold red", 
    "logging.level.critical": "reverse bold red",
})

def configure_logger(logger_name: str = "default", debug: bool = False, log_file: str = None):
    console = Console(theme=custom_theme)
    rich_handler = RichHandler(console=console, show_time=True, show_path=False)
    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    rich_handler.setFormatter(formatter)
    handlers = [rich_handler]
    if log_file:
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)
        
    if debug:
        logger_level = logging.DEBUG
    else:
        logger_level = logging.INFO
        
    logging.basicConfig(
        level=logger_level,
        handlers=handlers
    )
    
    return logging.getLogger(logger_name)

# Non strict singleton mode returns this logger
class GetLogger:
    _instance = {}
    
    def __new__(cls, logger_name="rich", debug=True, log_file=None):
        if logger_name not in cls._instance:
            cls._instance[logger_name] = configure_logger(logger_name, debug, log_file)
        return cls._instance[logger_name]

    def __init__(self):
        pass
