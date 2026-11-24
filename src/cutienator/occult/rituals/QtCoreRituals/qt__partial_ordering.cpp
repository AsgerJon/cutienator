//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcompare.h>
#include <QtCore/qflags.h>

//  bool operator==(partial_ordering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_16partial_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::partial_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator==(*lhs, *a1);
}

//  bool operator!=(partial_ordering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_16partial_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::partial_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator!=(*lhs, *a1);
}

//  bool operator<(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtltENS_16partial_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::partial_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<(*lhs, *a1);
}

//  bool operator<=(partial_ordering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtleENS_16partial_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::partial_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<=(*lhs, *a1);
}

//  bool operator>(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgtENS_16partial_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::partial_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>(*lhs, *a1);
}

//  bool operator>=(partial_ordering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgeENS_16partial_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::partial_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>=(*lhs, *a1);
}

//  bool operator==(QtPrivate::CompareAgainstLiteralZero a0, partial_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqEN9QtPrivate25CompareAgainstLiteralZeroENS_16partial_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::partial_ordering *rhs) {
  return operator==(*a0, *rhs);
}

//  bool operator!=(QtPrivate::CompareAgainstLiteralZero a0, partial_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneEN9QtPrivate25CompareAgainstLiteralZeroENS_16partial_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::partial_ordering *rhs) {
  return operator!=(*a0, *rhs);
}

//  bool operator<(QtPrivate::CompareAgainstLiteralZero a0, partial_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtltEN9QtPrivate25CompareAgainstLiteralZeroENS_16partial_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::partial_ordering *rhs) {
  return operator<(*a0, *rhs);
}

//  bool operator<=(QtPrivate::CompareAgainstLiteralZero a0, partial_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtleEN9QtPrivate25CompareAgainstLiteralZeroENS_16partial_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::partial_ordering *rhs) {
  return operator<=(*a0, *rhs);
}

//  bool operator>(QtPrivate::CompareAgainstLiteralZero a0, partial_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgtEN9QtPrivate25CompareAgainstLiteralZeroENS_16partial_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::partial_ordering *rhs) {
  return operator>(*a0, *rhs);
}

//  bool operator>=(QtPrivate::CompareAgainstLiteralZero a0, partial_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgeEN9QtPrivate25CompareAgainstLiteralZeroENS_16partial_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::partial_ordering *rhs) {
  return operator>=(*a0, *rhs);
}

//  bool operator==(partial_ordering lhs, partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_16partial_orderingES0_(
    const Qt::partial_ordering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(partial_ordering lhs, partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_16partial_orderingES0_(
    const Qt::partial_ordering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  Qt::partial_ordering::partial_ordering(QtPrivate::Ordering order)
extern "C" Q_DECL_EXPORT
Qt::partial_ordering *ritual_ZN2Qt16partial_orderingC1EN9QtPrivate8OrderingE(
    QtPrivate::Ordering order) {
  return new Qt::partial_ordering(order);
}

//  Qt::partial_ordering::partial_ordering(QtPrivate::Uncomparable order)
extern "C" Q_DECL_EXPORT
Qt::partial_ordering *ritual_ZN2Qt16partial_orderingC1EN9QtPrivate12UncomparableE(
    QtPrivate::Uncomparable order) {
  return new Qt::partial_ordering(order);
}

//  bool Qt::partial_ordering::isOrdered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK2Qt16partial_ordering9isOrderedEv(
    const Qt::partial_ordering *self) {
  return self->isOrdered();
}

//  Qt::partial_ordering::~partial_ordering()
extern "C" Q_DECL_EXPORT
void ritual_ZN2Qt16partial_orderingD1Ev(Qt::partial_ordering *self) {
  delete self;
}
