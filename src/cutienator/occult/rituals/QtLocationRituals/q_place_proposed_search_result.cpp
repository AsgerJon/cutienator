//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceproposedsearchresult.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtLocation/qplaceproposedsearchresult.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/qplacesearchrequest.h>

//  QPlaceProposedSearchResult::QPlaceProposedSearchResult()
extern "C" Q_DECL_EXPORT
QPlaceProposedSearchResult *ritual_ZN26QPlaceProposedSearchResultC1Ev() {
  return new QPlaceProposedSearchResult();
}

#if !(defined(Q_QDOC))
//  QPlaceProposedSearchResult::QPlaceProposedSearchResult(const
//      QPlaceSearchResult &other)
extern "C" Q_DECL_EXPORT
QPlaceProposedSearchResult *ritual_ZN26QPlaceProposedSearchResultC1ERK18QPlaceSearchResult(
    const QPlaceSearchResult *other) {
  return new QPlaceProposedSearchResult(*other);
}
#endif  // !(defined(Q_QDOC))

//  QPlaceProposedSearchResult::~QPlaceProposedSearchResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceProposedSearchResultD1Ev(
    QPlaceProposedSearchResult *self) {
  delete self;
}

//  QPlaceSearchRequest QPlaceProposedSearchResult::searchRequest() const
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZNK26QPlaceProposedSearchResult13searchRequestEv(
    const QPlaceProposedSearchResult *self) {
  return new QPlaceSearchRequest(self->searchRequest());
}

//  void QPlaceProposedSearchResult::setSearchRequest(const
//      QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceProposedSearchResult16setSearchRequestERK19QPlaceSearchRequest(
    QPlaceProposedSearchResult *self,
    const QPlaceSearchRequest *request) {
  self->setSearchRequest(*request);
}
