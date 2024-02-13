# Homework 1 - Introduction to Astrobiology

## Problem 1 - In this problem you can assume the asteroid orbits are circular, i.e. that the ’distance’ is the radius of asteroid’s orbit.

### a) Asteroid 121 Hermione orbits the Sun at distance of 3.45 AU.

#### What is the orbital period of this asteroid in years?

$$
\begin{align*}
\frac{d_1^3}{T_1^2} &= \frac{d_2^3}{T_2^2} \\

\frac{3.45^3}{T_1^2} &= \frac{1^3}{1^2} \\
T_1 &= \sqrt{\frac{3.45^3}{1}} \\
T_1 &\approx 6.4 \text{ years} \\
\end{align*}
$$

#### What is its orbital speed in km/s?

$$
\begin{align*}
v_1 &= \frac{2\pi d_1}{T_1} \\
v_1 &= \frac{2\pi 3.45}{6.4} \\
v_1 &\approx 3.475 \text{ AU/year} \\
v_1 &\approx 3.475 \text{ AU/year} \times 1.496 \times 10^8 \text{ km/AU} \\
v_1 &\approx 5.2 \times 10^8 \text{ km/year} \\
v_1 &\approx 5.2 \times 10^8 \text{ km/year} \times \frac{1}{365.25} \text{ year/day} \times \frac{1}{24} \text{ day/hour} \times \frac{1}{60} \text{ hour/minute} \times \frac{1}{60} \text{ minute/second} \\
v_1 &\approx 16.4778 \text{ km/s} \\

\end{align*}
$$

### b) Asteroid 2309 Mr. Spock orbits the Sun with the period of 5.22 years.

#### What is the distance of this asteroid from the Sun in AU?

$$
\begin{align*}
\frac{d_1^3}{T_1^2} &= \frac{d_2^3}{T_2^2} \\
\frac{1^3}{1^2} &= \frac{d_2^3}{5.22^2} \\
d_2 &= (5.22^2)^{1/3} \\
d_2 &\approx 3 \text{ AU} \\
\end{align*}
$$

#### What is its orbital speed in km/s?

$$
\begin{align*}
v_2 &= \frac{2\pi d_2}{T_2} \\
v_2 &= \frac{2\pi 3}{5.22} \\
v_2 &\approx 3.611 \text{ AU/year} \\
v_2 &\approx 3.611 \text{ AU/year} \times 1.496 \times 10^8 \text{ km/AU} \\
v_2 &\approx 5.4 \times 10^8 \text{ km/year} \\
v_2 &\approx 5.4 \times 10^8 \text{ km/year} \times \frac{1}{365.25} \text{ year/day} \times \frac{1}{24} \text{ day/hour} \times \frac{1}{60} \text{ hour/minute} \times \frac{1}{60} \text{ minute/second} \\
v_2 &\approx 17.12 \text{ km/s} \\
\end{align*}
$$

## Problem 2 - Find the altitude h above the ground of a geosynchronous satellite, i.e. one that has the same period of rotation as the Earth. These satellites, when placed in an orbit lying in the Earth’s equatorial plane, will always appear to sit above the same point on the Earth. Clearly, this is very useful for satellite communication, as you need not reposition satellite dish in order to track the satellite.

- $T$ = 24 hours = 86400 s
- $R_{\text{Earth}}$ = 6371 km = 6.371 $\times 10^6$ m
- $M_{\text{Earth}}$ = 5.972 $\times 10^{24}$ kg
- $G = 6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2$

$$
\begin{align*}
\frac{d^3}{T^2} &= \frac{GM}{4\pi^2} \\
\frac{(R_{\text{Earth}} + h)^3}{T^2} &= \frac{GM}{4\pi^2} \\
\frac{(R_{\text{Earth}} + h)^3}{T^2} &= 1.01 \times 10^{13} \text{ m}^3/\text{s}^2 \\
(R_{\text{Earth}} + h) &= 42231625.2 \\
h &= 42231625.2 - R_{\text{Earth}} \\
h &\approx 35860625.2 \text{ m} \\
h &\approx 35860.625 \text{ km} \\



\end{align*}
$$

## Problem 3 - This problem is dealing with the orbits of space missions. You can assume that all orbits are circular

### a) The International Space Station orbits the Earth in the so-called Low Earth Orbit at height of 400km.

