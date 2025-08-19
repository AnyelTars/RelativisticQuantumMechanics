# Relativistic Quantum Mechanics

By: Salazar Angel and Potosi Quray

## TISE:  The Barrier Potential 

#### 1. Solving the Schrodinger Equation

![079g4p3hjg4ep](img/079g4p3hjg4ep.png)

```wl
In[]:= f[x_] := Piecewise[{{0, x < 0}, {Subscript[V, 0], 0 <= x <= 2}}];
 Plot[f[x], {x, -4, 4}, PlotStyle -> Thick, AxesLabel -> {"x", "f(x)"},Filling -> Axis] 
  
 
```

![1d41wwy4is8a6](img/1d41wwy4is8a6.png)

```wl
In[]:= 
```

##### Regions to the left and right of the barrier potential

The time-independent Schrodinger Equation has different forms in the regions to the left and right of the barrier potential:

##### First region x<0:

![1sf713fw2jpk3](img/1sf713fw2jpk3.png)

![02l8ekxo5j4ty](img/02l8ekxo5j4ty.png)

Let k1 =  ![0qhwtbne3dhl4](img/0qhwtbne3dhl4.png) 

![1gmci66m7hp73](img/1gmci66m7hp73.png)

##### Second Region 0<x>a

![0iv4457p5l70o](img/0iv4457p5l70o.png)

![0ikvh3rky05zw](img/0ikvh3rky05zw.png)

 Let k2 =  ![0l5p7o8yy2dqp](img/0l5p7o8yy2dqp.png) 

![1s843416nijh7](img/1s843416nijh7.png)

##### Third Region x>a

![1tphsxw5rsgbk](img/1tphsxw5rsgbk.png)

![0qwucg14viqg8](img/0qwucg14viqg8.png)

![1qrex4wkvevuo](img/1qrex4wkvevuo.png)

#### 2. Getting the system of equations of Boundary Conditions

We apply the matching conditions for ψ(x) and ψ'(x), that is at the points x=0 and x=a, four equations in the arbitrary constants A, B, C, D, and F will be obtained: 

![1wh0749i2bjus](img/1wh0749i2bjus.png)

```wl
Out[]= A + B == C + D
```

![07a6jbbimc6tc](img/07a6jbbimc6tc.png)

```wl
Out[]= D E^(-2 I k2) + C E^(2 I k2) == E^(2 I k1) F
```

![1ikq82ph39h1s](img/1ikq82ph39h1s.png)

```wl
Out[]= I A k1 - I B k1 == I C k2 - I D k2
```

![1mk4l63kslouh](img/1mk4l63kslouh.png)

```wl
Out[]= -I D E^(-2 I k2)k2 + I C E^(2 I k2)k2 == I E^(2 I k1)F k1
```

#### 3. Solve this systems of equations in terms of A:

```wl
In[]:= Solve[{eq1, eq2, eq3, eq4}, {B, C, D, F}]
```

![0cfjozq69f42w](img/0cfjozq69f42w.png)

Thus we have: 

![14gm9xmu8yu5i](img/14gm9xmu8yu5i.png)

#### 4. Replacing with the constants found in the piece-wise Schrodinger equation:

![15h3v9cnn5xq9](img/15h3v9cnn5xq9.png)

with:

![1gehah09ue2vr](img/1gehah09ue2vr.png)

#### 5. Computing the Transmission and Reflection coefficient

##### The Reflection coefficient  R of the barrier is: 

![1h3odb7z4fzkl](img/1h3odb7z4fzkl.png)

![0h3usoqdxdgot](img/0h3usoqdxdgot.png)

Turning R expression into a function in order to plot where we are going to change the Energy (En) and Potential (V0).

![1ih4asklrfd7d](img/1ih4asklrfd7d.png)

##### Transmission coefficient T of the barrier is: 

![069gukmdjyqzy](img/069gukmdjyqzy.png)

![19kqafxokul55](img/19kqafxokul55.png)

Turning T expression into a function in order to plot where we are going to change the Energy (En) and Potential (V0).

#### 6. Plot of T and R with V0=2 and a=2

![1xnlurvwb4vxh](img/1xnlurvwb4vxh.png)

```wl
In[]:= V0 = 2;
 Plot[{Tf[En, 2], Rf[En, 2]}, {En, 0, 10}, PlotStyle -> {Red, Blue}, AxesLabel -> {"Energy", "T and R"}]
```

![0p8jwh93ylifc](img/0p8jwh93ylifc.png)

Now we fix the energy to E=1.1 and we vary values over the potential $V_0:$

#### 7. Plot of T and R with Energy = 1.1

```wl
In[]:= En = 1.1;
 Plot[{Tf[En, V], Rf[En, V]}, {V, 0, 10}, PlotStyle -> {Red, Blue}, AxesLabel -> {"\!\(\*SubscriptBox[\(V\), \(0\)]\)", "T and R"}]
```

![0i4ol4315zgu9](img/0i4ol4315zgu9.png)