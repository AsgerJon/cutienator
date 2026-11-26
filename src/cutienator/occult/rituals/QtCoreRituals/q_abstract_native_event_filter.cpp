//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractnativeeventfilter.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qabstractnativeeventfilter.h>
#include <QtCore/qbytearray.h>

//  QAbstractNativeEventFilter::~QAbstractNativeEventFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractNativeEventFilterD1Ev(
    QAbstractNativeEventFilter *self) {
  delete self;
}

//  bool QAbstractNativeEventFilter::nativeEventFilter(const QByteArray
//      &eventType, void *message, qintptr *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractNativeEventFilter17nativeEventFilterERK10QByteArrayPvPx(
    QAbstractNativeEventFilter *self,
    const QByteArray *eventType,
    void *message,
    qintptr *result) {
  return self->nativeEventFilter(*eventType, message, result);
}
