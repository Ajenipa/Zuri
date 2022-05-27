const mDom = document.getElementById("math")
const eDom = document.getElementById("eng")
const pDom = document.getElementById("phy")
const cDom = document.getElementById("chem")
const bDom = document.getElementById("bio")
const sDom = document.getElementById("sum")
const iDom = document.getElementById("i")
const oDom = document.getElementById("ok")
const btnDom = document.getElementById("btn")
btnDom.addEventListener('click', ()=>{
    console.log(iDom)
})
let sum = mDom.value + eDom.value
console.log( Number(mDom).value)