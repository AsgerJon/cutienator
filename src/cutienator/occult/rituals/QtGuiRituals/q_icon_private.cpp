//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qicon_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qicon.h"
#include "qicon_p.h"
#include "qiconengine.h"
#include "qiconengineplugin.h"
#include "qimagereader.h"
#include "private/qfactoryloader_p.h"
#include "private/qiconloader_p.h"
#include "qpainter.h"
#include "qfileinfo.h"
#if QT_CONFIG(mimetype)
#include <qmimedatabase.h>
#include <qmimetype.h>
#endif
#include "qpixmapcache.h"
#include "qvariant.h"
#include "qcache.h"
#include "qdebug.h"
#include "qdir.h"
#include "qpalette.h"
#include "qmath.h"
#include "private/qhexstring_p.h"
#include "private/qguiapplication_p.h"
#include "private/qoffsetstringarray_p.h"
#include "qpa/qplatformtheme.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qicon.cpp, line 156, as _ZN12QIconPrivate22pixmapDevicePixelRatioEdRK5QSizeS2_
#if !defined(QT_NO_ICON)
inline qreal QIconPrivate::pixmapDevicePixelRatio(qreal displayDevicePixelRatio, const QSize &requestedSize, const QSize &actualSize)
{
    QSize targetSize = requestedSize * displayDevicePixelRatio;
    if ((actualSize.width() == targetSize.width() && actualSize.height() <= targetSize.height()) ||
        (actualSize.width() <= targetSize.width() && actualSize.height() == targetSize.height())) {
        // Correctly scaled for dpr, just having different aspect ratio
        return displayDevicePixelRatio;
    }
    qreal scale = 0.5 * (qreal(actualSize.width()) / qreal(targetSize.width()) +
                         qreal(actualSize.height()) / qreal(targetSize.height()));
    qreal dpr = qMax(qreal(1.0), displayDevicePixelRatio * scale);
    return qRound(dpr * 100) / 100.0;
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

//  QIconPrivate::~QIconPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIconPrivateD1Ev(QIconPrivate *self) {
  delete self;
}

//  QIconPrivate *QIconPrivate::get(QIcon *icon)
extern "C" Q_DECL_EXPORT
QIconPrivate *ritual_ZN12QIconPrivate3getEP5QIcon(QIcon *icon) {
  return QIconPrivate::get(icon);
}

//  const QIconPrivate *QIconPrivate::get(const QIcon *icon)
extern "C" Q_DECL_EXPORT
const QIconPrivate *ritual_ZN12QIconPrivate3getEPK5QIcon(const QIcon *icon) {
  return QIconPrivate::get(icon);
}

#if !defined(QT_NO_ICON)
//  qreal QIconPrivate::pixmapDevicePixelRatio(qreal displayDevicePixelRatio,
//      const QSize &requestedSize, const QSize &actualSize)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN12QIconPrivate22pixmapDevicePixelRatioEdRK5QSizeS2_(
    qreal displayDevicePixelRatio,
    const QSize *requestedSize,
    const QSize *actualSize) {
  return QIconPrivate::pixmapDevicePixelRatio(
      displayDevicePixelRatio,
      *requestedSize,
      *actualSize);
}
#endif  // !defined(QT_NO_ICON)

#endif  // !defined(QT_NO_ICON)
