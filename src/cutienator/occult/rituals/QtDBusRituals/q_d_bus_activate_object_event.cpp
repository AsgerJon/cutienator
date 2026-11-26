//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from src/dbus/qdbusintegrator.cpp, line 1613, as _ZN24QDBusActivateObjectEvent13placeMetaCallEP7QObject
#if !defined(QT_NO_DBUS)
inline void QDBusActivateObjectEvent::placeMetaCall(QObject *)
{
    QDBusConnectionPrivate *that = QDBusConnectionPrivate::d(connection);

    QDBusLockerBase::reportThreadAction(HandleObjectCallPostEventAction,
                                        QDBusLockerBase::BeforeDeliver, that);
    that->activateObject(node, message, pathStartPos);
    QDBusLockerBase::reportThreadAction(HandleObjectCallPostEventAction,
                                        QDBusLockerBase::AfterDeliver, that);

    handled = true;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1601, as _ZN24QDBusActivateObjectEventD2Ev
#if !defined(QT_NO_DBUS)
inline QDBusActivateObjectEvent::~QDBusActivateObjectEvent()
{
    if (!handled) {
        // we're being destroyed without delivering
        // it means the object was deleted between posting and delivering
        QDBusConnectionPrivate *that = QDBusConnectionPrivate::d(connection);
        that->sendError(message, QDBusError::UnknownObject);
    }

    // semaphore releasing happens in ~QMetaCallEvent
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1452, as _ZN22QDBusConnectionPrivate14activateObjectERNS_14ObjectTreeNodeERK12QDBusMessagei
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::activateObject(ObjectTreeNode &node, const QDBusMessage &msg,
                                            int pathStartPos)
{
    // This is called by QDBusConnectionPrivate::handleObjectCall to place a call to a slot
    // on the object.
    //
    // The call is routed through the adaptor sub-objects if we have any

    // object may be null

    if (node.flags & QDBusConnectionPrivate::VirtualObject) {
        if (node.treeNode->handleMessage(msg, q(this))) {
            return;
        } else {
            if (activateInternalFilters(node, msg))
                return;
        }
    }

    if (pathStartPos != msg.path().size()) {
        node.flags &= ~QDBusConnection::ExportAllSignals;
        node.obj = findChildObject(&node, msg.path(), pathStartPos);
        if (!node.obj) {
            sendError(msg, QDBusError::UnknownObject);
            return;
        }
    }

    QDBusAdaptorConnector *connector;
    if (node.flags & QDBusConnection::ExportAdaptors &&
        (connector = qDBusFindAdaptorConnector(node.obj))) {
        auto newflags = node.flags | QDBusConnection::ExportAllSlots;

        if (msg.interface().isEmpty()) {
            // place the call in all interfaces
            // let the first one that handles it to work
            for (const QDBusAdaptorConnector::AdaptorData &adaptorData :
                 std::as_const(connector->adaptors)) {
                if (activateCall(adaptorData.adaptor, newflags, msg))
                    return;
            }
        } else {
            // check if we have an interface matching the name that was asked:
            QDBusAdaptorConnector::AdaptorMap::ConstIterator it;
            it = std::lower_bound(connector->adaptors.constBegin(), connector->adaptors.constEnd(),
                                  msg.interface());
            if (it != connector->adaptors.constEnd() && msg.interface() == QLatin1StringView(it->interface)) {
                if (!activateCall(it->adaptor, newflags, msg))
                    sendError(msg, QDBusError::UnknownMethod);
                return;
            }
        }
    }

    // no adaptors matched or were exported
    // try our standard filters
    if (activateInternalFilters(node, msg))
        return;                 // internal filters have already run or an error has been sent

    // try the object itself:
    if (node.flags & (QDBusConnection::ExportScriptableSlots|QDBusConnection::ExportNonScriptableSlots) ||
        node.flags & (QDBusConnection::ExportScriptableInvokables|QDBusConnection::ExportNonScriptableInvokables)) {
        bool interfaceFound = true;
        if (!msg.interface().isEmpty()) {
            if (!node.interfaceName.isEmpty())
                interfaceFound = msg.interface() == node.interfaceName;
            else
                interfaceFound = qDBusInterfaceInObject(node.obj, msg.interface());
        }

        if (interfaceFound) {
            if (!activateCall(node.obj, node.flags, msg))
                sendError(msg, QDBusError::UnknownMethod);
            return;
        }
    }

    // nothing matched, send an error code
    if (msg.interface().isEmpty())
        sendError(msg, QDBusError::UnknownMethod);
    else
        sendError(msg, QDBusError::UnknownInterface);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1371, as _ZN22QDBusConnectionPrivate9sendErrorERK12QDBusMessageN10QDBusError9ErrorTypeE
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::sendError(const QDBusMessage &msg, QDBusError::ErrorType code)
{
    if (code == QDBusError::UnknownMethod) {
        QString interfaceMsg;
        if (msg.interface().isEmpty())
            interfaceMsg = "any interface"_L1;
        else
            interfaceMsg = "interface '%1'"_L1.arg(msg.interface());

        send(msg.createErrorReply(code, "No such method '%1' in %2 at object path '%3' "
                                        "(signature '%4')"_L1
                                  .arg(msg.member(), interfaceMsg, msg.path(), msg.signature())));
    } else if (code == QDBusError::UnknownInterface) {
        send(msg.createErrorReply(QDBusError::UnknownInterface,
                                  "No such interface '%1' at object path '%2'"_L1
                                  .arg(msg.interface(), msg.path())));
    } else if (code == QDBusError::UnknownObject) {
        send(msg.createErrorReply(QDBusError::UnknownObject,
                                  "No such object path '%1'"_L1.arg(msg.path())));
    }
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusActivateObjectEvent that Python can take functions over in. Every QDBusActivateObjectEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusActivateObjectEventCall0)(const void *, QObject *, int *);
#endif  // !defined(QT_NO_DBUS)
typedef void (*CuteQDBusActivateObjectEventCall1)(const void *, bool, int *);
typedef void * (*CuteQDBusActivateObjectEventCall2)(const void *, int *);
class CuteQDBusActivateObjectEvent : public QDBusActivateObjectEvent {
public:
  using QDBusActivateObjectEvent::QDBusActivateObjectEvent;
  CuteQDBusActivateObjectEvent(const QDBusActivateObjectEvent & other) : QDBusActivateObjectEvent(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_DBUS)
  //  void QDBusActivateObjectEvent::placeMetaCall(QObject *a0)
  void placeMetaCall(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusActivateObjectEventCall0 call = reinterpret_cast<CuteQDBusActivateObjectEventCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDBusActivateObjectEvent::placeMetaCall(a0);
  }
#endif  // !defined(QT_NO_DBUS)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusActivateObjectEventCall1 call = reinterpret_cast<CuteQDBusActivateObjectEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusActivateObjectEventCall2 call = reinterpret_cast<CuteQDBusActivateObjectEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QDBusActivateObjectEvent::~QDBusActivateObjectEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusActivateObjectEventD1Ev(
    QDBusActivateObjectEvent *self) {
  delete self;
}

//  void QDBusActivateObjectEvent::placeMetaCall(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusActivateObjectEvent13placeMetaCallEP7QObject(
    QDBusActivateObjectEvent *self,
    QObject *a0) {
  self->placeMetaCall(a0);
}

//  a Python function taken by a CuteQDBusActivateObjectEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusActivateObjectEvent(
    QDBusActivateObjectEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusActivateObjectEvent *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
