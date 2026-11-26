//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttpheaders.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qdebug.h>
#include <QtCore/QSpan>
#include <QtNetwork/QHttpHeaderRangeSpec>

//  QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func()
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSetPrivate *ritual_ZN19QHttpHeaderRangeSet6d_funcEv(
    QHttpHeaderRangeSet *self) {
  return self->d_func();
}

//  const QHttpHeaderRangeSetPrivate *QHttpHeaderRangeSet::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpHeaderRangeSetPrivate *ritual_ZNK19QHttpHeaderRangeSet6d_funcEv(
    const QHttpHeaderRangeSet *self) {
  return self->d_func();
}

//  QHttpHeaderRangeSet::QHttpHeaderRangeSet()
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetC1Ev() {
  return new QHttpHeaderRangeSet();
}

//  QHttpHeaderRangeSet::QHttpHeaderRangeSet(const QHttpHeaderRangeSet
//      &other)
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetC1ERKS_(
    const QHttpHeaderRangeSet *other) {
  return new QHttpHeaderRangeSet(*other);
}

//  QHttpHeaderRangeSet::QHttpHeaderRangeSet(QHttpHeaderRangeSet &&a0)
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetC1EOS_(
    QHttpHeaderRangeSet *a0) {
  return new QHttpHeaderRangeSet(std::move(*a0));
}

//  QHttpHeaderRangeSet::QHttpHeaderRangeSet(QSpan<const
//      QHttpHeaderRangeSpec> r)
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetC1E5QSpanIK20QHttpHeaderRangeSpecLm18446744073709551615EE(
    const QSpan<const QHttpHeaderRangeSpec> *r) {
  return new QHttpHeaderRangeSet(*r);
}

//  QHttpHeaderRangeSet::QHttpHeaderRangeSet(std::initializer_list<QHttpHeade
//      rRangeSpec> r)
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetC1ESt16initializer_listI20QHttpHeaderRangeSpecE(
    const std::initializer_list<QHttpHeaderRangeSpec> *r) {
  return new QHttpHeaderRangeSet(*r);
}

//  QHttpHeaderRangeSet &QHttpHeaderRangeSet::operator=(const
//      QHttpHeaderRangeSet &other)
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetaSERKS_(
    QHttpHeaderRangeSet *self,
    const QHttpHeaderRangeSet *other) {
  return &(self->operator=(*other));
}

//  QHttpHeaderRangeSet &QHttpHeaderRangeSet::operator=(QHttpHeaderRangeSet
//      &&other)
extern "C" Q_DECL_EXPORT
QHttpHeaderRangeSet *ritual_ZN19QHttpHeaderRangeSetaSEOS_(
    QHttpHeaderRangeSet *self,
    QHttpHeaderRangeSet *other) {
  return &(self->operator=(std::move(*other)));
}

//  QHttpHeaderRangeSet::~QHttpHeaderRangeSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpHeaderRangeSetD1Ev(QHttpHeaderRangeSet *self) {
  delete self;
}

//  void QHttpHeaderRangeSet::swap(QHttpHeaderRangeSet &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpHeaderRangeSet4swapERS_(
    QHttpHeaderRangeSet *self,
    QHttpHeaderRangeSet *other) {
  self->swap(*other);
}

//  QSpan<const QHttpHeaderRangeSpec> QHttpHeaderRangeSet::ranges() const
extern "C" Q_DECL_EXPORT
QSpan<const QHttpHeaderRangeSpec> *ritual_ZNK19QHttpHeaderRangeSet6rangesEv(
    const QHttpHeaderRangeSet *self) {
  return new QSpan<const QHttpHeaderRangeSpec>(self->ranges());
}

//  void QHttpHeaderRangeSet::setRanges(QSpan<const QHttpHeaderRangeSpec> r)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpHeaderRangeSet9setRangesE5QSpanIK20QHttpHeaderRangeSpecLm18446744073709551615EE(
    QHttpHeaderRangeSet *self,
    const QSpan<const QHttpHeaderRangeSpec> *r) {
  self->setRanges(*r);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QHttpHeaderRangeSet &ranges)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QHttpHeaderRangeSet(
    const QDebug *debug,
    const QHttpHeaderRangeSet *ranges) {
  return new QDebug(operator<<(*debug, *ranges));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  bool operator==(const QHttpHeaderRangeSet &lhs, const QHttpHeaderRangeSet
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QHttpHeaderRangeSetS1_(
    const QHttpHeaderRangeSet *lhs,
    const QHttpHeaderRangeSet *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QHttpHeaderRangeSet &lhs, const QHttpHeaderRangeSet
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QHttpHeaderRangeSetS1_(
    const QHttpHeaderRangeSet *lhs,
    const QHttpHeaderRangeSet *rhs) {
  return operator!=(*lhs, *rhs);
}

//  a QSpan<const QHttpHeaderRangeSpec> a ritual of QHttpHeaderRangeSet gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHttpHeaderRangeSet__QSpan_const_QHttpHeaderRangeSpec(
    QSpan<const QHttpHeaderRangeSpec> *self) {
  delete self;
}
