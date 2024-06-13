class Counter {
    constructor(init) {
        this.init = init;
        this.val = init;
    }
    increment() {
        this.val += 1;
        return this.val;
    }
    decrement() {
        this.val -= 1;
        return this.val;
    }
    reset() {
        this.val = this.init;
        return this.val;
    }
}

const createCounter = function(num) {
    return new Counter(num);
};
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */