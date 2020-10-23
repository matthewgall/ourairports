ourairports
===========

ourairports is a functional wrapper around the
`ourairports.com <https://ourairports.com>`__ public domain
`datasets <https://ourairports.com/data/>`__

Installation
------------

Simply run:

::

   $ pip install ourairports

Usage
-----

Get airport information by ICAO identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   from ourairports import OurAirports
   airports = OurAirports().getAirportsByICAO('EGFF')

Get airport information by IATA identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   from ourairports import OurAirports
   airports = OurAirports().getAirportsByIATA('CWL')

Get airport information by distance from latitude/longitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   from ourairports import OurAirports
   airports = OurAirports().getAirportsByDistance('51.5007325', '-0.1268141', 25)
   for port in airports:
       print port.name

License
-------

This project is hereby released under the terms of the MIT License, and
is included below

::

   MIT License

   Copyright (c) 2020 Matthew Gall

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

Data Disclaimer
---------------

Data for ourairports is sourced from the
`ourairports.com <https://ourairports.com>`__ public datasets and
neither the author, nor the ourairports.com team provide any warranty of
any kind, express or implied, including but not limited to the
warranties of merchantability, fitness for a particular purpose,
accuracy, reliability or noninfringement of the data provided
