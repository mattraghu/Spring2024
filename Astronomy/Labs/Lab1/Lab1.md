# Lab 1 - Intro to Astronomy

## Introduction

The goal of this lab was to calculate the mass of Jupiter using the orbital period and distance of one of its moons. From the Newton's version of Kepler's third law, we can relate the orbital period and orbital radius using the following equation:

$$
T^2 = \frac{4\pi^2}{GM}R^3
$$

- $T$ is the orbital period
- $R$ is the orbital radius
- $M$ is the combined mass of the planet and the orbiting mass (we can ignore the mass of the moon due to its small mass compared to Jupiter)
- $G$ is the gravitational constant

Now, in actuality the calculated constant ($\frac{4\pi^2}{GM}$) may differ between different moons due to a variety of factors.

In this lab, we will plot the orbital period and orbital radius of Jupiter's moons and use the slope of the line to calculate the mass of Jupiter.

## Data

After collecting data on the orbital period and orbital radius of Jupiter's moons (https://www.britannica.com/topic/moons-of-Jupiter-2236909), I prepared a python script to format it and do the calculations. Check my github repository for the code.

The head of the dataframe looks like this:

| Name     | Orbital Period (days) | Radius (km) | Distance from Jupiter (km) | Galilean | Orbital Period (s) | Radius (m) | Distance from Jupiter (m) | R (m)       | R3                     | T2                |
| -------- | --------------------- | ----------- | -------------------------- | -------- | ------------------ | ---------- | ------------------------- | ----------- | ---------------------- | ----------------- |
| Metis    | 0.3                   | 21.5        | 128000                     | False    | 25919.999999999996 | 21500.0    | 128000000                 | 128021500.0 | 2.0982089455139382e+24 | 671846399.9999998 |
| Adrastea | 0.3                   | 8.2         | 129000                     | False    | 25919.999999999996 | 8200.0     | 129000000                 | 129008200.0 | 2.1470983946224314e+24 | 671846399.9999998 |
| Amalthea | 0.5                   | 83.5        | 181400                     | False    | 43200.0            | 83500.0    | 181400000                 | 181483500.0 | 5.977387881860633e+24  | 1866240000.0      |
| Thebe    | 0.68                  | 49.3        | 221900                     | False    | 58752.0            | 49300.0    | 221900000                 | 221949300.0 | 1.0933553615416017e+25 | 3451797504.0      |
| Io       | 1.77                  | 1821.6      | 421800                     | True     | 152928.0           | 1821600.0  | 421800000                 | 423621600.0 | 7.6021124363922526e+25 | 23386973184.0     |

## Plots

The data is plotted with plotly, and the slope of the line is calculated using numpy's polyfit function.

### All Moons
