from pybatfish.client.commands import *
from pybatfish.question.question import load_questions, list_questions
from pybatfish.question import bfq

load_questions()

NETWORK_NAME = "example_network"
SNAPSHOT_NAME = "example_snapshot"
SNAPSHOT_PATH = "network/"

bf_set_network(NETWORK_NAME)
bf_init_snapshot(SNAPSHOT_PATH, name=SNAPSHOT_NAME, overwrite=True)

ip_owners_ans = bfq.ipOwners().answer()
ip_owners_ans.frame().head()
