from mara_schema.schema import DataSet, Aggregation

from app.schema.entities.product import product_entity

product_data_set = DataSet(
    entity=product_entity,
    name='Products',
    max_entity_link_depth=1)

product_data_set.add_simple_metric(
    name='# Products',
    description='The number of products',
    aggregation=Aggregation.COUNT,
    column_name='product_id')
product_data_set.add_simple_metric(
    name='# Orders',
    description='The number of orders containing this product',
    aggregation=Aggregation.SUM,
    column_name='number_of_orders')
product_data_set.add_simple_metric(
    name='# Order items',
    description='The number of items referencing this product',
    aggregation=Aggregation.SUM,
    column_name='number_of_order_items')
product_data_set.add_simple_metric(
    name='# Customers',
    description='The number of customers that bought this product',
    aggregation=Aggregation.SUM,
    column_name='number_of_customers')
product_data_set.add_simple_metric(
    name='Revenue (all time)',
    description='All time revenue generated by this product',
    aggregation=Aggregation.SUM,
    column_name='revenue_all_time')
product_data_set.add_simple_metric(
    name='Total freight value',
    description='Total freight value',
    aggregation=Aggregation.SUM,
    column_name='total_freight_value')