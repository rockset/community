#!/usr/bin/env python3
"""
Utility to create a new Rockset collection on a csv dataset in s3
"""

import yaml
from argparse import ArgumentParser
from rockset import Client


def get_columns(schema):
    csv_column_names = []
    csv_column_types = []
    for field in schema:
        fname, ftype = field.split("::")
        csv_column_names.append(fname)
        csv_column_types.append(ftype)
    return csv_column_names, csv_column_types


def create_collection(args):
    if args.profile:
        rs = Client(profile=args.profile)
    else:
        rs = Client()

    with open(args.schema, 'r') as f:
        schema = yaml.full_load(f)
        field_types = schema['field_types']
        clustering_fields = schema.get('clustering_key')
    column_names, column_types = get_columns(field_types)
    format_params = rs.Source.csv_params(
        separator=args.separator,
        encoding='UTF-8',
        first_line_as_column_names=False,
        column_names=column_names,
        column_types=column_types
    )
    sources = [
        rs.Source.s3(
            bucket=args.s3_bucket,
            prefix=args.s3_prefix,
            format_params=format_params
        )
    ]

    if clustering_fields:
        clustering_key = [
            rs.ClusteringKey.clusteringField(field_name=cf, cluster_type='AUTO')
            for cf in clustering_fields
        ]
        rs.Collection.create(
            name=args.collection,
            workspace=args.workspace,
            sources=sources,
            clustering_key=clustering_key
        )
    else:
        rs.Collection.create(
            name=args.collection,
            workspace=args.workspace,
            sources=sources,
        )

    print(
        'Successfully created collection {}.{}'.format(
            args.workspace, args.collection
        )
    )


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '--collection',
        '-c',
        required=True,
        help='The name of the collection to create'
    )
    parser.add_argument('--workspace', '-w', default='commons')
    parser.add_argument(
        '--schema',
        '-s',
        required=True,
        help='The yaml schema file for the collection'
    )
    parser.add_argument(
        '--s3-bucket', required=True, help='The s3 bucket of the dataset'
    )
    parser.add_argument(
        '--s3-prefix',
        required=True,
        help='The object prefix in the s3 bucket of the dataset'
    )
    parser.add_argument(
        '--separator', default='|', help='The separator for the data files'
    )
    parser.add_argument(
        '--profile',
        '-p',
        help=
        'If specified use this Rockset profile, otherwise use the default (see `rock configure ls`)'
    )
    args = parser.parse_args()
    create_collection(args)


if __name__ == "__main__":
    main()
