# Pollster

A Python wrapper for the [Pollster API](http://elections.huffingtonpost.com/pollster/api) 
which provides access to political opinion polling data and trend estimates from The Huffington Post.

## Installation

    pip install pollster

## Getting started
```.py
from pollster import Pollster
pollster = Pollster()
```
See the current estimate of the president's job approval
```.py
chart = pollster.charts(topic='obama-job-approval')[0]
chart.estimate()
```
List charts about 2012 Senate races
```.py
pollster.charts(topic='2012-senate')
```
List charts about Wisconsin
```.py
pollster.charts(state='WI')
```
Calculate the margin between Obama and Romney from a recent general election poll
```.py
poll = pollster.polls(chart='2012-general-election-romney-vs-obama')[0]
question = [x['subpopulations'][0] for x in poll.questions if x['chart'] == '2012-general-election-romney-vs-obama'][0]
obama = [x for x in question['responses'] if x['choice'] == 'Obama'][0]
romney = [x for x in question['responses'] if x['choice'] == 'Romney'][0]
obama['value'] - romney['value']
```
See the methodology used in recent polls about the Affordable Care Act
```.py
chart = pollster.chart(slug='us-health-bill')
[[x.pollster, x.method] for x in chart.polls()]
```
## Authors

- Aaron Bycoffe, bycoffe@huffingtonpost.com

## Copyright

Copyright © 2012 The Huffington Post. See LICENSE for details.
