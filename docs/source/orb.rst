Orbit Mechanics Past Problems
=============================

Spring 2021
-----------

Problem Statement
~~~~~~~~~~~~~~~~~

Assume a system of four centrobaric bodies that can all move in any
spatial dimension.

#. From first principles, derive the vector differential equation
   governing relative motion. It is not possible to solve the
   corresponding scalar equations of motion. Why not?

#. Derive expressions for the 10 known integrals of motion associated
   with this vector differential equation for the 4-body system. What is
   the physical significance of each?

#. The motion of the Moon relative to the Earth, and influenced by the
   Sun, is one of the most challenging problems in orbital mechanics.
   Given the results in (a) and (b), discuss why the first statement is
   true.

Solution
~~~~~~~~

The vector from the :math:`i`\ th body to the :math:`j`\ th body is
given by:

.. math::

   \begin{aligned}
       \mathbf{r}_{ij} &= \mathbf{r}_j - \mathbf{r}_i \\
   \end{aligned}

Taking two derivatives with respect to time:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_{ij} &= \ddot{\mathbf{r}}_j - \ddot{\mathbf{r}}_i \\
   \end{aligned}

The acceleration of the :math:`i`\ th body is given by:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_i &= - \sum_{k\neq i} \frac{G m_k}{\left| \mathbf{r}_{ki} \right|^3} \mathbf{r}_{ki} \\
   \end{aligned}

The acceleration of the :math:`j`\ th body is given by:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_j &= -\sum_{k\neq j} \frac{G m_k}{\left| \mathbf{r}_{kj} \right|^3} \mathbf{r}_{kj} \\
   \end{aligned}

Such that the relative acceleration of the :math:`i`\ th body with
respect to the :math:`j`\ th body is given by:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_{ij} &= -\sum_{k\neq j} \frac{G m_k}{\left| \mathbf{r}_{kj} \right|^3} \mathbf{r}_{kj} + \sum_{k\neq i} \frac{G m_k}{\left| \mathbf{r}_{ki} \right|^3} \mathbf{r}_{ki} \\
   \end{aligned}

We can pull out the :math:`k=i` in the first sum and :math:`k=j` in the
second sum:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_{ij} &= -\frac{G m_i}{\left| \mathbf{r}_{ji} \right|^3} \mathbf{r}_{ji} + \frac{G m_j}{\left| \mathbf{r}_{ij} \right|^3} \mathbf{r}_{ij} -\sum_{k\neq j, k\neq i} \frac{G m_k}{\left| \mathbf{r}_{kj} \right|^3} \mathbf{r}_{kj} + \sum_{k\neq i, k\neq j} \frac{G m_k}{\left| \mathbf{r}_{ki} \right|^3} \mathbf{r}_{ki} \\
   \end{aligned}

Combining the first two terms and the last two terms:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_{ij} &= -\frac{G (m_i + m_j)}{\left| \mathbf{r}_{ji} \right|^3} \mathbf{r}_{ji} - \sum_{k\neq j, k\neq i} G m_k \left(\frac{\mathbf{r}_{kj}}{{\left| \mathbf{r}_{kj} \right|^3}} - \frac{\mathbf{r}_{ki}}{{\left| \mathbf{r}_{ki} \right|^3}}\right)
   \end{aligned}

Which in the case of the 4-body problem, we take the :math:`i=1` and
:math:`j=2`, :math:`k \in [3,4]`:

.. math::

   \begin{aligned}
       \ddot{\mathbf{r}}_{12} &= -\frac{G (m_1 + m_2)}{\left| \mathbf{r}_{21} \right|^3} \mathbf{r}_{21} - \sum_{k=3}^4 G m_k \left(\frac{\mathbf{r}_{k2}}{{\left| \mathbf{r}_{k2} \right|^3}} - \frac{\mathbf{r}_{k1}}{{\left| \mathbf{r}_{k1} \right|^3}}\right)
   \end{aligned}

Deriving the 10 known integrals of motion begins by first noting that
the sum of all forces on the system is zero:

.. math:: \sum_i F = \sum_i \sum_{j \neq i} \left( -\frac{G m_i m_j}{r_{ji}^3} \mathbf{r}_{ji} \right)

Because
:math:`F_{sys} = m_{sys} a_{sys} = \sum_i m_i \ddot{\mathbf{r}}_i = 0`
for the system as a whole, we can state:

.. math:: \int \sum_i m_i \ddot{\mathbf{r}}_i \: dt = m_{sys} v_{sys} = \sum_i m_i \dot{\mathbf{r}}_i

Integrating once more:

.. math:: \int \sum_i m_i \dot{\mathbf{r}}_i \: dt = m_{sys} v_{sys} t + m_{sys} r_{sys}  = \sum_i m_i \mathbf{r}_i

