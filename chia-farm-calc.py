'''
Initial code by: alok_tripathy
Source: https://www.reddit.com/r/chia/comments/n1be6d/how_much_luck_do_you_need/

Updates by: Mike Spicer
'''

import sys
 
# Approx 16 blocks in 5m.
BLOCK_TIME_PERIOD_SECONDS = (5 * 60) / 16
PLOT_SIZE_GIB = 101.4
 
 
def netspace_share(netspace_tib: float, n_plots: int) -> float:
    """What's your share of the netspace?"""
    netspace_gib = netspace_tib * (2 ** 20)
    return n_plots * PLOT_SIZE_GIB / netspace_gib
 
 
def n_blocks_odds(netspace: float, plot_count: int, n: int) -> float:
    p = netspace_share(netspace, plot_count)
    return 1 - (1-p) ** n
 
 
def estimate(netspace: float, hours: range, plot_counts: list):
    print("\t".join(["plots➝"] + [str(pc) for pc in plot_counts]))
    for h in hours:
        n_blocks = int(round(h * 3600 / BLOCK_TIME_PERIOD_SECONDS))
        odds = [
            str(round(n_blocks_odds(netspace, pc, n_blocks)*100))+"%"
            for pc in plot_counts
        ]
        print("\t".join([f"{h} hr"] + odds))
 
 
if __name__ == "__main__":
    """python estimates.py <net space in PiB> <plot_count_a> <plot_count_b> ..."""
    netspace = float(sys.argv[1])
    plot_counts = [int(a) for a in sys.argv[2:]]
    estimate(netspace, hours=range(4, 76, 4), plot_counts=plot_counts)
