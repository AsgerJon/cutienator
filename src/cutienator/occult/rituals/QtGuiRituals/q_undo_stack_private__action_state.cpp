//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qundostack_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(undocommand)
#if QT_CONFIG(undostack)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qundostack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const ActionState &lhs, const ActionState &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN17QUndoStackPrivate11ActionStateES2_(
    const QUndoStackPrivate::ActionState *lhs,
    const QUndoStackPrivate::ActionState *rhs) {
  return operator==(*lhs, *rhs);
}

#if !(defined(__cpp_impl_three_way_comparison))
//  bool operator!=(const ActionState &lhs, const ActionState &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN17QUndoStackPrivate11ActionStateES2_(
    const QUndoStackPrivate::ActionState *lhs,
    const QUndoStackPrivate::ActionState *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(defined(__cpp_impl_three_way_comparison))

//  QUndoStackPrivate::ActionState::~ActionState()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QUndoStackPrivate11ActionStateD1Ev(
    QUndoStackPrivate::ActionState *self) {
  delete self;
}

#endif  // QT_CONFIG(undostack)
#endif  // QT_CONFIG(undocommand)
