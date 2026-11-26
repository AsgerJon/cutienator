//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortercompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/QPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmlsortercompositor_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p_p.h>
#include <QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 30, as _ZN27QQmlSorterCompositorPrivate4initEv
inline void QQmlSorterCompositorPrivate::init()
{
    Q_Q(QQmlSorterCompositor);
    m_sfpmModel = qobject_cast<QQmlSortFilterProxyModel *>(q->parent());
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 196, as _ZN27QQmlSorterCompositorPrivate16setPrimarySorterEP14QQmlSorterBase
inline void QQmlSorterCompositorPrivate::setPrimarySorter(QQmlSorterBase *sorter)
{
    if (sorter == nullptr ||
        (std::find(m_sorters.constBegin(), m_sorters.constEnd(), sorter) != m_sorters.constEnd())) {
        m_primarySorter = sorter;
        if (m_primarySorter && m_primarySorter->enabled()) {
            m_sfpmModel->setPrimarySortOrder(m_primarySorter->sortOrder());
            m_sfpmModel->setPrimarySortColumn(m_primarySorter->column());
            return;
        }
    }
    resetPrimarySorter();
}

//  from ../qtdeclarative/src/qmlmodels/sfpm/sorters/qqmlsortercompositor.cpp, line 210, as _ZN27QQmlSorterCompositorPrivate18resetPrimarySorterEv
inline void QQmlSorterCompositorPrivate::resetPrimarySorter()
{
    if (!m_primarySorter) {
        if (!m_effectiveSorters.isEmpty()) {
            // Set the primary sort column and its order to the proxy model
            const auto *sorter = m_effectiveSorters.at(0);
            m_sfpmModel->setPrimarySortOrder(sorter->sortOrder());
            m_sfpmModel->setPrimarySortColumn(sorter->column());
        } else {
            // By default reset the  sort order to ascending order and the
            // column to 0
            m_sfpmModel->setPrimarySortOrder(Qt::AscendingOrder);
            m_sfpmModel->setPrimarySortColumn(0);
        }
    }
}
//  -----------------------------------------------------------------------

//  QQmlSorterCompositor *QQmlSorterCompositorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSorterCompositor *ritual_ZN27QQmlSorterCompositorPrivate6q_funcEv(
    QQmlSorterCompositorPrivate *self) {
  return self->q_func();
}

//  const QQmlSorterCompositor *QQmlSorterCompositorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSorterCompositor *ritual_ZNK27QQmlSorterCompositorPrivate6q_funcEv(
    const QQmlSorterCompositorPrivate *self) {
  return self->q_func();
}

//  void QQmlSorterCompositorPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlSorterCompositorPrivate4initEv(
    QQmlSorterCompositorPrivate *self) {
  self->init();
}

//  void QQmlSorterCompositorPrivate::setPrimarySorter(QQmlSorterBase
//      *sorter)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlSorterCompositorPrivate16setPrimarySorterEP14QQmlSorterBase(
    QQmlSorterCompositorPrivate *self,
    QQmlSorterBase *sorter) {
  self->setPrimarySorter(sorter);
}

//  QPointer<QQmlSorterBase> QQmlSorterCompositorPrivate::primarySorter()
//      const
extern "C" Q_DECL_EXPORT
QPointer<QQmlSorterBase> *ritual_ZNK27QQmlSorterCompositorPrivate13primarySorterEv(
    const QQmlSorterCompositorPrivate *self) {
  return new QPointer<QQmlSorterBase>(self->primarySorter());
}

//  void QQmlSorterCompositorPrivate::resetPrimarySorter()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlSorterCompositorPrivate18resetPrimarySorterEv(
    QQmlSorterCompositorPrivate *self) {
  self->resetPrimarySorter();
}

//  a QPointer<QQmlSorterBase> a ritual of QQmlSorterCompositorPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSorterCompositorPrivate__QPointer_QQmlSorterBase(
    QPointer<QQmlSorterBase> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
