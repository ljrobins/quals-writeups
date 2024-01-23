Orbit Mechanics Past Problems
=============================

Problem 0
---------

Problem statement
~~~~~~~~~~~~~~~~~

In Keplerian mechanics, several important types of orbital maneuvers are
noncoplanar. For example, the capability to change both the ascending
node and the inclination with only one maneuver is efficient and can
widen the launch window.

Assume that the orbital elements for an Earth orbit are given. If the
orbit is circular both initially and after the maneuver, let
:math:`i_0=30^\circ`, :math:`i_f=90^\circ`, :math:`\Omega_o=0^\circ`,
:math:`\Omega_f=60^\circ`, where :math:`o` reflects the original orbit
and :math:`f` indicates a value in the final orbit.

#. Determine the appropriate maneuver location in each orbit.

#. If the circular orbit possesses a radius of :math:`4R_\oplus`,
   determine the magnitude of the required single impulse to accomplish
   the goal.

Solution
~~~~~~~~

We’ll define the “location” of the maneuver in the initial and final
orbits with the argument of latitude :math:`\theta_o` and
:math:`\theta_f`, the angle between the ascending node and the
spacecraft’s position vector. Because the orbits are circular, we can’t
really use the true anomaly. We can then form a spherical triangle with
side lengths :math:`\Omega_f - \Omega_o` along the equator, and then
:math:`\theta_i` extending upwards from the left at an angle of
:math:`i_0`, and :math:`\theta_f` extending upwards from the right at an
angle of :math:`i_f`.

Using the spherical law of sines, we can solve for :math:`\theta_o`:

.. math::

   \begin{aligned}
       \frac{\sin\theta_o}{\sin i_f} &= \frac{\sin(\Omega_f - \Omega_o)}{\sin\left(180^\circ-i_0-i_f\right)} \\
       \sin\theta_o &= \frac{\sin i_f \sin(\Omega_f - \Omega_o)}{\sin\left(180^\circ-i_0-i_f\right)} \\
   \end{aligned}

Plugging in values, we find:

.. math::

   \begin{aligned}
       \sin\theta_o &= \frac{\sin 90^\circ \sin(60^\circ - 0^\circ)}{\sin\left(180^\circ-30^\circ-90^\circ\right)} \\
       &= \frac{\sin 60^\circ}{\sin 60^\circ} \\
       &= 1 \\
       \theta_o &= 90^\circ
   \end{aligned}

And similarly for :math:`\theta_f`:

.. math::

   \begin{aligned}
       \frac{\sin\theta_f}{\sin i_o} &= \frac{\sin(\Omega_f - \Omega_o)}{\sin\left(180^\circ-i_0-i_f\right)} = 1 \\
       \theta_f &= i_o = 30^\circ
   \end{aligned}

The magnitude of the required impulse is given by the law of cosines,
where we know that the angle between the initial and final position
vectors is :math:`i_f - i_o = 60^\circ`, the interior angle of the
spherical triangle at the point of intersection. The circular velocity
in the initial orbit is given by:

.. math::

   \begin{aligned}
       v_c &= \sqrt{\frac{\mu_\oplus}{r}} \\
       &= \sqrt{\frac{\mu_\oplus}{4R_\oplus}} \\
   \end{aligned}

And the magnitude of the required impulse is given by:

.. math::

   \begin{aligned}
       \frac{\Delta v}{2 v_c} &= \sin\left( \frac{60^\circ}{2} \right) \\
       &= \frac{1}{2} \\
       \Delta v &= v_c \\
       &= \sqrt{\frac{\mu_\oplus}{4R_\oplus}} \\
   \end{aligned}

Problem 1
---------

.. _problem-statement-1:

Problem statement
~~~~~~~~~~~~~~~~~

Consider a hyperbolic flyby of a planet

#. Determine the values of the periapsis flyby radius :math:`r_p` and
   hyperbolic excess speed :math:`v_\infty` that yield the *maximum
   possible* magnitude of the equivalent :math:`\Delta v_{eq}` for the
   spacecraft due to the flyby. Express your answer for :math:`r_p` in
   terms of the planet radius :math:`r_s`; include the constraint that
   :math:`r_p \geq r_s`.

#. Determine this maximum :math:`\Delta v_{eq}` in terms of :math:`v_s`,
   the circular speed at the surface of the planet. Also determine the
   numerical values for the corresponding turn angle :math:`\delta` and
   the hyperbolic eccentricity :math:`e`.

.. _solution-1:

Solution
~~~~~~~~

We know that the angle between the incoming and outgoing hyperbolic
asymptotes is given by:

.. math::

   \begin{aligned}
       \delta &= 2 \sin^{-1} \left( \frac{1}{e} \right) \\
       &= 2 \sin^{-1} \left( \frac{\Delta v_{eq}}{2 v_\infty} \right)
   \end{aligned}

We’ll use these two expressions for :math:`\delta` to solve for the
conditions that maximize :math:`\Delta v`. First, we have to find a way
to introduce :math:`r_p` into the equation. We know that the distance
from the attracting focus to the center of the hyperbola is given by:

