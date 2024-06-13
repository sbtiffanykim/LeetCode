/**
 * @param {string} val
 * @return {Object}
 */

function expect(val1) {
    return {
        toBe: function(val2) {
            if (val1 !== val2) {
              throw new Error('Not Equal')
            } 
            return true;
        },
        notToBe: function(val2) {
            if (val1 === val2) {
                throw new Error('Equal')
            } 
            return true;
        }
    }
}