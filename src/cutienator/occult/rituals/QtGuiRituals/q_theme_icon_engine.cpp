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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qiconengine.h>
#include <QtGui/private/qiconengine_p.h>
#include <QtGui/qpainter.h>
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

//  from src/gui/image/qiconengine.cpp, line 316, as _ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE
inline QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->actualSize(size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 371, as _ZN16QProxyIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd
inline QPixmap QProxyIconEngine::scaledPixmap(const QSize &size, QIcon::Mode mode, QIcon::State state, qreal scale)
{
    return proxiedEngine()->scaledPixmap(size, mode, state, scale);
}

//  from src/gui/image/qiconengine.cpp, line 376, as _ZN16QProxyIconEngine12virtual_hookEiPv
inline void QProxyIconEngine::virtual_hook(int id, void *data)
{
    proxiedEngine()->virtual_hook(id, data);
}

//  from src/gui/image/qiconengine.cpp, line 356, as _ZN16QProxyIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE
inline QList<QSize> QProxyIconEngine::availableSizes(QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->availableSizes(mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 311, as _ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE
inline void QProxyIconEngine::paint(QPainter *painter, const QRect &rect, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->paint(painter, rect, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 366, as _ZN16QProxyIconEngine6isNullEv
inline bool QProxyIconEngine::isNull()
{
    return proxiedEngine()->isNull();
}

//  from src/gui/image/qiconengine.cpp, line 321, as _ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE
inline QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->pixmap(size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 331, as _ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE
inline void QProxyIconEngine::addFile(const QString &fileName, const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->addFile(fileName, size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 361, as _ZN16QProxyIconEngine8iconNameEv
inline QString QProxyIconEngine::iconName()
{
    return proxiedEngine()->iconName();
}

//  from src/gui/image/qiconengine.cpp, line 326, as _ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE
inline void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->addPixmap(pixmap, mode, state);
}

//  from src/gui/image/qiconloader.cpp, line 744, as _ZNK16QThemeIconEngine5cloneEv
#if !defined(QT_NO_ICON)
inline QIconEngine *QThemeIconEngine::clone() const
{
    return new QThemeIconEngine(*this);
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

//  QIconEngine *QThemeIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK16QThemeIconEngine5cloneEv(
    const QThemeIconEngine *self) {
  return self->clone();
}

#endif  // !defined(QT_NO_ICON)
