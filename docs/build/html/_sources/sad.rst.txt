Attitude Dynamics Past Problems
===============================

Fall 2023
---------

This was the first problem written by Dr. Oguri.

Problem Statement
~~~~~~~~~~~~~~~~~

Let us analyically investigate the attitude motion of a satellite under
torque, :math:`\boldsymbol{L} \in \mathbb{R}^3`

The inertial frame and satellite body-fixed frames are represented by
:math:`\mathcal{N}` and :math:`\mathcal{B}`, where
:math:`\left\{\hat{\boldsymbol{n}}_1, \hat{\boldsymbol{n}}_2, \hat{\boldsymbol{n}}_3\right\}`
and
:math:`\left\{\hat{\boldsymbol{b}}_1, \hat{\boldsymbol{b}}_2, \hat{\boldsymbol{b}}_3\right\}`
are right-handed bases attached to the :math:`\mathcal{N}` and
:math:`\mathcal{B}` frames, respectively.

Denote the angular velocity of the :math:`\mathcal{B}` frame with
respect to the :math:`\mathcal{N}` frame as
:math:`\boldsymbol{\omega}_\mathcal{B/N} = \omega_i \hat{\boldsymbol{b}}_i`
and the inertia tensor dyadic of the stellite about its center of mass
(CoM) by
:math:`\boldsymbol{I} = I_i \hat{\boldsymbol{b}}_i \hat{\boldsymbol{b}}_i`.

#. Derive the following equation from
   :math:`\dot{\boldsymbol{H}} = \boldsymbol{L}`, where
   :math:`\boldsymbol{H}` represents the body’s angular momentum about
   the CoM.

   .. math:: \boldsymbol{I} \cdot \dot{\boldsymbol{\omega}}_\mathcal{B/N} = -\boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{I} \cdot \boldsymbol{\omega}_\mathcal{B/N} + \boldsymbol{L}

#. Starting from the above equation, derive a set of differential
   equations that describe the time derivative of :math:`\omega_i` for
   :math:`i = 1,2,3`, where
   :math:`\boldsymbol{L} = L_i \hat{\boldsymbol{b}}_i`.

#. Assume that :math:`I_1 < I_2 < I_3` and :math:`\boldsymbol{L} = 0`.
   Show that a rotation about :math:`\hat{b}_1` is a particular solution
   of the differential equations derived above, and discuss the linear
   stability of the solution; if it is linearly stable, also discuss
   whether or not the solution is asymptotically stable with the
   mathematical reasoning. Finally, qualitatively discuss whether the
   stability properties changes over time when there is energy
   dissipation (e.g., due to fuel sloshing).

#. Assume that :math:`I_1 > I_3 > I_2` and now :math:`\boldsymbol{L}`
   represents the gravity gradient (GG) torque in a circular orbit of
   radius :math:`R` about a planet of gravitational parameter
   :math:`\mu`. ?Using an attitude representation of your choice, derive
   both the Kinematic and dynamic differential equations that govern the
   satellite motion. Here, an approximate epression of the GG torque,
   :math:`\boldsymbol{L} \approx \frac{3\mu}{R^5} \boldsymbol{R} \times \boldsymbol{I} \cdot \boldsymbol{R}`
   where :math:`\boldsymbol{R} \in \mathbb{R}^3` is the orbit radius
   vector, can be used without derivation. Show a particular solution of
   the derived differential equations and discuss its linear stability.

Solution
~~~~~~~~

Part 1:

Beginning with:

.. math:: \dot{\boldsymbol{H}} = \boldsymbol{L}

We recognize that the angular momentum vector
:math:`\boldsymbol{H} = \boldsymbol{I} \boldsymbol{\omega}` such that in
the body frame:

.. math:: I \dot{\boldsymbol{\omega}} = \boldsymbol{L}

The BKE tells us that the time derivative of a vector in an reference
frame is related to the same vector’s derivative in the rotating frame
by the angular velocity:

.. math:: {}^\mathcal{N}\dot{\boldsymbol{v}} = {}^\mathcal{B}\dot{\boldsymbol{v}} + \boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{v}

