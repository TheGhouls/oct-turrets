import time

from base import BaseTurret
from canon import Canon


class Turret(BaseTurret):
    """This class represent the classic turret for oct
    """
    def start(self):
        """Start the turret and wait for the master to run the test
        """
        while self.start_loop:
            msg = self.master_publisher.recv_json()
            if 'command' in msg and msg['command'] == 'start':
                print("Starting the test")
                self.start_time = time.time()
                self.start_loop = False
                data = self.build_status_message('running')
                self.results_collector.send_json(data)
                self.run()
            elif 'command' in msg and msg['command'] == 'status_request':
                print("responding to master")
                data = self.build_status_message('ready')
                self.results_collector.send_json(data)

    def run(self):
        """The main run method
        """
        if 'rampup' in self.config:
            timeout = float(self.config['rampup'] / self.config['canons']) * 1000
        else:
            timeout = 10
        while self.run_loop:
            if len(self.canons) <= self.config['canons']:
                canon = Canon(self.start_time, self.config['run_time'], self.script_module)
                canon.daemon = True
                self.canons.append(canon)
                canon.start()
            else:
                timeout = None
            socks = dict(self.poller.poll(timeout))
            if self.master_publisher in socks:
                print(self.master_publisher.recv_json())
            if self.local_result in socks:
                self.results_collector.send_json(self.local_result.recv_json())
        for i in self.canons:
            i.join()
        data = self.build_status_message('ready')
        self.results_collector.send_json(data)
        self.start_loop = True
        self.start()
