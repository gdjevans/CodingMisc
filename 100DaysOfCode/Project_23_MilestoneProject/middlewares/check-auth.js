function checkAuthStatus(req, res, next) {
    const uid = req.session.uid;

    if (!uid) {
        return next();
    }

    res.locals.uid = uid;
    res.locals.isAuth = true;
    res.local.isAdmin = req.session.isAdmin;
    next();
}

module.exports = checkAuthStatus;