To be specific, when we say the derivative of a vector expressed in a
certain frame, like :math:`{}^\mathcal{N}\dot{\boldsymbol{v}}`, we mean
the time derivative of the vectors elements when expressed in the basis
vectors of that frame. So, for example, if we have a vector
:math:`\boldsymbol{v} = v_i \hat{\boldsymbol{n}}_i` expressed in the
:math:`\mathcal{N}` frame, then
:math:`{}^\mathcal{N}\dot{\boldsymbol{v}} = \dot{\boldsymbol{v}}_i \hat{\boldsymbol{n}}_i`
as the basis vectors are constant in their frame. Applying this to the
angular momentum, we can take its body frame derivative:

.. math::

   \begin{aligned}
       {}^\mathcal{N}\dot{\boldsymbol{H}} &= {}^\mathcal{B}\dot{\boldsymbol{H}} + \boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{H} \\
       &= \boldsymbol{I} \dot{\boldsymbol{\omega}}_\mathcal{B/N} + \boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{I} \boldsymbol{\omega}_\mathcal{B/N} \\
   \end{aligned}

Since we know that
:math:`{}^\mathcal{N}\dot{\boldsymbol{H}} = \boldsymbol{L}`, we can
substitute to yield:

.. math::

   \begin{aligned}
       \boldsymbol{L} &= \boldsymbol{I} \dot{\boldsymbol{\omega}}_\mathcal{B/N} + \boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{I} \boldsymbol{\omega}_\mathcal{B/N} \\
       \boldsymbol{I} \dot{\boldsymbol{\omega}}_\mathcal{B/N} &= -\boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{I} \boldsymbol{\omega}_\mathcal{B/N} + \boldsymbol{L} \\
   \end{aligned}

Completing the proof.

Part 2:

We can expand the above equation into its components, noting that if the
body basis vectors are the principal axes of the body, then the inertia
tensor is diagonal and the cross product terms are zero:

.. math::

   \begin{bmatrix}
           I_1 & 0 & 0 \\
           0 & I_2 & 0 \\
           0 & 0 & I_3 \\
       \end{bmatrix}
       \begin{bmatrix}
           \dot{\boldsymbol{\omega}}_1 \\
           \dot{\boldsymbol{\omega}}_2 \\
           \dot{\boldsymbol{\omega}}_3 \\
       \end{bmatrix}
       =
       \begin{bmatrix}
           \boldsymbol{\omega}_1 \\
           \boldsymbol{\omega}_2 \\
           \boldsymbol{\omega}_3 \\
       \end{bmatrix}
       \times
       \begin{bmatrix}
           I_1 & 0 & 0 \\
           0 & I_2 & 0 \\
           0 & 0 & I_3 \\
       \end{bmatrix}
       \begin{bmatrix}
           \boldsymbol{\omega}_1 \\
           \boldsymbol{\omega}_2 \\
           \boldsymbol{\omega}_3 \\
       \end{bmatrix}
       +
       \begin{bmatrix}
           L_1 \\
           L_2 \\
           L_3 \\
       \end{bmatrix}

Such that the scalar EOMs are:

.. math::

   \begin{aligned}
       \dot{\boldsymbol{\omega}}_1 &= \frac{1}{I_1} \left(\omega_2 \omega_3 \left(I_2 - I_3\right) + L_1 \right)\\
       \dot{\boldsymbol{\omega}}_2 &= \frac{1}{I_2} \left(\omega_3 \omega_1 \left(I_3 - I_1\right) + L_2 \right)\\
       \dot{\boldsymbol{\omega}}_3 &= \frac{1}{I_3} \left(\omega_1 \omega_2 \left(I_1 - I_2\right) + L_3 \right)\\
   \end{aligned}

Part 3:

A rotation purely about :math:`\hat{\boldsymbol{b}}_1` implies that
:math:`\boldsymbol{\omega} = \omega_1 \hat{\boldsymbol{b}}_1` with
:math:`\omega_2=\omega_3 = 0` such that the EOMs become when
:math:`\boldsymbol{L} = 0`:

.. math::

   \begin{aligned}
       \dot{\boldsymbol{\omega}}_1 &= \frac{1}{I_1} \left(0 \cdot 0 \left(I_2 - I_3\right) + 0 \right)\\
       \dot{\boldsymbol{\omega}}_2 &= \frac{1}{I_2} \left(0 \cdot \omega_1 \left(I_3 - I_1\right) + 0 \right)\\
       \dot{\boldsymbol{\omega}}_3 &= \frac{1}{I_3} \left(\omega_1 \cdot 0 \left(I_1 - I_2\right) + 0 \right)\\
   \end{aligned}

