// first draft

var reorganizeString = function(s) {
    let ans = '';
    let q = new MaxPriorityQueue({
        priority: (elem) => {
            return elem.count
        }
    });
    let map = {}
    for(let i=0; i<s.length; i++){
        map[s[i]] = map[s[i]] ? map[s[i]]+1 : 1;
    };
    Object.keys(map).forEach((key)=>{
        q.enqueue({ key, count: map[key]});
    });
    if( q.front().element.count > Math.floor((s.length +1)/2)) {
        return '';
    }
 
    while(q.size() > 1) {
        let first = q.dequeue();

        let second = q.dequeue();
        ans += first.element.key + second.element.key;
        // console.log('c', c);
        if(second.element.count !== 1) {
            q.enqueue({
                key: second.element.key,
                count: second.element.count-1
            })
        }
        if(first.element.count !== 1) {
            q.enqueue({
                key: first.element.key,
                count: first.element.count-1
            })
        }
    }
    if(q.size() === 1) {
        let first = q.dequeue();
        ans += first.element.key;

    }
    return ans;
}


// another way of doing it
var reorganizeString = function(s) {
    let map = {};
    let q = new MaxPriorityQueue({
        priority: (elem) => {
            return elem.count
        }
    });
    // let arr = s.split('');
    for(let c of s) {
        map[c] = map[c] ? map[c] + 1: 1;
    }
    for(let key in map) {
        q.enqueue({ letter: key, count: map[key]});
    }
    let ans = [];
    let prev;
    while(q.size()) {
        let curr = q.dequeue().element;
        if(prev) {
            ans.push(prev.letter);
            if(prev.count > 1) {
                q.enqueue({letter: prev.letter, count: prev.count-1});
            }
        }
        prev = curr;
    }
    if(prev.count > 1) {
        return '';
    }
    ans.push(prev.letter);
    return ans.join('');
}




// another way
var reorganizeString = function(s) {
    let map = {};
    let q = new MaxPriorityQueue({
        priority: (elem) => {
            return elem.count
        }
    });
    // let arr = s.split('');
    for(let c of s) {
        map[c] = map[c] ? map[c] + 1: 1;
    }
    for(let key in map) {
        q.enqueue({ letter: key, count: map[key]});
    }
    let ans = [];
    let prev;
    while(q.size() || prev) {
        if(prev && q.size() === 0) {
            return '';
        }
        let curr = q.dequeue().element;
        ans.push(curr.letter);
        if(prev) {
            q.enqueue({ letter: prev.letter, count: prev.count-1 });
            prev = null;
        }
        if(curr.count > 1) {
            prev = curr;
        }     
    }
    return ans.join('');
}



// there's also a o(n) way of doing it where we group them and then just put them in every other until the end then do every other again