// 2622. Cache With Time Limit

class TimeLimitedCache {
    map = {}
    set(key, value, duration) {
        let bool = false
        if(key in this.map){
            bool = true
            clearTimeout(this.map[key][1])
        }
        let timeout = setTimeout(()=>{
            delete this.map[key]
        }, duration)
        this.map[key] = [value, timeout]
        return bool
    };
    get(key) {
        if(key in this.map){
            return this.map[key][0]
        }
        return -1
    };
    count() {
        return Object.entries(this.map).length
    };
}