#include <iostream>
#include <cmath>

using namespace std;

// Función a encontrar la raíz
double f(double x) {
    return pow(x, 5) + 3*pow(x, 4) - 2*pow(x, 3) + 6*pow(x, 2) - x + 2;
}

// Método de Muller para encontrar la raíz
double muller(double x0, double x1, double x2, double tol) {
    double h1 = x1 - x0;
    double h2 = x2 - x1;
    double d1 = (f(x1) - f(x0)) / h1;
    double d2 = (f(x2) - f(x1)) / h2;
    double d3 = (f(x2) - f(x0)) / (h1 + h2);
    double a = d3;
    double b = a*h2 + d2;
    double c = f(x2);
    double x3 = x2 - (2*c) / (b + sqrt(pow(b, 2) - 4*a*c));
    double error = abs(x3 - x2);
    cout << "x0 = " << x0 << ", x1 = " << x1 << ", x2 = " << x2 << ", x3 = " << x3 << ", error = " << error << endl;
    if (error < tol) {
        return x3;
    } else {
        return muller(x1, x2, x3, tol);
    }
}

int main() {
    double x0 = 1;
    double x1 = 2;
    double x2 = 3;
    double tol = 1e-6;
    double root = muller(x0, x1, x2, tol);
    cout << "La raíz es: " << root << endl;
    return 0;
}