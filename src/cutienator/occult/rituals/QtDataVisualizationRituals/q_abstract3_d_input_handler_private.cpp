//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qabstract3dinputhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3dinputhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstract3dinputhandler_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/input/qabstract3dinputhandler.cpp, line 220, as _ZN30QAbstract3DInputHandlerPrivateC1EP23QAbstract3DInputHandler
inline QAbstract3DInputHandlerPrivate::QAbstract3DInputHandlerPrivate(QAbstract3DInputHandler *q) :
    q_ptr(q),
    m_prevDistance(0),
    m_previousInputPos(QPoint(0,0)),
    m_inputView(QAbstract3DInputHandler::InputViewNone),
    m_inputPosition(QPoint(0,0)),
    m_scene(0),
    m_isDefaultHandler(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/input/qabstract3dinputhandler.cpp, line 231, as _ZN30QAbstract3DInputHandlerPrivateD1Ev
inline QAbstract3DInputHandlerPrivate::~QAbstract3DInputHandlerPrivate()
{

}
//  -----------------------------------------------------------------------

//  QAbstract3DInputHandlerPrivate::QAbstract3DInputHandlerPrivate(QAbstract3
//      DInputHandler *q)
extern "C" Q_DECL_EXPORT
QAbstract3DInputHandlerPrivate *ritual_ZN30QAbstract3DInputHandlerPrivateC1EP23QAbstract3DInputHandler(
    QAbstract3DInputHandler *q) {
  return new QAbstract3DInputHandlerPrivate(q);
}

//  QAbstract3DInputHandlerPrivate::~QAbstract3DInputHandlerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QAbstract3DInputHandlerPrivateD1Ev(
    QAbstract3DInputHandlerPrivate *self) {
  delete self;
}
