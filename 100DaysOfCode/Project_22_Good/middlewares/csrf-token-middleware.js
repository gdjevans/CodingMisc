function addCSRFToken(rfeq, res, next) {
    res.locals.csrfToken = req.csrfToken();
    next();
}

module.exports = addCSRFToken;