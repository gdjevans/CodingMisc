function handleErrors(error, req, res, next) {
    console.log(error);
    res.render(500).render('shared/500');
}

module.exports = handleErrors;