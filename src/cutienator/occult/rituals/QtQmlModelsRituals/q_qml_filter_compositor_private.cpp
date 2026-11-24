//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlfiltercompositor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlfiltercompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmlfiltercompositor_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/sfpm/filters/qqmlfiltercompositor.cpp, line 34, as _ZN27QQmlFilterCompositorPrivate4initEv
inline void QQmlFilterCompositorPrivate::init()
{
    Q_Q(QQmlFilterCompositor);
    m_sfpmModel = qobject_cast<QQmlSortFilterProxyModel *>(q->parent());
}
//  -----------------------------------------------------------------------

//  QQmlFilterCompositor *QQmlFilterCompositorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlFilterCompositor *ritual_ZN27QQmlFilterCompositorPrivate6q_funcEv(
    QQmlFilterCompositorPrivate *self) {
  return self->q_func();
}

//  const QQmlFilterCompositor *QQmlFilterCompositorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlFilterCompositor *ritual_ZNK27QQmlFilterCompositorPrivate6q_funcEv(
    const QQmlFilterCompositorPrivate *self) {
  return self->q_func();
}

//  void QQmlFilterCompositorPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlFilterCompositorPrivate4initEv(
    QQmlFilterCompositorPrivate *self) {
  self->init();
}
