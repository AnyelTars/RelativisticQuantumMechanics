# Relativistic Quantum Mechanics

By: Salazar Angel and Potosi Quray

## TISE:  The Barrier Potential 

#### 1. Solving the Schrodinger Equation

![0tmvpxgmtpyp5](img/0tmvpxgmtpyp5.png)

```wl
In[]:= f[x_] := Piecewise[{{0, x < 0}, {Subscript[V, 0], 0 <= x <= 2}}];
 Plot[f[x], {x, -4, 4}, PlotStyle -> Thick, AxesLabel -> {"x", "f(x)"},Filling -> Axis] 
  
 
```

![1atgoq728cpnm](img/1atgoq728cpnm.png)

```wl
In[]:= 
```

##### Regions to the left and right of the barrier potential

The time-independent Schrodinger Equation has different forms in the regions to the left and right of the barrier potential:

##### First region x<0:

![0i3vmb7lm61p0](img/0i3vmb7lm61p0.png)

![18ko2rr66dty5](img/18ko2rr66dty5.png)

Let k1 =  ![0qhwtbne3dhl4](img/0qhwtbne3dhl4.png) 

![0u6hmcj1o0lga](img/0u6hmcj1o0lga.png)

##### Second Region 0<x>a

![1553oi2lsjcvy](img/1553oi2lsjcvy.png)

![06pxjbn8omylx](img/06pxjbn8omylx.png)

 Let k2 =  ![0l5p7o8yy2dqp](img/0l5p7o8yy2dqp.png) 

![1u8d3ffk9xa71](img/1u8d3ffk9xa71.png)

##### Third Region x>a

![1729c2edbg1xq](img/1729c2edbg1xq.png)

![09v7q8i15fn7i](img/09v7q8i15fn7i.png)

![1btvv5oodcu8d](img/1btvv5oodcu8d.png)

#### 2. Getting the system of equations of Boundary Conditions

We apply the matching conditions for ψ(x) and ψ'(x), that is at the points x=0 and x=a, four equations in the arbitrary constants A, B, C, D, and F will be obtained: 

![1b6meunoov88h](img/1b6meunoov88h.png)

```wl
Out[]= A + B == C + D
```

![08s1c1eh8m5mn](img/08s1c1eh8m5mn.png)

```wl
Out[]= D E^(-2 I k2) + C E^(2 I k2) == E^(2 I k1) F
```

![1pkn15wod9xji](img/1pkn15wod9xji.png)

```wl
Out[]= I A k1 - I B k1 == I C k2 - I D k2
```

![06zcd1y2rfzob](img/06zcd1y2rfzob.png)

```wl
Out[]= -I D E^(-2 I k2)k2 + I C E^(2 I k2)k2 == I E^(2 I k1)F k1
```

#### 3. Solve this systems of equations in terms of A:

```wl
In[]:= Solve[{eq1, eq2, eq3, eq4}, {B, C, D, F}]
```

![0cpclx4lf5c53](img/0cpclx4lf5c53.png)

Thus we have: 

![1av3h81hczde8](img/1av3h81hczde8.png)

#### 4. Replacing with the constants found in the piece-wise Schrodinger equation:

![1lnn1wzymmsbx](img/1lnn1wzymmsbx.png)

with:

![0fz5c4oghkzf1](img/0fz5c4oghkzf1.png)

#### 5. Computing the Transmission and Reflection coefficient

##### The Reflection coefficient  R of the barrier is: 

![0ur4rts1ej2ib](img/0ur4rts1ej2ib.png)

![0v3zc6ceoheec](img/0v3zc6ceoheec.png)

Turning R expression into a function in order to plot where we are going to change the Energy (En) and Potential (V0).

![1wtb8g74vthyb](img/1wtb8g74vthyb.png)

##### Transmission coefficient T of the barrier is: 

![02cbosu02hnln](img/02cbosu02hnln.png)

![1dozrpbh6mpl9](img/1dozrpbh6mpl9.png)

Turning T expression into a function in order to plot where we are going to change the Energy (En) and Potential (V0).

#### 6. Plot of T and R with V0=2 and a=2

![09x9xhoi1uh49](img/09x9xhoi1uh49.png)

```wl
In[]:= V0 = 2;
 Plot[{Tf[En, 2], Rf[En, 2]}, {En, 0, 10}, PlotStyle -> {Red, Blue}, AxesLabel -> {"Energy", "T and R"}]
```

![09mivfwi0tmh8](img/09mivfwi0tmh8.png)

Now we fix the energy to E=1.1 and we vary values over the potential $V_0:$

#### 7. Plot of T and R with Energy = 1.1

```wl
In[]:= En = 1.1;
 Plot[{Tf[En, V], Rf[En, V]}, {V, 0, 10}, PlotStyle -> {Red, Blue}, AxesLabel -> {"\!\(\*SubscriptBox[\(V\), \(0\)]\)", "T and R"}]
```

![007f4k88egm54](img/007f4k88egm54.png)