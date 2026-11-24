//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qundostack_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(undocommand)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qundostack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QUndoCommandPrivate::QUndoCommandPrivate()
extern "C" Q_DECL_EXPORT
QUndoCommandPrivate *ritual_ZN19QUndoCommandPrivateC1Ev() {
  return new QUndoCommandPrivate();
}

//  QUndoCommandPrivate::~QUndoCommandPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QUndoCommandPrivateD1Ev(QUndoCommandPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(undocommand)
