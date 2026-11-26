//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qcursor.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtCore/qlist.h>
#include <QtGui/qpainter.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qvarlengtharray.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/private/qsplitter_p.h>
#include <QtCore/qdebug.h>
#include <ctype.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qsplitter.cpp, line 327, as _ZN21QSplitterLayoutStruct13getWidgetSizeEN2Qt11OrientationE
inline int QSplitterLayoutStruct::getWidgetSize(Qt::Orientation orient)
{
    if (sizer == -1) {
        QSize s = widget->sizeHint();
        const int presizer = pick(s, orient);
        const int realsize = pick(widget->size(), orient);
        if (!s.isValid() || (widget->testAttribute(Qt::WA_Resized) && (realsize > presizer))) {
            sizer = pick(widget->size(), orient);
        } else {
            sizer = presizer;
        }
        QSizePolicy p = widget->sizePolicy();
        int sf = (orient == Qt::Horizontal) ? p.horizontalStretch() : p.verticalStretch();
        if (sf > 1)
            sizer *= sf;
    }
    return sizer;
}

//  from src/widgets/widgets/qsplitter.cpp, line 346, as _ZN21QSplitterLayoutStruct13getHandleSizeEN2Qt11OrientationE
inline int QSplitterLayoutStruct::getHandleSize(Qt::Orientation orient)
{
    return pick(handle->sizeHint(), orient);
}
//  -----------------------------------------------------------------------

//  QSplitterLayoutStruct::QSplitterLayoutStruct()
extern "C" Q_DECL_EXPORT
QSplitterLayoutStruct *ritual_ZN21QSplitterLayoutStructC1Ev() {
  return new QSplitterLayoutStruct();
}

//  QSplitterLayoutStruct::~QSplitterLayoutStruct()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSplitterLayoutStructD1Ev(QSplitterLayoutStruct *self) {
  delete self;
}

//  int QSplitterLayoutStruct::getWidgetSize(Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSplitterLayoutStruct13getWidgetSizeEN2Qt11OrientationE(
    QSplitterLayoutStruct *self,
    Qt::Orientation orient) {
  return self->getWidgetSize(orient);
}

//  int QSplitterLayoutStruct::getHandleSize(Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSplitterLayoutStruct13getHandleSizeEN2Qt11OrientationE(
    QSplitterLayoutStruct *self,
    Qt::Orientation orient) {
  return self->getHandleSize(orient);
}

//  int QSplitterLayoutStruct::pick(const QSize &size, Qt::Orientation
//      orient)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSplitterLayoutStruct4pickERK5QSizeN2Qt11OrientationE(
    QSplitterLayoutStruct *self,
    const QSize *size,
    Qt::Orientation orient) {
  return self->pick(*size, orient);
}

#endif  // QT_CONFIG(splitter)
#endif  // QT_CONFIG(splitter)