These two constants of integration :math:`\mathbf{r}_{sys}` and
:math:`\mathbf{v}_{sys}` are the first two integrals of motion (making
up six scalar equations). Specifically, they are solved for by dividing
by :math:`m_{sys}`:

.. math::

   \begin{aligned}
       \mathbf{r}_{sys} &= \frac{1}{m_{sys}} \sum_i m_i \mathbf{r}_i \\
       \mathbf{v}_{sys} &= \frac{1}{m_{sys}} \sum_i m_i \dot{\mathbf{r}}_i \\
   \end{aligned}

The next three integrals of motion are found by taking the summation of
the angular momentum of the system. We must develop this by taking the
sum of the torques on members of the system. First, we note that the
torque on the :math:`i`\ th body is given by:

.. math::

   \begin{aligned}
       \mathbf{\tau}_i &= \mathbf{r}_i \times \mathbf{F}_i \\
       &= \mathbf{r}_i \times \sum_{j \neq i} \left( -\frac{G m_i m_j}{r_{ji}^3} \mathbf{r}_{ji} \right) \\
   \end{aligned}

Such that the total torque on the system is:

.. math::

   \begin{aligned}
       \sum_i \mathbf{\tau}_i &= \sum_i \mathbf{r}_i \times \sum_{j \neq i} \left( -\frac{G m_i m_j}{r_{ji}^3} \mathbf{r}_{ji} \right) \\
       &= \sum_i \sum_{j \neq i} \mathbf{r}_i \times \left( -\frac{G m_i m_j}{r_{ji}^3} \mathbf{r}_{ji} \right) \\
   \end{aligned}

We then note that
:math:`\mathbf{r}_i \times \mathbf{r}_{ji} = -\mathbf{r}_{ji} \times \mathbf{r}_i`,
such that each term in the summation is annihilated by its counterpart.
This leaves us with:

.. math::

   \begin{aligned}
       \sum_i \mathbf{\tau}_i &= \mathbf{0} \\
       &= \sum_i \mathbf{r}_i \times m_i \ddot{\mathbf{r}}_i
   \end{aligned}

We notice that this summation expansion of the torque is the derivative
of another quantity:

.. math::

   \begin{aligned}
       \sum_i \mathbf{r}_i \times m_i \ddot{\mathbf{r}}_i &= \frac{d}{dt} \left( \sum_i \mathbf{r}_i \times m_i \dot{\mathbf{r}}_i \right) \\
   \end{aligned}

Which implies that the integral of the derived quantity is an integral
of motion:

.. math::

   \begin{aligned}
       \sum_i \mathbf{r}_i \times m_i \dot{\mathbf{r}}_i &= \mathbf{h}_{sys} \\
   \end{aligned}

Finally, we enforce conservation of energy by first finding the
potential function whose gradient is the force on the system:

.. math::

   \begin{aligned}
       U &= \frac{1}{2} G \sum_i \sum_{j \neq i} \frac{m_i m_j}{r_{ji}} \\
   \end{aligned}

Such that the gradient of the potential function is:

.. math::

   \begin{aligned}
       \nabla U &= -G \sum_i \sum_{j \neq i} \frac{m_i m_j}{r_{ji}^3} \mathbf{r}_{ji} \\
       &= \sum_i m_i \ddot{\mathbf{r}} \\
   \end{aligned}

Notice that we can express:

.. math::

   \begin{aligned}
       \sum_i \nabla U &= \sum_i\frac{d U}{d \mathbf{r}_i} \\
       &= \sum_i m_i \ddot{\mathbf{r}}
   \end{aligned}

If we multiply both sides by :math:`\dot{\mathbf{r}}`:

.. math::

   \begin{aligned}
       \sum_i m_i \dot{\mathbf{r}}_i \cdot \ddot{\mathbf{r}}_i &= \sum_i\frac{d U}{d \mathbf{r}_i} \frac{d \mathbf{r}_i}{dt} \\
       &= \frac{d U}{dt} \\
   \end{aligned}

We then notice that the left side can also be expressed as the
derivative of a quantity:

.. math::

   \begin{aligned}
       \frac{dU}{dt} &= \frac{d}{dt} \left( \sum_i m_i \dot{r}_i^2 \right) \\
       U = \sum_i m_i \dot{r}_i^2 + C_2 \\
   \end{aligned}

Where :math:`C_2` is the total system energy. Plugging in our particle
system representation of :math:`U`, we find that the total system energy
is given by:

.. math::

   \begin{aligned}
       C_2 &= \sum_i m_i \dot{r}_i^2 - \frac{1}{2} G \sum_i \sum_{j \neq i} \frac{m_i m_j}{r_{ji}} \\
   \end{aligned}

