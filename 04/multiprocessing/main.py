import sys
import time
import logging
from multiprocessing import Process, Queue


LOG_FORMAT = '%(asctime)s | %(process)d | %(levelname)s | %(message)s'
logging.basicConfig(
    filename='multiprocessing.log',
    filemode='w',
    format=LOG_FORMAT,
    level=logging.INFO
)
LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(stream=sys.stdout))


def _producer(queue: Queue, interval: int, number_or_messages: int) -> None:
    for i in range(number_or_messages):
        LOG.info(f'Message #{i}')
        queue.put(f'Message #{i}')
        time.sleep(interval)
    LOG.info('Producer Finished')


def _consumer(queue: Queue, sampling_rate: int, no_of_unsuccessful_read: int) -> None:
    no_of_try = 0
    while no_of_try < no_of_unsuccessful_read:
        if not queue.empty():
            no_of_try = 0
            LOG.info(queue.get())
        else:
            LOG.info(f'Unsuccessful Read, Try #{no_of_try}')
            no_of_try += 1
        time.sleep(sampling_rate)
    LOG.info('Consumer Finished')


if __name__ == '__main__':
    queue = Queue()
    producer = Process(target=_producer, args=(queue, 2, 10))
    consumer = Process(target=_consumer, args=(queue, 1, 3))
    producer.start()
    LOG.info('Start Producer')
    consumer.start()
    LOG.info('Start Consumer')
    producer.join()
    LOG.info('Join Producer')
    consumer.join()
    LOG.info('Join Consumer')
    # consumer.kill()
