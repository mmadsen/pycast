#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Copyright (c) 2012 Christian Schwarz
#
#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from pycast.errors import BaseErrorMeasure

class MeanSquaredError(BaseErrorMeasure):
    """Implements the mean squared error measure.

    Explanation:
        http://en.wikipedia.org/wiki/Mean_squared_error

    @todo implement calculate
    """

    def calculate(self, startingPercentage, endPercentage):
        """This is the error calculation function that gets called by get_error().

        Both parameters will be correct at this time.

        @param startingPercentage Defines the start of the interval. This has to be a float value in [0.0, 100.0].
                             It represents the value, where the error calculation should be started. 
                             25.0 for example means that the first 25%% of all calculated errors will be ignored.
        @param endPercentage      Defines the end of the interval. This has to be a float value in [0.0, 100.0].
                             It represents the vlaue, after which all error values will be ignored.
                             90.0 for example means that the last 10%% of all local errors will be ignored.

        @return Returns a float representing the error.
        """
        errorValues = self._get_error_values(startingPercentage, endPercentage)
        return float(sum(errorValues)) / float(len(errorValues))


    def local_error(self, originalValue, calculatedValue):
        """Calculates the error between the two given values.

        @param originalValue   Value of the original data.
        @param calculatedValue Value of the calculated TimeSeries that
                               corresponds to originalValue.

        @return Returns the squared error:
                (calculatedValue - originalValue)^2
        """
        return (calculatedValue - originalValue)**2