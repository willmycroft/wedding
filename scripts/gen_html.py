#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:39:13 2019

@author: will
"""

import os

cd ~/wedding/wedding/images


html = """
<div class="ww-section bg-light" id="gallery">
  <div class="ww-photo-gallery">
    <div class="container">
      <h2 class="h1 text-center pb-3 ww-title" data-aos="zoom-in-down" data-aos-duration="1000">Photo Gallery</h2>
      <div class="col-md-12 text-center ww-category-filter mb-4">
	  <p style="text-align: justify; text-justify: inter-word;">
      		Text about video
	  </p>
      <a class="btn btn-outline-primary ww-filter-button" href="#" data-filter="all">All</a>
      {buttons}
     </div>
      <div class="ww-gallery" data-aos="fade-zoom-in" data-aos-easing="ease-in-back" data-aos-delay="300" data-aos-duration="1000" data-aos-offset="0">
        <div class="card-columns">
            {cards}
       </div>
      </div>
    </div>
  </div>
</div>
"""

button_template = """<a class="btn btn-outline-primary ww-filter-button" href="#" data-filter="{code}">{text}</a>"""
template = """<div class="card" data-groups="[&quot;{group}&quot;]"><a href="images/{path}" data-toggle="lightbox" data-gallery="ww-gallery"><img class="img-fluid" src="images/{path}"/></a></div>"""

groups = [
         {'folder': 'townhall', 'text': 'Town Hall'},
         {'folder': 'nhm', 'text': 'Natural History Museum'},
         {'folder': 'sabrinawill', 'text': 'Sabrina & Will'},
         ]

button_html = ''
card_html = ''
for g in groups:
    button_html += button_template.format(code=g['folder'], text=g['text'])
    for f in os.listdir(g['folder']):
        card_html += template.format(group=g['folder'], path=os.path.join(g['folder'], f))
        card_html += '\n'
        
import pyperclip
pyperclip.copy(html.format(buttons=button_html, cards=card_html))