Which simplify:

.. math::

   \begin{aligned}
       \dot{\boldsymbol{\omega}}_1 &= 0\\
       \dot{\boldsymbol{\omega}}_2 &= 0\\
       \dot{\boldsymbol{\omega}}_3 &= 0\\
   \end{aligned}

This means that the angular velocity is constant in time, and therefore
this is a particular solution to the EOMs. To determine the stability of
this solution, we can linearize the EOMs about this solution by taking
the first order Taylor series expansion of the EOMs about the solution,
where we substitute
:math:`\boldsymbol{\omega} = \boldsymbol{\omega} + \delta\boldsymbol{\omega}`,
discarding any higher order terms in :math:`\delta\boldsymbol{\omega}`:

.. math::

   \boldsymbol{\omega} = 
       \begin{bmatrix} \omega_1 + \delta\omega_1 \\ 0 + \delta\omega_2 \\ 0 + \delta\omega_3 \end{bmatrix}

.. math::

   \begin{aligned}
       \dot{\boldsymbol{\omega}}_1 &= \frac{1}{I_1} \left(\left(\delta\omega_3 \cdot  \delta\omega_2\right) \left(I_2 - I_3\right) \right)\\
       \dot{\boldsymbol{\omega}}_2 &= \frac{1}{I_2} \left(\left(\left(\omega_1 + \delta\omega_1\right) \cdot \delta\omega_3\right) \left(I_3 - I_1\right) \right)\\
       \dot{\boldsymbol{\omega}}_3 &= \frac{1}{I_3} \left(\left(\left(\omega_1 + \delta\omega_1\right) \cdot \delta\omega_2\right) \left(I_1 - I_2\right) \right)\\
   \end{aligned}

Simplifying:

.. math::

   \begin{aligned}
       \dot{\boldsymbol{\omega}}_1 &= 0 \\
       \dot{\boldsymbol{\omega}}_2 &= \frac{1}{I_2} \left(\omega_1 \cdot \delta\omega_3 \left(I_3 - I_1\right) \right)\\
       \dot{\boldsymbol{\omega}}_3 &= \frac{1}{I_3} \left(\omega_1 \cdot \delta\omega_2 \left(I_1 - I_2\right) \right)\\
   \end{aligned}

Finding the eigenvalues of this system will determine its linear
stability. We can rearrange this as a linear system in terms of the
perturbation :math:`\delta \omega_i`:

.. math::

   \begin{aligned}
       \dot{\boldsymbol{\omega}} &= \boldsymbol{A} \delta \omega \\
       &= \begin{bmatrix}
           0 & 0 & 0 \\
           0 & 0 & \frac{1}{I_2} \left(\omega_1 \left(I_3 - I_1\right) \right)\\
           0 & \frac{1}{I_3} \left(\omega_1 \left(I_1 - I_2\right) \right) & 0 \\
       \end{bmatrix}
       \begin{bmatrix} \delta\omega_1 \\ \delta\omega_2 \\ \delta\omega_3 \end{bmatrix}
   \end{aligned}

The eigenvalues of this linear system are given by the solution to:

.. math:: \det\left(\boldsymbol{A} - \lambda \boldsymbol{I}\right) = 0

.. math::

   \begin{aligned}
       \det\left(\begin{bmatrix}
           -\lambda & 0 & 0 \\
           0 & -\lambda & \frac{1}{I_2} \left(\omega_1 \left(I_3 - I_1\right) \right)\\
           0 & \frac{1}{I_3} \left(\omega_1 \left(I_1 - I_2\right) \right) & -\lambda \\
       \end{bmatrix}\right) &= 0 \\
       \lambda \left( \lambda^2 - \frac{\omega_1^2 \left(I_1 - I_2\right) \left(I_3 - I_1\right)}{I_2 I_3} \right) &= 0 \\
   \end{aligned}

Which has solutions:

.. math::

   \begin{aligned}
       \lambda_1 &= 0 \\
       \lambda_2 &= \sqrt{\frac{\omega_1^2 \left(I_1 - I_2\right) \left(I_3 - I_1\right)}{I_2 I_3}} \\
       \lambda_3 &= -\sqrt{\frac{\omega_1^2 \left(I_1 - I_2\right) \left(I_3 - I_1\right)}{I_2 I_3}} \\
   \end{aligned}

