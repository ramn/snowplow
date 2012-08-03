# -----------------------------------------
# 	ETL from log_events
# -----------------------------------------

SELECT
	# DIMENSIONS
		# Dimensions related to the customer
			user_id,
			MIN(dt) AS first_visit_date,
			NULL AS email_address, # TO WRITE: base on ev_value WHERE ev_action = 'enter_email'  
			NULL AS country, # TO WRITE: base on Maxmind lookup
		# Dimensions related to the visit
			# Descriptions of visit		
				CONCAT(user_id, "-", visit_id) AS visit_unique_id,
				visit_id AS visit_counter,
				NULL AS stage_in_purchase_funnel_reached, # TO WRITE: base on parsing ev_action fields and page_url fields for a particular visit
			# Marketing related metrics (i.e. referrer)
				NULL AS mkt_source, # TO WRITE: base on values for first line of data in logs for each visit
				NULL AS mkt_medium, 
				NULL AS mkt_campaign,
				NULL as mkt_term,
				NULL AS mkt_content,
				NULL AS mkt_rank,
				NULL AS mkt_page,
			# Description of technology used (IP address, device, browser, operating system)
				# Device
					MAX(dvce_ismobile) AS dvce_ismobile,
					MAX(dvce_type) AS dvce_type,
					MAX(dvce_screenwidth) AS dvce_screenwidth,
					MAX(dvce_screenheight) AS dvce_screenheight,			
				# Operating system
					MAX(os_name) AS os_name,
					MAX(os_family) AS os_family,
					MAX(os_manufacturer) AS os_manufacturer,
				# Browser
					MAX(br_name) AS br_name,
					MAX(br_family) AS br_family,
					MAX(br_version) AS br_version,
					MAX(br_type) AS br_type,
					MAX(br_renderengine) AS br_renderengine,
					MAX(br_lang) AS br_lang,
					MAX(br_features_pdf) AS br_features_pdf,
					MAX(br_features_flash) AS br_features_flash,
					MAX(br_features_java) AS br_features_java,
					MAX(br_features_director) AS br_featurse_director,
					MAX(br_features_quicktime) AS br_features_quicktime,
					MAX(br_features_realplayer) AS br_features_realplayer,
					MAX(br_features_windowsmedia) AS br_features_windowsmedia,
					MAX(br_features_gears) AS br_features_gears,
					MAX(br_features_silverlight) AS br_features_silverlight,
	# METRICS
		NULL AS page_views # need to count all rows WHERE page_url IS NOT NULL
		COUNT(*) AS actions,
		COUNT(DISTINCT(page_url)) - 1 as unique_pages_per_visit,
		NULL as of_add_to_baskets, # based on COUNT where ev_action = add-to-basket
		NULL as value_of_goods_added_to_basket, # base on sum of ev_value where ev_action = 'add-to-basket' - sum of ev_value where ev_action = 'remove_from_basket'
		NULL as revenue # base on sum of ev_value where ev_action = 'order-confirmation'
		


FROM log_events
GROUP BY user_id, visit_id