Fall 2023
---------

Note that this problem was also given in Fall 2021.

.. _problem-statement-1:

Problem Statement
~~~~~~~~~~~~~~~~~

Assuming Keplerian motion, several important types of orbital maneuvers
are noncoplanar. For example, the capability to change the ascending
node can widen the launch window.

Assume that the orbital elements for an Earth orbit are given.

#. To change only the ascending node, derive an equation (or equations)
   that, if solved, will identify the location. i.e. the argument of
   latitude, for the location of the maneuver in the original and final
   orbits.

#. If the orbit is circular, let :math:`e=0.0`, :math:`i=55^\circ`,
   :math:`\Omega_i=0^\circ`, :math:`\Omega_f=45^\circ`, where :math:`o`
   reflects the original orbit and :math:`f` indicates a value in the
   final orbit. In the relationships from (a), demonstrate that the
   maneuver location is defined as :math:`\theta_o = 103.36^\circ`. What
   is the value of :math:`\theta_f`?

#. If the circular orbit possesses a radius of :math:`3R_\oplus`, find
   the required :math:`\Delta v`.

.. _solution-1:

Solution
~~~~~~~~

We can form a spherical triangle with side lengths
:math:`\Omega_f - \Omega_o` along the equator, and then :math:`\theta_i`
extending upwards from the left at an angle of :math:`i_o`, and
:math:`\theta_f` extending upwards from the right at an angle of
:math:`180^\circ-i_o`. The angle at the top of the triangle is the angle
between the initial and final position vectors, which is the angle of
the required :math:`\Delta v`. We can then use the spherical law of
cosines to solve for this angle:

.. math::

   \begin{aligned}
       \cos a &= \cos b \cos c + \sin b \sin c \cos A \\
       \cos A &= - \cos b \cos c + \sin b \sin c \cos a \\
   \end{aligned}

Where the lowercase letters are the side lengths and the uppercase
letters are the interior angles. Rephrased for our problem, we find the
third interior angle :math:`a_3`:

.. math::

   \begin{aligned}
       \cos a_3 &= - \cos i_o \cos (180^\circ - i_f) + \sin i_o \sin (180^\circ - i_f) \cos(\Omega_f - \Omega_o) \\
       &= \cos^2 55^\circ + \sin^2 55^\circ \cos(45^\circ) \\
       &= \cos^2 55^\circ + \frac{\sqrt{2}}{2} \sin^2 55^\circ \\
       a_3 &= \cos^{-1} \left( \cos^2 55^\circ + \frac{\sqrt{2}}{2} \sin^2 55^\circ \right) \\
       &\approx 37^\circ \\
   \end{aligned}

We can then use the spherical law of sines to solve for
:math:`\theta_o`:

.. math::

   \begin{aligned}
       \frac{\sin\theta_o}{\sin i_f} &= \frac{\sin(\Omega_f - \Omega_o)}{\sin a_3} \\
       \sin\theta_o &= \frac{\sin i_f \sin(\Omega_f - \Omega_o)}{\sin a_3} \\
       \theta_o &= 76.64^\circ \\
   \end{aligned}

Notice that the arcsin is also solved by
:math:`\theta_o = 180^\circ - 76.64^\circ = 103.36^\circ`. We choose
this solution to yield an intersection in the first half of the initial
orbit.

Solving for :math:`\theta_f` similarly:

.. math::

   \begin{aligned}
       \frac{\sin\theta_f}{\sin i_o} &= \frac{\sin(\Omega_f - \Omega_o)}{\sin a_3} \\
       \sin\theta_f &= \frac{\sin i_o \sin(\Omega_f - \Omega_o)}{\sin a_3} \\
       \theta_f &= 76.64^\circ \\
   \end{aligned}

We can then find the magnitude of the required :math:`\Delta v` using
the law of cosines by recognizing that the magnitude of the velocity is
the same for both the initial and final orbits:

.. math::

   \begin{aligned}
       v_c &= \sqrt{\frac{\mu_\oplus}{r}} \\
       &= \sqrt{\frac{\mu_\oplus}{3R_\oplus}} \\
   \end{aligned}

And the magnitude of the required :math:`\Delta v` is given by:

.. math::

   \begin{aligned}
       \frac{\Delta v}{2 v_c} &= \sin\left( \frac{a_3}{2} \right) \\
       &= \sin\left( \frac{37^\circ}{2} \right) \\
       &\approx 0.30 \\
       \Delta v &\approx 0.60 v_c \\
       &\approx 0.60 \sqrt{\frac{\mu_\oplus}{3R_\oplus}} \\
       &\approx 2.86 \: [km/s] \\
   \end{aligned}

