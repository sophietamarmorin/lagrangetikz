# lagrangetikz


I decided to make this because I was preparing a bunch of graphing problems for my precalculus students. There are a few less-than-satisfactory ways to plot functions in TikZ (https://tikz.dev/tikz-plots). Something that TikZ does quite well is plotting polynomials, so you might as well just fit an interpolating polynomial to your desired function and have TikZ plot that. The goal for this package is to take a function (or table of values) and some plotting parameters and output TikZ code that can be pasted into a TeX file.

I wrote my own Lagrange interpolator in core Python as an exercise, but it would probably be better to use numpy. It might also be better to use Chebyshev polynomials via chebpy (https://github.com/chebpy/chebpy). If I get that far I'll probably fork this repo so that the choice of interpolating polynomials can be passed as a parameter.