#### Find the orbital speed and orbital period of the ISS.

- $G = 6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2$
- $d = R_{\text{Earth}} + h = 6371 \text{ km} + 400 \text{ km} = 6771 \text{ km} = 6.771 \times 10^6 \text{ m}$
- $M_{\text{Earth}} = 5.972 \times 10^{24}$ kg

$$
\begin{align*}
v_s &= \sqrt{\frac{GM}{d}} \\
v_s &= \sqrt{\frac{6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2 \times 5.972 \times 10^{24} \text{ kg}}{6.771 \times 10^6 \text{ m}}} \\
v_s &\approx 7.67 \times 10^3 \text{ m/s} \\ \\
T &= \frac{2\pi d}{v_e} \\
T &= \frac{2\pi 6.771 \times 10^6 \text{ m}}{7.67 \times 10^3 \text{ m/s}} \\
T &\approx 5.5 \times 10^3 \text{ s} \\
\end{align*}
$$

#### What is Earth’s gravitational acceleration at the position of the ISS?

$$
\begin{align*}
g = \frac{GM}{d^2} \\
g = \frac{6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2 \times 5.972 \times 10^{24} \text{ kg}}{(6.771 \times 10^6 \text{ m})^2} \\
g \approx 8.7 \text{ m/s}^2 \\
\end{align*}
$$

### b) Asteroid 101955 Bennu was the target of NASA’s OsirisREX sample re-turn mission. The spacecraft briefly landed on the asteroid, collected sam- ples, and brought them back to Earth. For the purpose of this problem you can assume that Bennu is spherical in shape, with the mean radius of 262 m and a mass of 7.8 ∗ 1010 kg.

- $G = 6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2$
- $R_{\text{Bennu}} = 262 \text{ m}$
- $M_{\text{Bennu}} = 7.8 \times 10^{10}$ kg

#### What is the escape speed from the surface of Bennu in m/s?

$$
\begin{align*}
v_e &= \sqrt{\frac{2GM}{R}} \\
v_e &= \sqrt{\frac{2 \times 6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2 \times 7.8 \times 10^{10} \text{ kg}}{262 \text{ m}}} \\
v_e &\approx 0.199 \text{ m/s} \\
\end{align*}
$$

#### Would you be able to jump off Bennu’s surface and escape its gravitational field?

$$
\begin{align*}
g &= \frac{GM}{R^2} \\
g &= \frac{6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2 \times 7.8 \times 10^{10} \text{ kg}}{(262 \text{ m})^2} \\
g &\approx 7.57 \times 10^{-5} \text{ m/s}^2 \\
\end{align*}
$$

**Yes** unless you are a very-very bad jumper.

### c) Mars Reconnaissance Orbiter (MRO) has been orbiting Mars for close to 18 years. The altitude about the surface of Mars is 300 km.

#### Find the orbital speed and the period of the MRO in its orbit about Mars.

- $G = 6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2$
- $d = R_{\text{Mars}} + h = 3390 \text{ km} + 300 \text{ km} = 3690 \text{ km} = 3.69 \times 10^6 \text{ m}$
- $M_{\text{Mars}} = 6.42 \times 10^{23}$ kg

$$
\begin{align*}
v_s &= \sqrt{\frac{GM}{d}} \\
v_s &= \sqrt{\frac{6.67 \times 10^{-11} \text{ Nm}^2/\text{kg}^2 \times 6.42 \times 10^{23} \text{ kg}}{3.69 \times 10^6 \text{ m}}} \\
v_s &\approx 3.4 \times 10^3 \text{ m/s} \\ \\
T &= \frac{2\pi d}{v_e} \\
T &= \frac{2\pi 3.69 \times 10^6 \text{ m}}{3.6 \times 10^3 \text{ m/s}} \\
T &\approx 6.44 \times 10^3 \text{ s} \\
\end{align*}
$$

## In this problem you’ll compare the energy of an asteroid impact with those of the Hiroshima bomb (yield 15 kt TNT) and the Castle Bravo bomb (the largest nuclear test by the US with the yield of 15 Mt TNT). Energy yield of 1 ton of TNT is equivalent to 109 cal = 4.184 ∗ 109 J. The tons here are metric tons. Suppose that the impact speed of an asteroid is 25 km/s. This is given at impact, i.e. gravitational attraction is already taken into account and you need not add potential energy. You can assume that the asteroid is perfectly spher- ical in shape and made of stony material (’S-type asteroid’) with the mean density of ρ = 2700 kg/m3

