//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 1575, as _Z28lcTableViewDelegateLifecyclev
inline const QLoggingCategory &lcTableViewDelegateLifecycle()
{
    static const QLoggingCategory category("qt.quick.tableview.lifecycle");
    return category;
}
//  -----------------------------------------------------------------------

//  void QQuickTableViewPrivate::TableEdgeLoadRequest::begin(const QPoint
//      &cell, const QPointF &pos, QQmlIncubator::IncubationMode
//      incubationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest5beginERK6QPointRK7QPointFN13QQmlIncubator14IncubationModeE(
    QQuickTableViewPrivate::TableEdgeLoadRequest *self,
    const QPoint *cell,
    const QPointF *pos,
    QQmlIncubator::IncubationMode incubationMode) {
  self->begin(*cell, *pos, incubationMode);
}

//  void QQuickTableViewPrivate::TableEdgeLoadRequest::begin(Qt::Edge
//      edgeToLoad, int edgeIndex, const QList<int> visibleCellsInEdge,
//      QQmlIncubator::IncubationMode incubationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest5beginEN2Qt4EdgeEi5QListIiEN13QQmlIncubator14IncubationModeE(
    QQuickTableViewPrivate::TableEdgeLoadRequest *self,
    Qt::Edge edgeToLoad,
    int edgeIndex,
    const QList<int> *visibleCellsInEdge,
    QQmlIncubator::IncubationMode incubationMode) {
  self->begin(edgeToLoad, edgeIndex, *visibleCellsInEdge, incubationMode);
}

//  void QQuickTableViewPrivate::TableEdgeLoadRequest::markAsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest10markAsDoneEv(
    QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  self->markAsDone();
}

//  bool QQuickTableViewPrivate::TableEdgeLoadRequest::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest8isActiveEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return self->isActive();
}

//  QPoint QQuickTableViewPrivate::TableEdgeLoadRequest::currentCell() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest11currentCellEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return new QPoint(self->currentCell());
}

//  bool QQuickTableViewPrivate::TableEdgeLoadRequest::hasCurrentCell() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest14hasCurrentCellEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return self->hasCurrentCell();
}

//  void QQuickTableViewPrivate::TableEdgeLoadRequest::moveToNextCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest14moveToNextCellEv(
    QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  self->moveToNextCell();
}

//  Qt::Edge QQuickTableViewPrivate::TableEdgeLoadRequest::edge() const
extern "C" Q_DECL_EXPORT
Qt::Edge ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest4edgeEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return self->edge();
}

//  int QQuickTableViewPrivate::TableEdgeLoadRequest::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest3rowEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return self->row();
}

//  int QQuickTableViewPrivate::TableEdgeLoadRequest::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest6columnEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return self->column();
}

//  QQmlIncubator::IncubationMode
//      QQuickTableViewPrivate::TableEdgeLoadRequest::incubationMode() const
extern "C" Q_DECL_EXPORT
QQmlIncubator::IncubationMode ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest14incubationModeEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return self->incubationMode();
}

//  QPointF QQuickTableViewPrivate::TableEdgeLoadRequest::startPosition()
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest13startPositionEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return new QPointF(self->startPosition());
}

//  QString QQuickTableViewPrivate::TableEdgeLoadRequest::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest8toStringEv(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  return new QString(self->toString());
}

//  QPoint QQuickTableViewPrivate::TableEdgeLoadRequest::cellAt(int index)
//      const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest6cellAtEi(
    const QQuickTableViewPrivate::TableEdgeLoadRequest *self,
    int index) {
  return new QPoint(self->cellAt(index));
}

//  QQuickTableViewPrivate::TableEdgeLoadRequest::~TableEdgeLoadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequestD1Ev(
    QQuickTableViewPrivate::TableEdgeLoadRequest *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_tableview)