Because we are told that :math:`I_1 < I_2 < I_3`, we know that
:math:`\left(I_1 - I_2\right) < 0` and
:math:`\left(I_3 - I_1\right) > 0` such that second and third
eigenvalues are purely imaginary as the argument under the square root
must be negative. Due to the presence of a zero eigenvalue, the system
is marginally stable in the linear sense.

The system is not asymptotically stable as no eigenvalues have negative
real parts. This means that the system will not return to the
equilibrium solution after a perturbation. This makes intuitive sense as
torque-free rigid body motion has no damping capability to return the
system to the equilibrium solution.

Let’s now turn out attention to the question of energy dissipation. We
know that the total kinetic energy of the system is given by:

.. math:: T = \frac{1}{2} \boldsymbol{\omega} \cdot \boldsymbol{I} \cdot \boldsymbol{\omega}

We know that as long as no torque is applied to the system due to an
external force, the total angular momentum of the system is conserved.
Thinking back to the construction of the energy ellipsoid and momentum
sphere (expressed in body-frame angular momentum coordinates), losing
energy will shrink the energy ellipsoid nonlinearly along all its axes.
This could completely change the stability properties of the motion.
Shrinking the ellipsoid to the point where are one of its axes has the
same magnitude as the angular momentum sphere will create a directrix,
resulting in unstable motion about the intermediate axis.

Part 4:

The attitude representation of choice for this writeup is the direction
cosine matrix (DCM). We know that the DCM
:math:`\left[\mathcal{BN}\right]` is defined as the matrix that takes
vectors from the inertial frame to the body frame:

.. math:: {}^\mathcal{B}\boldsymbol{v} = \left[\mathcal{BN}\right] {}^\mathcal{N}\boldsymbol{v}

The kinematic differential equation for the DCM is a relationship
between the time derivative of the DCM and the angular velocity of the
body frame with respect to the inertial frame. We can derive a
relationship between these quantities by taking the
:math:`\mathcal{N}`-frame derivative of the :math:`\mathcal{B}`-frame
basis vectors:

.. math::

   {}^\mathcal{N}\frac{d}{dt}\left(
           \begin{bmatrix}
               \hat{\boldsymbol{b}}_1 \\ \hat{\boldsymbol{b}}_2 \\ \hat{\boldsymbol{b}}_3
           \end{bmatrix}
       \right) = {}^\mathcal{B}\frac{d}{dt}\left(
           \begin{bmatrix}
               \hat{\boldsymbol{b}}_1 \\ \hat{\boldsymbol{b}}_2 \\ \hat{\boldsymbol{b}}_3
           \end{bmatrix}
       \right) + \boldsymbol{\omega}_\mathcal{B/N} \times \left(
           \begin{bmatrix}
               \hat{\boldsymbol{b}}_1 \\ \hat{\boldsymbol{b}}_2 \\ \hat{\boldsymbol{b}}_3
           \end{bmatrix}
       \right)

Here we note that the :math:`\mathcal{B}`-frame derivative of the
:math:`\hat{\boldsymbol{b}}_i` unit vectors is zero. Further, we can
replace the cross product on the right hand side with the matrix
multiplication of the skew symmetric matrix of the angular velocity with
the basis vectors:

.. math::

   \begin{aligned}
       {}^\mathcal{N}\frac{d}{dt}\left(
           \begin{bmatrix}
               \hat{\boldsymbol{b}}_1 \\ \hat{\boldsymbol{b}}_2 \\ \hat{\boldsymbol{b}}_3
           \end{bmatrix}
       \right) &= [\boldsymbol{\omega}_\mathcal{B/N}\times]
           \begin{bmatrix}
               \hat{\boldsymbol{b}}_1 \\ \hat{\boldsymbol{b}}_2 \\ \hat{\boldsymbol{b}}_3
           \end{bmatrix} \\
           &= \begin{bmatrix}
               0 & -\omega_3 & \omega_2 \\
               \omega_3 & 0 & -\omega_1 \\
               -\omega_2 & \omega_1 & 0 \\
           \end{bmatrix}
           \begin{bmatrix}
               \hat{\boldsymbol{b}}_1 \\ \hat{\boldsymbol{b}}_2 \\ \hat{\boldsymbol{b}}_3
           \end{bmatrix} \\
   \end{aligned}

