//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickstate_p_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickstategroup_p.h>
#include <QtQuick/private/qquickstatechangescript_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 287, as _ZNK18QQuickStatePrivate18generateActionListEv
inline QQuickStateOperation::ActionList
QQuickStatePrivate::generateActionList() const
{
    QQuickStateOperation::ActionList applyList;
    if (inState)
        return applyList;

    // Prevent "extends" recursion
    inState = true;

    if (!extends.isEmpty()) {
        QList<QQuickState *> states = group ? group->states() : QList<QQuickState *>();
        for (int ii = 0; ii < states.size(); ++ii)
            if (states.at(ii)->name() == extends) {
                qmlExecuteDeferred(states.at(ii));
                applyList = static_cast<QQuickStatePrivate*>(states.at(ii)->d_func())->generateActionList();
            }
    }

    for (QQuickStateOperation *op : operations)
        applyList << op->actions();

    inState = false;
    return applyList;
}

//  from ../qtdeclarative/src/quick/util/qquickstate.cpp, line 263, as _ZN18QQuickStatePrivate8completeEv
inline void QQuickStatePrivate::complete()
{
    Q_Q(QQuickState);

    for (int ii = 0; ii < reverting.size(); ++ii) {
        for (int jj = 0; jj < revertList.size(); ++jj) {
            const QQuickRevertAction &revert = reverting.at(ii);
            const QQuickSimpleAction &simple = revertList.at(jj);
            if ((revert.event && simple.event() == revert.event) ||
                simple.property() == revert.property) {
                revertList.removeAt(jj);
                break;
            }
        }
    }
    reverting.clear();

    if (group)
        group->stateAboutToComplete();
    emit q->completed();
}
//  -----------------------------------------------------------------------

//  QQuickState *QQuickStatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickState *ritual_ZN18QQuickStatePrivate6q_funcEv(
    QQuickStatePrivate *self) {
  return self->q_func();
}

//  const QQuickState *QQuickStatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickState *ritual_ZNK18QQuickStatePrivate6q_funcEv(
    const QQuickStatePrivate *self) {
  return self->q_func();
}

//  QQuickStatePrivate::QQuickStatePrivate()
extern "C" Q_DECL_EXPORT
QQuickStatePrivate *ritual_ZN18QQuickStatePrivateC1Ev() {
  return new QQuickStatePrivate();
}

//  void QQuickStatePrivate::operations_append(QQmlListProperty<QQuickStateOp
//      eration> *prop, QQuickStateOperation *op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate17operations_appendEP16QQmlListPropertyI20QQuickStateOperationEPS1_(
    QQmlListProperty<QQuickStateOperation> *prop,
    QQuickStateOperation *op) {
  QQuickStatePrivate::operations_append(prop, op);
}

//  void QQuickStatePrivate::operations_clear(QQmlListProperty<QQuickStateOpe
//      ration> *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate16operations_clearEP16QQmlListPropertyI20QQuickStateOperationE(
    QQmlListProperty<QQuickStateOperation> *prop) {
  QQuickStatePrivate::operations_clear(prop);
}

//  qsizetype QQuickStatePrivate::operations_count(QQmlListProperty<QQuickSta
//      teOperation> *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN18QQuickStatePrivate16operations_countEP16QQmlListPropertyI20QQuickStateOperationE(
    QQmlListProperty<QQuickStateOperation> *prop) {
  return QQuickStatePrivate::operations_count(prop);
}

//  QQuickStateOperation
//      *QQuickStatePrivate::operations_at(QQmlListProperty<QQuickStateOperat
//      ion> *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuickStateOperation *ritual_ZN18QQuickStatePrivate13operations_atEP16QQmlListPropertyI20QQuickStateOperationEx(
    QQmlListProperty<QQuickStateOperation> *prop,
    qsizetype index) {
  return QQuickStatePrivate::operations_at(prop, index);
}

//  void QQuickStatePrivate::operations_replace(QQmlListProperty<QQuickStateO
//      peration> *prop, qsizetype index, QQuickStateOperation *op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate18operations_replaceEP16QQmlListPropertyI20QQuickStateOperationExPS1_(
    QQmlListProperty<QQuickStateOperation> *prop,
    qsizetype index,
    QQuickStateOperation *op) {
  QQuickStatePrivate::operations_replace(prop, index, op);
}

//  void QQuickStatePrivate::operations_removeLast(QQmlListProperty<QQuickSta
//      teOperation> *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate21operations_removeLastEP16QQmlListPropertyI20QQuickStateOperationE(
    QQmlListProperty<QQuickStateOperation> *prop) {
  QQuickStatePrivate::operations_removeLast(prop);
}

//  QQuickStateOperation::ActionList QQuickStatePrivate::generateActionList()
//      const
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZNK18QQuickStatePrivate18generateActionListEv(
    const QQuickStatePrivate *self) {
  return new QList<QQuickStateAction>(self->generateActionList());
}

//  void QQuickStatePrivate::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStatePrivate8completeEv(QQuickStatePrivate *self) {
  self->complete();
}
