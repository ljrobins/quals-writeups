Orbit Determination Past Problems
=================================

Fall 2023
---------

Problem Statement
~~~~~~~~~~~~~~~~~

Assume an object in a highly eccentric inclined orbit (HEO) around the
Earth. The object is reported in its Cartesian state space with a mean
:math:`[x_1,x_2,x_3,v_1,v_2,v_3]` and the second moment :math:`\Sigma`
in an inertial coordinate frame.

#. The coordinates are reported in J2000. How is that frame defined.
   What is the motivation for it? Transform into the coordinates that
   you would need to report to your sensor. Define your sensor location.
   Distinguish between the geocentric and geodetic coordinates
   explicitly.

#. Write out the second moment in the correct form with units S
   explicitly assuming the state (mean and second moment) have been
   propagated through an Extended Kalman filter since the last
   measurement. What probability density distribution does your object
   have? Hypothesize concrete values, justify all your assumptions and
   answers quantitatively and qualitatively.

#. You have the chance to observe the HEO object using a ground-based
   sensor.

   #. At which anomaly of the orbit are you choosing to observe? Justify
      all your answers qualitatively and quantitatively and explicate
      any assumptions.

   #. You are determining a circular orbit with your chosen
      observations. Compute explicitly the error that is inherent in
      that orbit determination.

   #. Your orbit has significant uncertainty, how does the uncertainty
      manifest in your circular orbit detemination? Compute explicitly.

#. Assume in a ground-based sensor you can only make measurements of the
   velocity components of an Earth-orbiting space object. Device an
   initial orbit determination method for this case. Explicate any
   assumptions and limitations of your method.

Solution
~~~~~~~~