We now proceed by computing the effect of the :math:`\mathcal{N}`-frame
derivative on each of the :math:`\mathcal{B}`-frame basis vectors,
beginning with :math:`\hat{\boldsymbol{b}}_1`:

.. math::

   \begin{aligned}
       {}^\mathcal{N}\frac{d}{dt}\left(\hat{\boldsymbol{b}}_1\right) &= \begin{bmatrix}
               0 & -\omega_3 & \omega_2 \\
               \omega_3 & 0 & -\omega_1 \\
               -\omega_2 & \omega_1 & 0 \\
           \end{bmatrix}
           \begin{bmatrix}
               1 \\ 0 \\ 0
           \end{bmatrix} = \begin{bmatrix}
               0 \\ \omega_3 \\ -\omega_2
           \end{bmatrix} \\
   \end{aligned}

.. math::

   \begin{aligned}
       {}^\mathcal{N}\frac{d}{dt}\left(\hat{\boldsymbol{b}}_2\right) &= \begin{bmatrix}
               0 & -\omega_3 & \omega_2 \\
               \omega_3 & 0 & -\omega_1 \\
               -\omega_2 & \omega_1 & 0 \\
           \end{bmatrix}
           \begin{bmatrix}
               0 \\ 1 \\ 0
           \end{bmatrix} = \begin{bmatrix}
               -\omega_3 \\ 0 \\ \omega_1
           \end{bmatrix} \\
   \end{aligned}

.. math::

   \begin{aligned}
       {}^\mathcal{N}\frac{d}{dt}\left(\hat{\boldsymbol{b}}_3\right) &= \begin{bmatrix}
               0 & -\omega_3 & \omega_2 \\
               \omega_3 & 0 & -\omega_1 \\
               -\omega_2 & \omega_1 & 0 \\
           \end{bmatrix}
           \begin{bmatrix}
               0 \\ 0 \\ 1
           \end{bmatrix} = \begin{bmatrix}
               \omega_2 \\ -\omega_1 \\ 0
           \end{bmatrix} \\
   \end{aligned}

At this point, we notice that since the DCM can be expressed as the dot
product of the basis vectors of the two frames:

.. math::

   \left[\mathcal{BN}\right] = \begin{bmatrix}
           \hat{\boldsymbol{b}}_1 \cdot \hat{\boldsymbol{n}}_1 & \hat{\boldsymbol{b}}_1 \cdot \hat{\boldsymbol{n}}_2 & \hat{\boldsymbol{b}}_1 \cdot \hat{\boldsymbol{n}}_3 \\
           \hat{\boldsymbol{b}}_2 \cdot \hat{\boldsymbol{n}}_1 & \hat{\boldsymbol{b}}_2 \cdot \hat{\boldsymbol{n}}_2 & \hat{\boldsymbol{b}}_2 \cdot \hat{\boldsymbol{n}}_3 \\
           \hat{\boldsymbol{b}}_3 \cdot \hat{\boldsymbol{n}}_1 & \hat{\boldsymbol{b}}_3 \cdot \hat{\boldsymbol{n}}_2 & \hat{\boldsymbol{b}}_3 \cdot \hat{\boldsymbol{n}}_3 \\
       \end{bmatrix}

Which is really just rows of :math:`\mathcal{B}`-frame vectors expressed
in the :math:`\mathcal{N}`-frame:

.. math::

   \left[\mathcal{BN}\right] = \begin{bmatrix}
           {}^\mathcal{N}\hat{\boldsymbol{b}}_1 \\ {}^\mathcal{N}\hat{\boldsymbol{b}}_2 \\ {}^\mathcal{N}\hat{\boldsymbol{b}}_3 \\
       \end{bmatrix}

Differentiating:

.. math::

   \begin{aligned}
       \left[\dot{\mathcal{BN}}\right] = \begin{bmatrix}
           {}^\mathcal{N}\frac{d}{dt}\left(\hat{\boldsymbol{b}}_1\right) \\ {}^\mathcal{N}\frac{d}{dt}\left(\hat{\boldsymbol{b}}_2\right) \\ {}^\mathcal{N}\frac{d}{dt}\left(\hat{\boldsymbol{b}}_3\right) \\
       \end{bmatrix} = \begin{bmatrix}
           0 & \omega_3 & -\omega_2 \\
           -\omega_3 & 0 & \omega_1 \\
           \omega_2 & -\omega_1 & 0 \\
       \end{bmatrix}
       \begin{bmatrix}
           {}^\mathcal{N}\hat{\boldsymbol{b}}_1 \\ {}^\mathcal{N}\hat{\boldsymbol{b}}_2 \\ {}^\mathcal{N}\hat{\boldsymbol{b}}_3 \\
       \end{bmatrix} \\
   \end{aligned}

