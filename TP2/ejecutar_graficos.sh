echo "Seleccione qué gráfico desea ejecutar:"
echo "1) Tiempo de ejecución vs Cantidad de elementos"
echo "2) Puntos de Sophia y Mateo vs Cantidad de elementos"
echo "3) X victorias de Sophia vs Cantidad de juegos simulados"

read -p "Ingrese una opción (1-3): " opcion

case $opcion in
    1)
        py grafico.py --grafico tiempo_vs_cantidad
        ;;
    2)
        py grafico.py --grafico puntos_vs_cantidad
        ;;
    3)
        while true; do
            read -p "Ingrese la cantidad de juegos a simular (o deje en blanco para valor por defecto): " cantidad

            if [[ -z "$cantidad" ]]; then
                py grafico.py --grafico victorias_sofia
                break
            fi

            case $cantidad in
                ''|*[!0-9]*)
                    echo "La cantidad debe ser un número entero positivo"
                    ;;
                0)
                    echo "La cantidad no puede ser 0"
                    ;;
                *)
                    # Con 10.000 elementos alcanza y sobra para tener una buena idea de cómo se comporta el algoritmo
                    if (( cantidad > 10000 )); then
                        echo "La cantidad no puede ser mayor a 10,000"
                    else
                        py grafico.py --grafico victorias_sofia --cantidad "$cantidad"
                        break
                    fi
                    ;;
            esac
        done
        ;;
    *)
        echo "Opción no válida"
        ;;
esac
