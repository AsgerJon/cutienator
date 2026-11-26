//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'ProxyInfo' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 3 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtRemoteObjects/QRemoteObjectHostBase>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectregistry.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qabstractitemmodel.h>
#include <memory>
#include <algorithm>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from QtRemoteObjects__ProxyInfo.cpp, line 1, as moc:ProxyInfo
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN9ProxyInfoE_t {};
} // unnamed namespace

template <> constexpr inline auto ProxyInfo::qt_create_metaobjectdata<qt_meta_tag_ZN9ProxyInfoE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "ProxyInfo"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<ProxyInfo, qt_meta_tag_ZN9ProxyInfoE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject ProxyInfo::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9ProxyInfoE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9ProxyInfoE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN9ProxyInfoE_t>.metaTypes,
    nullptr
} };

void ProxyInfo::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<ProxyInfo *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *ProxyInfo::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *ProxyInfo::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN9ProxyInfoE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int ProxyInfo::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2878, as _ZN9ProxyInfoD0Ev
inline ProxyInfo::~ProxyInfo() {
    for (ProxyReplicaInfo* info : std::as_const(proxiedReplicas))
        delete info;
    delete proxyNode;
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2841, as _ZN9ProxyInfoC1EP17QRemoteObjectNodeP21QRemoteObjectHostBaseSt8functionIFb11QStringViewS5_EE
inline ProxyInfo::ProxyInfo(QRemoteObjectNode *node, QRemoteObjectHostBase *parent,
                     QRemoteObjectHostBase::RemoteObjectNameFilter filter)
    : QObject(parent)
    , proxyNode(node)
    , parentNode(parent)
    , proxyFilter(filter)
{
    const auto registry = node->registry();
    proxyNode->setObjectName(QLatin1String("_ProxyNode"));

    connect(registry, &QRemoteObjectRegistry::remoteObjectAdded, this,
            [this](const QRemoteObjectSourceLocation &entry)
    {
        this->proxyObject(entry, ProxyDirection::Forward);
    });
    connect(registry, &QRemoteObjectRegistry::remoteObjectRemoved, this,
            &ProxyInfo::unproxyObject);
    connect(registry, &QRemoteObjectRegistry::initialized, this, [registry, this]() {
        QRemoteObjectSourceLocations locations = registry->sourceLocations();
        QRemoteObjectSourceLocations::const_iterator i = locations.constBegin();
        while (i != locations.constEnd()) {
            proxyObject(QRemoteObjectSourceLocation(i.key(), i.value()));
            ++i;
        }
    });

    connect(registry, &QRemoteObjectRegistry::stateChanged, this,
            [this](QRemoteObjectRegistry::State state, QRemoteObjectRegistry::State /*oldState*/) {
        if (state != QRemoteObjectRegistry::Suspect)
            return;
        // unproxy all objects
        for (ProxyReplicaInfo* info : std::as_const(proxiedReplicas))
            disableAndDeleteObject(info);
        proxiedReplicas.clear();
    });
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2884, as _ZN9ProxyInfo15setReverseProxyESt8functionIFb11QStringViewS1_EE
inline bool ProxyInfo::setReverseProxy(QRemoteObjectHostBase::RemoteObjectNameFilter filter)
{
    if (qobject_cast<QRemoteObjectRegistryHost *>(parentNode) == nullptr) {
        qWarning() << "Setting up reverseProxy() can only be done on a Registry node.";
        return false;
    }
    const auto registry = parentNode->registry();
    this->reverseFilter = filter;

    connect(registry, &QRemoteObjectRegistry::remoteObjectAdded, this,
            [this](const QRemoteObjectSourceLocation &entry)
    {
        this->proxyObject(entry, ProxyDirection::Reverse);
    });
    connect(registry, &QRemoteObjectRegistry::remoteObjectRemoved, this,
            &ProxyInfo::unproxyObject);
    connect(registry, &QRemoteObjectRegistry::initialized, this, [registry, this]() {
        QRemoteObjectSourceLocations locations = registry->sourceLocations();
        QRemoteObjectSourceLocations::const_iterator i = locations.constBegin();
        while (i != locations.constEnd()) {
            proxyObject(QRemoteObjectSourceLocation(i.key(), i.value()), ProxyDirection::Reverse);
            ++i;
        }
    });

    return true;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2912, as _ZN9ProxyInfo11proxyObjectERKSt4pairI7QString31QRemoteObjectSourceLocationInfoENS_14ProxyDirectionE
inline void ProxyInfo::proxyObject(const QRemoteObjectSourceLocation &entry, ProxyDirection direction)
{
    const QString name = entry.first;
    const QString typeName = entry.second.typeName;

    if (direction == ProxyDirection::Forward) {
        // If we are using the reverse proxy, this can be called when reverse proxy objects are added
        // Don't try to proxy those back.  We can detect this because the hosting node will be our proxyNode.
        auto host = qobject_cast<QRemoteObjectHost *>(proxyNode);
        if (host && entry.second.hostUrl == host->hostUrl())
            return;
        if (!proxyFilter(name, typeName))
            return;
        Q_ASSERT(!proxiedReplicas.contains(name));

        qCDebug(QT_REMOTEOBJECT) << "Starting proxy for" << name << "from" << entry.second.hostUrl;

        if (entry.second.typeName == QAIMADAPTER()) {
            QAbstractItemModelReplica *rep = proxyNode->acquireModel(name);
            proxiedReplicas.insert(name, new ProxyReplicaInfo{rep, direction});
            connect(rep, &QAbstractItemModelReplica::initialized, this,
                    [rep, name, this]() { this->parentNode->enableRemoting(rep, name, QList<int>()); });
        } else {
            QRemoteObjectDynamicReplica *rep = proxyNode->acquireDynamic(name);
            proxiedReplicas.insert(name, new ProxyReplicaInfo{rep, direction});
            connect(rep, &QRemoteObjectDynamicReplica::initialized, this,
                    [rep, name, this]() { this->parentNode->enableRemoting(rep, name); });
        }
    } else {
        // If we are using the reverse proxy, this can be called when proxy objects are added
        // Don't try to proxy those back.  We can detect this because the hosting node will be the parentNode.
        // Since we know the parentNode has to be a RegistryNode for reverse proxy to work, we compare against
        // the registryUrl().
        if (entry.second.hostUrl == parentNode->registryUrl())
            return;
        if (!reverseFilter(name, typeName))
            return;
        Q_ASSERT(!proxiedReplicas.contains(name));

        qCDebug(QT_REMOTEOBJECT) << "Starting reverse proxy for" << name << "from" << entry.second.hostUrl;

        if (entry.second.typeName == QAIMADAPTER()) {
            QAbstractItemModelReplica *rep = this->parentNode->acquireModel(name);
            proxiedReplicas.insert(name, new ProxyReplicaInfo{rep, direction});
            connect(rep, &QAbstractItemModelReplica::initialized, this,
                    [rep, name, this]()
            {
                QRemoteObjectHostBase *host = qobject_cast<QRemoteObjectHostBase *>(this->proxyNode);
                Q_ASSERT(host);
                host->enableRemoting(rep, name, QList<int>());
            });
        } else {
            QRemoteObjectDynamicReplica *rep = this->parentNode->acquireDynamic(name);
            proxiedReplicas.insert(name, new ProxyReplicaInfo{rep, direction});
            connect(rep, &QRemoteObjectDynamicReplica::initialized, this,
                    [rep, name, this]()
            {
                QRemoteObjectHostBase *host = qobject_cast<QRemoteObjectHostBase *>(this->proxyNode);
                Q_ASSERT(host);
                host->enableRemoting(rep, name);
            });
        }
    }

}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2978, as _ZN9ProxyInfo13unproxyObjectERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE
inline void ProxyInfo::unproxyObject(const QRemoteObjectSourceLocation &entry)
{
    const QString name = entry.first;

    if (proxiedReplicas.contains(name)) {
        qCDebug(QT_REMOTEOBJECT)  << "Stopping proxy for" << name;
        auto const info = proxiedReplicas.take(name);
        disableAndDeleteObject(info);
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2989, as _ZN9ProxyInfo22disableAndDeleteObjectEP16ProxyReplicaInfo
inline void ProxyInfo::disableAndDeleteObject(ProxyReplicaInfo* info)
{
    if (info->direction == ProxyDirection::Forward)
        this->parentNode->disableRemoting(info->replica);
    else {
        QRemoteObjectHostBase *host = qobject_cast<QRemoteObjectHostBase *>(this->proxyNode);
        Q_ASSERT(host);
        host->disableRemoting(info->replica);
    }
    delete info;
}
//  -----------------------------------------------------------------------

//  A ProxyInfo that Python can take functions over in. Every ProxyInfo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteProxyInfoCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteProxyInfoCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProxyInfoCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProxyInfoCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProxyInfoCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProxyInfoCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProxyInfoCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteProxyInfo : public ProxyInfo {
public:
  using ProxyInfo::ProxyInfo;
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
      CuteProxyInfoCall0 call = reinterpret_cast<CuteProxyInfoCall0>(taken[0]);
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
      CuteProxyInfoCall1 call = reinterpret_cast<CuteProxyInfoCall1>(taken[1]);
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
      CuteProxyInfoCall2 call = reinterpret_cast<CuteProxyInfoCall2>(taken[2]);
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
      CuteProxyInfoCall3 call = reinterpret_cast<CuteProxyInfoCall3>(taken[3]);
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
      CuteProxyInfoCall4 call = reinterpret_cast<CuteProxyInfoCall4>(taken[4]);
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
      CuteProxyInfoCall5 call = reinterpret_cast<CuteProxyInfoCall5>(taken[5]);
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
      CuteProxyInfoCall6 call = reinterpret_cast<CuteProxyInfoCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ProxyInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9ProxyInfo10metaObjectEv(
    const ProxyInfo *self) {
  return self->metaObject();
}

//  void *ProxyInfo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9ProxyInfo11qt_metacastEPKc(ProxyInfo *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int ProxyInfo::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9ProxyInfo11qt_metacallEN11QMetaObject4CallEiPPv(
    ProxyInfo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ProxyInfo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9ProxyInfo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ProxyInfo::tr(s, c, n));
}

//  ProxyInfo::ProxyInfo(QRemoteObjectNode *node, QRemoteObjectHostBase
//      *parent, QRemoteObjectHostBase::RemoteObjectNameFilter filter)
extern "C" Q_DECL_EXPORT
ProxyInfo *ritual_ZN9ProxyInfoC1EP17QRemoteObjectNodeP21QRemoteObjectHostBaseSt8functionIFb11QStringViewS5_EE(
    QRemoteObjectNode *node,
    QRemoteObjectHostBase *parent,
    const QRemoteObjectHostBase::RemoteObjectNameFilter *filter) {
  return new CuteProxyInfo(node, parent, *filter);
}

//  ProxyInfo::~ProxyInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9ProxyInfoD1Ev(ProxyInfo *self) {
  delete self;
}

//  bool
//      ProxyInfo::setReverseProxy(QRemoteObjectHostBase::RemoteObjectNameFil
//      ter filter)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9ProxyInfo15setReverseProxyESt8functionIFb11QStringViewS1_EE(
    ProxyInfo *self,
    const QRemoteObjectHostBase::RemoteObjectNameFilter *filter) {
  return self->setReverseProxy(*filter);
}

//  void ProxyInfo::proxyObject(const QRemoteObjectSourceLocation &entry,
//      ProxyDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN9ProxyInfo11proxyObjectERKSt4pairI7QString31QRemoteObjectSourceLocationInfoENS_14ProxyDirectionE(
    ProxyInfo *self,
    const QRemoteObjectSourceLocation *entry,
    ProxyInfo::ProxyDirection direction) {
  self->proxyObject(*entry, direction);
}

//  void ProxyInfo::unproxyObject(const QRemoteObjectSourceLocation &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN9ProxyInfo13unproxyObjectERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    ProxyInfo *self,
    const QRemoteObjectSourceLocation *entry) {
  self->unproxyObject(*entry);
}

//  void ProxyInfo::disableAndDeleteObject(ProxyReplicaInfo *info)
extern "C" Q_DECL_EXPORT
void ritual_ZN9ProxyInfo22disableAndDeleteObjectEP16ProxyReplicaInfo(
    ProxyInfo *self,
    ProxyReplicaInfo *info) {
  self->disableAndDeleteObject(info);
}

//  a Python function taken by a CuteProxyInfo, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_ProxyInfo(ProxyInfo *self, const char *key, void *call) {
  return static_cast<CuteProxyInfo *>(self)->take(key, call);
}
