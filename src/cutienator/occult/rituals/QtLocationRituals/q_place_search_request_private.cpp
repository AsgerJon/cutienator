//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacesearchrequest_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacesearchrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacesearchrequest.h>

//  bool QPlaceSearchRequestPrivate::operator==(const
//      QPlaceSearchRequestPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPlaceSearchRequestPrivateeqERKS_(
    const QPlaceSearchRequestPrivate *self,
    const QPlaceSearchRequestPrivate *other) {
  return self->operator==(*other);
}

//  void QPlaceSearchRequestPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceSearchRequestPrivate5clearEv(
    QPlaceSearchRequestPrivate *self) {
  self->clear();
}

//  const QPlaceSearchRequestPrivate *QPlaceSearchRequestPrivate::get(const
//      QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
const QPlaceSearchRequestPrivate *ritual_ZN26QPlaceSearchRequestPrivate3getERK19QPlaceSearchRequest(
    const QPlaceSearchRequest *request) {
  return QPlaceSearchRequestPrivate::get(*request);
}

//  QPlaceSearchRequestPrivate
//      *QPlaceSearchRequestPrivate::get(QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceSearchRequestPrivate *ritual_ZN26QPlaceSearchRequestPrivate3getER19QPlaceSearchRequest(
    QPlaceSearchRequest *request) {
  return QPlaceSearchRequestPrivate::get(*request);
}

//  QPlaceSearchRequestPrivate::~QPlaceSearchRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceSearchRequestPrivateD1Ev(
    QPlaceSearchRequestPrivate *self) {
  delete self;
}
