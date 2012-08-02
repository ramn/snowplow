/*
 * Data for products cube used in OLAP applications
 * This table is derived from the original log_events table
 * In the event that any customer definitions change, the structure and / or contents
 * of this table may need to be recalculated from the event_logs table 
 * Note: each line of data represents one visit
 */

 CREATE TABLE IF NOT EXISTS products_cube (
 	# DIMENSIONS
 		# Product
	 		`product_sku` varchar(16) comment 'lookup',
	 		`product_name` varchar(255) comment 'lookup',
	 		`product_category` varchar(255) comment 'lookup',
	 		`page_url` varchar(2083), 
	 		`product_sku` varchar(16),
 		# Customer details
			`user_id` varchar(16) comment 'lookup',
			`visit_id` int,		

	 		`dt` date,
			`tm` time,
			`step_in_visit` int,
			`visit_referrer_source` varchar(255)
			`visit_referrer_medium` varchar(255)
			`visit_referrer_term` varchar(255)
			`visit_referrer_content` varchar(2083)
			`visit_referrer_campaign` varchar(255)
			`page_referrer` string # want to differentiate people who came to the site looking for this product, vs referrals from other product pages, vs referrals from menus
 	# METRICS
 		`page_views` int,
 		`add_to_baskets` int,
 		`number_bought` int,
 		`revenue` float 


 ) ENGINE BRIGHTHOUSE DEFAULT CHARSET=utf8;