//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
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
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qitemselectionmodel.h>
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodeladapter.cpp, line 48, as _ZN31QAbstractItemModelSourceAdapterC1EP18QAbstractItemModelP19QItemSelectionModelRK5QListIiE
inline QAbstractItemModelSourceAdapter::QAbstractItemModelSourceAdapter(QAbstractItemModel *obj, QItemSelectionModel *sel, const QList<int> &roles)
    : QObject(obj),
      m_model(obj),
      m_availableRoles(roles)
{
    QAbstractItemModelSourceAdapter::registerTypes();
    m_selectionModel = sel;
    connect(m_model, &QAbstractItemModel::dataChanged, this, &QAbstractItemModelSourceAdapter::sourceDataChanged);
    connect(m_model, &QAbstractItemModel::rowsInserted, this, &QAbstractItemModelSourceAdapter::sourceRowsInserted);
    connect(m_model, &QAbstractItemModel::columnsInserted, this, &QAbstractItemModelSourceAdapter::sourceColumnsInserted);
    connect(m_model, &QAbstractItemModel::rowsRemoved, this, &QAbstractItemModelSourceAdapter::sourceRowsRemoved);
    connect(m_model, &QAbstractItemModel::rowsMoved, this, &QAbstractItemModelSourceAdapter::sourceRowsMoved);
    connect(m_model, &QAbstractItemModel::layoutChanged, this, &QAbstractItemModelSourceAdapter::sourceLayoutChanged);
    if (m_selectionModel)
        connect(m_selectionModel, &QItemSelectionModel::currentChanged, this, &QAbstractItemModelSourceAdapter::sourceCurrentChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 247, as _ZN15QtRemoteObjects37getTypeNameAndMetaobjectFromClassInfoERPK11QMetaObject
inline QString QtRemoteObjects::getTypeNameAndMetaobjectFromClassInfo(const QMetaObject *& meta) {
    QString typeName;
    const int ind = meta->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE);
    if (ind != -1) { //We have an object created from repc or at least with QCLASSINFO defined
        typeName = QString::fromLatin1(meta->classInfo(ind).value());
        while (true) {
            Q_ASSERT(meta->superClass());//This recurses to QObject, which doesn't have QCLASSINFO_REMOTEOBJECT_TYPE
            //At the point superclass doesn't have the same QCLASSINFO_REMOTEOBJECT_TYPE,
            //we have the metaobject we should work from
            if (ind != meta->superClass()->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE))
                break;
            meta = meta->superClass();
        }
    }
    return typeName;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 373, as _ZN23QRemoteObjectSourceBase11marshalArgsEiPPv
inline QVariantList* QRemoteObjectSourceBase::marshalArgs(int index, void **a)
{
    QVariantList &list = m_marshalledArgs;
    int N = m_api->signalParameterCount(index);
    if (N == 1 && QMetaType(m_api->signalParameterType(index, 0)).flags().testFlag(QMetaType::PointerToQObject))
        N = 0; // Don't try to send pointers, the will be handle by QRO_
    if (list.size() < N)
        list.reserve(N);
    const int minFill = std::min(int(list.size()), N);
    for (int i = 0; i < minFill; ++i) {
        const int type = m_api->signalParameterType(index, i);
        if (type == QMetaType::QVariant)
            list[i] = *reinterpret_cast<QVariant *>(a[i + 1]);
        else
            list[i] = QVariant(QMetaType(type), a[i + 1]);
    }
    for (int i = int(list.size()); i < N; ++i) {
        const int type = m_api->signalParameterType(index, i);
        if (type == QMetaType::QVariant)
            list << *reinterpret_cast<QVariant *>(a[i + 1]);
        else
            list << QVariant(QMetaType(type), a[i + 1]);
    }
    for (int i = N; i < list.size(); ++i)
        list.removeLast();
    return &m_marshalledArgs;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectsource.cpp, line 401, as _ZN23QRemoteObjectSourceBase6invokeEN11QMetaObject4CallEiRK5QListI8QVariantEPS3_
inline bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int index, const QVariantList &args, QVariant* returnValue)
{
    int status = -1;
    int flags = 0;
    bool forAdapter = (c == QMetaObject::InvokeMetaMethod ? m_api->isAdapterMethod(index) : m_api->isAdapterProperty(index));
    int resolvedIndex = (c == QMetaObject::InvokeMetaMethod ? m_api->sourceMethodIndex(index) : m_api->sourcePropertyIndex(index));
    if (resolvedIndex < 0)
        return false;
    QVarLengthArray<void*, 10> param(args.size() + 1);

    if (c == QMetaObject::InvokeMetaMethod) {
        QMetaMethod method;
        if (!forAdapter)
            method = parent()->metaObject()->method(resolvedIndex);

        if (returnValue) {
            if (!forAdapter && method.isValid() && method.returnType() == QMetaType::QVariant)
                param[0] = const_cast<void*>(reinterpret_cast<const void*>(returnValue));
            else
                param[0] = returnValue->data();
        } else {
            param[0] = nullptr;
        }

        auto argument = [&](int i) -> void * {
            if ((forAdapter && m_api->methodParameterType(index, i) == QMetaType::QVariant) ||
                    (method.isValid() && method.parameterType(i) == QMetaType::QVariant)) {
                return const_cast<void*>(reinterpret_cast<const void*>(&args.at(i)));
            }
            return const_cast<void*>(args.at(i).data());
        };

        for (int i = 0; i < args.size(); ++i) {
            param[i + 1] = argument(i);
        }
    } else if (c == QMetaObject::WriteProperty || c == QMetaObject::ReadProperty) {
        bool isQVariant = !forAdapter && parent()->metaObject()->property(resolvedIndex).userType() == QMetaType::QVariant;
        for (int i = 0; i < args.size(); ++i) {
            if (isQVariant)
                param[i] = const_cast<void*>(reinterpret_cast<const void*>(&args.at(i)));
            else
                param[i] = const_cast<void*>(args.at(i).data());
        }
        if (c == QMetaObject::WriteProperty) {
            Q_ASSERT(param.size() == 2); // for return-value and setter value
            // check QMetaProperty::write for an explanation of these
            param.append(&status);
            param.append(&flags);
        }
    } else {
        // Better safe than sorry
        return false;
    }
    int r = -1;
    if (forAdapter)
        r = m_adapter->qt_metacall(c, resolvedIndex, param.data());
    else
        r = parent()->qt_metacall(c, resolvedIndex, param.data());
    return r == -1 && status == -1;
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectSourceBase that Python can take functions over in. Every QRemoteObjectSourceBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQRemoteObjectSourceBaseCall0)(const void *, int *);
typedef bool (*CuteQRemoteObjectSourceBaseCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceBaseCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectSourceBaseCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectSourceBaseCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectSourceBase : public QRemoteObjectSourceBase {
public:
  using QRemoteObjectSourceBase::QRemoteObjectSourceBase;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QRemoteObjectSourceBase6isRootEv")) {
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

  //  QString QRemoteObjectSourceBase::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectSourceBaseCall0 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  bool QRemoteObjectSourceBase::isRoot() const
  bool isRoot() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectSourceBaseCall1 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectSourceBaseCall2 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall2>(taken[2]);
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
      CuteQRemoteObjectSourceBaseCall3 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall3>(taken[3]);
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
      CuteQRemoteObjectSourceBaseCall4 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall4>(taken[4]);
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
      CuteQRemoteObjectSourceBaseCall5 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall5>(taken[5]);
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
      CuteQRemoteObjectSourceBaseCall6 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall6>(taken[6]);
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
      CuteQRemoteObjectSourceBaseCall7 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall7>(taken[7]);
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
      CuteQRemoteObjectSourceBaseCall8 call = reinterpret_cast<CuteQRemoteObjectSourceBaseCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRemoteObjectSourceBase::~QRemoteObjectSourceBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRemoteObjectSourceBaseD1Ev(QRemoteObjectSourceBase *self) {
  delete self;
}

//  bool QRemoteObjectSourceBase::hasAdapter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRemoteObjectSourceBase10hasAdapterEv(
    const QRemoteObjectSourceBase *self) {
  return self->hasAdapter();
}

//  QString QRemoteObjectSourceBase::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRemoteObjectSourceBase4nameEv(
    const QRemoteObjectSourceBase *self) {
  return new QString(self->name());
}

//  bool QRemoteObjectSourceBase::isRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRemoteObjectSourceBase6isRootEv(
    const QRemoteObjectSourceBase *self) {
  return self->isRoot();
}

//  QVariantList *QRemoteObjectSourceBase::marshalArgs(int index, void **a)
extern "C" Q_DECL_EXPORT
QVariantList *ritual_ZN23QRemoteObjectSourceBase11marshalArgsEiPPv(
    QRemoteObjectSourceBase *self,
    int index,
    void **a) {
  return self->marshalArgs(index, a);
}

//  bool QRemoteObjectSourceBase::invoke(QMetaObject::Call c, int index,
//      const QVariantList &args, QVariant *returnValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QRemoteObjectSourceBase6invokeEN11QMetaObject4CallEiRK5QListI8QVariantEPS3_(
    QRemoteObjectSourceBase *self,
    QMetaObject::Call c,
    int index,
    const QList<QVariant> *args,
    QVariant *returnValue) {
  return self->invoke(c, index, *args, returnValue);
}

//  a Python function taken by a CuteQRemoteObjectSourceBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectSourceBase(
    QRemoteObjectSourceBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectSourceBase *>(self)->take(key, call);
}
