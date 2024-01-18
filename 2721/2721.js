// 2721. Execute Asynchronous Functions in Parallel

// then/catch
const promiseAll = function(functions) {
    if(functions.length === 0){
        resolve([]);
        return;
    }
    let promises = [];
    for(let i=0;i<functions.length;i++){
        promises.push(functions[i]());
    }
    let ans = [];
    let done = 0;
    return new Promise((resolve,reject)=>{
        for(let i=0;i<promises.length;i++){
            promises[i].then(res=>{
                ans[i] = res;
                done++;
                if(done === functions.length){
                    resolve(ans);
                }
            }).catch(error=>{
                reject(error);
            })
        }
    })
};

// async/await with forEach
// note await is blocking for the rest of the code in the container async function
// with forEach we are using an async function for each await
const promiseAll2 = function(functions) {
    if(functions.length === 0){
        resolve([]);
        return;
    }
    let promises = []
    for(let i=0;i<functions.length;i++){
        promises.push(functions[i]());
    }
    let ans = []
    let done = 0
    return new Promise((resolve, reject)=>{
        promises.forEach(async (p, i)=>{
            try {
                ans[i] = await p;
                if(++done === promises.length){
                    resolve(ans);
                }
            } catch(error){
                reject(error);
            }
        })
    })
};

// async await with for loop and function

const promiseAll3 = function(functions) {
    if(functions.length === 0){
        resolve([]);
        return;
    }
    let promises = []
    for(let i=0;i<functions.length;i++){
        promises.push(functions[i]());
    }
    let ans = []
    let done = 0
    let wrapper = async (i, resolve, reject)=>{
        try {
            ans[i] = await promises[i];
            if(++done === promises.length){
                resolve(ans);
            }
        } catch(error){
            reject(error);
        }
    }
    return new Promise((resolve, reject)=>{
        for(let i=0;i<promises.length;i++){
            wrapper(i, resolve, reject)
        }
    })
};