/*
 * Data for customers cube used in OLAP applications
 * This table is derived from the original log_events table
 * In the event that any customer definitions change, the structure and / or contents
 * of this table may need to be recalculated from the event_logs table 
 *
 */

CREATE TABLE IF NOT EXISTS customers_cube (
# Dimensions
	# Dimensions related to the customer
		`user_id` varchar(16) comment 'lookup'
		`first_visit_date` date,
	# Dimensions related to the visit
		# Marketing related metrics (i.e. referrer)
			# Fields for paid traffic. (Can we appropriate the same fields for organic / referral?)
				`mkt_source` varchar(255) comment 'lookup',
				`mkt_medium` varchar(255) comment 'lookup',
				`mkt_campaign` varchar(255) comment 'lookup',
				`mkt_term` varchar(255) comment 'lookup',
				`mkt_content` varchar(255) comment 'lookup',

# Metrics
	# Metrics for each visit
		`page_views` int,
		`actions` int,
		`number_of_product_pages_visited` int,
		`stage_in_purchase_funnel` ENUM('stage1', 'stage2', 'stage3', 'stage4', 'stage5')
		`number_of_add_to_baskets` int,
		`value_of_goods_added_to_basket` float,
		`revenue` float

);