.. math::

   \begin{aligned}
       ae &= r_p + a \\
       e &= \frac{r_p}{a} + 1
   \end{aligned}

We also know that by conservation of energy at :math:`r=\infty`, we can
express the semi-major axis :math:`a` in terms of the hyperbolic excess
speed :math:`v_\infty`:

.. math::

   \begin{aligned}
       \frac{v_\infty^2}{2} &= \frac{\mu}{2a} \\
       a &= \frac{\mu}{v_\infty^2}
   \end{aligned}

Substituting this into the expression for :math:`e`:

.. math::

   \begin{aligned}
       e &= \frac{r_p}{\mu/v_\infty^2} + 1 \\
       &= \frac{r_p v_\infty^2}{\mu} + 1
   \end{aligned}

Such that we can equate the two expressions for :math:`\delta`:

.. math::

   \begin{aligned}
       2 \sin^{-1} \left( \frac{\Delta v_{eq}}{2 v_\infty} \right) &= 2 \sin^{-1} \left( \frac{1}{\frac{r_p v_\infty^2}{\mu} + 1} \right) \\
       \frac{\Delta v_{eq}}{2 v_\infty} &= \frac{1}{\frac{r_p v_\infty^2}{\mu} + 1} \\
       \Delta v_{eq} &= \frac{2 v_\infty}{\frac{r_p v_\infty^2}{\mu} + 1} \\
   \end{aligned}

This tells us that for any given :math:`v_\infty`, minimizing
:math:`r_p` will maximize :math:`\Delta v_{eq}`. The minimum value of
:math:`r_p` is :math:`r_s`, the radius of the planet. Solving for the
:math:`v_\infty` that corresponds to this minimum :math:`r_p` requires
taking the derivative of the :math:`\Delta v_{eq}` expression with
respect to :math:`v_\infty` and looking for critical points:

.. math::

   \begin{aligned}
       \frac{\partial \Delta v_{eq}}{\partial v_\infty} &= \frac{2}{\frac{r_p v_\infty^2}{\mu} + 1} - \frac{2 v_\infty}{\left( \frac{r_p v_\infty^2}{\mu} + 1 \right)^2} \frac{2 r_p v_\infty}{\mu} \\
       &= \frac{\frac{2r_p v_\infty^2}{\mu} + 2 - \frac{4r_p v_\infty^2}{\mu}}{\left( \frac{r_p v_\infty^2}{\mu} + 1 \right)^2} \\
       &= \frac{2 - \frac{2r_p v_\infty^2}{\mu}}{\left( \frac{r_p v_\infty^2}{\mu} + 1 \right)^2} \\
   \end{aligned}

We notice that the denominator is always positive, so we can simply set
the numerator to zero:

.. math::

   \begin{aligned}
       2 - \frac{2r_p v_\infty^2}{\mu} &= 0 \\
       \frac{2r_p v_\infty^2}{\mu} &= 2 \\
       v_\infty^2 &= \frac{\mu}{r_p} \\
       v_\infty &= \sqrt{\frac{\mu}{r_p}}
   \end{aligned}

This is an interesting result! We have found that the hyperbolic excess
velocity for maximum :math:`\Delta v_{eq}` is equal to the circular
velocity at the surface of the planet. Solving for the corresponding
value of :math:`\Delta v_{eq}`:

.. math::

   \begin{aligned}
       \Delta v_{eq} &= \frac{2 v_\infty}{\frac{r_p v_\infty^2}{\mu} + 1} \\
       &= \frac{2 \sqrt{\frac{\mu}{r_p}}}{\frac{r_p \left( \sqrt{\frac{\mu}{r_p}} \right)^2}{\mu} + 1} \\
       &= \frac{2 \sqrt{\frac{\mu}{r_p}}}{\frac{\mu}{\mu} + 1} \\
       &= \frac{2 \sqrt{\frac{\mu}{r_p}}}{2} \\
       &= \sqrt{\frac{\mu}{r_p}}
   \end{aligned}

We can also solve for the corresponding values of :math:`\delta`:

.. math::

   \begin{aligned}
       \delta &= 2 \sin^{-1} \left( \frac{1}{e} \right) \\
       &= 2 \sin^{-1} \left( \frac{\Delta v_{eq}}{2 v_\infty} \right) \\
       &= 2 \sin^{-1} \left( \frac{\sqrt{\frac{\mu}{r_p}}}{2 \sqrt{\frac{\mu}{r_p}}} \right) \\
       &= 2 \sin^{-1} \left( \frac{1}{2} \right) \\
       &= 60^\circ \\
   \end{aligned}

And :math:`e`:

.. math::

   \begin{aligned}
       e &= \frac{r_p}{a} + 1 \\
       &= \frac{r_p}{\frac{\mu}{v_\infty^2}} + 1 \\
       &= \frac{r_p v_\infty^2}{\mu} + 1 \\
       &= \frac{\mu}{\mu} + 1 \\
       &= 2
   \end{aligned}
