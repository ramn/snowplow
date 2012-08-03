


CREATE TABLE "public"."log_events" (
	"dt" date DEFAULT NULL,
	"tm" time(6) DEFAULT NULL,
	"txn_id" int4 DEFAULT NULL,
	"user_id" text DEFAULT NULL,
	"user_ipaddress" text DEFAULT NULL,
	"visit_id" int2 DEFAULT NULL,
	"page_url" text DEFAULT NULL,
	"page_title" text DEFAULT NULL,
	"page_referrer" text DEFAULT NULL,
	"mkt_source" text DEFAULT NULL,
	"mkt_medium" text DEFAULT NULL,
	"mkt_campaign" text DEFAULT NULL,
	"mkt_content" text DEFAULT NULL,
	"mkt_name" text DEFAULT NULL,
	"ev_category" text DEFAULT NULL,
	"ev_action" text DEFAULT NULL,
	"ev_label" text DEFAULT NULL,
	"ev_property" text DEFAULT NULL,
	"ev_value" text DEFAULT NULL,
	"br_name" text DEFAULT NULL,
	"br_family" text DEFAULT NULL,
	"br_version" text DEFAULT NULL,
	"br_type" text DEFAULT NULL,
	"br_renderengine" text DEFAULT NULL,
	"br_lang" text DEFAULT NULL,
	"br_features_pdf" bool DEFAULT NULL,
	"br_features_flash" bool DEFAULT NULL,
	"br_features_java" bool DEFAULT NULL,
	"br_features_director" bool DEFAULT NULL,
	"br_features_quicktime" bool DEFAULT NULL,
	"br_features_realplayer" bool DEFAULT NULL,
	"br_features_windowsmedia" bool DEFAULT NULL,
	"br_features_gears" bool DEFAULT NULL,
	"br_features_silverlight" bool DEFAULT NULL,
	"br_cookies" bool DEFAULT NULL,
	"os_name" text DEFAULT NULL,
	"os_family" text DEFAULT NULL,
	"os_manufacturer" text DEFAULT NULL,
	"dvce_type" text DEFAULT NULL,
	"dvce_ismobile" bool DEFAULT NULL,
	"dvce_screenwidth" int4 DEFAULT NULL,
	"dvce_screenheight" int4 DEFAULT NULL
	)
WITH (OIDS=FALSE)
;

ALTER TABLE "public"."events" OWNER TO "postgres";;
