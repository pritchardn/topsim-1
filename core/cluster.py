import json
from core.machine import Machine
from queue import Queue, PriorityQueue


class Cluster(object):
	def __init__(self, machines):
		self.machines = []
		self._add_machines(machines)
		self.running_tasks = []
		self.finished_tasks = []
		self.waiting_tasks = []
		# self.workflows = []  # Keeping here to stop runtime errors
		self.finished_workflows = []

	def _add_machines(self, machine_config):
		machines = _process_machine_config(machine_config)
		for machine in machines:
			self.machines.append(machine)


# Helper function that acts as static function for Cluster
def _process_machine_config(machine_config):
	with open(machine_config, 'r') as infile:
		config = json.load(infile)
	machines = config['system']['resources']
	machine_list = []
	for machine in machines:
		machine_list.append(Machine(
			machine,
			machines[machine]['flops'],
			1,
			1,
		))
	return machine_list

