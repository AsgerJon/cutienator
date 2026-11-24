//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef QT_NO_ICON
#include <private/qiconloader_p.h>
#include <private/qguiapplication_p.h>
#include <private/qicon_p.h>
#include <QtGui/QIconEnginePlugin>
#include <QtGui/QPixmapCache>
#include <qpa/qplatformtheme.h>
#include <QtGui/qfontdatabase.h>
#include <QtGui/QPalette>
#include <QtCore/qmath.h>
#include <QtCore/QList>
#include <QtCore/QDir>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(settings)
#include <QtCore/QSettings>
#endif
#include <QtGui/QPainter>
#include <private/qhexstring_p.h>
#include <private/qfactoryloader_p.h>
#include <private/qfonticonengine_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qiconloader.cpp, line 970, as _ZN13ScalableEntry6pixmapERK5QSizeN5QIcon4ModeENS3_5StateEd
#if !defined(QT_NO_ICON)
inline QPixmap ScalableEntry::pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state, qreal scale)
{
    if (svgIcon.isNull())
        svgIcon = QIcon(filename);

    return svgIcon.pixmap(size, scale, mode, state);
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_ICON)
//  QPixmap ScalableEntry::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN13ScalableEntry6pixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    ScalableEntry *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->pixmap(*size, mode, state, scale));
}
#endif  // !defined(QT_NO_ICON)

//  ScalableEntry::~ScalableEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13ScalableEntryD1Ev(ScalableEntry *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)
