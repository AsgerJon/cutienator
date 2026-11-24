//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttpheaders.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qdebug.h>

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

//  QHttpHeaderRangeSet::~QHttpHeaderRangeSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpHeaderRangeSetD1Ev(QHttpHeaderRangeSet *self) {
  delete self;
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
