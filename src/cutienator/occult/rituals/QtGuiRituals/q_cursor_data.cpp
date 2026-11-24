//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcursor_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcursor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcursor.h>
#include <QtCore/qcoreapplication.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qimage.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qvariant.h>
#include <QtGui/private/qcursor_p.h>
#include <QtCore/qdebug.h>
#include <QtGui/qpa/qplatformcursor.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/kernel/qcursor.cpp, line 663, as _ZN11QCursorDataC1EN2Qt11CursorShapeE
#if !defined(QT_NO_CURSOR)
inline QCursorData::QCursorData(Qt::CursorShape s)
    : ref(1), cshape(s), bm(nullptr), bmm(nullptr), hx(0), hy(0)
{
}
#endif  // !defined(QT_NO_CURSOR)

//  from src/gui/kernel/qcursor.cpp, line 668, as _ZN11QCursorDataD1Ev
#if !defined(QT_NO_CURSOR)
inline QCursorData::~QCursorData()
{
    delete bm;
    delete bmm;
}
#endif  // !defined(QT_NO_CURSOR)

//  from src/gui/kernel/qcursor.cpp, line 718, as _ZN11QCursorData6updateEv
#if !defined(QT_NO_CURSOR)
inline void QCursorData::update()
{
}
#endif  // !defined(QT_NO_CURSOR)
//  -----------------------------------------------------------------------

//  QCursorData::QCursorData(Qt::CursorShape s)
extern "C" Q_DECL_EXPORT
QCursorData *ritual_ZN11QCursorDataC1EN2Qt11CursorShapeE(Qt::CursorShape s) {
  return new QCursorData(s);
}

//  QCursorData::~QCursorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCursorDataD1Ev(QCursorData *self) {
  delete self;
}

#if !defined(QT_NO_CURSOR)
//  void QCursorData::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCursorData6updateEv(QCursorData *self) {
  self->update();
}
#endif  // !defined(QT_NO_CURSOR)
