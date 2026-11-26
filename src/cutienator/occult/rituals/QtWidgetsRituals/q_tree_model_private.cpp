//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qheaderview.h>
#include <QtGui/qpainter.h>
#include <QtCore/qstack.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtreewidget_p.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/private/qtreewidgetitemiterator_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qtreewidget.cpp, line 766, as _ZNK10QTreeModel10isChangingEv
inline bool QTreeModel::isChanging() const
{
    Q_D(const QTreeModel);
    return !d->changes.isEmpty();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 3368, as _ZNK17QTreeModelPrivate24executePendingOperationsEv
inline void QTreeModelPrivate::executePendingOperations() const
{
    q_func()->executePendingSort();
}
//  -----------------------------------------------------------------------

//  QTreeModel *QTreeModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTreeModel *ritual_ZN17QTreeModelPrivate6q_funcEv(QTreeModelPrivate *self) {
  return self->q_func();
}

//  const QTreeModel *QTreeModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTreeModel *ritual_ZNK17QTreeModelPrivate6q_funcEv(
    const QTreeModelPrivate *self) {
  return self->q_func();
}

//  void QTreeModelPrivate::executePendingOperations() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QTreeModelPrivate24executePendingOperationsEv(
    const QTreeModelPrivate *self) {
  self->executePendingOperations();
}

//  void QTreeModelPrivate::executePendingOperations() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QTreeModelPrivate24executePendingOperationsEv(
    const QTreeModelPrivate *self) {
  self->QTreeModelPrivate::executePendingOperations();
}

#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(treewidget)
