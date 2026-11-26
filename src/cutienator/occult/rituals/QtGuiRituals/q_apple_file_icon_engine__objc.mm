//  Written by hand on 2026-11-26 from
//  QtGui/6.12.0/QtGui/private/qapplefileiconengine_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again.
//  Objective-C++: the class holds an Objective-C object ('nil'), so only a
//  compiler of Objective-C++ on Apple's systems reads the header; 'summon'
//  builds this file there only. Qt's library offers the class, and the
//  rituals call it.
#include <QtGui/qtguiglobal.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qapplefileiconengine_p.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/qpixmap.h>

//  QAppleFileIconEngine::QAppleFileIconEngine(const QFileInfo &info,
//      QPlatformTheme::IconOptions opts)
extern "C" Q_DECL_EXPORT
QAppleFileIconEngine *ritual_ZN20QAppleFileIconEngineC1ERK9QFileInfo6QFlagsIN14QPlatformTheme10IconOptionEE(
    const QFileInfo *info,
    int opts) {
  return new QAppleFileIconEngine(
      *info, QPlatformTheme::IconOptions::fromInt(opts));
}

//  QAppleFileIconEngine::~QAppleFileIconEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAppleFileIconEngineD1Ev(
    QAppleFileIconEngine *self) {
  delete self;
}

//  bool QAppleFileIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAppleFileIconEngine6isNullEv(
    QAppleFileIconEngine *self) {
  return self->isNull();
}

//  QList<QSize> QAppleFileIconEngine::availableSizes(QIcon::Mode a0,
//      QIcon::State a1)
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZN20QAppleFileIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE(
    QAppleFileIconEngine *self,
    int a0,
    int a1) {
  return new QList<QSize>(self->availableSizes(
      static_cast<QIcon::Mode>(a0), static_cast<QIcon::State>(a1)));
}

//  QPixmap QAppleFileIconEngine::filePixmap(const QSize &size, QIcon::Mode
//      a1, QIcon::State a2)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN20QAppleFileIconEngine10filePixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAppleFileIconEngine *self,
    const QSize *size,
    int a1,
    int a2) {
  return new QPixmap(self->filePixmap(
      *size, static_cast<QIcon::Mode>(a1), static_cast<QIcon::State>(a2)));
}

#endif
