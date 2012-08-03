/*
 * Data for customers cube used in OLAP applications
 * This table is derived from the original log_events table
 * In the event that any customer definitions change, the structure and / or contents
 * of this table may need to be recalculated from the event_logs table 
 * Note: each line of data represents 1 visit
 */

# -----------------------------------------
# 	TABLE DEFINITION
# -----------------------------------------

CREATE TABLE IF NOT EXISTS customers_cube (
# Dimensions
	# Dimensions related to the customer
		`user_id` varchar(16) comment 'lookup',
		`first_visit_date` date,
		`email_address` varchar(30),
		`country` varchar(30),
	# Dimensions related to the visit
		# Descriptions of visit
			`visit_unique_id` varchar(25)
			`visit_counter` int,
			`stage_in_purchase_funnel_reached` ENUM('1. Add-to-basket', '2. Checkout', '3. Enter email', '4. Paypal', '5. Buy')
		# Marketing related metrics (i.e. referrer)
			/*
			 * Proposed model for incoming traffic fields (based on Google Analytics, subject to revision):
			 * 	mkt_medium is highest level: defines the type of marketing (organic, cpc, referrer, affiliate / cpa, cpm, email, lead-gen)
			 * 		-> note: for non-paid traffic we need to disinguish search (organic), social (social) and referrer (all others)
			 *  mkt_source is where the traffic came from (i.e. differentiate different organic by what search engine, different cpc by provider)
			 * 		-> note: for non-paid traffic
			 *  mkt_term is keywords (for search) - differentiate people from same source / medium
			 *  mkt_content is creative_id (e.g. email id, banner id, adwords text)
			 *
			 * mkt_campaign is orthogonal to the above: possible that one campaign spans many sources / mediums / keywords and creatives
			 * New fields added by SnowPlow:
			 * mkt_paid (some sources will be paid and others not, but having a dedicated field should make analysis easier)
			 * mkt_rank (for search - whether the paid ad was top ranked, or result was top rated)
			 * mkt_page (for search, what page on results)
			 */
				`mkt_source` varchar(255) comment 'lookup',
				`mkt_medium` varchar(255) comment 'lookup',
				`mkt_campaign` varchar(255) comment 'lookup',
				`mkt_term` varchar(255) comment 'lookup',
				`mkt_content` varchar(255) comment 'lookup',
				`mkt_paid` boolean,
				`mkt_rank` int,
				`mkt_page` int,
		# Description of technology used (IP address, device, browser, operating system)
			# Device
				`dvce_ismobile` boolean,
				`dvce_type` varchar(30) comment 'lookup',	
				`dvce_screenwidth` mediumint,
				`dvce_screenheight` mediumint,		
			# Operating system
				`os_name` varchar(30) comment 'lookup',
				`os_family` varchar(30) comment 'lookup',
				`os_manufacturer` varchar(30) comment 'lookup',
			# Browser		
				`br_name` varchar(30) comment 'lookup',
				`br_family` varchar(30) comment 'lookup',
				`br_version` varchar(30) comment 'lookup',
				`br_type` varchar(30) comment 'lookup',
				`br_renderengine` varchar(30) comment 'lookup',
				`br_lang` varchar(10) comment 'lookup',
				`br_features_pdf` boolean,
				`br_features_flash` boolean,
				`br_features_java` boolean,
				`br_features_director` boolean,
				`br_features_quicktime` boolean,
				`br_features_realplayer` boolean,
				`br_features_windowsmedia` boolean,
				`br_features_gears` boolean,
				`br_features_silverlight` boolean,


# Metrics
	# Metrics for each visit
		`page_views` int,
		`unique_pages_per_visit` int,
		`actions` int,
		`product_pages_visited` int,
		`unique_product_pages_visited` int,
		`add_to_baskets` int,
		`value_of_goods_added_to_basket` float,
		`revenue` float

) ENGINE=BRIGHTHOUSE DEFAULT CHARSET=utf8;

