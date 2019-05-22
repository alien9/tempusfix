#!/usr/bin/env python2

# -*- coding: utf-8 -*-


import re,mysql.connector, datetime
from db import *

cursor = cnx.cursor(buffered=True)
cursor.execute("SELECT p.id, p.post_content, p.post_title, p.post_type, m.meta_value from wp_posts p join wp_postmeta m on m.post_id=p.id where m.meta_key='air_video_link'", ())
r=cursor.fetchall()
for row in r:
	#print(row)
	m=re.search('"([^"]+.png)"', row[1])
	url = None
	if m:
		url=m.group(1)
	else:
		m=re.search('"([^"]+.jpe?g)"', row[1])
		if m:
			url=m.group(1)
		else:
			print("image not found %s" % (row[0]))
	if url is not None:
		print(url)
		print("SELECT p.id from wp_posts p where p.guid='%s'"%(url))
		cursor.execute("SELECT p.id from wp_posts p where p.guid='%s'"%(url))
		s=cursor.fetchone()
		
		if s is not None:
			print("id %s" % (s[0]))
			id=s[0]
		else:
			date=datetime.datetime.now();
			cursor.execute("INSERT INTO wp_posts (post_author, post_date, post_modified, post_date_gmt, post_modified_gmt,post_title, post_name, guid, post_type, post_mime_type, post_content, post_excerpt, to_ping, pinged, post_content_filtered) VALUES (1, '%s','%s','%s','%s','%s','%s','%s','attachment','image/png', '', '', '','','')" % (date, date, date, date, url, url, url))
			cnx.commit()
			
		print(s)

"""
	cursor.execute("update wp_posts set post_type='portfolio-item' where id=%s"%(row[0]))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_post_gallery_layout', 'classic-gallery'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_gallery_fullwidth', 'off'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_post_primarygallery_layout', 'slider-gallery'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_gallery_layout', 'slider-gallery'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_show_infobutton', 'on'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_video_link', row[4]))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_show_aslightbox', 'on'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_featured_gallery_style', 'style-3x3'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_featured_gallery', 'off'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_preview_size', 'size-1x1'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_portfolio_title', 'on'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_portfolio_filters', 'a:1:{i:48;s:2:"48";}'))
	cursor.execute("insert into wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, '%s', '%s')" % (row[0], 'tempus_title_style', 'titlestyle-left'))
	cnx.commit()
"""
