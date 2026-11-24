//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnectionfactories_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnectionfactories_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qconnectionfactories_p.h"
#include "qremoteobjectpacket_p.h"
#if defined(Q_OS_QNX)
#include "qconnection_qnx_backend_p.h"
#endif
#include "qconnection_local_backend_p.h"
#include "qconnection_tcpip_backend_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 231, as _ZNK20QtROExternalIoDevice10connectionEv
inline QIODevice *QtROExternalIoDevice::connection() const
{
    Q_D(const QtROExternalIoDevice);
    return d->m_device;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 237, as _ZNK20QtROExternalIoDevice6isOpenEv
inline bool QtROExternalIoDevice::isOpen() const
{
    Q_D(const QtROExternalIoDevice);
    if (!d->m_device)
        return false;
    return d->m_device->isOpen() && QtROIoDeviceBase::isOpen();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 245, as _ZN20QtROExternalIoDevice7doCloseEv
inline void QtROExternalIoDevice::doClose()
{
    Q_D(QtROExternalIoDevice);
    if (isOpen())
        d->m_device->close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 252, as _ZNK20QtROExternalIoDevice10deviceTypeEv
inline QString QtROExternalIoDevice::deviceType() const
{
    return QStringLiteral("QtROExternalIoDevice");
}
//  -----------------------------------------------------------------------

//  Only a class built on QtROExternalIoDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtROExternalIoDevice : QtROExternalIoDevice {
  using QtROExternalIoDevice::doClose;
  using QtROExternalIoDevice::deviceType;
};

//  const QMetaObject *QtROExternalIoDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QtROExternalIoDevice10metaObjectEv(
    const QtROExternalIoDevice *self) {
  return self->metaObject();
}

//  QIODevice *QtROExternalIoDevice::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK20QtROExternalIoDevice10connectionEv(
    const QtROExternalIoDevice *self) {
  return self->connection();
}

//  bool QtROExternalIoDevice::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QtROExternalIoDevice6isOpenEv(
    const QtROExternalIoDevice *self) {
  return self->isOpen();
}

//  void QtROExternalIoDevice::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QtROExternalIoDevice7doCloseEv(QtROExternalIoDevice *self) {
  self->doClose();
}

//  QString QtROExternalIoDevice::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QtROExternalIoDevice10deviceTypeEv(
    const QtROExternalIoDevice *self) {
  return new QString(self->deviceType());
}

//  QtROExternalIoDevicePrivate *QtROExternalIoDevice::d_func()
extern "C" Q_DECL_EXPORT
QtROExternalIoDevicePrivate *ritual_ZN20QtROExternalIoDevice6d_funcEv(
    QtROExternalIoDevice *self) {
  return self->d_func();
}

//  const QtROExternalIoDevicePrivate *QtROExternalIoDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QtROExternalIoDevicePrivate *ritual_ZNK20QtROExternalIoDevice6d_funcEv(
    const QtROExternalIoDevice *self) {
  return self->d_func();
}

//  QIODevice *QtROExternalIoDevice::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZNK20QtROExternalIoDevice10connectionEv(
    const QtROExternalIoDevice *self) {
  return self->QtROExternalIoDevice::connection();
}

//  bool QtROExternalIoDevice::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QtROExternalIoDevice6isOpenEv(
    const QtROExternalIoDevice *self) {
  return self->QtROExternalIoDevice::isOpen();
}

//  void QtROExternalIoDevice::doClose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QtROExternalIoDevice7doCloseEv(
    QtROExternalIoDevice *self) {
  static_cast<OwnQtROExternalIoDevice *>(self)->OwnQtROExternalIoDevice::doClose();
}

//  QString QtROExternalIoDevice::deviceType() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QtROExternalIoDevice10deviceTypeEv(
    const QtROExternalIoDevice *self) {
  return new QString(
      static_cast<const OwnQtROExternalIoDevice *>(self)->OwnQtROExternalIoDevice::deviceType());
}
