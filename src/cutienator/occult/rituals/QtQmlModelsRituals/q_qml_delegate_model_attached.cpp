//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtQmlModels/private/qqmlabstractdelegatecomponent_p.h>
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertytopropertybinding_p.h>
#include <QtQmlModels/private/qqmltableinstancemodel_p.h>
#include <QtQmlModels/private/qquickpackage_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1473, as _ZN24QQmlDelegateModelPrivate12removeGroupsEN18QQmlListCompositor8iteratorEiNS0_5GroupEi
inline void QQmlDelegateModelPrivate::removeGroups(
        Compositor::iterator from, int count, Compositor::Group group, int groupFlags)
{
    QList<Compositor::Remove> removes;
    m_compositor.clearFlags(from, count, group, groupFlags, &removes);
    itemsRemoved(removes);
    emitChanges();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1464, as _ZN24QQmlDelegateModelPrivate9addGroupsEN18QQmlListCompositor8iteratorEiNS0_5GroupEi
inline void QQmlDelegateModelPrivate::addGroups(
        Compositor::iterator from, int count, Compositor::Group group, int groupFlags)
{
    QList<Compositor::Insert> inserts;
    m_compositor.setFlags(from, count, group, groupFlags, &inserts);
    itemsInserted(inserts);
    emitChanges();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1482, as _ZN24QQmlDelegateModelPrivate9setGroupsEN18QQmlListCompositor8iteratorEiNS0_5GroupEi
inline void QQmlDelegateModelPrivate::setGroups(
        Compositor::iterator from, int count, Compositor::Group group, int groupFlags)
{
    QList<Compositor::Remove> removes;
    QList<Compositor::Insert> inserts;

    m_compositor.setFlags(from, count, group, groupFlags, &inserts);
    itemsInserted(inserts);
    const int removeFlags = ~groupFlags & Compositor::GroupMask;

    from = m_compositor.find(from.group, from.index[from.group]);
    m_compositor.clearFlags(from, count, group, removeFlags, &removes);
    itemsRemoved(removes);
    emitChanges();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2756, as _ZNK25QQmlDelegateModelAttached16inPersistedItemsEv
inline bool QQmlDelegateModelAttached::inPersistedItems() const
{
    if (!m_cacheItem)
        return false;
    const uint groupFlag = (1 << QQmlListCompositor::Persisted);
    return m_cacheItem->groups() & groupFlag;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2764, as _ZNK25QQmlDelegateModelAttached19persistedItemsIndexEv
inline int QQmlDelegateModelAttached::persistedItemsIndex() const
{
    if (!m_cacheItem)
        return -1;
    return m_cacheItem->groupIndex(QQmlListCompositor::Persisted);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2799, as _ZNK25QQmlDelegateModelAttached7inItemsEv
inline bool QQmlDelegateModelAttached::inItems() const
{
    if (!m_cacheItem)
        return false;
    const uint groupFlag = (1 << QQmlListCompositor::Default);
    return m_cacheItem->groups() & groupFlag;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2807, as _ZNK25QQmlDelegateModelAttached10itemsIndexEv
inline int QQmlDelegateModelAttached::itemsIndex() const
{
    if (!m_cacheItem)
        return -1;
    return m_cacheItem->groupIndex(QQmlListCompositor::Default);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2822, as _ZNK25QQmlDelegateModelAttached5modelEv
inline QQmlDelegateModel *QQmlDelegateModelAttached::model() const
{
    return m_cacheItem ? m_cacheItem->metaType()->delegateModel() : nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2835, as _ZNK25QQmlDelegateModelAttached6groupsEv
inline QStringList QQmlDelegateModelAttached::groups() const
{
    QStringList groups;

    if (!m_cacheItem)
        return groups;
    const auto &metaType = m_cacheItem->metaType();
    for (qsizetype i = 0, end = metaType->groupCount(); i < end; ++i) {
        if (m_cacheItem->groups() & (1 << (i + 1)))
            groups.append(metaType->groupNames.at(i));
    }
    return groups;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2877, as _ZNK25QQmlDelegateModelAttached12isUnresolvedEv
inline bool QQmlDelegateModelAttached::isUnresolved() const
{
    if (!m_cacheItem)
        return false;

    return m_cacheItem->groups() & Compositor::UnresolvedFlag;
}
//  -----------------------------------------------------------------------

//  A QQmlDelegateModelAttached that Python can take functions over in. Every QQmlDelegateModelAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDelegateModelAttached : public QQmlDelegateModelAttached {
public:
  using QQmlDelegateModelAttached::QQmlDelegateModelAttached;
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
      CuteQQmlDelegateModelAttachedCall0 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall0>(taken[0]);
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
      CuteQQmlDelegateModelAttachedCall1 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall1>(taken[1]);
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
      CuteQQmlDelegateModelAttachedCall2 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall2>(taken[2]);
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
      CuteQQmlDelegateModelAttachedCall3 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall3>(taken[3]);
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
      CuteQQmlDelegateModelAttachedCall4 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall4>(taken[4]);
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
      CuteQQmlDelegateModelAttachedCall5 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall5>(taken[5]);
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
      CuteQQmlDelegateModelAttachedCall6 call = reinterpret_cast<CuteQQmlDelegateModelAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDelegateModelAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQmlDelegateModelAttached10metaObjectEv(
    const QQmlDelegateModelAttached *self) {
  return self->metaObject();
}

//  bool QQmlDelegateModelAttached::inPersistedItems() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlDelegateModelAttached16inPersistedItemsEv(
    const QQmlDelegateModelAttached *self) {
  return self->inPersistedItems();
}

//  int QQmlDelegateModelAttached::persistedItemsIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlDelegateModelAttached19persistedItemsIndexEv(
    const QQmlDelegateModelAttached *self) {
  return self->persistedItemsIndex();
}

//  bool QQmlDelegateModelAttached::inItems() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlDelegateModelAttached7inItemsEv(
    const QQmlDelegateModelAttached *self) {
  return self->inItems();
}

//  int QQmlDelegateModelAttached::itemsIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlDelegateModelAttached10itemsIndexEv(
    const QQmlDelegateModelAttached *self) {
  return self->itemsIndex();
}

//  QQmlDelegateModel *QQmlDelegateModelAttached::model() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZNK25QQmlDelegateModelAttached5modelEv(
    const QQmlDelegateModelAttached *self) {
  return self->model();
}

//  QStringList QQmlDelegateModelAttached::groups() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK25QQmlDelegateModelAttached6groupsEv(
    const QQmlDelegateModelAttached *self) {
  return new QList<QString>(self->groups());
}

//  bool QQmlDelegateModelAttached::isUnresolved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlDelegateModelAttached12isUnresolvedEv(
    const QQmlDelegateModelAttached *self) {
  return self->isUnresolved();
}

//  a Python function taken by a CuteQQmlDelegateModelAttached, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelAttached(
    QQmlDelegateModelAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelAttached *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
