//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <QtRemoteObjects/QRemoteObjectPendingReply>
#include <QtCore/QSize>
#include <QtCore/QVariantList>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 119, as local:qremoteobjectabstractitemmodelreplica.cpp:removeIndexFromRow
inline void removeIndexFromRow(const QModelIndex &index, const QList<int> &roles, CachedRowEntry *entry)
{
    CachedRowEntry &entryRef = *entry;
    if (index.column() < entryRef.size()) {
        CacheEntry &entry = entryRef[index.column()];
        if (roles.isEmpty()) {
            entry.data.clear();
        } else {
            for (int role : roles)
                entry.data.remove(role);
        }
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 30, as _ZN9CacheDataC1EP39QAbstractItemModelReplicaImplementationPS_
inline CacheData::CacheData(QAbstractItemModelReplicaImplementation *model, CacheData *parentItem)
    : replicaModel(model)
    , parent(parentItem)
    , hasChildren(false)
    , columnCount(0)
    , rowCount(0)
{
    if (parent)
        replicaModel->m_activeParents.insert(parent);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 41, as _ZN9CacheDataD1Ev
inline CacheData::~CacheData() {
    if (parent && !replicaModel->m_activeParents.empty())
        replicaModel->m_activeParents.erase(this);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 77, as _ZN39QAbstractItemModelReplicaImplementation10initializeEv
inline void QAbstractItemModelReplicaImplementation::initialize()
{
    QVariantList properties;
    properties << QVariant::fromValue(QList<int>());
    properties << QVariant::fromValue(QIntHash());
    setProperties(std::move(properties));
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectabstractitemmodelreplica.cpp, line 149, as _ZN39QAbstractItemModelReplicaImplementation10clearCacheERK5QListIN9QtPrivate10ModelIndexEES5_RKS0_IiE
inline bool QAbstractItemModelReplicaImplementation::clearCache(const QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const QList<int> &roles = QList<int>())
{
    Q_ASSERT(start.size() == end.size());

    bool ok = true;
    const QModelIndex startIndex = toQModelIndex(start, q, &ok);
    if (!ok)
        return false;
    const QModelIndex endIndex = toQModelIndex(end, q, &ok);
    if (!ok)
        return false;
    Q_ASSERT(startIndex.isValid());
    Q_ASSERT(endIndex.isValid());
    Q_ASSERT(startIndex.parent() == endIndex.parent());
    Q_UNUSED(endIndex)
    QModelIndex parentIndex = startIndex.parent();
    auto parentItem = cacheData(parentIndex);

    const int startRow = start.last().row;
    const int lastRow = end.last().row;
    const int startColumn = start.last().column;
    const int lastColumn = end.last().column;
    for (int row = startRow; row <= lastRow; ++row) {
        Q_ASSERT_X(row >= 0 && row < parentItem->rowCount, __FUNCTION__, qPrintable(QString(QLatin1String("0 <= %1 < %2")).arg(row).arg(parentItem->rowCount)));
        auto item = parentItem->children.get(row);
        if (item) {
            CachedRowEntry *entry = &(item->cachedRowEntry);
            for (int column = startColumn; column <= lastColumn; ++column)
                removeIndexFromRow(q->index(row, column, parentIndex), roles, entry);
        }
    }
    return true;
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

//  void *QAbstractItemModelReplicaImplementation::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN39QAbstractItemModelReplicaImplementation11qt_metacastEPKc(
    QAbstractItemModelReplicaImplementation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QAbstractItemModelReplicaImplementation::qt_metacall(QMetaObject::Cal
//      l a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN39QAbstractItemModelReplicaImplementation11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractItemModelReplicaImplementation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  const QList<int>
//      &QAbstractItemModelReplicaImplementation::availableRoles() const
extern "C" Q_DECL_EXPORT
const QList<int> *ritual_ZNK39QAbstractItemModelReplicaImplementation14availableRolesEv(
    const QAbstractItemModelReplicaImplementation *self) {
  return &(self->availableRoles());
}

//  bool QAbstractItemModelReplicaImplementation::clearCache(const
//      QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const
//      QList<int> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN39QAbstractItemModelReplicaImplementation10clearCacheERK5QListIN9QtPrivate10ModelIndexEES5_RKS0_IiE(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *start,
    const QtPrivate::IndexList *end,
    const QList<int> *roles) {
  return self->clearCache(*start, *end, *roles);
}

//  void QAbstractItemModelReplicaImplementation::availableRolesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation21availableRolesChangedEv(
    QAbstractItemModelReplicaImplementation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "availableRolesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "availableRolesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QAbstractItemModelReplicaImplementation::dataChanged(QtPrivate::Index
//      List topLeft, QtPrivate::IndexList bottomRight, QList<int> roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation11dataChangedE5QListIN9QtPrivate10ModelIndexEES3_S0_IiE(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *topLeft,
    const QtPrivate::IndexList *bottomRight,
    const QList<int> *roles) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dataChanged(QtPrivate::IndexList,QtPrivate::IndexList,QList<int>)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dataChanged(QtPrivate::IndexList,QtPrivate::IndexList,QList<int>)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(topLeft)),
      const_cast<void *>(static_cast<const void *>(bottomRight)),
      const_cast<void *>(static_cast<const void *>(roles)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::rowsInserted(QtPrivate::Ind
//      exList parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation12rowsInsertedE5QListIN9QtPrivate10ModelIndexEEii(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int first,
    int last) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rowsInserted(QtPrivate::IndexList,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rowsInserted(QtPrivate::IndexList,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&first)),
      const_cast<void *>(static_cast<const void *>(&last)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QAbstractItemModelReplicaImplementation::rowsRemoved(QtPrivate::Index
//      List parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation11rowsRemovedE5QListIN9QtPrivate10ModelIndexEEii(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int first,
    int last) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rowsRemoved(QtPrivate::IndexList,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rowsRemoved(QtPrivate::IndexList,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&first)),
      const_cast<void *>(static_cast<const void *>(&last)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QAbstractItemModelReplicaImplementation::rowsMoved(QtPrivate::IndexLi
//      st parent, int start, int end, QtPrivate::IndexList destination, int
//      row)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation9rowsMovedE5QListIN9QtPrivate10ModelIndexEEiiS3_i(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int start,
    int end,
    const QtPrivate::IndexList *destination,
    int row) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rowsMoved(QtPrivate::IndexList,int,int,QtPrivate::IndexList,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rowsMoved(QtPrivate::IndexList,int,int,QtPrivate::IndexList,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
      const_cast<void *>(static_cast<const void *>(destination)),
      const_cast<void *>(static_cast<const void *>(&row)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::currentChanged(QtPrivate::I
//      ndexList current, QtPrivate::IndexList previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation14currentChangedE5QListIN9QtPrivate10ModelIndexEES3_(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *current,
    const QtPrivate::IndexList *previous) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentChanged(QtPrivate::IndexList,QtPrivate::IndexList)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentChanged(QtPrivate::IndexList,QtPrivate::IndexList)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(current)),
      const_cast<void *>(static_cast<const void *>(previous)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::modelReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation10modelResetEv(
    QAbstractItemModelReplicaImplementation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "modelReset()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "modelReset()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::headerDataChanged(Qt::Orien
//      tation a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation17headerDataChangedEN2Qt11OrientationEii(
    QAbstractItemModelReplicaImplementation *self,
    Qt::Orientation a0,
    int a1,
    int a2) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "headerDataChanged(Qt::Orientation,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "headerDataChanged(Qt::Orientation,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
      const_cast<void *>(static_cast<const void *>(&a2)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::columnsInserted(QtPrivate::
//      IndexList parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation15columnsInsertedE5QListIN9QtPrivate10ModelIndexEEii(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int first,
    int last) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "columnsInserted(QtPrivate::IndexList,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "columnsInserted(QtPrivate::IndexList,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&first)),
      const_cast<void *>(static_cast<const void *>(&last)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::layoutChanged(QtPrivate::In
//      dexList parents, QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation13layoutChangedE5QListIN9QtPrivate10ModelIndexEEN18QAbstractItemModel16LayoutChangeHintE(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "layoutChanged(QtPrivate::IndexList,QAbstractItemModel::LayoutChangeHint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "layoutChanged(QtPrivate::IndexList,QAbstractItemModel::LayoutChangeHint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parents)),
      const_cast<void *>(static_cast<const void *>(&hint)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onHeaderDataChanged(Qt::Ori
//      entation orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation19onHeaderDataChangedEN2Qt11OrientationEii(
    QAbstractItemModelReplicaImplementation *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onHeaderDataChanged(Qt::Orientation,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onHeaderDataChanged(Qt::Orientation,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&orientation)),
      const_cast<void *>(static_cast<const void *>(&first)),
      const_cast<void *>(static_cast<const void *>(&last)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onDataChanged(const
//      QtPrivate::IndexList &start, const QtPrivate::IndexList &end, const
//      QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation13onDataChangedERK5QListIN9QtPrivate10ModelIndexEES5_RKS0_IiE(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *start,
    const QtPrivate::IndexList *end,
    const QList<int> *roles) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onDataChanged(const QtPrivate::IndexList &,const QtPrivate::IndexList &,const QList<int> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onDataChanged(const QtPrivate::IndexList &,const QtPrivate::IndexList &,const QList<int> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(start)),
      const_cast<void *>(static_cast<const void *>(end)),
      const_cast<void *>(static_cast<const void *>(roles)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onRowsInserted(const
//      QtPrivate::IndexList &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation14onRowsInsertedERK5QListIN9QtPrivate10ModelIndexEEii(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int start,
    int end) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRowsInserted(const QtPrivate::IndexList &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRowsInserted(const QtPrivate::IndexList &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onRowsRemoved(const
//      QtPrivate::IndexList &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation13onRowsRemovedERK5QListIN9QtPrivate10ModelIndexEEii(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int start,
    int end) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRowsRemoved(const QtPrivate::IndexList &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRowsRemoved(const QtPrivate::IndexList &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onColumnsInserted(const
//      QtPrivate::IndexList &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation17onColumnsInsertedERK5QListIN9QtPrivate10ModelIndexEEii(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parent,
    int start,
    int end) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onColumnsInserted(const QtPrivate::IndexList &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onColumnsInserted(const QtPrivate::IndexList &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parent)),
      const_cast<void *>(static_cast<const void *>(&start)),
      const_cast<void *>(static_cast<const void *>(&end)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QAbstractItemModelReplicaImplementation::onRowsMoved(QtPrivate::Index
//      List srcParent, int srcRow, int count, QtPrivate::IndexList
//      destParent, int destRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation11onRowsMovedE5QListIN9QtPrivate10ModelIndexEEiiS3_i(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *srcParent,
    int srcRow,
    int count,
    const QtPrivate::IndexList *destParent,
    int destRow) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onRowsMoved(QtPrivate::IndexList,int,int,QtPrivate::IndexList,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onRowsMoved(QtPrivate::IndexList,int,int,QtPrivate::IndexList,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(srcParent)),
      const_cast<void *>(static_cast<const void *>(&srcRow)),
      const_cast<void *>(static_cast<const void *>(&count)),
      const_cast<void *>(static_cast<const void *>(destParent)),
      const_cast<void *>(static_cast<const void *>(&destRow)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onCurrentChanged(QtPrivate:
//      :IndexList current, QtPrivate::IndexList previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation16onCurrentChangedE5QListIN9QtPrivate10ModelIndexEES3_(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *current,
    const QtPrivate::IndexList *previous) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onCurrentChanged(QtPrivate::IndexList,QtPrivate::IndexList)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onCurrentChanged(QtPrivate::IndexList,QtPrivate::IndexList)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(current)),
      const_cast<void *>(static_cast<const void *>(previous)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onModelReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation12onModelResetEv(
    QAbstractItemModelReplicaImplementation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onModelReset()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onModelReset()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::requestedData(QRemoteObject
//      PendingCallWatcher *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation13requestedDataEP31QRemoteObjectPendingCallWatcher(
    QAbstractItemModelReplicaImplementation *self,
    QRemoteObjectPendingCallWatcher *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestedData(QRemoteObjectPendingCallWatcher *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestedData(QRemoteObjectPendingCallWatcher *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::requestedHeaderData(QRemote
//      ObjectPendingCallWatcher *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation19requestedHeaderDataEP31QRemoteObjectPendingCallWatcher(
    QAbstractItemModelReplicaImplementation *self,
    QRemoteObjectPendingCallWatcher *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestedHeaderData(QRemoteObjectPendingCallWatcher *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestedHeaderData(QRemoteObjectPendingCallWatcher *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation4initEv(
    QAbstractItemModelReplicaImplementation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "init()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "init()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::fetchPendingData()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation16fetchPendingDataEv(
    QAbstractItemModelReplicaImplementation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fetchPendingData()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fetchPendingData()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::fetchPendingHeaderData()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation22fetchPendingHeaderDataEv(
    QAbstractItemModelReplicaImplementation *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fetchPendingHeaderData()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fetchPendingHeaderData()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::handleInitDone(QRemoteObjec
//      tPendingCallWatcher *watcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation14handleInitDoneEP31QRemoteObjectPendingCallWatcher(
    QAbstractItemModelReplicaImplementation *self,
    QRemoteObjectPendingCallWatcher *watcher) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleInitDone(QRemoteObjectPendingCallWatcher *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleInitDone(QRemoteObjectPendingCallWatcher *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&watcher)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::handleModelResetDone(QRemot
//      eObjectPendingCallWatcher *watcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation20handleModelResetDoneEP31QRemoteObjectPendingCallWatcher(
    QAbstractItemModelReplicaImplementation *self,
    QRemoteObjectPendingCallWatcher *watcher) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleModelResetDone(QRemoteObjectPendingCallWatcher *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleModelResetDone(QRemoteObjectPendingCallWatcher *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&watcher)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::handleSizeDone(QRemoteObjec
//      tPendingCallWatcher *watcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation14handleSizeDoneEP31QRemoteObjectPendingCallWatcher(
    QAbstractItemModelReplicaImplementation *self,
    QRemoteObjectPendingCallWatcher *watcher) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSizeDone(QRemoteObjectPendingCallWatcher *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSizeDone(QRemoteObjectPendingCallWatcher *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&watcher)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QAbstractItemModelReplicaImplementation::onReplicaCurrentChanged(cons
//      t QModelIndex &current, const QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation23onReplicaCurrentChangedERK11QModelIndexS2_(
    QAbstractItemModelReplicaImplementation *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onReplicaCurrentChanged(const QModelIndex &,const QModelIndex &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onReplicaCurrentChanged(const QModelIndex &,const QModelIndex &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(current)),
      const_cast<void *>(static_cast<const void *>(previous)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::fillCache(const
//      QtPrivate::IndexValuePair &pair, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation9fillCacheERKN9QtPrivate14IndexValuePairERK5QListIiE(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexValuePair *pair,
    const QList<int> *roles) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fillCache(const QtPrivate::IndexValuePair &,const QList<int> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fillCache(const QtPrivate::IndexValuePair &,const QList<int> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(pair)),
      const_cast<void *>(static_cast<const void *>(roles)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractItemModelReplicaImplementation::onLayoutChanged(const
//      QtPrivate::IndexList &parents, QAbstractItemModel::LayoutChangeHint
//      hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QAbstractItemModelReplicaImplementation15onLayoutChangedERK5QListIN9QtPrivate10ModelIndexEEN18QAbstractItemModel16LayoutChangeHintE(
    QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractItemModelReplicaImplementation")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onLayoutChanged(const QtPrivate::IndexList &,QAbstractItemModel::LayoutChangeHint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onLayoutChanged(const QtPrivate::IndexList &,QAbstractItemModel::LayoutChangeHint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(parents)),
      const_cast<void *>(static_cast<const void *>(&hint)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  CacheData *QAbstractItemModelReplicaImplementation::cacheData(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
CacheData *ritual_ZNK39QAbstractItemModelReplicaImplementation9cacheDataERK11QModelIndex(
    const QAbstractItemModelReplicaImplementation *self,
    const QModelIndex *index) {
  return self->cacheData(*index);
}

//  CacheData *QAbstractItemModelReplicaImplementation::cacheData(const
//      QtPrivate::IndexList &index) const
extern "C" Q_DECL_EXPORT
CacheData *ritual_ZNK39QAbstractItemModelReplicaImplementation9cacheDataERK5QListIN9QtPrivate10ModelIndexEE(
    const QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *index) {
  return self->cacheData(*index);
}

//  CacheData *QAbstractItemModelReplicaImplementation::createCacheData(const
//      QtPrivate::IndexList &index) const
extern "C" Q_DECL_EXPORT
CacheData *ritual_ZNK39QAbstractItemModelReplicaImplementation15createCacheDataERK5QListIN9QtPrivate10ModelIndexEE(
    const QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *index) {
  return self->createCacheData(*index);
}

//  CacheEntry *QAbstractItemModelReplicaImplementation::cacheEntry(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
CacheEntry *ritual_ZNK39QAbstractItemModelReplicaImplementation10cacheEntryERK11QModelIndex(
    const QAbstractItemModelReplicaImplementation *self,
    const QModelIndex *index) {
  return self->cacheEntry(*index);
}

//  CacheEntry *QAbstractItemModelReplicaImplementation::cacheEntry(const
//      QtPrivate::IndexList &index) const
extern "C" Q_DECL_EXPORT
CacheEntry *ritual_ZNK39QAbstractItemModelReplicaImplementation10cacheEntryERK5QListIN9QtPrivate10ModelIndexEE(
    const QAbstractItemModelReplicaImplementation *self,
    const QtPrivate::IndexList *index) {
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

//  a QRemoteObjectPendingReply<QSize> a ritual of
//      QAbstractItemModelReplicaImplementation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemModelReplicaImplementation__QRemoteObjectPendingReply_QSize(
    QRemoteObjectPendingReply<QSize> *self) {
  delete self;
}

//  a QRemoteObjectPendingReply<QtPrivate::DataEntries> a ritual of
//      QAbstractItemModelReplicaImplementation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemModelReplicaImplementation__QRemoteObjectPendingReply_QtPrivate_DataEntries(
    QRemoteObjectPendingReply<QtPrivate::DataEntries> *self) {
  delete self;
}

//  a QRemoteObjectPendingReply<QVariantList> a ritual of
//      QAbstractItemModelReplicaImplementation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemModelReplicaImplementation__QRemoteObjectPendingReply_QVariantList(
    QRemoteObjectPendingReply<QVariantList> *self) {
  delete self;
}

//  a QRemoteObjectPendingReply<QtPrivate::MetaAndDataEntries> a ritual of
//      QAbstractItemModelReplicaImplementation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractItemModelReplicaImplementation__QRemoteObjectPendingReply_QtPrivate_MetaAndDataEntries(
    QRemoteObjectPendingReply<QtPrivate::MetaAndDataEntries> *self) {
  delete self;
}
