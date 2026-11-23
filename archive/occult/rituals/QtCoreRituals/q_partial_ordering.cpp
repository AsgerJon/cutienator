//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcompare.h>

//  bool operator==(QPartialOrdering lhs, QPartialOrdering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq16QPartialOrderingS_(
    const QPartialOrdering *lhs,
    const QPartialOrdering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(QPartialOrdering lhs, QPartialOrdering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zne16QPartialOrderingS_(
    const QPartialOrdering *lhs,
    const QPartialOrdering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QPartialOrdering::QPartialOrdering(QtPrivate::Ordering order)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN9QtPrivate8OrderingE(
    QtPrivate::Ordering order) {
  return new QPartialOrdering(order);
}

//  QPartialOrdering::QPartialOrdering(QtPrivate::LegacyUncomparable order)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN9QtPrivate18LegacyUncomparableE(
    QtPrivate::LegacyUncomparable order) {
  return new QPartialOrdering(order);
}

//  bool QPartialOrdering::isOrdered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QPartialOrdering9isOrderedEv(const QPartialOrdering *self) {
  return self->isOrdered();
}

//  QPartialOrdering::~QPartialOrdering()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPartialOrderingD1Ev(QPartialOrdering *self) {
  delete self;
}
