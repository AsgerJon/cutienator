//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qscxmlglobals_p.h"
#include "qscxmlexecutablecontent_p.h"
#include "qscxmlcompiler_p.h"
#include "qscxmlevent_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlexecutablecontent.cpp, line 238, as _ZN21QScxmlExecutionEngineC1EP18QScxmlStateMachine
#if !defined(BUILD_QSCXMLC)
inline QScxmlExecutionEngine::QScxmlExecutionEngine(QScxmlStateMachine *stateMachine)
    : stateMachine(stateMachine)
{
    Q_ASSERT(stateMachine);
}
#endif  // !defined(BUILD_QSCXMLC)
//  -----------------------------------------------------------------------

//  QScxmlExecutionEngine::QScxmlExecutionEngine(QScxmlStateMachine
//      *stateMachine)
extern "C" Q_DECL_EXPORT
QScxmlExecutionEngine *ritual_ZN21QScxmlExecutionEngineC1EP18QScxmlStateMachine(
    QScxmlStateMachine *stateMachine) {
  return new QScxmlExecutionEngine(stateMachine);
}
