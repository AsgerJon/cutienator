//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qlocalserver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qlocalserver.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qlocalserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLocalServer *QLocalServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLocalServer *ritual_ZN19QLocalServerPrivate6q_funcEv(
    QLocalServerPrivate *self) {
  return self->q_func();
}

//  const QLocalServer *QLocalServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLocalServer *ritual_ZNK19QLocalServerPrivate6q_funcEv(
    const QLocalServerPrivate *self) {
  return self->q_func();
}

//  QLocalServerPrivate::QLocalServerPrivate()
extern "C" Q_DECL_EXPORT
QLocalServerPrivate *ritual_ZN19QLocalServerPrivateC1Ev() {
  return new QLocalServerPrivate();
}

//  size_t QLocalServerPrivate::_qt_property_socketOptions_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN19QLocalServerPrivate33_qt_property_socketOptions_offsetEv() {
  return QLocalServerPrivate::_qt_property_socketOptions_offset();
}

#endif  // QT_CONFIG(localserver)
#endif  // QT_CONFIG(localserver)