Such that:

.. math:: \dot{\left[\mathcal{BN}\right]} = -\left[\boldsymbol{\omega}_\mathcal{B/N}\times\right] \left[\mathcal{BN}\right]

Deriving the dynamic differential equation in terms of the DCM requires
us to express the orbital radius vector (defined in the orbital frame as
:math:`\boldsymbol{R} = R \hat{o}_1`):

.. math::

   \begin{aligned}
       {}^\mathcal{B}\boldsymbol{R} &= \left[\mathcal{BO}\right] \begin{bmatrix} R \\ 0 \\ 0 \end{bmatrix} \\
       &= R \begin{bmatrix} C_{11} \\ C_{21} \\ C_{31} \end{bmatrix} \\
   \end{aligned}

Such that the gravity gradient torque is:

.. math::

   \begin{aligned}
       \boldsymbol{L} &= \frac{3\mu}{R^5} \boldsymbol{R} \times \boldsymbol{I} \cdot \boldsymbol{R} \\
       &= \frac{3\mu}{R^3} \begin{bmatrix} C_{11} \\ C_{21} \\ C_{31} \end{bmatrix} \times \begin{bmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{bmatrix} \begin{bmatrix} C_{11} \\ C_{21} \\ C_{31} \end{bmatrix} \\
       &= \frac{3\mu}{R^3} \begin{bmatrix} C_{21} C_{31} \left(I_3 - I_2\right) \\ C_{31} C_{11} \left(I_1 - I_3\right) \\ C_{11} C_{21} \left(I_2 - I_1\right) \end{bmatrix} \\
   \end{aligned}

Plugging this into the EOMs:

.. math::

   \begin{aligned}
       \boldsymbol{I} \cdot \dot{\boldsymbol{\omega}}_\mathcal{B/N} &= -\boldsymbol{\omega}_\mathcal{B/N} \times \boldsymbol{I} \cdot \boldsymbol{\omega}_\mathcal{B/N} + \boldsymbol{L} \\
       \begin{bmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{bmatrix} \begin{bmatrix} \dot{\boldsymbol{\omega}}_1 \\ \dot{\boldsymbol{\omega}}_2 \\ \dot{\boldsymbol{\omega}}_3 \end{bmatrix} &= \begin{bmatrix} \omega_2 \omega_3 \left(I_2 - I_3\right) \\ \omega_3 \omega_1 \left(I_3 - I_1\right) \\ \omega_1 \omega_2 \left(I_1 - I_2\right) \end{bmatrix} + \frac{3\mu}{R^3} \begin{bmatrix} C_{21} C_{31} \left(I_3 - I_2\right) \\ C_{31} C_{11} \left(I_1 - I_3\right) \\ C_{11} C_{21} \left(I_2 - I_1\right) \end{bmatrix} \\
   \end{aligned}

A particular solution of these equations occurs when the body is
oriented such that one of its principal axes is in line with the orbital
radius vector and body is rotating at the same rate as the orbit
(:math:`\Omega`). If we choose to align the largest moment of inertia
body axis (:math:`I_1`) with the orbital radius vector, then we can
simplify the above equations by noticing that :math:`C_{11} = 1`,
:math:`C_{21} = C_{31} = 0`, while :math:`\omega_3 = \Omega`,
:math:`\omega_2 = \omega_1 = 0`:

.. math::

   \begin{aligned}
       \begin{bmatrix} I_1 & 0 & 0 \\ 0 & I_2 & 0 \\ 0 & 0 & I_3 \end{bmatrix} \begin{bmatrix} \dot{\boldsymbol{\omega}}_1 \\ \dot{\boldsymbol{\omega}}_2 \\ \dot{\boldsymbol{\omega}}_3 \end{bmatrix} &= \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} 
   \end{aligned}

This particular solution is expected to be unstable as any small
rotation about :math:`\hat{\boldsymbol{b}}_3` will create an additional
torque that will cause large-scale oscillations. This is illustrated by
drawing the scenario and showing that any small reorientation will
produce a net torque which is not restoring.
