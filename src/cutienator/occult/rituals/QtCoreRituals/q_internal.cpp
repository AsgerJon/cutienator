//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qnamespace.h>

//  bool QInternal::registerCallback(Callback a0, qInternalCallback a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QInternal16registerCallbackENS_8CallbackEPFbPPvE(
    QInternal::Callback a0,
    void *a1) {
  return QInternal::registerCallback(
      a0,
      reinterpret_cast<qInternalCallback>(a1));
}

//  bool QInternal::unregisterCallback(Callback a0, qInternalCallback a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QInternal18unregisterCallbackENS_8CallbackEPFbPPvE(
    QInternal::Callback a0,
    void *a1) {
  return QInternal::unregisterCallback(
      a0,
      reinterpret_cast<qInternalCallback>(a1));
}

//  bool QInternal::activateCallbacks(Callback a0, void **a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QInternal17activateCallbacksENS_8CallbackEPPv(
    QInternal::Callback a0,
    void **a1) {
  return QInternal::activateCallbacks(a0, a1);
}

//  QInternal::~QInternal()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QInternalD1Ev(QInternal *self) {
  delete self;
}
