import time
from api.moduls.functions import file_records
import threading

def api_data_rewriteDecorators(fun):
    def _wrapper(request):
        """"
        TODO: Decorator - runs 2 tasks in parallel
        """
        global _event
        try:
            _event = fun(request)

        except (ValueError):
            time.sleep(1)
            _event = fun(request)

        finally:
            def task2(_evnt):
                """
                TODO: This's run up a second task in parallel
                """
                _evnt.set()
                file_records()
            #
            _evnt = threading.Event()
            thread2 = threading.Thread(target=task2, args=(_evnt, ))
            thread2.start()

            return _event
    return _wrapper
