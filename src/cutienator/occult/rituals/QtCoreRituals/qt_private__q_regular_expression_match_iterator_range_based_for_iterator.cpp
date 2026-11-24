//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(regularexpression)
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>

//  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::QRegular
//      ExpressionMatchIteratorRangeBasedForIterator()
extern "C" Q_DECL_EXPORT
QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBasedForIteratorC1Ev() {
  return new QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator();
}

//  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::QRegular
//      ExpressionMatchIteratorRangeBasedForIterator(const
//      QRegularExpressionMatchIterator &iterator)
extern "C" Q_DECL_EXPORT
QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBasedForIteratorC1ERK31QRegularExpressionMatchIterator(
    const QRegularExpressionMatchIterator *iterator) {
  return new QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator(
      *iterator);
}

//  const QRegularExpressionMatch &QtPrivate::QRegularExpressionMatchIterator
//      RangeBasedForIterator::operator*() const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZNK9QtPrivate52QRegularExpressionMatchIteratorRangeBasedForIteratordeEv(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *self) {
  return new QRegularExpressionMatch(self->operator*());
}

//  QRegularExpressionMatchIteratorRangeBasedForIterator QtPrivate::QRegularE
//      xpressionMatchIteratorRangeBasedForIterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBasedForIteratorppEi(
    QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *self,
    int a0) {
  return new QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator(
      self->operator++(
          a0));
}

//  bool operator==(const
//      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
//      QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_52QRegularExpressionMatchIteratorRangeBasedForIteratorES2_(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *lhs,
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const
//      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
//      QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_52QRegularExpressionMatchIteratorRangeBasedForIteratorES2_(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *lhs,
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const
//      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
//      QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_52QRegularExpressionMatchIteratorRangeBasedForIteratorERKNS_60QRegularExpressionMatchIteratorRangeBasedForIteratorSentinelE(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *lhs,
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const
//      QRegularExpressionMatchIteratorRangeBasedForIterator &lhs, const
//      QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_52QRegularExpressionMatchIteratorRangeBasedForIteratorERKNS_60QRegularExpressionMatchIteratorRangeBasedForIteratorSentinelE(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *lhs,
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const
//      QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &lhs,
//      const QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_60QRegularExpressionMatchIteratorRangeBasedForIteratorSentinelERKNS_52QRegularExpressionMatchIteratorRangeBasedForIteratorE(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel *lhs,
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const
//      QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel &lhs,
//      const QRegularExpressionMatchIteratorRangeBasedForIterator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_60QRegularExpressionMatchIteratorRangeBasedForIteratorSentinelERKNS_52QRegularExpressionMatchIteratorRangeBasedForIteratorE(
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIteratorSentinel *lhs,
    const QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator::~QRegula
//      rExpressionMatchIteratorRangeBasedForIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate52QRegularExpressionMatchIteratorRangeBasedForIteratorD1Ev(
    QtPrivate::QRegularExpressionMatchIteratorRangeBasedForIterator *self) {
  delete self;
}

#endif  // QT_CONFIG(regularexpression)
#endif  // QT_CONFIG(regularexpression)
