from src.TouristInitSpec import TouristInitSpec
from src.status import *
from src.Timer import Timer

def findAllPaths(node, childrenFn, depth, _depth=0, _parents={}):
    if _depth == depth - 1:
        # path found with certain length, create path and stop traversing
        path = []
        parent = node
        for i in range(depth):
            path.insert(0, parent)
            if not parent in _parents:
                continue
            parent = _parents[parent]
            if parent in path:
                return # this path is cyclic, forget
        yield path
        return

    for nb in childrenFn(node):
        _parents[nb] = node # keep track of where we came from
        for p in findAllPaths(nb, childrenFn, depth, _depth + 1, _parents):
            yield p

class Tourist:

    TO_VISIT = True
    NOT_VISIT = False

    def __init__(self, init_spec):

        assert_type(init_spec, TouristInitSpec)

        # model
        self.model = init_spec.model
        # age group
        self.age_group = init_spec.age_group
        # speed
        self.speed = init_spec.speed
        # time_budget
        self.time_budget = init_spec.time_budget
        # path eval distance
        self.path_eval_dist = init_spec.path_eval_dist

        # init status
        # NOte: single entrance Node - Special Case
        entering_node = Node("entering_node_id", "entering_node_name")
        self._status = EnteringStatus(entering_node)

        # action count down
        self._action_count_down = Timer(0)

    @property
    def status(self):
        return self._status

    @property
    def action_count_down(self):
        return self._action_count_down

    @action_count_down.setter
    def action_count_down(self, value):
        self._action_count_down = value

    """
    --- Status Control Section ----
    """

    # Leaving Statues control
    @property
    def is_leaving(self):
        return self.status.name == STATUS.LEAVING

    # Change to Leaving Status
    # TODO
    def to_leave(self, evac_path):
        assert_path(evac_path)
        pass

    # Proceed Leave
    # TODO:
    def leave(self):
        pass

    # Entering Status Control
    @property
    def is_entering(self):
        return self.status.name == STATUS.ENTERING

    # TODO
    def enter(self):
        pass

    # moving status control
    @property
    def is_moving(self):
        return self.status.name == STATUS.MOVING

    # TODO
    def to_move(self, target_node):
        assert_node(target_node)
        pass

    # TODO
    def move(self):
        pass

    # visiting status control
    @property
    def is_visiting(self):
        return self.status.name == STATUS.VISITING

    # TODO
    def to_visit(self, target_node):
        assert_node(target_node)
        pass

    # TODO
    def visit(self):
        pass

    """
    ---- Processing & Algorithms ----
    """

    # TODO
    def calculate_evac_path(self):
        pass

    def calculate4_visit_decision(self):
        pass

    def calculate_next_move_target(self,node):
            optional_paths= []
            self.node=node
            self.previous_node=None
            print("current node: %d" % self.node)
            for depth in range(2,6):
                for p in findAllPaths(self.node, lambda a:graph[a], depth):#if depth ==1, stay at node
                    if p[1] != self.previous_node: #no return
                        optional_paths.append(p)

            if not optional_paths:
                print("no option")
            else:
                a=[]
                for i in optional_paths:
                    a.append(sum(i))
                index, item = max(enumerate(a), key=operator.itemgetter(1))
                target = optional_paths[index][1]
                print("next target:", target)
                print(optional_paths)
                #self.node=target
                #self.calculate_next_move_target(self.node)
    """
    ---- Act - Tourist main process ----
    """

    # TODO
    def act(self):
        # Model specified tick step, used to proceed internal timer
        tick_step = self.model.tick_step
        self.time_budget.forward(tick_step)
        self.action_count_down.forward(tick_step)

        if self.time_budget.is_exhausted():
            if self.status.name != STATUS.LEAVING:
                eval_path = self.calculate_evac_path()
                self.to_leave(eval_path)
            else:
                self.leave()
        else:
            if self.action_count_down.is_exhausted():
                # current action ends, re-calculation and decide status
                if self.status.name == STATUS.MOVING:

                    visit_decision = self.calculate4_visit_decision()
                    if visit_decision is Tourist.TO_VISIT:
                        # Moving ends
                        # visit node is the to_node from moving status
                        arriving_node = self.status.to_node
                        self.to_visit(arriving_node)
                    elif visit_decision is Tourist.NOT_VISIT:
                        # Continue Move
                        move_target_node = self.calculate_next_move_target()
                        self.to_move(move_target_node)
                    else:
                        raise ValueError("visit_decision value error, get %s" % visit_decision)

                elif self.status.name == STATUS.VISITING:
                    # visiting ends, find target to move
                    move_target_node = self.calculate_next_move_target()
                    self.to_move(move_target_node)

                elif self.status.name == STATUS.ENTERING:
                    # entering ends, find target to move
                    move_target_node = self.calculate_next_move_target()
                    self.to_move(move_target_node)

                else:
                    raise ValueError("Unhandled status transition case: %s" % self.status.name)

            elif not self.action_count_down.is_exhausted():
                if self.status.name == STATUS.MOVING:
                    self.move()
                elif self.status.name == STATUS.VISITING:
                    self.visit()
                elif self.status.name == STATUS.ENTERING:
                    self.enter()
                else:
                    raise ValueError("Unhandled status transition case: %s" % self.status.name)
