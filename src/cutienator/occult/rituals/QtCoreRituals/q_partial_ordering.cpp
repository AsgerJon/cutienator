//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcompare.h>
#include <QtCore/qflags.h>

//  bool operator==(QPartialOrdering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZeroE(
    const QPartialOrdering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator==(*lhs, *a1);
}

//  bool operator!=(QPartialOrdering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zne16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZeroE(
    const QPartialOrdering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator!=(*lhs, *a1);
}

//  bool operator<(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zlt16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZeroE(
    const QPartialOrdering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<(*lhs, *a1);
}

//  bool operator<=(QPartialOrdering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zle16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZeroE(
    const QPartialOrdering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator<=(*lhs, *a1);
}

//  bool operator>(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero
//      a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zgt16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZeroE(
    const QPartialOrdering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>(*lhs, *a1);
}

//  bool operator>=(QPartialOrdering lhs,
//      QtPrivate::CompareAgainstLiteralZero a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zge16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZeroE(
    const QPartialOrdering *lhs,
    const QtPrivate::CompareAgainstLiteralZero *a1) {
  return operator>=(*lhs, *a1);
}

//  bool operator==(QtPrivate::CompareAgainstLiteralZero a0, QPartialOrdering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN9QtPrivate25CompareAgainstLiteralZeroE16QPartialOrdering(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const QPartialOrdering *rhs) {
  return operator==(*a0, *rhs);
}

//  bool operator!=(QtPrivate::CompareAgainstLiteralZero a0, QPartialOrdering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN9QtPrivate25CompareAgainstLiteralZeroE16QPartialOrdering(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const QPartialOrdering *rhs) {
  return operator!=(*a0, *rhs);
}

//  bool operator<(QtPrivate::CompareAgainstLiteralZero a0, QPartialOrdering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltN9QtPrivate25CompareAgainstLiteralZeroE16QPartialOrdering(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const QPartialOrdering *rhs) {
  return operator<(*a0, *rhs);
}

//  bool operator<=(QtPrivate::CompareAgainstLiteralZero a0, QPartialOrdering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleN9QtPrivate25CompareAgainstLiteralZeroE16QPartialOrdering(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const QPartialOrdering *rhs) {
  return operator<=(*a0, *rhs);
}

//  bool operator>(QtPrivate::CompareAgainstLiteralZero a0, QPartialOrdering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtN9QtPrivate25CompareAgainstLiteralZeroE16QPartialOrdering(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const QPartialOrdering *rhs) {
  return operator>(*a0, *rhs);
}

//  bool operator>=(QtPrivate::CompareAgainstLiteralZero a0, QPartialOrdering
//      rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeN9QtPrivate25CompareAgainstLiteralZeroE16QPartialOrdering(
    const QtPrivate::CompareAgainstLiteralZero *a0,
    const QPartialOrdering *rhs) {
  return operator>=(*a0, *rhs);
}

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

//  QPartialOrdering::QPartialOrdering(Qt::partial_ordering order)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN2Qt16partial_orderingE(
    const Qt::partial_ordering *order) {
  return new QPartialOrdering(*order);
}

//  QPartialOrdering::QPartialOrdering(Qt::weak_ordering stdorder)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN2Qt13weak_orderingE(
    const Qt::weak_ordering *stdorder) {
  return new QPartialOrdering(*stdorder);
}

//  QPartialOrdering::QPartialOrdering(Qt::strong_ordering stdorder)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN2Qt15strong_orderingE(
    const Qt::strong_ordering *stdorder) {
  return new QPartialOrdering(*stdorder);
}

//  Qt::partial_ordering QPartialOrdering::operator partial_ordering() const
extern "C" Q_DECL_EXPORT
Qt::partial_ordering *ritual_ZNK16QPartialOrderingcvN2Qt16partial_orderingEEv(
    const QPartialOrdering *self) {
  return new Qt::partial_ordering(self->operator Qt::partial_ordering());
}

//  bool operator==(QPartialOrdering lhs, Qt::partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq16QPartialOrderingN2Qt16partial_orderingE(
    const QPartialOrdering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(QPartialOrdering lhs, Qt::partial_ordering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zne16QPartialOrderingN2Qt16partial_orderingE(
    const QPartialOrdering *lhs,
    const Qt::partial_ordering *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(Qt::partial_ordering lhs, QPartialOrdering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN2Qt16partial_orderingE16QPartialOrdering(
    const Qt::partial_ordering *lhs,
    const QPartialOrdering *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(Qt::partial_ordering lhs, QPartialOrdering rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN2Qt16partial_orderingE16QPartialOrdering(
    const Qt::partial_ordering *lhs,
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
