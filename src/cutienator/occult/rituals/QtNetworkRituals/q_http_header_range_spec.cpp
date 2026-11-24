//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttpheaders.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qdebug.h>

//  bool QHttpHeaderRangeSpec::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QHttpHeaderRangeSpec7isValidEv(
    const QHttpHeaderRangeSpec *self) {
  return self->isValid();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QHttpHeaderRangeSpec &range)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK20QHttpHeaderRangeSpec(
    const QDebug *debug,
    const QHttpHeaderRangeSpec *range) {
  return new QDebug(operator<<(*debug, *range));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  bool operator==(const QHttpHeaderRangeSpec &lhs, const
//      QHttpHeaderRangeSpec &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QHttpHeaderRangeSpecS1_(
    const QHttpHeaderRangeSpec *lhs,
    const QHttpHeaderRangeSpec *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QHttpHeaderRangeSpec &lhs, const
//      QHttpHeaderRangeSpec &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QHttpHeaderRangeSpecS1_(
    const QHttpHeaderRangeSpec *lhs,
    const QHttpHeaderRangeSpec *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QHttpHeaderRangeSpec::~QHttpHeaderRangeSpec()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpHeaderRangeSpecD1Ev(QHttpHeaderRangeSpec *self) {
  delete self;
}
