//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsourceio_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearrayview.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <cstring>
#include <QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#include <QtCore/qstringlist.h>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qabstractitemmodel.h>
#include <algorithm>
#include <iterator>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 1101, as _ZN20QRemoteObjectPackets16DataStreamPacketC1Et
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline DataStreamPacket::DataStreamPacket(quint16 id)
    : QDataStream(&array, QIODevice::WriteOnly), baseAddress(0), size(0)
{
    this->setVersion(QtRemoteObjects::dataStreamVersion);
    this->setByteOrder(QDataStream::LittleEndian);
    *this << quint32(0);
    *this << id;
}
}  // namespace QRemoteObjectPackets

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsourceio.cpp, line 272, as _ZN21QRemoteObjectSourceIo16handleConnectionEv
inline void QRemoteObjectSourceIo::handleConnection()
{
    qRODebug(this) << "handleConnection" << m_connections;

    QtROServerIoDevice *conn = m_server->nextPendingConnection();
    newConnection(conn);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 526, as _ZN13DynamicApiMapC1EP7QObjectPK11QMetaObjectRK7QStringS7_
inline DynamicApiMap::DynamicApiMap(QObject *object, const QMetaObject *metaObject, const QString &name, const QString &typeName)
    : m_name(name),
      m_typeName(typeName),
      m_metaObject(metaObject),
      m_cachedMetamethodIndex(-1)
{
    m_enumOffset = metaObject->enumeratorOffset();
    m_enumCount = metaObject->enumeratorCount() - m_enumOffset;

    const int propCount = metaObject->propertyCount();
    const int propOffset = metaObject->propertyOffset();
    m_properties.reserve(propCount-propOffset);
    QSet<int> invalidSignals;
    for (int i = propOffset; i < propCount; ++i) {
        const QMetaProperty property = metaObject->property(i);
        const auto metaType = property.metaType();
        if (metaType.flags().testFlag(QMetaType::PointerToQObject)) {
            auto propertyMeta = metaType.metaObject();
            QObject *child = property.read(object).value<QObject *>();
            const QMetaObject *meta = child ? child->metaObject() : propertyMeta;
            if (!meta) {
                const int notifyIndex = metaObject->property(i).notifySignalIndex();
                if (notifyIndex != -1)
                    invalidSignals << notifyIndex;
                continue;
            }
            if (meta->inherits(&QAbstractItemModel::staticMetaObject)) {
                const QByteArray name = QByteArray::fromRawData(property.name(),
                                                                qsizetype(qstrlen(property.name())));
                const QByteArray infoName = name.toUpper() + QByteArrayLiteral("_ROLES");
                const int infoIndex = metaObject->indexOfClassInfo(infoName.constData());
                QByteArray roleInfo;
                if (infoIndex >= 0) {
                    auto ci = metaObject->classInfo(infoIndex);
                    roleInfo = QByteArray::fromRawData(ci.value(), qsizetype(qstrlen(ci.value())));
                }
                m_models << ModelInfo({qobject_cast<QAbstractItemModel *>(child),
                                       QString::fromLatin1(property.name()),
                                       roleInfo});
            } else {
                QString typeName = QtRemoteObjects::getTypeNameAndMetaobjectFromClassInfo(meta);
                if (typeName.isNull()) {
                    typeName = QString::fromLatin1(meta->className());
                    if (typeName.contains(QLatin1String("QQuick")))
                        typeName.remove(QLatin1String("QQuick"));
                    else if (int index = typeName.indexOf(QLatin1String("_QMLTYPE_")))
                        typeName.truncate(index);
                    // TODO better way to ensure we have consistent typenames between source/replicas?
                    else if (typeName.endsWith(QLatin1String("Source")))
                        typeName.chop(6);
                }

                m_subclasses << new DynamicApiMap(child, meta, QString::fromLatin1(property.name()), typeName);
            }
        }
        m_properties << i;
        const int notifyIndex = metaObject->property(i).notifySignalIndex();
        if (notifyIndex != -1) {
            m_signals << notifyIndex;
            m_propertyAssociatedWithSignal.append(i-propOffset);
            //The starting values of _signals will be the notify signals
            //So if we are processing _signal with index i, api->sourcePropertyIndex(_propertyAssociatedWithSignal.at(i))
            //will be the property that changed.  This is only valid if i < _propertyAssociatedWithSignal.size().
        }
    }
    const int methodCount = metaObject->methodCount();
    const int methodOffset = metaObject->methodOffset();
    for (int i = methodOffset; i < methodCount; ++i) {
        const QMetaMethod mm = metaObject->method(i);
        const QMetaMethod::MethodType m = mm.methodType();
        if (m == QMetaMethod::Signal) {
            if (m_signals.indexOf(i) >= 0)  // Already added as a property notifier
                continue;
            if (invalidSignals.contains(i)) // QObject with no metatype
                continue;
            m_signals << i;
        } else if (m == QMetaMethod::Slot || m == QMetaMethod::Method)
            m_methods << i;
    }

    m_objectSignature = QtPrivate::qtro_classinfo_signature(metaObject);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 174, as _ZN15LocalServerImpl16setSocketOptionsE6QFlagsIN12QLocalServer12SocketOptionEE
inline void LocalServerImpl::setSocketOptions(QLocalServer::SocketOptions options)
{
    m_server.setSocketOptions(options);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsourceio.cpp, line 81, as _ZN21QRemoteObjectSourceIo15disableRemotingEP7QObject
inline bool QRemoteObjectSourceIo::disableRemoting(QObject *object)
{
    QRemoteObjectRootSource *source = m_objectToSourceMap.take(object);
    if (!source)
        return false;

    delete source;
    return true;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsourceio.cpp, line 303, as _ZNK21QRemoteObjectSourceIo13serverAddressEv
inline QUrl QRemoteObjectSourceIo::serverAddress() const
{
    if (m_server)
        return m_server->address();
    return m_address;
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectSourceIo that Python can take functions over in. Every QRemoteObjectSourceIo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceIoCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceIoCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceIoCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceIoCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceIoCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceIoCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceIoCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectSourceIo : public QRemoteObjectSourceIo {
public:
  using QRemoteObjectSourceIo::QRemoteObjectSourceIo;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall0 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall1 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall2 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall3 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall4 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall5 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectSourceIoCall6 call = reinterpret_cast<CuteQRemoteObjectSourceIoCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectSourceIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QRemoteObjectSourceIo10metaObjectEv(
    const QRemoteObjectSourceIo *self) {
  return self->metaObject();
}

//  void *QRemoteObjectSourceIo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QRemoteObjectSourceIo11qt_metacastEPKc(
    QRemoteObjectSourceIo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QRemoteObjectSourceIo::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QRemoteObjectSourceIo11qt_metacallEN11QMetaObject4CallEiPPv(
    QRemoteObjectSourceIo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QRemoteObjectSourceIo::~QRemoteObjectSourceIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIoD1Ev(QRemoteObjectSourceIo *self) {
  delete self;
}

//  bool QRemoteObjectSourceIo::disableRemoting(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QRemoteObjectSourceIo15disableRemotingEP7QObject(
    QRemoteObjectSourceIo *self,
    QObject *object) {
  return self->disableRemoting(object);
}

//  QUrl QRemoteObjectSourceIo::serverAddress() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QRemoteObjectSourceIo13serverAddressEv(
    const QRemoteObjectSourceIo *self) {
  return new QUrl(self->serverAddress());
}

//  void QRemoteObjectSourceIo::handleConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIo16handleConnectionEv(
    QRemoteObjectSourceIo *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectSourceIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleConnection()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleConnection()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRemoteObjectSourceIo::onServerDisconnect(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIo18onServerDisconnectEP7QObject(
    QRemoteObjectSourceIo *self,
    QObject *obj) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectSourceIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onServerDisconnect(QObject *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onServerDisconnect(QObject *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&obj)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRemoteObjectSourceIo::onServerRead(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIo12onServerReadEP7QObject(
    QRemoteObjectSourceIo *self,
    QObject *obj) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectSourceIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onServerRead(QObject *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onServerRead(QObject *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&obj)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRemoteObjectSourceIo::remoteObjectAdded(const
//      QRemoteObjectSourceLocation &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIo17remoteObjectAddedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRemoteObjectSourceIo *self,
    const QRemoteObjectSourceLocation *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectSourceIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteObjectAdded(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteObjectAdded(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRemoteObjectSourceIo::remoteObjectRemoved(const
//      QRemoteObjectSourceLocation &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIo19remoteObjectRemovedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRemoteObjectSourceIo *self,
    const QRemoteObjectSourceLocation *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectSourceIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteObjectRemoved(const QRemoteObjectSourceLocation &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteObjectRemoved(const QRemoteObjectSourceLocation &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QRemoteObjectSourceIo::serverRemoved(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectSourceIo13serverRemovedERK4QUrl(
    QRemoteObjectSourceIo *self,
    const QUrl *url) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QRemoteObjectSourceIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serverRemoved(const QUrl &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serverRemoved(const QUrl &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(url)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQRemoteObjectSourceIo, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectSourceIo(
    QRemoteObjectSourceIo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectSourceIo *>(self)->take(key, call);
}
