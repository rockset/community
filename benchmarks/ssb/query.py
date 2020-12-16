#!/usr/bin/env python3
"""
Utility to run queries against Rockset
"""

import os
import time
import statistics

from argparse import ArgumentParser
from rockset import Client, Q


def run(args):
    if args.profile:
        rs = Client(profile=args.profile)
    else:
        rs = Client()

    queries = []
    for f in os.listdir(args.query_dir):
        if not f.endswith('.sql'):
            continue
        query_id = os.path.splitext(f)[0]
        with open(os.path.join(args.query_dir, f), 'r') as f:
            query_str = f.read()
        queries.append((query_id, query_str))
    queries = sorted(queries)
    print(
        'Found {} queries to run. Will run each {} times and take the median'
        ' runtime.'.format(len(queries), args.runs)
    )
    print('=' * 70)

    for query_id, query_str in queries:
        times = []
        rows = None
        error = False
        for _ in range(args.runs):
            start = time.time()
            try:
                resp = rs.sql(Q(query_str))
                if rows is None:
                    rows = len(resp.results())
                else:
                    assert rows == len(resp.results())
                times.append(1000 * (time.time() - start))
            except Exception as e:
                print('Query {} produced an error: {}'.format(query_id, str(e)))
                error = True
                break
        if not error:
            print(
                'Query {} produced {:>3d} rows in {:>5.0f} ms'.format(
                    query_id, rows, statistics.median(times)
                )
            )


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--query-dir',
        '-d',
        required=True,
        help='The directory of queries to run'
    )
    parser.add_argument(
        '--runs',
        '-r',
        default=3,
        type=int,
        help=
        'How many times to run the query in a row and take a median of the runtimes'
    )
    parser.add_argument(
        '--profile',
        '-p',
        help=
        'If specified use this Rockset profile, otherwise use the default (see `rock configure ls`)'
    )
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()
