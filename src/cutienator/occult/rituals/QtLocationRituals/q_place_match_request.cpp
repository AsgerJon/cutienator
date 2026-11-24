//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacematchrequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacematchrequest.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QPlaceMatchRequest::QPlaceMatchRequest()
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestC1Ev() {
  return new QPlaceMatchRequest();
}

//  QPlaceMatchRequest::QPlaceMatchRequest(const QPlaceMatchRequest &other)
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestC1ERKS_(
    const QPlaceMatchRequest *other) {
  return new QPlaceMatchRequest(*other);
}

//  QPlaceMatchRequest::~QPlaceMatchRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequestD1Ev(QPlaceMatchRequest *self) {
  delete self;
}

//  bool operator==(const QPlaceMatchRequest &lhs, const QPlaceMatchRequest
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QPlaceMatchRequestS1_(
    const QPlaceMatchRequest *lhs,
    const QPlaceMatchRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceMatchRequest &lhs, const QPlaceMatchRequest
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QPlaceMatchRequestS1_(
    const QPlaceMatchRequest *lhs,
    const QPlaceMatchRequest *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QPlace> QPlaceMatchRequest::places() const
extern "C" Q_DECL_EXPORT
QList<QPlace> *ritual_ZNK18QPlaceMatchRequest6placesEv(
    const QPlaceMatchRequest *self) {
  return new QList<QPlace>(self->places());
}

//  void QPlaceMatchRequest::setPlaces(const QList<QPlace> &places)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest9setPlacesERK5QListI6QPlaceE(
    QPlaceMatchRequest *self,
    const QList<QPlace> *places) {
  self->setPlaces(*places);
}

//  void QPlaceMatchRequest::setResults(const QList<QPlaceSearchResult>
//      &results)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest10setResultsERK5QListI18QPlaceSearchResultE(
    QPlaceMatchRequest *self,
    const QList<QPlaceSearchResult> *results) {
  self->setResults(*results);
}

//  QVariantMap QPlaceMatchRequest::parameters() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK18QPlaceMatchRequest10parametersEv(
    const QPlaceMatchRequest *self) {
  return new QMap<QString, QVariant>(self->parameters());
}

//  void QPlaceMatchRequest::setParameters(const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest13setParametersERK4QMapI7QString8QVariantE(
    QPlaceMatchRequest *self,
    const QMap<QString, QVariant> *parameters) {
  self->setParameters(*parameters);
}

//  void QPlaceMatchRequest::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest5clearEv(QPlaceMatchRequest *self) {
  self->clear();
}

//  bool QPlaceMatchRequest::isEqual(const QPlaceMatchRequest &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPlaceMatchRequest7isEqualERKS_(
    const QPlaceMatchRequest *self,
    const QPlaceMatchRequest *other) {
  return self->isEqual(*other);
}
