//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>
#include <QtCore/private/qproperty_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/QScopeGuard>
#include <QtCore/qalloc.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmutex.h>
#include <QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qproperty.cpp, line 603, as _ZN9QtPrivate22BindingEvaluationStateC1EP23QPropertyBindingPrivateP14QBindingStatus
namespace QtPrivate {
inline BindingEvaluationState::BindingEvaluationState(QPropertyBindingPrivate *binding, QBindingStatus *status)
    : binding(binding)
{
    Q_ASSERT(status);
    QBindingStatus *s = status;
    // store a pointer to the currentBindingEvaluationState to avoid a TLS lookup in
    // the destructor (as these come with a non zero cost)
    currentState = &s->currentlyEvaluatingBinding;
    previousState = *currentState;
    *currentState = this;
    binding->clearDependencyObservers();
}
}  // namespace QtPrivate
//  -----------------------------------------------------------------------

//  QtPrivate::BindingEvaluationState::BindingEvaluationState(QPropertyBindin
//      gPrivate *binding, QBindingStatus *status)
extern "C" Q_DECL_EXPORT
QtPrivate::BindingEvaluationState *ritual_ZN9QtPrivate22BindingEvaluationStateC1EP23QPropertyBindingPrivateP14QBindingStatus(
    QPropertyBindingPrivate *binding,
    QBindingStatus *status) {
  return new QtPrivate::BindingEvaluationState(binding, status);
}

//  QtPrivate::BindingEvaluationState::~BindingEvaluationState()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate22BindingEvaluationStateD1Ev(
    QtPrivate::BindingEvaluationState *self) {
  delete self;
}
