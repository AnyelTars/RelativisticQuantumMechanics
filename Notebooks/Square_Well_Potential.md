# Relativistic Quantum Mechanics

By: Salazar Angel and Potosi Quray

## TISE:  The Barrier Potential 

#### 1. Solving the Schrodinger Equation

![1om84xti6pbm5](img/1om84xti6pbm5.png)

```wl
In[]:= f[x_] := Piecewise[{{0, x < 0}, {Subscript[V, 0], 0 <= x <= 2}}];
 Plot[f[x], {x, -4, 4}, PlotStyle -> Thick, AxesLabel -> {"x", "f(x)"},Filling -> Axis] 
  
 
```

![150wmq57jq5uq](img/150wmq57jq5uq.png)

```wl
In[]:= 
```

##### Regions to the left and right of the barrier potential

The time-independent Schrodinger Equation has different forms in the regions to the left and right of the barrier potential:

##### First region x<0:

![1bvct61j8zc2w](img/1bvct61j8zc2w.png)

![03uq3v5va8rrv](img/03uq3v5va8rrv.png)

Let k1 =  ![0qhwtbne3dhl4](img/0qhwtbne3dhl4.png) 

![0she2g59srw89](img/0she2g59srw89.png)

##### Second Region 0<x>a

![0gdrt6xe5te5d](img/0gdrt6xe5te5d.png)

![14e13ioazyrfx](img/14e13ioazyrfx.png)

 Let k2 =  ![0l5p7o8yy2dqp](img/0l5p7o8yy2dqp.png) 

![0bv7zw5oluacg](img/0bv7zw5oluacg.png)

##### Third Region x>a

![0snjj70j2b8pa](img/0snjj70j2b8pa.png)

![0vlgjmhuv9h8h](img/0vlgjmhuv9h8h.png)

![101fwdcmag0ry](img/101fwdcmag0ry.png)

#### 2. Getting the system of equations of Boundary Conditions

We apply the matching conditions for ψ(x) and ψ'(x), that is at the points x=0 and x=a, four equations in the arbitrary constants A, B, C, D, and F will be obtained: 

![0h62nm67oawi2](img/0h62nm67oawi2.png)

```wl
Out[]= A + B == C + D
```

![1dlvx72uufi47](img/1dlvx72uufi47.png)

```wl
Out[]= D E^(-2 I k2) + C E^(2 I k2) == E^(2 I k1) F
```

![0wrls663xwq9u](img/0wrls663xwq9u.png)

```wl
Out[]= I A k1 - I B k1 == I C k2 - I D k2
```

![0kn8q3av2a5aj](img/0kn8q3av2a5aj.png)

```wl
Out[]= -I D E^(-2 I k2)k2 + I C E^(2 I k2)k2 == I E^(2 I k1)F k1
```

#### 3. Solve this systems of equations in terms of A:

```wl
In[]:= Solve[{eq1, eq2, eq3, eq4}, {B, C, D, F}]
```

![0bpyk3r8onodv](img/0bpyk3r8onodv.png)

Thus we have: 

![0q2ri8ud62t4x](img/0q2ri8ud62t4x.png)

#### 4. Replacing with the constants found in the piece-wise Schrodinger equation:

![12zjrnl8h6a5o](img/12zjrnl8h6a5o.png)

with:

![0sydjzi1p26bf](img/0sydjzi1p26bf.png)

#### 5. Computing the Transmission and Reflection coefficient

##### The Reflection coefficient  R of the barrier is: 

![1izohslv7xmjf](img/1izohslv7xmjf.png)

![07lqzzpk7zcum](img/07lqzzpk7zcum.png)

Turning R expression into a function in order to plot where we are going to change the Energy (En) and Potential (V0).

![1dusu8w0psdln](img/1dusu8w0psdln.png)

##### Transmission coefficient T of the barrier is: 

![182hale3rimd7](img/182hale3rimd7.png)

![1w2ja4mup1rnb](img/1w2ja4mup1rnb.png)

Turning T expression into a function in order to plot where we are going to change the Energy (En) and Potential (V0).

#### 6. Plot of T and R with V0=2 and a=2

![1iqpwkmzctg7x](img/1iqpwkmzctg7x.png)

```wl
In[]:= V0 = 2;
 Plot[{Tf[En, 2], Rf[En, 2]}, {En, 0, 10}, PlotStyle -> {Red, Blue}, AxesLabel -> {"Energy", "T and R"}]
```

![05zvyfx05aoj1](img/05zvyfx05aoj1.png)

Now we fix the energy to E=1.1 and we vary values over the potential $V_0:$

#### 7. Plot of T and R with Energy = 1.1

```wl
In[]:= En = 1.1;
 Plot[{Tf[En, V], Rf[En, V]}, {V, 0, 10}, PlotStyle -> {Red, Blue}, AxesLabel -> {"\!\(\*SubscriptBox[\(V\), \(0\)]\)", "T and R"}]
```

![05r0s33g027za](img/05r0s33g027za.png)