### Calculate the impact energy for the asteroid diameter of 10 m, 100 m and 1km in Joules, and express it in terms of energy yields of the Hiroshima and Castle Bravo bombs.

- $v = 25 \times 10^3 \text{ m/s}$
- $\rho = 2700 \text{ kg/m}^3$
- $E_{\text{Hiroshima}} = 15 \times 10^3 \text{ tons} \times 4.184 \times 10^9 \text{ J/ton} = 6.276 \times 10^{13} \text{ J}$
- $E_{\text{Castle Bravo}} = 15 \times 10^6 \text{ tons} \times 4.184 \times 10^9 \text{ J/ton} = 6.276 \times 10^{16} \text{ J}$

#### 10 m

$$
\begin{align*}
V &= \frac{4}{3}\pi r^3 \\
V &= \frac{4}{3}\pi (5 \text{ m})^3 \\
V &\approx 523.6 \text{ m}^3 \\ \\

m &= \rho V \\
m &= 2700 \text{ kg/m}^3 \times 523.6 \text{ m}^3 \\
m &\approx 1.413 \times 10^6 \text{ kg} \\ \\

E &= \frac{1}{2}mv^2 \\
E &= \frac{1}{2} \times 1.413 \times 10^6 \text{ kg} \times (25 \times 10^3 \text{ m/s})^2 \\
E &\approx 4.413 \times 10^{14} \text{ J} \\

\frac{E}{E_{\text{Hiroshima}}} &\approx 7.03 \times 10^0 \text{ Hiroshima bombs} \\
\frac{E}{E_{\text{Castle Bravo}}} &\approx 7.03 \times 10^{-3} \text{ Castle Bravo bombs} \\

\end{align*}
$$

#### 100 m

$$
\begin{align*}
V &= \frac{4}{3}\pi r^3 \\
V &= \frac{4}{3}\pi (50 \text{ m})^3 \\
V &\approx 5.236 \times 10^5 \text{ m}^3 \\ \\
m &= \rho V \\
m &= 2700 \text{ kg/m}^3 \times 5.236 \times 10^5 \text{ m}^3 \\
m &\approx 1.413 \times 10^9 \text{ kg} \\ \\
E &= \frac{1}{2}mv^2 \\
E &= \frac{1}{2} \times 1.413 \times 10^9 \text{ kg} \times (25 \times 10^3 \text{ m/s})^2 \\
E &\approx 4.413 \times 10^{17} \text{ J} \\
\frac{E}{E_{\text{Hiroshima}}} &\approx 7.03 \times 10^3 \text{ Hiroshima bombs} \\
\frac{E}{E_{\text{Castle Bravo}}} &\approx 7.03 \times 10^0 \text{ Castle Bravo bombs} \\
\end{align*}
$$

#### 1 km

$$
\begin{align*}
V &= \frac{4}{3}\pi r^3 \\
V &= \frac{4}{3}\pi (500 \text{ m})^3 \\
V &\approx 5.236 \times 10^8 \text{ m}^3 \\ \\
m &= \rho V \\
m &= 2700 \text{ kg/m}^3 \times 523.6 \text{ m}^3 \\
m &\approx 1.413 \times 10^{12} \text{ kg} \\ \\
E &= \frac{1}{2}mv^2 \\
E &= \frac{1}{2} \times 1.413 \times 10^{12} \text{ kg} \times (25 \times 10^3 \text{ m/s})^2 \\
E &\approx 4.413 \times 10^{20} \text{ J} \\
\frac{E}{E_{\text{Hiroshima}}} &\approx 7.03 \times 10^6 \text{ Hiroshima bombs} \\
\frac{E}{E_{\text{Castle Bravo}}} &\approx 7.03 \times 10^3 \text{ Castle Bravo bombs} \\
\end{align*}
$$

### Any comments?

It's crazy how even a 10 m asteroid can have the energy of 7 Hiroshima bombs. It's incredible to think about how easy it is for life on Earth to be wiped out. If even just one small asteroid were to hit Earth, it could be catastrophic. Earth's atmosphere is an amazing protector.
