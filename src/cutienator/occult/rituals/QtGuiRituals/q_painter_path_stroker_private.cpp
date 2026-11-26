//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainterpath_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainterpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/private/qpainterpath_p.h>
#include <QtGui/qbitmap.h>
#include <QtCore/qdebug.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qlist.h>
#include <QtGui/qpen.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qmath.h>
#include <QtGui/private/qbezier_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtGui/private/qpathclipper_p.h>
#include <QtGui/private/qstroker_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <cmath>
#include <limits.h>
#if 0
#include <performance.h>
#else
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpainterpath.cpp, line 2546, as local:qpainterpath.cpp:qt_path_stroke_move_to
inline void qt_path_stroke_move_to(qfixed x, qfixed y, void *data)
{
    ((QPainterPath *) data)->moveTo(qt_fixed_to_real(x), qt_fixed_to_real(y));
}

//  from src/gui/painting/qpainterpath.cpp, line 2551, as local:qpainterpath.cpp:qt_path_stroke_line_to
inline void qt_path_stroke_line_to(qfixed x, qfixed y, void *data)
{
    ((QPainterPath *) data)->lineTo(qt_fixed_to_real(x), qt_fixed_to_real(y));
}

//  from src/gui/painting/qpainterpath.cpp, line 2556, as local:qpainterpath.cpp:qt_path_stroke_cubic_to
inline void qt_path_stroke_cubic_to(qfixed c1x, qfixed c1y,
                             qfixed c2x, qfixed c2y,
                             qfixed ex, qfixed ey,
                             void *data)
{
    ((QPainterPath *) data)->cubicTo(qt_fixed_to_real(c1x), qt_fixed_to_real(c1y),
                                     qt_fixed_to_real(c2x), qt_fixed_to_real(c2y),
                                     qt_fixed_to_real(ex), qt_fixed_to_real(ey));
}

//  from src/gui/painting/qpainterpath.cpp, line 2617, as _ZN26QPainterPathStrokerPrivateC1Ev
inline QPainterPathStrokerPrivate::QPainterPathStrokerPrivate()
    : dashOffset(0)
{
    stroker.setMoveToHook(qt_path_stroke_move_to);
    stroker.setLineToHook(qt_path_stroke_line_to);
    stroker.setCubicToHook(qt_path_stroke_cubic_to);
}
//  -----------------------------------------------------------------------

//  QPainterPathStrokerPrivate::QPainterPathStrokerPrivate()
extern "C" Q_DECL_EXPORT
QPainterPathStrokerPrivate *ritual_ZN26QPainterPathStrokerPrivateC1Ev() {
  return new QPainterPathStrokerPrivate();
}
