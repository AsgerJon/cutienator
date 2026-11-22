//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qiconengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qiconengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qstring.h>

//  QIconEngine::~QIconEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngineD1Ev(QIconEngine *self) {
  delete self;
}

//  void QIconEngine::paint(QPainter *painter, const QRect &rect, QIcon::Mode
//      mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5StateE(
    QIconEngine *self,
    QPainter *painter,
    const QRect *rect,
    QIcon::Mode mode,
    QIcon::State state) {
  self->paint(painter, *rect, mode, state);
}

//  QSize QIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QSize(self->actualSize(*size, mode, state));
}

//  QPixmap QIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  return new QPixmap(self->pixmap(*size, mode, state));
}

//  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
//      QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE(
    QIconEngine *self,
    const QPixmap *pixmap,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addPixmap(*pixmap, mode, state);
}

//  void QIconEngine::addFile(const QString &fileName, const QSize &size,
//      QIcon::Mode mode, QIcon::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5StateE(
    QIconEngine *self,
    const QString *fileName,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state) {
  self->addFile(*fileName, *size, mode, state);
}

//  QString QIconEngine::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QIconEngine3keyEv(const QIconEngine *self) {
  return new QString(self->key());
}

//  QIconEngine *QIconEngine::clone() const
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZNK11QIconEngine5cloneEv(const QIconEngine *self) {
  return self->clone();
}

//  QString QIconEngine::iconName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QIconEngine8iconNameEv(QIconEngine *self) {
  return new QString(self->iconName());
}

//  bool QIconEngine::isNull()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QIconEngine6isNullEv(QIconEngine *self) {
  return self->isNull();
}

//  QPixmap QIconEngine::scaledPixmap(const QSize &size, QIcon::Mode mode,
//      QIcon::State state, qreal scale)
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateEd(
    QIconEngine *self,
    const QSize *size,
    QIcon::Mode mode,
    QIcon::State state,
    qreal scale) {
  return new QPixmap(self->scaledPixmap(*size, mode, state, scale));
}
