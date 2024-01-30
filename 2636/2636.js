// 2636. Promise Pool

var promisePool = async function(functions, n) {
    return new Promise((resolve)=>{
        let processing = 0;
        let index = 0;
        let helper = () =>{
            if(processing === 0 && index === functions.length){
                resolve()
                return
            }
            while(processing < n && index < functions.length){
                processing++;
                functions[index++]().then(()=>{
                    processing--;
                    helper()
                })
            }
        }
        helper()
    })
};