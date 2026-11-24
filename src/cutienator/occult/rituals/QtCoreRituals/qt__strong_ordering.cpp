//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcompare.h>
#include <QtCore/qflags.h>

//  partial_ordering Qt::strong_ordering::operator partial_ordering() const
extern "C" Q_DECL_EXPORT
Qt::partial_ordering *ritual_ZNK2Qt15strong_orderingcvNS_16partial_orderingEEv(
    const Qt::strong_ordering *self) {
  return new Qt::partial_ordering(self->operator Qt::partial_ordering());
}

//  weak_ordering Qt::strong_ordering::operator weak_ordering() const
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZNK2Qt15strong_orderingcvNS_13weak_orderingEEv(
    const Qt::strong_ordering *self) {
  return new Qt::weak_ordering(self->operator Qt::weak_ordering());
}

//  bool operator==(strong_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_15strong_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::strong_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator==(*lhs, *a1);
}

//  bool operator!=(strong_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_15strong_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::strong_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator!=(*lhs, *a1);
}

//  bool operator<(strong_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtltENS_15strong_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::strong_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<(*lhs, *a1);
}

//  bool operator<=(strong_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtleENS_15strong_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::strong_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<=(*lhs, *a1);
}

//  bool operator>(strong_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgtENS_15strong_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::strong_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>(*lhs, *a1);
}

//  bool operator>=(strong_ordering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgeENS_15strong_orderingEN9QtPrivate25CompareAgainstLiteralZeroE(
    const Qt::strong_ordering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>=(*lhs, *a1);
}

//  bool operator==(QtPrivate::CompareAgainstLiteralZero a0, strong_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqEN9QtPrivate25CompareAgainstLiteralZeroENS_15strong_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::strong_ordering *rhs) {
  return operator==(*a0, *rhs);
}

//  bool operator!=(QtPrivate::CompareAgainstLiteralZero a0, strong_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneEN9QtPrivate25CompareAgainstLiteralZeroENS_15strong_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::strong_ordering *rhs) {
  return operator!=(*a0, *rhs);
}

//  bool operator<(QtPrivate::CompareAgainstLiteralZero a0, strong_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtltEN9QtPrivate25CompareAgainstLiteralZeroENS_15strong_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::strong_ordering *rhs) {
  return operator<(*a0, *rhs);
}

//  bool operator<=(QtPrivate::CompareAgainstLiteralZero a0, strong_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtleEN9QtPrivate25CompareAgainstLiteralZeroENS_15strong_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::strong_ordering *rhs) {
  return operator<=(*a0, *rhs);
}

//  bool operator>(QtPrivate::CompareAgainstLiteralZero a0, strong_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgtEN9QtPrivate25CompareAgainstLiteralZeroENS_15strong_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::strong_ordering *rhs) {
  return operator>(*a0, *rhs);
}

//  bool operator>=(QtPrivate::CompareAgainstLiteralZero a0, strong_ordering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtgeEN9QtPrivate25CompareAgainstLiteralZeroENS_15strong_orderingE(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const Qt::strong_ordering *rhs) {
  return operator>=(*a0, *rhs);
}

//  bool operator==(strong_ordering lhs, strong_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_15strong_orderingES0_(
    const Qt::strong_ordering *lhs,
    const Qt::strong_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(strong_ordering lhs, strong_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_15strong_orderingES0_(
    const Qt::strong_ordering *lhs,
    const Qt::strong_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(strong_ordering lhs, partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_15strong_orderingENS_16partial_orderingE(
    const Qt::strong_ordering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(strong_ordering lhs, partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_15strong_orderingENS_16partial_orderingE(
    const Qt::strong_ordering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(partial_ordering lhs, strong_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_16partial_orderingENS_15strong_orderingE(
    const Qt::partial_ordering *lhs,
    const Qt::strong_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(partial_ordering lhs, strong_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_16partial_orderingENS_15strong_orderingE(
    const Qt::partial_ordering *lhs,
    const Qt::strong_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(strong_ordering lhs, weak_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_15strong_orderingENS_13weak_orderingE(
    const Qt::strong_ordering *lhs,
    const Qt::weak_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(strong_ordering lhs, weak_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_15strong_orderingENS_13weak_orderingE(
    const Qt::strong_ordering *lhs,
    const Qt::weak_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(weak_ordering lhs, strong_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QteqENS_13weak_orderingENS_15strong_orderingE(
    const Qt::weak_ordering *lhs,
    const Qt::strong_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(weak_ordering lhs, strong_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN2QtneENS_13weak_orderingENS_15strong_orderingE(
    const Qt::weak_ordering *lhs,
    const Qt::strong_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  Qt::strong_ordering::strong_ordering(QtPrivate::Ordering order)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN2Qt15strong_orderingC1EN9QtPrivate8OrderingE(
    QtPrivate::Ordering order) {
  return new Qt::strong_ordering(order);
}

//  Qt::strong_ordering::~strong_ordering()
extern "C" Q_DECL_EXPORT
void ritual_ZN2Qt15strong_orderingD1Ev(Qt::strong_ordering *self) {
  delete self;
}
