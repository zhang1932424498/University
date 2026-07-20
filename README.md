
この課題では、2次元力学系の Morse Decomposition を可視化した。
使用した力学系は次のとおりである。
使用した力学系：
dx/dt = x - x^3
dy/dt = -y

Python プログラムでは、ベクトル場と3つの平衡点を描画した。
  M- = (-1, 0)：安定平衡点
  M0 = (0, 0)：鞍点
  M+ = (1, 0)：安定平衡点
これらの平衡点は不変集合（Invariant Set）であり、Morse Set とみなすことができる。
鞍点 M0 からは M- と M+ に向かう軌道が存在する。そのため、Morse Graph は次のようになる。
      M0
    ↓    ↓
   M-    M+
この図は、不変集合とその接続関係によって力学系の長期的な振る舞いを表現したものである。また、この図は Morse Decomposition の基本的な考え方を示している。
  dynamical.py：図を生成するプログラム
  morse_decomposition_2d.png：生成した図
