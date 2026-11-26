//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtransposeproxymodel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(proxymodel) && QT_CONFIG(transposeproxymodel)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qtransposeproxymodel.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtransposeproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtransposeproxymodel.h>
#include <QtCore/private/qtransposeproxymodel_p.h>
#include <QtCore/qlist.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qsize.h>
#include <QtCore/qmap.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 17, as _ZN27QTransposeProxyModelPrivateD1Ev
inline QTransposeProxyModelPrivate::~QTransposeProxyModelPrivate()
    = default;

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 14, as _ZN27QTransposeProxyModelPrivateC1Ev
inline QTransposeProxyModelPrivate::QTransposeProxyModelPrivate()
    = default;

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 20, as _ZNK27QTransposeProxyModelPrivate20uncheckedMapToSourceERK11QModelIndex
inline QModelIndex QTransposeProxyModelPrivate::uncheckedMapToSource(const QModelIndex &proxyIndex) const
{
    if (!model || !proxyIndex.isValid())
        return QModelIndex();
    Q_Q(const QTransposeProxyModel);
    return q->createSourceIndex(proxyIndex.column(), proxyIndex.row(), proxyIndex.internalPointer());
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 28, as _ZNK27QTransposeProxyModelPrivate22uncheckedMapFromSourceERK11QModelIndex
inline QModelIndex QTransposeProxyModelPrivate::uncheckedMapFromSource(const QModelIndex &sourceIndex) const
{
    if (!model || !sourceIndex.isValid())
        return QModelIndex();
    Q_Q(const QTransposeProxyModel);
    return q->createIndex(sourceIndex.column(), sourceIndex.row(), sourceIndex.internalPointer());
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 36, as _ZN27QTransposeProxyModelPrivate15onLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void QTransposeProxyModelPrivate::onLayoutChanged(const QList<QPersistentModelIndex> &parents, QAbstractItemModel::LayoutChangeHint hint)
{
    Q_Q(QTransposeProxyModel);
    Q_ASSERT(layoutChangeProxyIndexes.size() == layoutChangePersistentIndexes.size());
    QModelIndexList toList;
    toList.reserve(layoutChangePersistentIndexes.size());
    for (const QPersistentModelIndex &persistIdx : std::as_const(layoutChangePersistentIndexes))
        toList << q->mapFromSource(persistIdx);
    q->changePersistentIndexList(layoutChangeProxyIndexes, toList);
    layoutChangeProxyIndexes.clear();
    layoutChangePersistentIndexes.clear();
    QList<QPersistentModelIndex> proxyParents;
    proxyParents.reserve(parents.size());
    for (const QPersistentModelIndex &srcParent : parents)
        proxyParents << q->mapFromSource(srcParent);
    QAbstractItemModel::LayoutChangeHint proxyHint = QAbstractItemModel::NoLayoutChangeHint;
    if (hint == QAbstractItemModel::VerticalSortHint)
        proxyHint = QAbstractItemModel::HorizontalSortHint;
    else if (hint == QAbstractItemModel::HorizontalSortHint)
        proxyHint = QAbstractItemModel::VerticalSortHint;
    emit q->layoutChanged(proxyParents, proxyHint);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 59, as _ZN27QTransposeProxyModelPrivate24onLayoutAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void QTransposeProxyModelPrivate::onLayoutAboutToBeChanged(const QList<QPersistentModelIndex> &sourceParents, QAbstractItemModel::LayoutChangeHint hint)
{
    Q_Q(QTransposeProxyModel);
    QList<QPersistentModelIndex> proxyParents;
    proxyParents.reserve(sourceParents.size());
    for (const QPersistentModelIndex &parent : sourceParents) {
        if (!parent.isValid()) {
            proxyParents << QPersistentModelIndex();
            continue;
        }
        const QModelIndex mappedParent = q->mapFromSource(parent);
        Q_ASSERT(mappedParent.isValid());
        proxyParents << mappedParent;
    }
    QAbstractItemModel::LayoutChangeHint proxyHint = QAbstractItemModel::NoLayoutChangeHint;
    if (hint == QAbstractItemModel::VerticalSortHint)
        proxyHint = QAbstractItemModel::HorizontalSortHint;
    else if (hint == QAbstractItemModel::HorizontalSortHint)
        proxyHint = QAbstractItemModel::VerticalSortHint;
    emit q->layoutAboutToBeChanged(proxyParents, proxyHint);
    const QModelIndexList proxyPersistentIndexes = q->persistentIndexList();
    layoutChangeProxyIndexes.clear();
    layoutChangePersistentIndexes.clear();
    layoutChangeProxyIndexes.reserve(proxyPersistentIndexes.size());
    layoutChangePersistentIndexes.reserve(proxyPersistentIndexes.size());
    for (const QModelIndex &proxyPersistentIndex : proxyPersistentIndexes) {
        layoutChangeProxyIndexes << proxyPersistentIndex;
        Q_ASSERT(proxyPersistentIndex.isValid());
        const QPersistentModelIndex srcPersistentIndex = q->mapToSource(proxyPersistentIndex);
        Q_ASSERT(srcPersistentIndex.isValid());
        layoutChangePersistentIndexes << srcPersistentIndex;
    }
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 93, as _ZN27QTransposeProxyModelPrivate13onDataChangedERK11QModelIndexS2_RK5QListIiE
inline void QTransposeProxyModelPrivate::onDataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight,
                                                const QList<int> &roles)
{
    Q_Q(QTransposeProxyModel);
    emit q->dataChanged(q->mapFromSource(topLeft), q->mapFromSource(bottomRight), roles);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 100, as _ZN27QTransposeProxyModelPrivate19onHeaderDataChangedEN2Qt11OrientationEii
inline void QTransposeProxyModelPrivate::onHeaderDataChanged(Qt::Orientation orientation, int first, int last)
{
    Q_Q(QTransposeProxyModel);
    emit q->headerDataChanged(orientation == Qt::Horizontal ? Qt::Vertical : Qt::Horizontal, first, last);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 106, as _ZN27QTransposeProxyModelPrivate26onColumnsAboutToBeInsertedERK11QModelIndexii
inline void QTransposeProxyModelPrivate::onColumnsAboutToBeInserted(const QModelIndex &parent, int first, int last)
{
    Q_Q(QTransposeProxyModel);
    q->beginInsertRows(q->mapFromSource(parent), first, last);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 112, as _ZN27QTransposeProxyModelPrivate25onColumnsAboutToBeRemovedERK11QModelIndexii
inline void QTransposeProxyModelPrivate::onColumnsAboutToBeRemoved(const QModelIndex &parent, int first, int last)
{
    Q_Q(QTransposeProxyModel);
    q->beginRemoveRows(q->mapFromSource(parent), first, last);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 118, as _ZN27QTransposeProxyModelPrivate23onColumnsAboutToBeMovedERK11QModelIndexiiS2_i
inline void QTransposeProxyModelPrivate::onColumnsAboutToBeMoved(const QModelIndex &sourceParent, int sourceStart, int sourceEnd, const QModelIndex &destinationParent, int destinationColumn)
{
    Q_Q(QTransposeProxyModel);
    q->beginMoveRows(q->mapFromSource(sourceParent), sourceStart, sourceEnd, q->mapFromSource(destinationParent), destinationColumn);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 124, as _ZN27QTransposeProxyModelPrivate23onRowsAboutToBeInsertedERK11QModelIndexii
inline void QTransposeProxyModelPrivate::onRowsAboutToBeInserted(const QModelIndex &parent, int first, int last)
{
    Q_Q(QTransposeProxyModel);
    q->beginInsertColumns(q->mapFromSource(parent), first, last);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 130, as _ZN27QTransposeProxyModelPrivate22onRowsAboutToBeRemovedERK11QModelIndexii
inline void QTransposeProxyModelPrivate::onRowsAboutToBeRemoved(const QModelIndex &parent, int first, int last)
{
    Q_Q(QTransposeProxyModel);
    q->beginRemoveColumns(q->mapFromSource(parent), first, last);
}

//  from src/corelib/itemmodels/qtransposeproxymodel.cpp, line 136, as _ZN27QTransposeProxyModelPrivate20onRowsAboutToBeMovedERK11QModelIndexiiS2_i
inline void QTransposeProxyModelPrivate::onRowsAboutToBeMoved(const QModelIndex &sourceParent, int sourceStart, int sourceEnd, const QModelIndex &destinationParent, int destinationRow)
{
    Q_Q(QTransposeProxyModel);
    q->beginMoveColumns(q->mapFromSource(sourceParent), sourceStart, sourceEnd, q->mapFromSource(destinationParent), destinationRow);
}
//  -----------------------------------------------------------------------

//  QTransposeProxyModel *QTransposeProxyModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTransposeProxyModel *ritual_ZN27QTransposeProxyModelPrivate6q_funcEv(
    QTransposeProxyModelPrivate *self) {
  return self->q_func();
}

//  const QTransposeProxyModel *QTransposeProxyModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTransposeProxyModel *ritual_ZNK27QTransposeProxyModelPrivate6q_funcEv(
    const QTransposeProxyModelPrivate *self) {
  return self->q_func();
}

//  QTransposeProxyModelPrivate::QTransposeProxyModelPrivate()
extern "C" Q_DECL_EXPORT
QTransposeProxyModelPrivate *ritual_ZN27QTransposeProxyModelPrivateC1Ev() {
  return new QTransposeProxyModelPrivate();
}

//  QTransposeProxyModelPrivate::~QTransposeProxyModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivateD1Ev(
    QTransposeProxyModelPrivate *self) {
  delete self;
}

//  QModelIndex QTransposeProxyModelPrivate::uncheckedMapToSource(const
//      QModelIndex &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK27QTransposeProxyModelPrivate20uncheckedMapToSourceERK11QModelIndex(
    const QTransposeProxyModelPrivate *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->uncheckedMapToSource(*proxyIndex));
}

//  QModelIndex QTransposeProxyModelPrivate::uncheckedMapFromSource(const
//      QModelIndex &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK27QTransposeProxyModelPrivate22uncheckedMapFromSourceERK11QModelIndex(
    const QTransposeProxyModelPrivate *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->uncheckedMapFromSource(*sourceIndex));
}

//  void QTransposeProxyModelPrivate::onLayoutChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate15onLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QTransposeProxyModelPrivate *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->onLayoutChanged(*parents, hint);
}

//  void QTransposeProxyModelPrivate::onLayoutAboutToBeChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate24onLayoutAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QTransposeProxyModelPrivate *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->onLayoutAboutToBeChanged(*parents, hint);
}

