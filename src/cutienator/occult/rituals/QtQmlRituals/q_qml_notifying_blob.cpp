//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlnotifyingblob_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlnotifyingblob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQmlNotifyingBlob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlNotifyingBlob : QQmlNotifyingBlob {
  using QQmlNotifyingBlob::completed;
  using QQmlNotifyingBlob::downloadProgressChanged;
};

//  void QQmlNotifyingBlob::registerCallback(Callback *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob16registerCallbackEPNS_8CallbackE(
    QQmlNotifyingBlob *self,
    QQmlNotifyingBlob::Callback *callback) {
  self->registerCallback(callback);
}

//  void QQmlNotifyingBlob::unregisterCallback(Callback *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob18unregisterCallbackEPNS_8CallbackE(
    QQmlNotifyingBlob *self,
    QQmlNotifyingBlob::Callback *callback) {
  self->unregisterCallback(callback);
}

//  void QQmlNotifyingBlob::completed()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob9completedEv(QQmlNotifyingBlob *self) {
  self->completed();
}

//  void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlNotifyingBlob23downloadProgressChangedEd(
    QQmlNotifyingBlob *self,
    qreal a0) {
  self->downloadProgressChanged(a0);
}

//  void QQmlNotifyingBlob::completed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlNotifyingBlob9completedEv(QQmlNotifyingBlob *self) {
  static_cast<OwnQQmlNotifyingBlob *>(self)->OwnQQmlNotifyingBlob::completed();
}

//  void QQmlNotifyingBlob::downloadProgressChanged(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlNotifyingBlob23downloadProgressChangedEd(
    QQmlNotifyingBlob *self,
    qreal a0) {
  static_cast<OwnQQmlNotifyingBlob *>(self)->OwnQQmlNotifyingBlob::downloadProgressChanged(
      a0);
}