This concludes the derivation of the ten integrals of motion for the
n-body problem. The first six scalars are the initial position and
velocity of the system, and the next three are the angular momentum of
the system. The final scalar is the total energy of the system.

Problem 0
---------

.. _problem-statement-2:

Problem Statement
~~~~~~~~~~~~~~~~~

In Keplerian mechanics, several important types of orbital maneuvers are
noncoplanar. For example, the capability to change both the ascending
node and the inclination with only one maneuver is efficient and can
widen the launch window.

Assume that the orbital elements for an Earth orbit are given. If the
orbit is circular both initially and after the maneuver, let
:math:`i_o=30^\circ`, :math:`i_f=90^\circ`, :math:`\Omega_o=0^\circ`,
:math:`\Omega_f=60^\circ`, where :math:`o` reflects the original orbit
and :math:`f` indicates a value in the final orbit.

#. Determine the appropriate maneuver location in each orbit.

#. If the circular orbit possesses a radius of :math:`4R_\oplus`,
   determine the magnitude of the required single impulse to accomplish
   the goal.

.. _solution-2:

Solution
~~~~~~~~

We’ll define the “location” of the maneuver in the initial and final
orbits with the argument of latitude :math:`\theta_o` and
:math:`\theta_f`, the angle between the ascending node and the
spacecraft’s position vector. Because the orbits are circular, we can’t
really use the true anomaly. We can then form a spherical triangle with
side lengths :math:`\Omega_f - \Omega_o` along the equator, and then
:math:`\theta_i` extending upwards from the left at an angle of
:math:`i_o`, and :math:`\theta_f` extending upwards from the right at an
angle of :math:`i_f`. Note: that in general, a spherical triangle has a
sum of interior angles greater than :math:`180^\circ`. This means that
we must solve for the interior angle at the top of the triangle using
the spherical law of cosines:

.. math::

   \begin{aligned}
       \cos a &= \cos b \cos c + \sin b \sin c \cos A \\
       \cos A &= - \cos b \cos c + \sin b \sin c \cos a \\
   \end{aligned}

Where the lowercase letters are the side lengths and the uppercase
letters are the interior angles. Rephrased for our problem, we find the
third interior angle :math:`a_3`:

.. math::

   \begin{aligned}
       \cos a_3 &= - \cos i_o \cos i_f + \sin i_o \sin i_f \cos(\Omega_f - \Omega_o) \\
       &= - \cos 30^\circ \cos 90^\circ + \sin 30^\circ \sin 90^\circ \cos(60^\circ - 0^\circ) \\
       &= - \frac{\sqrt{3}}{2} \cdot 0 + \frac{1}{2} \cdot 1 \cdot \frac{1}{2} \\
       &= \frac{1}{4} \\
       a_3 &= \cos^{-1} \left( \frac{1}{4} \right) \approx 76^\circ \\
   \end{aligned}

Using the spherical law of sines, we can solve for :math:`\theta_o`:

.. math::

   \begin{aligned}
       \frac{\sin\theta_o}{\sin i_f} &= \frac{\sin(\Omega_f - \Omega_o)}{\sin a_3} \\
       \sin\theta_o &= \frac{\sin i_f \sin(\Omega_f - \Omega_o)}{\sin a_3} \\
   \end{aligned}

Plugging in values, we find:

.. math::

   \begin{aligned}
       \sin\theta_o &= \frac{\sin 90^\circ \sin(60^\circ)}{\sin 76^\circ} \\
       &= \frac{\sin 60^\circ}{\sin 76^\circ} \\
       &\approx 0.89 \\
       \theta_o &\approx 63^\circ
   \end{aligned}

And similarly for :math:`\theta_f`:

.. math::

   \begin{aligned}
       \frac{\sin\theta_f}{\sin i_o} &= \frac{\sin(\Omega_f - \Omega_o)}{\sin a_3} = 1 \\
       \sin\theta_f &= \sin 30^\circ \frac{\sin(60^\circ)}{\sin 76^\circ} \\
       &\approx 0.63 \\
       \theta_f &\approx 26.5^\circ
   \end{aligned}

The magnitude of the required impulse is given by the law of cosines,
where we know that the angle between the initial and final position
vectors is :math:`a_3 \approx 76^\circ`, the interior angle of the
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
       \frac{\Delta v}{2 v_c} &= \sin\left( \frac{76^\circ}{2} \right) \\
       &\approx 0.62 \\
       \Delta v &\approx 1.23 v_c \\
       &\approx 1.23 \sqrt{\frac{\mu_\oplus}{4R_\oplus}} \\
   \end{aligned}

Fall 2019
---------

.. _problem-statement-3:

Problem Statement
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

.. _solution-3:

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
