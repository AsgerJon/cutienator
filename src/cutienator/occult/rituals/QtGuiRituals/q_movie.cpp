//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qmovie.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qmovie.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QMovie::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QMovie10metaObjectEv(const QMovie *self) {
  return self->metaObject();
}

//  QString QMovie::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QMovie2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QMovie::tr(s, c, n));
}

//  QMovie::QMovie(QObject *parent)
extern "C" Q_DECL_EXPORT
QMovie *ritual_ZN6QMovieC1EP7QObject(QObject *parent) {
  return new QMovie(parent);
}

//  QMovie::QMovie(QIODevice *device, const QByteArray &format, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QMovie *ritual_ZN6QMovieC1EP9QIODeviceRK10QByteArrayP7QObject(
    QIODevice *device,
    const QByteArray *format,
    QObject *parent) {
  return new QMovie(device, *format, parent);
}

//  QMovie::QMovie(const QString &fileName, const QByteArray &format, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QMovie *ritual_ZN6QMovieC1ERK7QStringRK10QByteArrayP7QObject(
    const QString *fileName,
    const QByteArray *format,
    QObject *parent) {
  return new QMovie(*fileName, *format, parent);
}

//  QMovie::~QMovie()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovieD1Ev(QMovie *self) {
  delete self;
}

//  void QMovie::setDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie9setDeviceEP9QIODevice(
    QMovie *self,
    QIODevice *device) {
  self->setDevice(device);
}

//  QIODevice *QMovie::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK6QMovie6deviceEv(const QMovie *self) {
  return self->device();
}

//  void QMovie::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie11setFileNameERK7QString(
    QMovie *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QMovie::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QMovie8fileNameEv(const QMovie *self) {
  return new QString(self->fileName());
}

//  void QMovie::setFormat(const QByteArray &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie9setFormatERK10QByteArray(
    QMovie *self,
    const QByteArray *format) {
  self->setFormat(*format);
}

//  QByteArray QMovie::format() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK6QMovie6formatEv(const QMovie *self) {
  return new QByteArray(self->format());
}

//  void QMovie::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie18setBackgroundColorERK6QColor(
    QMovie *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  QColor QMovie::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QMovie15backgroundColorEv(const QMovie *self) {
  return new QColor(self->backgroundColor());
}

//  MovieState QMovie::state() const
extern "C" Q_DECL_EXPORT
QMovie::MovieState ritual_ZNK6QMovie5stateEv(const QMovie *self) {
  return self->state();
}

//  QRect QMovie::frameRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QMovie9frameRectEv(const QMovie *self) {
  return new QRect(self->frameRect());
}

//  QImage QMovie::currentImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QMovie12currentImageEv(const QMovie *self) {
  return new QImage(self->currentImage());
}

//  QPixmap QMovie::currentPixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QMovie13currentPixmapEv(const QMovie *self) {
  return new QPixmap(self->currentPixmap());
}

//  bool QMovie::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QMovie7isValidEv(const QMovie *self) {
  return self->isValid();
}

//  QImageReader::ImageReaderError QMovie::lastError() const
extern "C" Q_DECL_EXPORT
QImageReader::ImageReaderError ritual_ZNK6QMovie9lastErrorEv(
    const QMovie *self) {
  return self->lastError();
}

//  QString QMovie::lastErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QMovie15lastErrorStringEv(const QMovie *self) {
  return new QString(self->lastErrorString());
}

//  bool QMovie::jumpToFrame(int frameNumber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMovie11jumpToFrameEi(QMovie *self, int frameNumber) {
  return self->jumpToFrame(frameNumber);
}

//  int QMovie::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QMovie9loopCountEv(const QMovie *self) {
  return self->loopCount();
}

//  int QMovie::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QMovie10frameCountEv(const QMovie *self) {
  return self->frameCount();
}

//  int QMovie::nextFrameDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QMovie14nextFrameDelayEv(const QMovie *self) {
  return self->nextFrameDelay();
}

//  int QMovie::currentFrameNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QMovie18currentFrameNumberEv(const QMovie *self) {
  return self->currentFrameNumber();
}

//  int QMovie::speed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QMovie5speedEv(const QMovie *self) {
  return self->speed();
}

//  QSize QMovie::scaledSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN6QMovie10scaledSizeEv(QMovie *self) {
  return new QSize(self->scaledSize());
}

//  void QMovie::setScaledSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie13setScaledSizeERK5QSize(
    QMovie *self,
    const QSize *size) {
  self->setScaledSize(*size);
}

//  CacheMode QMovie::cacheMode() const
extern "C" Q_DECL_EXPORT
QMovie::CacheMode ritual_ZNK6QMovie9cacheModeEv(const QMovie *self) {
  return self->cacheMode();
}

//  void QMovie::setCacheMode(CacheMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie12setCacheModeENS_9CacheModeE(
    QMovie *self,
    QMovie::CacheMode mode) {
  self->setCacheMode(mode);
}

//  void QMovie::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie5startEv(QMovie *self) {
  self->start();
}

//  bool QMovie::jumpToNextFrame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMovie15jumpToNextFrameEv(QMovie *self) {
  return self->jumpToNextFrame();
}

//  void QMovie::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie9setPausedEb(QMovie *self, bool paused) {
  self->setPaused(paused);
}

//  void QMovie::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie4stopEv(QMovie *self) {
  self->stop();
}

//  void QMovie::setSpeed(int percentSpeed)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMovie8setSpeedEi(QMovie *self, int percentSpeed) {
  self->setSpeed(percentSpeed);
}