//  void QTransposeProxyModelPrivate::onDataChanged(const QModelIndex
//      &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate13onDataChangedERK11QModelIndexS2_RK5QListIiE(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight,
    const QList<int> *roles) {
  self->onDataChanged(*topLeft, *bottomRight, *roles);
}

//  void QTransposeProxyModelPrivate::onHeaderDataChanged(Qt::Orientation
//      orientation, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate19onHeaderDataChangedEN2Qt11OrientationEii(
    QTransposeProxyModelPrivate *self,
    Qt::Orientation orientation,
    int first,
    int last) {
  self->onHeaderDataChanged(orientation, first, last);
}

//  void QTransposeProxyModelPrivate::onColumnsAboutToBeInserted(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate26onColumnsAboutToBeInsertedERK11QModelIndexii(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->onColumnsAboutToBeInserted(*parent, first, last);
}

//  void QTransposeProxyModelPrivate::onColumnsAboutToBeRemoved(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate25onColumnsAboutToBeRemovedERK11QModelIndexii(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->onColumnsAboutToBeRemoved(*parent, first, last);
}

//  void QTransposeProxyModelPrivate::onColumnsAboutToBeMoved(const
//      QModelIndex &sourceParent, int sourceStart, int sourceEnd, const
//      QModelIndex &destinationParent, int destinationColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate23onColumnsAboutToBeMovedERK11QModelIndexiiS2_i(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationColumn) {
  self->onColumnsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationColumn);
}

//  void QTransposeProxyModelPrivate::onRowsAboutToBeInserted(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate23onRowsAboutToBeInsertedERK11QModelIndexii(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->onRowsAboutToBeInserted(*parent, first, last);
}

//  void QTransposeProxyModelPrivate::onRowsAboutToBeRemoved(const
//      QModelIndex &parent, int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate22onRowsAboutToBeRemovedERK11QModelIndexii(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->onRowsAboutToBeRemoved(*parent, first, last);
}

//  void QTransposeProxyModelPrivate::onRowsAboutToBeMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QTransposeProxyModelPrivate20onRowsAboutToBeMovedERK11QModelIndexiiS2_i(
    QTransposeProxyModelPrivate *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationRow) {
  self->onRowsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationRow);
}

#endif  // QT_CONFIG(proxymodel) && QT_CONFIG(transposeproxymodel)
