const db = require('../data/database');

class Quote {
    static async getRandomQuote() {
        const quotes = await db.getDb().collection('quotes').find().toArray();
        const randomQuote = Math.floor(Math.random * quotes.length);
        // [1, 2, 3] => length: 3 => 0.8 * 3 => 2.4 => Math.floor(2.4) => 2
        
        return randomQuote;
    }
}

module.exports = Quote;