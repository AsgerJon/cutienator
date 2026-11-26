//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusintegrator_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/private/qlatch_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qobject.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qset.h>
#include <QtDBus/qdbusargument.h>
#include <QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/private/qdbusconnectionmanager_p.h>
#include <QtDBus/private/qdbusinterface_p.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbusmetatype.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/qdbusabstractadaptor.h>
#include <QtDBus/private/qdbusabstractadaptor_p.h>
#include <QtDBus/qdbusserver.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtDBus/qdbusvirtualobject.h>
#include <QtDBus/private/qdbusmessage_p.h>
#include <QtDBus/private/qdbuscontext_p.h>
#include <QtDBus/private/qdbuspendingcall_p.h>
#include <QtDBus/private/qdbusthreaddebug_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/dbus/qdbusintegrator.cpp, line 57, as local:qdbusintegrator.cpp:qDBusDebug
#if !defined(QT_NO_DBUS)
#define qDBusDebug              if (::isDebugging.loadRelaxed() == 0); else qDebug
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 339, as local:qdbusintegrator.cpp:buildMatchRule
#if !defined(QT_NO_DBUS)
static QByteArray buildMatchRule(const QString &service,
                                 const QString &objectPath, const QString &interface,
                                 const QString &member, const QDBusConnectionPrivate::ArgMatchRules &argMatch, const QString & /*signature*/)
{
    QString result;
    result += "type='signal',"_L1;
    const auto keyValue = "%1='%2',"_L1;

    if (!service.isEmpty())
        result += keyValue.arg("sender"_L1, service);
    if (!objectPath.isEmpty())
        result += keyValue.arg("path"_L1, objectPath);
    if (!interface.isEmpty())
        result += keyValue.arg("interface"_L1, interface);
    if (!member.isEmpty())
        result += keyValue.arg("member"_L1, member);

    // add the argument string-matching now
    if (!argMatch.args.isEmpty()) {
        const QString keyValue = "arg%1='%2',"_L1;
        for (int i = 0; i < argMatch.args.size(); ++i)
            if (!argMatch.args.at(i).isNull())
                result += keyValue.arg(i).arg(argMatch.args.at(i));
    }
    if (!argMatch.arg0namespace.isEmpty()) {
        result += "arg0namespace='%1',"_L1.arg(argMatch.arg0namespace);
    }

    result.chop(1);             // remove ending comma
    return result.toLatin1();
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 371, as local:qdbusintegrator.cpp:findObject
#if !defined(QT_NO_DBUS)
static bool findObject(const QDBusConnectionPrivate::ObjectTreeNode *root,
                       const QString &fullpath, int &usedLength,
                       QDBusConnectionPrivate::ObjectTreeNode &result)
{
    if (!fullpath.compare("/"_L1) && root->obj) {
        usedLength = 1;
        result = *root;
        return root;
    }
    int start = 0;
    int length = fullpath.size();
    if (fullpath.at(0) == u'/')
        start = 1;

    // walk the object tree
    const QDBusConnectionPrivate::ObjectTreeNode *node = root;
    while (start < length && node) {
        if (node->flags & QDBusConnection::ExportChildObjects)
            break;
        if ((node->flags & QDBusConnectionPrivate::VirtualObject) && (node->flags & QDBusConnection::SubPath))
            break;
        int end = fullpath.indexOf(u'/', start);
        end = (end == -1 ? length : end);
        QStringView pathComponent = QStringView{fullpath}.mid(start, end - start);

        QDBusConnectionPrivate::ObjectTreeNode::DataList::ConstIterator it =
            std::lower_bound(node->children.constBegin(), node->children.constEnd(), pathComponent);
        if (it != node->children.constEnd() && it->name == pathComponent)
            // match
            node = &(*it);
        else
            node = nullptr;

        start = end + 1;
    }

    // found our object
    usedLength = (start > length ? length : start);
    if (node) {
        if (node->obj || !node->children.isEmpty())
            result = *node;
        else
            // there really is no object here
            // we're just looking at an unused space in the QList
            node = nullptr;
    }
    return node;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 420, as local:qdbusintegrator.cpp:findChildObject
#if !defined(QT_NO_DBUS)
static QObject *findChildObject(const QDBusConnectionPrivate::ObjectTreeNode *root,
                                const QString &fullpath, int start)
{
    int length = fullpath.size();

    // any object in the tree can tell us to switch to its own object tree:
    const QDBusConnectionPrivate::ObjectTreeNode *node = root;
    if (node && node->flags & QDBusConnection::ExportChildObjects) {
        QObject *obj = node->obj;

        while (obj) {
            if (start >= length)
                // we're at the correct level
                return obj;

            int pos = fullpath.indexOf(u'/', start);
            pos = (pos == -1 ? length : pos);
            auto pathComponent = QStringView{fullpath}.mid(start, pos - start);

            // find a child with the proper name
            QObject *next = nullptr;
            for (QObject *child : std::as_const(obj->children())) {
                if (child->objectName() == pathComponent) {
                    next = child;
                    break;
                }
            }

            if (!next)
                break;

            obj = next;
            start = pos + 1;
        }
    }

    // object not found
    return nullptr;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 460, as local:qdbusintegrator.cpp:matchArgsForService
#if !defined(QT_NO_DBUS)
static QDBusConnectionPrivate::ArgMatchRules matchArgsForService(const QString &service, QDBusServiceWatcher::WatchMode mode)
{
    QDBusConnectionPrivate::ArgMatchRules matchArgs;
    if (service.endsWith(u'*')) {
        matchArgs.arg0namespace = service.chopped(1);
        matchArgs.args << QString();
    }
    else
        matchArgs.args << service;

    switch (mode) {
    case QDBusServiceWatcher::WatchForOwnerChange:
        break;

    case QDBusServiceWatcher::WatchForRegistration:
        matchArgs.args << QString::fromLatin1("", 0);
        break;

    case QDBusServiceWatcher::WatchForUnregistration:
        matchArgs.args << QString() << QString::fromLatin1("", 0);
        break;
    }
    return matchArgs;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 604, as local:qdbusintegrator.cpp:huntAndUnregister
#if !defined(QT_NO_DBUS)
static void huntAndUnregister(const QList<QStringView> &pathComponents, int i,
                              QDBusConnection::UnregisterMode mode,
                              QDBusConnectionPrivate::ObjectTreeNode *node)
{
    if (pathComponents.size() == i) {
        // found it
        node->obj = nullptr;
        node->flags = {};

        if (mode == QDBusConnection::UnregisterTree) {
            // clear the sub-tree as well
            node->children.clear();  // can't disconnect the objects because we really don't know if they can
                            // be found somewhere else in the path too
        }
    } else {
        // keep going
        QDBusConnectionPrivate::ObjectTreeNode::DataList::Iterator end = node->children.end();
        QDBusConnectionPrivate::ObjectTreeNode::DataList::Iterator it =
            std::lower_bound(node->children.begin(), end, pathComponents.at(i));
        if (it == end || it->name != pathComponents.at(i))
            return;              // node not found

        huntAndUnregister(pathComponents, i + 1, mode, &(*it));
        if (!it->isActive())
            node->children.erase(it);
    }
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 786, as local:qdbusintegrator.cpp:DIRECT_DELIVERY
#if !defined(QT_NO_DBUS)
static QDBusCallDeliveryEvent * const DIRECT_DELIVERY = (QDBusCallDeliveryEvent *)1;
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2686, as _ZN22QDBusConnectionPrivate21registerServiceNoLockERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::registerServiceNoLock(const QString &serviceName)
{
    serviceNames.append(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2697, as _ZN22QDBusConnectionPrivate23unregisterServiceNoLockERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::unregisterServiceNoLock(const QString &serviceName)
{
    serviceNames.removeAll(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 788, as _ZN22QDBusConnectionPrivate12prepareReplyEPS_P7QObjectiRK5QListI9QMetaTypeERK12QDBusMessage
#if !defined(QT_NO_DBUS)
inline QDBusCallDeliveryEvent *QDBusConnectionPrivate::prepareReply(QDBusConnectionPrivate *target,
                                                             QObject *object, int idx,
                                                             const QList<QMetaType> &metaTypes,
                                                             const QDBusMessage &msg)
{
    Q_ASSERT(object);

    int n = metaTypes.size() - 1;
    if (metaTypes[n] == QDBusMetaTypeId::message())
        --n;

    if (msg.arguments().size() < n)
        return nullptr;               // too few arguments

    // check that types match
    for (int i = 0; i < n; ++i)
        if (metaTypes.at(i + 1) != msg.arguments().at(i).metaType() &&
            msg.arguments().at(i).metaType() != QMetaType::fromType<QDBusArgument>())
            return nullptr;           // no match

    // we can deliver
    // prepare for the call
    if (target == object)
        return DIRECT_DELIVERY;
    return new QDBusCallDeliveryEvent(QDBusConnection(target), idx, target, msg, metaTypes);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1179, as _ZN22QDBusConnectionPrivate10timerEventEP11QTimerEvent
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
{
    {
        DBusTimeout *timeout = timeouts.value(e->timerId(), nullptr);
        if (timeout)
            q_dbus_timeout_handle(timeout);
    }

    doDispatch();
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2536, as _ZN22QDBusConnectionPrivate18shouldWatchServiceERK7QString
#if !defined(QT_NO_DBUS)
inline bool QDBusConnectionPrivate::shouldWatchService(const QString &service)
{
    // we don't have to watch anything in peer mode
    if (mode != ClientMode)
        return false;
    // we don't have to watch wildcard services (empty strings)
    if (service.isEmpty())
        return false;
    // we don't have to watch the bus driver
    if (service == QDBusUtil::dbusService())
        return false;
    return true;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2471, as _ZN22QDBusConnectionPrivate16unregisterObjectERK7QStringN15QDBusConnection14UnregisterModeE
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::unregisterObject(const QString &path, QDBusConnection::UnregisterMode mode)
{
    QDBusConnectionPrivate::ObjectTreeNode *node = &rootNode;
    QList<QStringView> pathComponents;
    int i;
    if (path == "/"_L1) {
        i = 0;
    } else {
        pathComponents = QStringView{path}.split(u'/');
        i = 1;
    }

    huntAndUnregister(pathComponents, i, mode, node);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2680, as _ZN22QDBusConnectionPrivate15registerServiceERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::registerService(const QString &serviceName)
{
    QDBusWriteLocker locker(RegisterServiceAction, this);
    registerServiceNoLock(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2691, as _ZN22QDBusConnectionPrivate17unregisterServiceERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::unregisterService(const QString &serviceName)
{
    QDBusWriteLocker locker(UnregisterServiceAction, this);
    unregisterServiceNoLock(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2713, as _ZN22QDBusConnectionPrivate17postEventToThreadEiP7QObjectP6QEvent
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::postEventToThread(int action, QObject *object, QEvent *ev)
{
    QDBusLockerBase::reportThreadAction(action, QDBusLockerBase::BeforePost, this);
    QCoreApplication::postEvent(object, ev);
    QDBusLockerBase::reportThreadAction(action, QDBusLockerBase::AfterPost, this);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1103, as _ZN22QDBusConnectionPrivate17collectAllObjectsERNS_14ObjectTreeNodeER4QSetIP7QObjectE
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::collectAllObjects(QDBusConnectionPrivate::ObjectTreeNode &haystack,
                                               QSet<QObject *> &set)
{
    for (ObjectTreeNode &child : haystack.children)
        collectAllObjects(child, set);

    if (haystack.obj)
        set.insert(haystack.obj);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2702, as _ZN22QDBusConnectionPrivate27isServiceRegisteredByThreadERK7QString
#if !defined(QT_NO_DBUS)
inline bool QDBusConnectionPrivate::isServiceRegisteredByThread(const QString &serviceName)
{
    if (!serviceName.isEmpty() && serviceName == baseService)
        return true;
    if (serviceName == QDBusUtil::dbusService())
        return false;

    QDBusReadLocker locker(UnregisterServiceAction, this);
    return serviceNames.contains(serviceName);
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusConnectionPrivate that Python can take functions over in. Every QDBusConnectionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
typedef void (*CuteQDBusConnectionPrivateCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusConnectionPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusConnectionPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusConnectionPrivate : public QDBusConnectionPrivate {
public:
  using QDBusConnectionPrivate::QDBusConnectionPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
  //  void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall0 call = reinterpret_cast<CuteQDBusConnectionPrivateCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QDBusConnectionPrivate::timerEvent(e);
  }
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall1 call = reinterpret_cast<CuteQDBusConnectionPrivateCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall2 call = reinterpret_cast<CuteQDBusConnectionPrivateCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall3 call = reinterpret_cast<CuteQDBusConnectionPrivateCall3>(taken[3]);
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
      CuteQDBusConnectionPrivateCall4 call = reinterpret_cast<CuteQDBusConnectionPrivateCall4>(taken[4]);
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
      CuteQDBusConnectionPrivateCall5 call = reinterpret_cast<CuteQDBusConnectionPrivateCall5>(taken[5]);
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
      CuteQDBusConnectionPrivateCall6 call = reinterpret_cast<CuteQDBusConnectionPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusConnectionPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDBusConnectionPrivate10metaObjectEv(
    const QDBusConnectionPrivate *self) {
  return self->metaObject();
}

//  void *QDBusConnectionPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QDBusConnectionPrivate11qt_metacastEPKc(
    QDBusConnectionPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusConnectionPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDBusConnectionPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusConnectionPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if !defined(QT_NO_DBUS)
//  bool QDBusConnectionPrivate::shouldWatchService(const QString &service)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDBusConnectionPrivate18shouldWatchServiceERK7QString(
    QDBusConnectionPrivate *self,
    const QString *service) {
  return self->shouldWatchService(*service);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::unregisterObject(const QString &path,
//      QDBusConnection::UnregisterMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate16unregisterObjectERK7QStringN15QDBusConnection14UnregisterModeE(
    QDBusConnectionPrivate *self,
    const QString *path,
    QDBusConnection::UnregisterMode mode) {
  self->unregisterObject(*path, mode);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::registerService(const QString &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate15registerServiceERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  self->registerService(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::unregisterService(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate17unregisterServiceERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  self->unregisterService(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::postEventToThread(int action, QObject
//      *target, QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate17postEventToThreadEiP7QObjectP6QEvent(
    QDBusConnectionPrivate *self,
    int action,
    QObject *target,
    QEvent *event) {
  self->postEventToThread(action, target, event);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::collectAllObjects(ObjectTreeNode &node,
//      QSet<QObject *> &set)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate17collectAllObjectsERNS_14ObjectTreeNodeER4QSetIP7QObjectE(
    QDBusConnectionPrivate *self,
    QDBusConnectionPrivate::ObjectTreeNode *node,
    QSet<QObject *> *set) {
  self->collectAllObjects(*node, *set);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  bool QDBusConnectionPrivate::isServiceRegisteredByThread(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDBusConnectionPrivate27isServiceRegisteredByThreadERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  return self->isServiceRegisteredByThread(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate10timerEventEP11QTimerEvent(
    QDBusConnectionPrivate *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QDBusConnectionPrivate::setDispatchEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate18setDispatchEnabledEb(
    QDBusConnectionPrivate *self,
    bool enable) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setDispatchEnabled(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setDispatchEnabled(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enable)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::doDispatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate10doDispatchEv(
    QDBusConnectionPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "doDispatch()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "doDispatch()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::socketRead(qintptr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate10socketReadEx(
    QDBusConnectionPrivate *self,
    qintptr a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "socketRead(qintptr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "socketRead(qintptr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::socketWrite(qintptr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate11socketWriteEx(
    QDBusConnectionPrivate *self,
    qintptr a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "socketWrite(qintptr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "socketWrite(qintptr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::objectDestroyed(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate15objectDestroyedEP7QObject(
    QDBusConnectionPrivate *self,
    QObject *o) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "objectDestroyed(QObject *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "objectDestroyed(QObject *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&o)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::relaySignal(QObject *obj, const QMetaObject
//      *a1, int signalId, const QVariantList &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate11relaySignalEP7QObjectPK11QMetaObjectiRK5QListI8QVariantE(
    QDBusConnectionPrivate *self,
    QObject *obj,
    const QMetaObject *a1,
    int signalId,
    const QList<QVariant> *args) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "relaySignal(QObject *,const QMetaObject *,int,const QVariantList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "relaySignal(QObject *,const QMetaObject *,int,const QVariantList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&obj)),
      const_cast<void *>(static_cast<const void *>(&a1)),
      const_cast<void *>(static_cast<const void *>(&signalId)),
      const_cast<void *>(static_cast<const void *>(args)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::serviceOwnerChangedNoLock(const QString
//      &name, const QString &oldOwner, const QString &newOwner)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate25serviceOwnerChangedNoLockERK7QStringS2_S2_(
    QDBusConnectionPrivate *self,
    const QString *name,
    const QString *oldOwner,
    const QString *newOwner) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serviceOwnerChangedNoLock(const QString &,const QString &,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serviceOwnerChangedNoLock(const QString &,const QString &,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(name)),
      const_cast<void *>(static_cast<const void *>(oldOwner)),
      const_cast<void *>(static_cast<const void *>(newOwner)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::registerServiceNoLock(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate21registerServiceNoLockERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "registerServiceNoLock(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "registerServiceNoLock(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(serviceName)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::unregisterServiceNoLock(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate23unregisterServiceNoLockERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "unregisterServiceNoLock(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "unregisterServiceNoLock(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(serviceName)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::handleDBusDisconnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate23handleDBusDisconnectionEv(
    QDBusConnectionPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleDBusDisconnection()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleDBusDisconnection()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::dispatchStatusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate21dispatchStatusChangedEv(
    QDBusConnectionPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dispatchStatusChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dispatchStatusChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::spyHooksFinished(const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate16spyHooksFinishedERK12QDBusMessage(
    QDBusConnectionPrivate *self,
    const QDBusMessage *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "spyHooksFinished(const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "spyHooksFinished(const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::messageNeedsSending(QDBusPendingCallPrivate
//      *pcall, void *msg, int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate19messageNeedsSendingEP23QDBusPendingCallPrivatePvi(
    QDBusConnectionPrivate *self,
    QDBusPendingCallPrivate *pcall,
    void *msg,
    int timeout) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "messageNeedsSending(QDBusPendingCallPrivate *,void *,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "messageNeedsSending(QDBusPendingCallPrivate *,void *,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&pcall)),
      const_cast<void *>(static_cast<const void *>(&msg)),
      const_cast<void *>(static_cast<const void *>(&timeout)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::serviceOwnerChanged(const QString &name,
//      const QString &oldOwner, const QString &newOwner)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate19serviceOwnerChangedERK7QStringS2_S2_(
    QDBusConnectionPrivate *self,
    const QString *name,
    const QString *oldOwner,
    const QString *newOwner) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serviceOwnerChanged(const QString &,const QString &,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serviceOwnerChanged(const QString &,const QString &,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(name)),
      const_cast<void *>(static_cast<const void *>(oldOwner)),
      const_cast<void *>(static_cast<const void *>(newOwner)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusConnectionPrivate::callWithCallbackFailed(const QDBusError
//      &error, const QDBusMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate22callWithCallbackFailedERK10QDBusErrorRK12QDBusMessage(
    QDBusConnectionPrivate *self,
    const QDBusError *error,
    const QDBusMessage *message) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusConnectionPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "callWithCallbackFailed(const QDBusError &,const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "callWithCallbackFailed(const QDBusError &,const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(error)),
      const_cast<void *>(static_cast<const void *>(message)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QDBusConnection::ConnectionCapabilities
//      QDBusConnectionPrivate::connectionCapabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QDBusConnectionPrivate22connectionCapabilitiesEv(
    const QDBusConnectionPrivate *self) {
  return static_cast<int>(self->connectionCapabilities().toInt());
}

//  QDBusConnectionPrivate *QDBusConnectionPrivate::d(const QDBusConnection
//      &q)
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate *ritual_ZN22QDBusConnectionPrivate1dERK15QDBusConnection(
    const QDBusConnection *q) {
  return QDBusConnectionPrivate::d(*q);
}

//  QDBusConnection QDBusConnectionPrivate::q(QDBusConnectionPrivate
//      *connection)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN22QDBusConnectionPrivate1qEPS_(
    QDBusConnectionPrivate *connection) {
  return new QDBusConnection(QDBusConnectionPrivate::q(connection));
}

//  a Python function taken by a CuteQDBusConnectionPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusConnectionPrivate(
    QDBusConnectionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusConnectionPrivate *>(self)->take(key, call);
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
