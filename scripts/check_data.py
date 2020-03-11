# -*- coding: utf-8 -*-
"""
Created on 2017-10-04

@author: dougashton
"""

# %% setup

import sdg

def main():
    """Run csv checks on all indicator csvs in the data directory"""
    status = True

    status = status & sdg.open_sdg_check()
    status = status & sdg.open_sdg_check()

    return status

if __name__ == '__main__':
    status = main()
    if(not status):
        raise RuntimeError("Failed checks")
    else:
        print("Success")
