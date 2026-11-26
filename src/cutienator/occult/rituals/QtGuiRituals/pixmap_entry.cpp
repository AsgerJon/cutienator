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
#include <QtGui/qicon.h>
#include <QtGui/private/qicon_p.h>
#include <QtGui/qiconengine.h>
#include <QtGui/qiconengineplugin.h>
#include <QtGui/qimagereader.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtGui/private/qiconloader_p.h>
#include <QtGui/qpainter.h>
#include <QtCore/qfileinfo.h>
#if QT_CONFIG(mimetype)
#include <QtCore/qmimedatabase.h>
#include <QtCore/qmimetype.h>
#endif
#include <QtGui/qpixmapcache.h>
#include <QtCore/qvariant.h>
#include <QtCore/qcache.h>
#include <QtCore/qdebug.h>
#include <QtCore/qdir.h>
#include <QtGui/qpalette.h>
#include <QtCore/qmath.h>
#include <QtGui/private/qhexstring_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#ifndef QT_NO_ICON
#include <QtGui/private/qiconloader_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qicon_p.h>
#include <QtGui/QIconEnginePlugin>
#include <QtGui/QPixmapCache>
#include <QtGui/qpa/qplatformtheme.h>
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
#include <QtGui/private/qhexstring_p.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtGui/private/qfonticonengine_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  from src/gui/image/qiconloader.cpp, line 933, as _ZN11PixmapEntry6pixmapERK5QSizeN5QIcon4ModeENS3_5StateEd
#if !defined(QT_NO_ICON)
inline QPixmap PixmapEntry::pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state, qreal scale)
{
    Q_UNUSED(state);

    // Ensure that basePixmap is lazily initialized before generating the
    // key, otherwise the cache key is not unique
    if (basePixmap.isNull())
        basePixmap.load(filename);

    // If the size of the best match we have (basePixmap) is larger than the
    // requested size, we downscale it to match.
    const auto actualSize = QPixmapIconEngine::adjustSize(size * scale, basePixmap.size());
    const auto calculatedDpr = QIconPrivate::pixmapDevicePixelRatio(scale, size, actualSize);
    QString key = "$qt_theme_"_L1
                  % HexString<quint64>(basePixmap.cacheKey())
                  % HexString<quint8>(mode)
                  % HexString<quint64>(QGuiApplication::palette().cacheKey())
                  % HexString<uint>(actualSize.width())
                  % HexString<uint>(actualSize.height())
                  % HexString<quint16>(qRound(calculatedDpr * 1000));

    QPixmap cachedPixmap;
    if (QPixmapCache::find(key, &cachedPixmap)) {
        return cachedPixmap;
    } else {
        if (basePixmap.size() != actualSize)
            cachedPixmap = basePixmap.scaled(actualSize, Qt::IgnoreAspectRatio, Qt::SmoothTransformation);
        else
            cachedPixmap = basePixmap;
        if (QGuiApplication *guiApp = qobject_cast<QGuiApplication *>(qApp))
            cachedPixmap = static_cast<QGuiApplicationPrivate*>(QObjectPrivate::get(guiApp))->applyQIconStyleHelper(mode, cachedPixmap);
        cachedPixmap.setDevicePixelRatio(calculatedDpr);
        QPixmapCache::insert(key, cachedPixmap);
    }
    return cachedPixmap;
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_ICON)
//  QPixmap PixmapEntry::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11PixmapEntry6pixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    PixmapEntry *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->pixmap(*size, mode, state, scale));
}
#endif  // !defined(QT_NO_ICON)

//  PixmapEntry::~PixmapEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN11PixmapEntryD1Ev(PixmapEntry *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)
