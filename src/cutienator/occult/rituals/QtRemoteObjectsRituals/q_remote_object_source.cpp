//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtRemoteObjects/private/qremoteobjectsourceio_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 344, as _ZN19QRemoteObjectSourceD2Ev
inline QRemoteObjectSource::~QRemoteObjectSource()
{
    for (const auto &it : std::as_const(m_children)) {
        // We used QPointers for m_children because we don't control the lifetime of child QObjects
        // Since the this/source QObject's parent is the referenced QObject, it could have already
        // been deleted
        delete it.data();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsourceio.cpp, line 104, as _ZN21QRemoteObjectSourceIo14registerSourceEP23QRemoteObjectSourceBase
inline void QRemoteObjectSourceIo::registerSource(QRemoteObjectSourceBase *source)
{
    Q_ASSERT(source);
    const QString &name = source->name();
    m_sourceObjects[name] = source;
    if (source->isRoot()) {
        QRemoteObjectRootSource *root = static_cast<QRemoteObjectRootSource *>(source);
        qRODebug(this) << "Registering" << name;
        m_sourceRoots[name] = root;
        m_objectToSourceMap[source->m_object] = root;
        if (serverAddress().isValid()) {
            const auto &type = source->m_api->typeName();
            emit remoteObjectAdded(qMakePair(name, QRemoteObjectSourceLocationInfo(type, serverAddress())));
        }
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 514, as _ZN23QRemoteObjectSourceBase11qt_metacallEN11QMetaObject4CallEiPPv
inline int QRemoteObjectSourceBase::qt_metacall(QMetaObject::Call call, int methodId, void **a)
{
    methodId = QObject::qt_metacall(call, methodId, a);
    if (methodId < 0)
        return methodId;

    if (call == QMetaObject::InvokeMetaMethod)
        handleMetaCall(methodId, call, a);

    return -1;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 165, as _ZN23QRemoteObjectSourceBaseC2EP7QObjectPNS_7PrivateEPK12SourceApiMapS1_
inline QRemoteObjectSourceBase::QRemoteObjectSourceBase(QObject *obj, Private *d, const SourceApiMap *api,
                                                 QObject *adapter)
    : QObject(obj),
      m_object(obj),
      m_adapter(adapter),
      m_api(api),
      d(d)
{
    if (!obj) {
        qCWarning(QT_REMOTEOBJECT) << "QRemoteObjectSourceBase: Cannot replicate a NULL object" << m_api->name();
        return;
    }

    setConnections();

    const auto nChildren = api->m_models.size() + api->m_subclasses.size();
    if (nChildren > 0) {
        QList<int> roles;
        const int numProperties = api->propertyCount();
        int modelIndex = 0, subclassIndex = 0;
        for (int i = 0; i < numProperties; ++i) {
            if (api->isAdapterProperty(i))
                continue;
            const int index = api->sourcePropertyIndex(i);
            const auto property = m_object->metaObject()->property(index);
            const auto metaType = property.metaType();
            if (metaType.flags().testFlag(QMetaType::PointerToQObject)) {
                auto propertyMeta = metaType.metaObject();
                QObject *child = property.read(m_object).value<QObject *>();
                const QMetaObject *meta = child ? child->metaObject() : propertyMeta;
                if (!meta)
                    continue;
                if (meta->inherits(&QAbstractItemModel::staticMetaObject)) {
                    const auto modelInfo = api->m_models.at(modelIndex++);
                    QAbstractItemModel *model = qobject_cast<QAbstractItemModel *>(child);
                    QAbstractItemAdapterSourceAPI<QAbstractItemModel, QAbstractItemModelSourceAdapter> *modelApi =
                        new QAbstractItemAdapterSourceAPI<QAbstractItemModel, QAbstractItemModelSourceAdapter>(modelInfo.name);
                    if (!model)
                        m_children.insert(i, new QRemoteObjectSource(nullptr, d, modelApi, nullptr, api->name()));
                    else {
                        roles.clear();
                        const auto knownRoles = model->roleNames();
                        const auto modelInfoRoles = modelInfo.roles.split('|');
                        for (const auto &role : modelInfoRoles) {
                            if (role.isEmpty())
                                continue;
                            const int roleIndex = knownRoles.key(role, -1);
                            if (roleIndex == -1) {
                                qCWarning(QT_REMOTEOBJECT) << "Invalid role" << role << "for model" << model->metaObject()->className();
                                qCWarning(QT_REMOTEOBJECT) << "  known roles:" << knownRoles;
                            } else
                                roles << roleIndex;
                        }
                        auto adapter = new QAbstractItemModelSourceAdapter(model, nullptr,
                                                                           roles.isEmpty() ? knownRoles.keys().toVector() : roles);
                        m_children.insert(i, new QRemoteObjectSource(model, d, modelApi, adapter, api->name()));
                    }
                } else {
                    const auto classApi = api->m_subclasses.at(subclassIndex++);
                    m_children.insert(i, new QRemoteObjectSource(child, d, classApi, nullptr, api->name()));
                }
            }
        }
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 248, as _ZN23QRemoteObjectSourceBaseD2Ev
inline QRemoteObjectSourceBase::~QRemoteObjectSourceBase()
{
    delete m_api;
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectSource that Python can take functions over in. Every QRemoteObjectSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRemoteObjectSourceCall0)(const void *, int *);
typedef QString * (*CuteQRemoteObjectSourceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectSource : public QRemoteObjectSource {
public:
  using QRemoteObjectSource::QRemoteObjectSource;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase6isRootEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase4nameEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QRemoteObjectSource::isRoot() const
  bool isRoot() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall0 call = reinterpret_cast<CuteQRemoteObjectSourceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRemoteObjectSource::isRoot();
  }

  //  QString QRemoteObjectSource::name() const
  QString name() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall1 call = reinterpret_cast<CuteQRemoteObjectSourceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QRemoteObjectSource::name();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall2 call = reinterpret_cast<CuteQRemoteObjectSourceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall3 call = reinterpret_cast<CuteQRemoteObjectSourceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall4 call = reinterpret_cast<CuteQRemoteObjectSourceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall5 call = reinterpret_cast<CuteQRemoteObjectSourceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall6 call = reinterpret_cast<CuteQRemoteObjectSourceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall7 call = reinterpret_cast<CuteQRemoteObjectSourceCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRemoteObjectSourceCall8 call = reinterpret_cast<CuteQRemoteObjectSourceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRemoteObjectSource::~QRemoteObjectSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRemoteObjectSourceD1Ev(QRemoteObjectSource *self) {
  delete self;
}

//  bool QRemoteObjectSource::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QRemoteObjectSource6isRootEv(
    const QRemoteObjectSource *self) {
  return self->isRoot();
}

//  QString QRemoteObjectSource::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QRemoteObjectSource4nameEv(
    const QRemoteObjectSource *self) {
  return new QString(self->name());
}

//  a Python function taken by a CuteQRemoteObjectSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectSource(
    QRemoteObjectSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectSource *>(self)->take(key, call);
}

//  bool QRemoteObjectSource::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QRemoteObjectSource6isRootEv(
    const QRemoteObjectSource *self) {
  return self->QRemoteObjectSource::isRoot();
}

//  QString QRemoteObjectSource::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QRemoteObjectSource4nameEv(
    const QRemoteObjectSource *self) {
  return new QString(self->QRemoteObjectSource::name());
}
