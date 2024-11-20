echo "Seleccione qué gráfico desea ejecutar:"
echo "1) BACKTRACKING: Tiempo de ejecución vs Proporcion de datos de entrada (n x m)^k"
# echo "2) PROGRAMACION LINEAL: Tiempo de ejecución vs Proporcion de datos de entrada (n x m)^k"
echo "3) APROXIMACIÓN: Tiempo de ejecución vs Proporcion de datos de entrada (n x m)^k"
echo "4) APROXIMACIÓN:  r'(A) vs Proporcion de datos de entrada (n*m)^k"

read -p "Ingrese una opción (1-4): " opcion

case $opcion in
    1)
        py grafico.py --grafico BT_tiempo_vs_matriz
        ;;
    2)
        py grafico.py --grafico PL_tiempo_vs_matriz
        ;;
    3)
        py grafico.py --grafico APROX_tiempo_vs_matriz
        ;;
    4)
        py grafico.py --grafico APROX_cota
        ;;
    *)
        echo "Opción no válida"
        ;;
esac
