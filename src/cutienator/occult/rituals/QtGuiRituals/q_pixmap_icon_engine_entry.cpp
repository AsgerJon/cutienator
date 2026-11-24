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
#include <QtGui/qpixmap.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>

//  QPixmapIconEngineEntry::QPixmapIconEngineEntry()
extern "C" Q_DECL_EXPORT
QPixmapIconEngineEntry *ritual_ZN22QPixmapIconEngineEntryC1Ev() {
  return new QPixmapIconEngineEntry();
}

//  QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QPixmap &pm,
//      QIcon::Mode m, QIcon::State s)
extern "C" Q_DECL_EXPORT
QPixmapIconEngineEntry *ritual_ZN22QPixmapIconEngineEntryC1ERK7QPixmapN5QIcon4ModeENS3_5StateE(
    const QPixmap *pm,
    QIcon::Mode m,
    QIcon::State s) {
  return new QPixmapIconEngineEntry(*pm, m, s);
}

//  QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QString &file, const
//      QSize &sz, QIcon::Mode m, QIcon::State s)
extern "C" Q_DECL_EXPORT
QPixmapIconEngineEntry *ritual_ZN22QPixmapIconEngineEntryC1ERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    const QString *file,
    const QSize *sz,
    QIcon::Mode m,
    QIcon::State s) {
  return new QPixmapIconEngineEntry(*file, *sz, m, s);
}

//  QPixmapIconEngineEntry::QPixmapIconEngineEntry(const QString &file, const
//      QImage &image, QIcon::Mode m, QIcon::State s)
extern "C" Q_DECL_EXPORT
QPixmapIconEngineEntry *ritual_ZN22QPixmapIconEngineEntryC1ERK7QStringRK6QImageN5QIcon4ModeENS6_5StateE(
    const QString *file,
    const QImage *image,
    QIcon::Mode m,
    QIcon::State s) {
  return new QPixmapIconEngineEntry(*file, *image, m, s);
}

//  QPixmapIconEngineEntry::~QPixmapIconEngineEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPixmapIconEngineEntryD1Ev(QPixmapIconEngineEntry *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)
