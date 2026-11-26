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
#include <QtCore/qstring.h>
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

using namespace Qt::StringLiterals;

//  from src/gui/image/qiconengine.cpp, line 311, as _ZN16QProxyIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE
inline void QProxyIconEngine::paint(QPainter *painter, const QRect &rect, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->paint(painter, rect, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 316, as _ZN16QProxyIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE
inline QSize QProxyIconEngine::actualSize(const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->actualSize(size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 321, as _ZN16QProxyIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE
inline QPixmap QProxyIconEngine::pixmap(const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->pixmap(size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 326, as _ZN16QProxyIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE
inline void QProxyIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->addPixmap(pixmap, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 331, as _ZN16QProxyIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE
inline void QProxyIconEngine::addFile(const QString &fileName, const QSize &size, QIcon::Mode mode, QIcon::State state)
{
    proxiedEngine()->addFile(fileName, size, mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 336, as _ZNK16QProxyIconEngine3keyEv
inline QString QProxyIconEngine::key() const
{
    return proxiedEngine()->key();
}

//  from src/gui/image/qiconengine.cpp, line 341, as _ZNK16QProxyIconEngine5cloneEv
inline QIconEngine *QProxyIconEngine::clone() const
{
    return proxiedEngine()->clone();
}

//  from src/gui/image/qiconengine.cpp, line 346, as _ZN16QProxyIconEngine4readER11QDataStream
inline bool QProxyIconEngine::read(QDataStream &in)
{
    return proxiedEngine()->read(in);
}

//  from src/gui/image/qiconengine.cpp, line 351, as _ZNK16QProxyIconEngine5writeER11QDataStream
inline bool QProxyIconEngine::write(QDataStream &out) const
{
    return proxiedEngine()->write(out);
}

//  from src/gui/image/qiconengine.cpp, line 356, as _ZN16QProxyIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE
inline QList<QSize> QProxyIconEngine::availableSizes(QIcon::Mode mode, QIcon::State state)
{
    return proxiedEngine()->availableSizes(mode, state);
}

//  from src/gui/image/qiconengine.cpp, line 361, as _ZN16QProxyIconEngine8iconNameEv
inline QString QProxyIconEngine::iconName()
{
    return proxiedEngine()->iconName();
}

//  from src/gui/image/qiconengine.cpp, line 366, as _ZN16QProxyIconEngine6isNullEv
inline bool QProxyIconEngine::isNull()
{
    return proxiedEngine()->isNull();
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

//  from src/gui/image/qiconloader.cpp, line 744, as _ZNK16QThemeIconEngine5cloneEv
#if !defined(QT_NO_ICON)
inline QIconEngine *QThemeIconEngine::clone() const
{
    return new QThemeIconEngine(*this);
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 749, as _ZN16QThemeIconEngine4readER11QDataStream
#if !defined(QT_NO_ICON)
inline bool QThemeIconEngine::read(QDataStream &in) {
    in >> m_iconName;
    return true;
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 754, as _ZNK16QThemeIconEngine5writeER11QDataStream
#if !defined(QT_NO_ICON)
inline bool QThemeIconEngine::write(QDataStream &out) const
{
    out << m_iconName;
    return true;
}
#endif  // !defined(QT_NO_ICON)

//  from src/gui/image/qiconloader.cpp, line 736, as _ZNK16QThemeIconEngine3keyEv
#if !defined(QT_NO_ICON)
inline QString QThemeIconEngine::key() const
{
    // Although we proxy the underlying engine, that's an implementation
    // detail, so from the point of view of QIcon, and in terms of
    // serialization, we are the one and only theme icon engine.
    return u"QThemeIconEngine"_s;
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

//  QIconEngine *QThemeIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK16QThemeIconEngine5cloneEv(
    const QThemeIconEngine *self) {
  return self->clone();
}

//  bool QThemeIconEngine::read(QDataStream &in)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QThemeIconEngine4readER11QDataStream(
    QThemeIconEngine *self,
    QDataStream *in) {
  return self->read(*in);
}

//  bool QThemeIconEngine::write(QDataStream &out) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QThemeIconEngine5writeER11QDataStream(
    const QThemeIconEngine *self,
    QDataStream *out) {
  return self->write(*out);
}

//  QIconEngine *QThemeIconEngine::proxiedEngine() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK16QThemeIconEngine13proxiedEngineEv(
    const QThemeIconEngine *self) {
  return self->proxiedEngine();
}

//  QString QThemeIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QThemeIconEngine3keyEv(const QThemeIconEngine *self) {
  return new QString(self->key());
}

#if !defined(QT_NO_ICON)
//  QString QThemeIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK16QThemeIconEngine3keyEv(
    const QThemeIconEngine *self) {
  return new QString(self->QThemeIconEngine::key());
}
#endif  // !defined(QT_NO_ICON)

#endif  // !defined(QT_NO_ICON)
