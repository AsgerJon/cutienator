//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcansignaldescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSerialBus/qcansignaldescription.h>
#include <QtCore/qdebug.h>

//  bool operator==(const MultiplexValueRange &lhs, const MultiplexValueRange
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN21QCanSignalDescription19MultiplexValueRangeES2_(
    const QCanSignalDescription::MultiplexValueRange *lhs,
    const QCanSignalDescription::MultiplexValueRange *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const MultiplexValueRange &lhs, const MultiplexValueRange
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN21QCanSignalDescription19MultiplexValueRangeES2_(
    const QCanSignalDescription::MultiplexValueRange *lhs,
    const QCanSignalDescription::MultiplexValueRange *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const MultiplexValueRange &range)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRKN21QCanSignalDescription19MultiplexValueRangeE(
    const QDebug *dbg,
    const QCanSignalDescription::MultiplexValueRange *range) {
  return new QDebug(operator<<(*dbg, *range));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QCanSignalDescription::MultiplexValueRange::debugStreaming(QDebug
//      dbg, const MultiplexValueRange &range)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN21QCanSignalDescription19MultiplexValueRange14debugStreamingE6QDebugRKS0_(
    const QDebug *dbg,
    const QCanSignalDescription::MultiplexValueRange *range) {
  return new QDebug(
      QCanSignalDescription::MultiplexValueRange::debugStreaming(
          *dbg,
          *range));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QCanSignalDescription::MultiplexValueRange::~MultiplexValueRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanSignalDescription19MultiplexValueRangeD1Ev(
    QCanSignalDescription::MultiplexValueRange *self) {
  delete self;
}
