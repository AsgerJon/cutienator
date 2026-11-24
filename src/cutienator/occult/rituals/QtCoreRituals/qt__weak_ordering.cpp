//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcompare.h>
#include <QtCore/qflags.h>

//  partial_ordering Qt::weak_ordering::operator partial_ordering() const
extern "C" Q_DECL_EXPORT
Qt::partial_ordering *ritual_ZNK2Qt13weak_orderingcvNS_16partial_orderingEEv(
    const Qt::weak_ordering *self) {
  return new Qt::partial_ordering(self->operator Qt::partial_ordering());
}

//  bool operator==(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_13weak_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::weak_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator==(*lhs, *a1);
}

//  bool operator!=(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_13weak_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::weak_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator!=(*lhs, *a1);
}

//  bool operator<(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtltENS_13weak_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::weak_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<(*lhs, *a1);
}

//  bool operator<=(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtleENS_13weak_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::weak_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<=(*lhs, *a1);
}

//  bool operator>(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgtENS_13weak_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::weak_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>(*lhs, *a1);
}

//  bool operator>=(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgeENS_13weak_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::weak_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>=(*lhs, *a1);
}

//  bool operator==(QtPrivate::CompareAgainstLiteralZero a0, weak_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqEN9QtPrivate25CompareAgainstLiteralZeroENS_13weak_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::weak_ordering *rhs) {
  return operator==(*a0, *rhs);
}

//  bool operator!=(QtPrivate::CompareAgainstLiteralZero a0, weak_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneEN9QtPrivate25CompareAgainstLiteralZeroENS_13weak_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::weak_ordering *rhs) {
  return operator!=(*a0, *rhs);
}

//  bool operator<(QtPrivate::CompareAgainstLiteralZero a0, weak_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtltEN9QtPrivate25CompareAgainstLiteralZeroENS_13weak_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::weak_ordering *rhs) {
  return operator<(*a0, *rhs);
}

//  bool operator<=(QtPrivate::CompareAgainstLiteralZero a0, weak_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtleEN9QtPrivate25CompareAgainstLiteralZeroENS_13weak_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::weak_ordering *rhs) {
  return operator<=(*a0, *rhs);
}

//  bool operator>(QtPrivate::CompareAgainstLiteralZero a0, weak_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgtEN9QtPrivate25CompareAgainstLiteralZeroENS_13weak_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::weak_ordering *rhs) {
  return operator>(*a0, *rhs);
}

//  bool operator>=(QtPrivate::CompareAgainstLiteralZero a0, weak_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgeEN9QtPrivate25CompareAgainstLiteralZeroENS_13weak_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::weak_ordering *rhs) {
  return operator>=(*a0, *rhs);
}

//  bool operator==(weak_ordering lhs, weak_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_13weak_orderingES0_(
    const Qt::weak_ordering *lhs,
    const Qt::weak_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(weak_ordering lhs, weak_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_13weak_orderingES0_(
    const Qt::weak_ordering *lhs,
    const Qt::weak_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(weak_ordering lhs, partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_13weak_orderingENS_16partial_orderingE(
    const Qt::weak_ordering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(weak_ordering lhs, partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_13weak_orderingENS_16partial_orderingE(
    const Qt::weak_ordering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(partial_ordering lhs, weak_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_16partial_orderingENS_13weak_orderingE(
    const Qt::partial_ordering *lhs,
    const Qt::weak_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(partial_ordering lhs, weak_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_16partial_orderingENS_13weak_orderingE(
    const Qt::partial_ordering *lhs,
    const Qt::weak_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  Qt::weak_ordering::weak_ordering(QtPrivate::Ordering order)
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZN2Qt13weak_orderingC1EN9QtPrivate8OrderingE(
    QtPrivate::Ordering order) {
  return new Qt::weak_ordering(order);
}

//  Qt::weak_ordering::~weak_ordering()
extern "C" Q_DECL_EXPORT
void ritual_ZN2Qt13weak_orderingD1Ev(Qt::weak_ordering *self) {
  delete self;
}
