//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplaceresult.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/qplace.h>

//  QPlaceResult::QPlaceResult()
extern "C" Q_DECL_EXPORT
QPlaceResult *ritual_ZN12QPlaceResultC1Ev() {
  return new QPlaceResult();
}

#if !(defined(Q_QDOC))
//  QPlaceResult::QPlaceResult(const QPlaceSearchResult &other)
extern "C" Q_DECL_EXPORT
QPlaceResult *ritual_ZN12QPlaceResultC1ERK18QPlaceSearchResult(
    const QPlaceSearchResult *other) {
  return new QPlaceResult(*other);
}
#endif  // !(defined(Q_QDOC))

//  QPlaceResult::~QPlaceResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResultD1Ev(QPlaceResult *self) {
  delete self;
}

//  qreal QPlaceResult::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPlaceResult8distanceEv(const QPlaceResult *self) {
  return self->distance();
}

//  void QPlaceResult::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResult11setDistanceEd(
    QPlaceResult *self,
    qreal distance) {
  self->setDistance(distance);
}

//  QPlace QPlaceResult::place() const
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZNK12QPlaceResult5placeEv(const QPlaceResult *self) {
  return new QPlace(self->place());
}

//  void QPlaceResult::setPlace(const QPlace &place)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResult8setPlaceERK6QPlace(
    QPlaceResult *self,
    const QPlace *place) {
  self->setPlace(*place);
}

//  bool QPlaceResult::isSponsored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPlaceResult11isSponsoredEv(const QPlaceResult *self) {
  return self->isSponsored();
}

//  void QPlaceResult::setSponsored(bool sponsored)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResult12setSponsoredEb(
    QPlaceResult *self,
    bool sponsored) {
  self->setSponsored(sponsored);
}
