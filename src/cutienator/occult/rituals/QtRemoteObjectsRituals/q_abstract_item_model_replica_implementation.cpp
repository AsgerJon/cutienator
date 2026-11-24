//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtCore/qdebug.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 71, as _ZN39QAbstractItemModelReplicaImplementationD1Ev
inline QAbstractItemModelReplicaImplementation::~QAbstractItemModelReplicaImplementation()
{
    m_rootItem.clear();
    qDeleteAll(m_pendingRequests);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 77, as _ZN39QAbstractItemModelReplicaImplementation10initializeEv
inline void QAbstractItemModelReplicaImplementation::initialize()
{
    QVariantList properties;
    properties << QVariant::fromValue(QList<int>());
    properties << QVariant::fromValue(QIntHash());
    setProperties(std::move(properties));
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 647, as _ZN39QAbstractItemModelReplicaImplementation19onHeaderDataChangedEN2Qt11OrientationEii
inline void QAbstractItemModelReplicaImplementation::onHeaderDataChanged(Qt::Orientation orientation, int first, int last)
{
    // TODO clean cache
    const int index = orientation == Qt::Horizontal ? 0 : 1;
    QList<CacheEntry> &entries = m_headerData[index];
    for (int i = first; i <= last && i < entries.size(); ++i )
        entries[i].data.clear();
    emit q->headerDataChanged(orientation, first, last);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 384, as _ZN39QAbstractItemModelReplicaImplementation14handleSizeDoneEP31QRemoteObjectPendingCallWatcher
inline void QAbstractItemModelReplicaImplementation::handleSizeDone(QRemoteObjectPendingCallWatcher *watcher)
{
    SizeWatcher *sizeWatcher = static_cast<SizeWatcher*>(watcher);
    const QSize size = sizeWatcher->returnValue().toSize();
    auto parentItem = cacheData(sizeWatcher->parentList);
    const QModelIndex parent = toQModelIndex(sizeWatcher->parentList, q);

    if (size.width() != parentItem->columnCount) {
        const int columnCount = std::max(0, parentItem->columnCount);
        Q_ASSERT_X(size.width() >= parentItem->columnCount, __FUNCTION__, "The column count should only shrink in columnsRemoved!!");
        parentItem->columnCount = size.width();
        if (size.width() > columnCount) {
            Q_ASSERT(size.width() > 0);
            q->beginInsertColumns(parent, columnCount, size.width() - 1);
            q->endInsertColumns();
        } else {
            Q_ASSERT_X(size.width() == columnCount, __FUNCTION__, qPrintable(QString(QLatin1String("%1 != %2")).arg(size.width()).arg(columnCount)));
        }
    }

    Q_ASSERT_X(size.height() >= parentItem->rowCount, __FUNCTION__, "The new size and the current size should match!!");
    if (!parentItem->rowCount) {
        if (size.height() > 0) {
            q->beginInsertRows(parent, 0, size.height() - 1);
            parentItem->rowCount = size.height();
            q->endInsertRows();
        }
    } else {
        Q_ASSERT_X(parentItem->rowCount == size.height(), __FUNCTION__, qPrintable(QString(QLatin1String("%1 != %2")).arg(parentItem->rowCount).arg(size.height())));
    }
    m_pendingRequests.removeAll(watcher);
    delete watcher;
}
//  -----------------------------------------------------------------------

//  A QAbstractItemModelReplicaImplementation that Python can take functions over in. Every QAbstractItemModelReplicaImplementation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractItemModelReplicaImplementationCall0)(const void *, int *);
typedef void (*CuteQAbstractItemModelReplicaImplementationCall1)(const void *, QRemoteObjectNode *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemModelReplicaImplementationCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemModelReplicaImplementationCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaImplementationCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaImplementationCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaImplementationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaImplementationCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaImplementationCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractItemModelReplicaImplementation : public QAbstractItemModelReplicaImplementation {
public:
  using QAbstractItemModelReplicaImplementation::QAbstractItemModelReplicaImplementation;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QRemoteObjectReplica10initializeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode")) {
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

  //  void QAbstractItemModelReplicaImplementation::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaImplementationCall0 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModelReplicaImplementation::initialize();
  }

  //  void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)
  void setNode(QRemoteObjectNode *node) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaImplementationCall1 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall1>(taken[1]);
      call(this, node, &handled);
      if (handled) return;
    }
    QRemoteObjectReplica::setNode(node);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaImplementationCall2 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall2>(taken[2]);
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
      CuteQAbstractItemModelReplicaImplementationCall3 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall3>(taken[3]);
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
      CuteQAbstractItemModelReplicaImplementationCall4 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall4>(taken[4]);
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
      CuteQAbstractItemModelReplicaImplementationCall5 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall5>(taken[5]);
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
      CuteQAbstractItemModelReplicaImplementationCall6 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall6>(taken[6]);
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
      CuteQAbstractItemModelReplicaImplementationCall7 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall7>(taken[7]);
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
      CuteQAbstractItemModelReplicaImplementationCall8 call = reinterpret_cast<CuteQAbstractItemModelReplicaImplementationCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractItemModelReplicaImplementation::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK39QAbstractItemModelReplicaImplementation10metaObjectEv(
    const QAbstractItemModelReplicaImplementation *self) {
  return self->metaObject();
}

//  QAbstractItemModelReplicaImplementation::~QAbstractItemModelReplicaImplem
//      entation()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementationD1Ev(
    QAbstractItemModelReplicaImplementation *self) {
  delete self;
}

//  void QAbstractItemModelReplicaImplementation::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation10initializeEv(
    QAbstractItemModelReplicaImplementation *self) {
  self->initialize();
}

//  void QAbstractItemModelReplicaImplementation::onHeaderDataChanged(Qt::Ori
//      entation orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation19onHeaderDataChangedEN2Qt11OrientationEii(
    QAbstractItemModelReplicaImplementation *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  self->onHeaderDataChanged(orientation, first, last);
}

//  void QAbstractItemModelReplicaImplementation::handleSizeDone(QRemoteObjec
//      tPendingCallWatcher *watcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation14handleSizeDoneEP31QRemoteObjectPendingCallWatcher(
    QAbstractItemModelReplicaImplementation *self,
    QRemoteObjectPendingCallWatcher *watcher) {
  self->handleSizeDone(watcher);
}

//  CacheData *QAbstractItemModelReplicaImplementation::cacheData(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
CacheData *ritual_ZNK39QAbstractItemModelReplicaImplementation9cacheDataERK11QModelIndex(
    const QAbstractItemModelReplicaImplementation *self,
    const QModelIndex *index) {
  return self->cacheData(*index);
}

//  CacheEntry *QAbstractItemModelReplicaImplementation::cacheEntry(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
CacheEntry *ritual_ZNK39QAbstractItemModelReplicaImplementation10cacheEntryERK11QModelIndex(
    const QAbstractItemModelReplicaImplementation *self,
    const QModelIndex *index) {
  return self->cacheEntry(*index);
}

//  a Python function taken by a CuteQAbstractItemModelReplicaImplementation,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemModelReplicaImplementation(
    QAbstractItemModelReplicaImplementation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemModelReplicaImplementation *>(self)->take(key, call);
}
