"""
Algorithm presents the abstract base class for any Scheduling algorithm.
"""


from abc import ABC, abstractmethod


class Algorithm(ABC):
    """
    Abstract base class for all Scheduling Algorithms (used in the dynamic
    allocation by the 'scheduler').

    The Algorithm base class only requires the single `run()` method to be 
    implemented; the `to_df` may simply be used as a stubb. 

    Attributes
    ----------

    Notes
    -----
    It is important to note that the simulation will run with an 'incorrect' algorithm.
    An algorithm is 'incorrect' if it attempts to:

    - Allocate to a machine that is already occupied
    - Schedule a task to a machine that has already been scheduled. 

    These will raise RuntimeErrors. 

    It is also important for the algorithm to take into account 


    """

    def __init__(self):
        self.name = "AbstractAlgorithm"

    @abstractmethod
    def run(self, cluster, clock, plan, schedule):
        """

        Parameters
        ----------
        cluster: :py:obj:`~topsim.core.cluster.Cluster` 
            The cluster object for the simulation. 
        clock: int
            Current simulation time (usually generated by)
        plan
        schedule

        Returns
        -------

        """

        pass

    @abstractmethod
    def to_df(self):
        """
        Produce a Pandas DataFrame object to return current state of the
        scheduling algorithm

        Returns
        -------
        df : pandas.DataFrame
            DataFrame with current state
        """
