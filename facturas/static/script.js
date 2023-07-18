const addButton = document.getElementById('add')
const producto = document.getElementById('producto')
const listProducto = document.getElementById('facturar2')
const deleteButton = document.querySelectorAll('.delete')


addButton.addEventListener(
    'click',
    function (e){
        e.preventDefault()
        coleDIV = producto.cloneNode(true)
        const botonClone = coleDIV.querySelector('.delete')
        botonClone.addEventListener('click',
        function(e){
            e.preventDefault()
            const contenedor = this.parentElement;
            contenedor.remove()
        }
        )
        listProducto.appendChild(coleDIV)
        
        
    }
)

deleteButton.forEach(element => {
    element.addEventListener('click',
    function(e){
        e.preventDefault()
        const contenedor = this.parentElement;
        contenedor.remove()
    }
    )
});


  