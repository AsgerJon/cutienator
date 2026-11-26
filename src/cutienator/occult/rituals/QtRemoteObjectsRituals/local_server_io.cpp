//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'LocalServerIo' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 5 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__LocalServerIo.cpp, line 1, as moc:LocalServerIo
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN13LocalServerIoE_t {};
} // unnamed namespace

template <> constexpr inline auto LocalServerIo::qt_create_metaobjectdata<qt_meta_tag_ZN13LocalServerIoE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "LocalServerIo"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<LocalServerIo, qt_meta_tag_ZN13LocalServerIoE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject LocalServerIo::staticMetaObject = { {
    QMetaObject::SuperData::link<QtROServerIoDevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13LocalServerIoE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13LocalServerIoE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN13LocalServerIoE_t>.metaTypes,
    nullptr
} };

void LocalServerIo::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<LocalServerIo *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *LocalServerIo::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *LocalServerIo::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13LocalServerIoE_t>.strings))
        return static_cast<void*>(this);
    return QtROServerIoDevice::qt_metacast(_clname);
}

int LocalServerIo::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtROServerIoDevice::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 95, as _ZN13LocalServerIoC1EP12QLocalSocketP7QObject
inline LocalServerIo::LocalServerIo(QLocalSocket *conn, QObject *parent)
    : QtROServerIoDevice(parent), m_connection(conn)
{
    m_connection->setParent(this);
    connect(conn, &QIODevice::readyRead, this, &QtROServerIoDevice::readyRead);
    connect(conn, &QLocalSocket::disconnected, this, &QtROServerIoDevice::disconnected);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 103, as _ZNK13LocalServerIo10connectionEv
inline QIODevice *LocalServerIo::connection() const
{
    return m_connection;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 108, as _ZN13LocalServerIo7doCloseEv
inline void LocalServerIo::doClose()
{
    m_connection->disconnectFromServer();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *LocalServerIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13LocalServerIo10metaObjectEv(
    const LocalServerIo *self) {
  return self->metaObject();
}

//  void *LocalServerIo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13LocalServerIo11qt_metacastEPKc(
    LocalServerIo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LocalServerIo::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13LocalServerIo11qt_metacallEN11QMetaObject4CallEiPPv(
    LocalServerIo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LocalServerIo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13LocalServerIo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LocalServerIo::tr(s, c, n));
}

//  LocalServerIo::LocalServerIo(QLocalSocket *conn, QObject *parent)
extern "C" Q_DECL_EXPORT
LocalServerIo *ritual_ZN13LocalServerIoC1EP12QLocalSocketP7QObject(
    QLocalSocket *conn,
    QObject *parent) {
  return new LocalServerIo(conn, parent);
}

//  QIODevice *LocalServerIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK13LocalServerIo10connectionEv(
    const LocalServerIo *self) {
  return self->connection();
}

//  void LocalServerIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalServerIo7doCloseEv(LocalServerIo *self) {
  self->doClose();
}
