//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnectionfactories_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QtROExternalIoDevice' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnectionfactories_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#if defined(Q_OS_QNX)
#include <QtRemoteObjects/private/qconnection_qnx_backend_p.h>
#endif
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#include <QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__QtROExternalIoDevice.cpp, line 1, as moc:QtROExternalIoDevice
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QtROExternalIoDeviceE_t {};
} // unnamed namespace

template <> constexpr inline auto QtROExternalIoDevice::qt_create_metaobjectdata<qt_meta_tag_ZN20QtROExternalIoDeviceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtROExternalIoDevice"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QtROExternalIoDevice, qt_meta_tag_ZN20QtROExternalIoDeviceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtROExternalIoDevice::staticMetaObject = { {
    QMetaObject::SuperData::link<QtROIoDeviceBase::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QtROExternalIoDeviceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QtROExternalIoDeviceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QtROExternalIoDeviceE_t>.metaTypes,
    nullptr
} };

void QtROExternalIoDevice::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QtROExternalIoDevice *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QtROExternalIoDevice::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtROExternalIoDevice::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QtROExternalIoDeviceE_t>.strings))
        return static_cast<void*>(this);
    return QtROIoDeviceBase::qt_metacast(_clname);
}

int QtROExternalIoDevice::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtROIoDeviceBase::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 245, as _ZN20QtROExternalIoDevice7doCloseEv
inline void QtROExternalIoDevice::doClose()
{
    Q_D(QtROExternalIoDevice);
    if (isOpen())
        d->m_device->close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 231, as _ZNK20QtROExternalIoDevice10connectionEv
inline QIODevice *QtROExternalIoDevice::connection() const
{
    Q_D(const QtROExternalIoDevice);
    return d->m_device;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 252, as _ZNK20QtROExternalIoDevice10deviceTypeEv
inline QString QtROExternalIoDevice::deviceType() const
{
    return QStringLiteral("QtROExternalIoDevice");
}

//  from ../qtremoteobjects/src/remoteobjects/qconnectionfactories.cpp, line 237, as _ZNK20QtROExternalIoDevice6isOpenEv
inline bool QtROExternalIoDevice::isOpen() const
{
    Q_D(const QtROExternalIoDevice);
    if (!d->m_device)
        return false;
    return d->m_device->isOpen() && QtROIoDeviceBase::isOpen();
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

//  void *QtROExternalIoDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QtROExternalIoDevice11qt_metacastEPKc(
    QtROExternalIoDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtROExternalIoDevice::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QtROExternalIoDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    QtROExternalIoDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtROExternalIoDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QtROExternalIoDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtROExternalIoDevice::tr(s, c, n));
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
