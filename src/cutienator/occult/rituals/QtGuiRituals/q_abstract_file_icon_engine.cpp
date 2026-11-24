//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qabstractfileiconengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qabstractfileiconengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qstring.h>

//  Only a class built on QAbstractFileIconEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractFileIconEngine : QAbstractFileIconEngine {
  using QAbstractFileIconEngine::cacheKey;
};

//  QPixmap QAbstractFileIconEngine::pixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State a2)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN23QAbstractFileIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State a2) {
  return new QPixmap(self->pixmap(*size, mode, a2));
}

//  QPixmap QAbstractFileIconEngine::scaledPixmap(const QSize &size,
//      QIcon::Mode mode, QIcon::State a2, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN23QAbstractFileIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State a2,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, a2, scale));
}

//  QSize QAbstractFileIconEngine::actualSize(const QSize &size, QIcon::Mode
//      mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN23QAbstractFileIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  bool QAbstractFileIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QAbstractFileIconEngine6isNullEv(
    QAbstractFileIconEngine *self) {
  return self->isNull();
}

//  QFileInfo QAbstractFileIconEngine::fileInfo() const
extern "C" Q_DECL_EXPORT
QFileInfo *ritual_ZNK23QAbstractFileIconEngine8fileInfoEv(
    const QAbstractFileIconEngine *self) {
  return new QFileInfo(self->fileInfo());
}

//  QPlatformTheme::IconOptions QAbstractFileIconEngine::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QAbstractFileIconEngine7optionsEv(
    const QAbstractFileIconEngine *self) {
  return static_cast<int>(self->options().toInt());
}

//  QPixmap QAbstractFileIconEngine::filePixmap(const QSize &size,
//      QIcon::Mode mode, QIcon::State a2)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN23QAbstractFileIconEngine10filePixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State a2) {
  return new QPixmap(self->filePixmap(*size, mode, a2));
}

//  QString QAbstractFileIconEngine::cacheKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QAbstractFileIconEngine8cacheKeyEv(
    const QAbstractFileIconEngine *self) {
  return new QString(self->cacheKey());
}

//  QPixmap QAbstractFileIconEngine::pixmap(const QSize &size, QIcon::Mode
//      mode, QIcon::State a2)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN23QAbstractFileIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State a2) {
  return new QPixmap(self->QAbstractFileIconEngine::pixmap(*size, mode, a2));
}

//  QPixmap QAbstractFileIconEngine::scaledPixmap(const QSize &size,
//      QIcon::Mode mode, QIcon::State a2, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZN23QAbstractFileIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State a2,
    qreal scale) {
  return new QPixmap(
      self->QAbstractFileIconEngine::scaledPixmap(
          *size,
          mode,
          a2,
          scale));
}

//  QSize QAbstractFileIconEngine::actualSize(const QSize &size, QIcon::Mode
//      mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN23QAbstractFileIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QAbstractFileIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(
      self->QAbstractFileIconEngine::actualSize(
          *size,
          mode,
          state));
}

//  bool QAbstractFileIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QAbstractFileIconEngine6isNullEv(
    QAbstractFileIconEngine *self) {
  return self->QAbstractFileIconEngine::isNull();
}

//  QString QAbstractFileIconEngine::cacheKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QAbstractFileIconEngine8cacheKeyEv(
    const QAbstractFileIconEngine *self) {
  return new QString(
      static_cast<const OwnQAbstractFileIconEngine *>(self)->OwnQAbstractFileIconEngine::cacheKey());
}
