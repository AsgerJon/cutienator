//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qvideoframe.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, rituals for functions the generator leaves out: 1. Kept as
//  it is when the generator runs again.
#include <QtMultimedia/qvideoframe.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  QVideoFrame::QVideoFrame()
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameC1Ev() {
  return new QVideoFrame();
}

//  QVideoFrame::QVideoFrame(const QVideoFrameFormat &format)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameC1ERK17QVideoFrameFormat(
    const QVideoFrameFormat *format) {
  return new QVideoFrame(*format);
}

//  QVideoFrame::QVideoFrame(const QImage &image)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameC1ERK6QImage(const QImage *image) {
  return new QVideoFrame(*image);
}

//  QVideoFrame::QVideoFrame(const QVideoFrame &other)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameC1ERKS_(const QVideoFrame *other) {
  return new QVideoFrame(*other);
}

//  QVideoFrame::~QVideoFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrameD1Ev(QVideoFrame *self) {
  delete self;
}

//  QVideoFrame::QVideoFrame(QVideoFrame &&other)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameC1EOS_(QVideoFrame *other) {
  return new QVideoFrame(std::move(*other));
}

//  QVideoFrame &QVideoFrame::operator=(QVideoFrame &&other)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameaSEOS_(
    QVideoFrame *self,
    QVideoFrame *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QVideoFrame::swap(QVideoFrame &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame4swapERS_(QVideoFrame *self, QVideoFrame *other) {
  self->swap(*other);
}

//  QVideoFrame &QVideoFrame::operator=(const QVideoFrame &other)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameaSERKS_(
    QVideoFrame *self,
    const QVideoFrame *other) {
  return &(self->operator=(*other));
}

//  bool QVideoFrame::operator==(const QVideoFrame &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrameeqERKS_(
    const QVideoFrame *self,
    const QVideoFrame *other) {
  return self->operator==(*other);
}

//  bool QVideoFrame::operator!=(const QVideoFrame &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrameneERKS_(
    const QVideoFrame *self,
    const QVideoFrame *other) {
  return self->operator!=(*other);
}

//  bool QVideoFrame::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrame7isValidEv(const QVideoFrame *self) {
  return self->isValid();
}

//  QVideoFrameFormat::PixelFormat QVideoFrame::pixelFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZNK11QVideoFrame11pixelFormatEv(
    const QVideoFrame *self) {
  return self->pixelFormat();
}

//  QVideoFrameFormat QVideoFrame::surfaceFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK11QVideoFrame13surfaceFormatEv(
    const QVideoFrame *self) {
  return new QVideoFrameFormat(self->surfaceFormat());
}

//  QVideoFrame::HandleType QVideoFrame::handleType() const
extern "C" Q_DECL_EXPORT
QVideoFrame::HandleType ritual_ZNK11QVideoFrame10handleTypeEv(
    const QVideoFrame *self) {
  return self->handleType();
}

//  QSize QVideoFrame::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QVideoFrame4sizeEv(const QVideoFrame *self) {
  return new QSize(self->size());
}

//  int QVideoFrame::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QVideoFrame5widthEv(const QVideoFrame *self) {
  return self->width();
}

//  int QVideoFrame::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QVideoFrame6heightEv(const QVideoFrame *self) {
  return self->height();
}

//  bool QVideoFrame::isMapped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrame8isMappedEv(const QVideoFrame *self) {
  return self->isMapped();
}

//  bool QVideoFrame::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrame10isReadableEv(const QVideoFrame *self) {
  return self->isReadable();
}

//  bool QVideoFrame::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrame10isWritableEv(const QVideoFrame *self) {
  return self->isWritable();
}

//  QVideoFrame::MapMode QVideoFrame::mapMode() const
extern "C" Q_DECL_EXPORT
QVideoFrame::MapMode ritual_ZNK11QVideoFrame7mapModeEv(
    const QVideoFrame *self) {
  return self->mapMode();
}

//  bool QVideoFrame::map(QVideoFrame::MapMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QVideoFrame3mapENS_7MapModeE(
    QVideoFrame *self,
    QVideoFrame::MapMode mode) {
  return self->map(mode);
}

//  void QVideoFrame::unmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame5unmapEv(QVideoFrame *self) {
  self->unmap();
}

//  int QVideoFrame::bytesPerLine(int plane) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QVideoFrame12bytesPerLineEi(
    const QVideoFrame *self,
    int plane) {
  return self->bytesPerLine(plane);
}

//  const uchar *QVideoFrame::bits(int plane) const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK11QVideoFrame4bitsEi(
    const QVideoFrame *self,
    int plane) {
  return self->bits(plane);
}

//  int QVideoFrame::mappedBytes(int plane) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QVideoFrame11mappedBytesEi(
    const QVideoFrame *self,
    int plane) {
  return self->mappedBytes(plane);
}

//  int QVideoFrame::planeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QVideoFrame10planeCountEv(const QVideoFrame *self) {
  return self->planeCount();
}

//  qint64 QVideoFrame::startTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QVideoFrame9startTimeEv(const QVideoFrame *self) {
  return self->startTime();
}

//  void QVideoFrame::setStartTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame12setStartTimeEx(QVideoFrame *self, qint64 time) {
  self->setStartTime(time);
}

//  qint64 QVideoFrame::endTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QVideoFrame7endTimeEv(const QVideoFrame *self) {
  return self->endTime();
}

//  void QVideoFrame::setEndTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame10setEndTimeEx(QVideoFrame *self, qint64 time) {
  self->setEndTime(time);
}

#if QT_DEPRECATED_SINCE(6, 7)
//  void QVideoFrame::setRotationAngle(RotationAngle angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame16setRotationAngleENS_13RotationAngleE(
    QVideoFrame *self,
    QVideoFrame::RotationAngle angle) {
  self->setRotationAngle(angle);
}
#endif  // QT_DEPRECATED_SINCE(6, 7)

#if QT_DEPRECATED_SINCE(6, 7)
//  RotationAngle QVideoFrame::rotationAngle() const
extern "C" Q_DECL_EXPORT
QVideoFrame::RotationAngle ritual_ZNK11QVideoFrame13rotationAngleEv(
    const QVideoFrame *self) {
  return self->rotationAngle();
}
#endif  // QT_DEPRECATED_SINCE(6, 7)

//  void QVideoFrame::setRotation(QtVideo::Rotation angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame11setRotationEN7QtVideo8RotationE(
    QVideoFrame *self,
    QtVideo::Rotation angle) {
  self->setRotation(angle);
}

//  QtVideo::Rotation QVideoFrame::rotation() const
extern "C" Q_DECL_EXPORT
QtVideo::Rotation ritual_ZNK11QVideoFrame8rotationEv(
    const QVideoFrame *self) {
  return self->rotation();
}

//  void QVideoFrame::setMirrored(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame11setMirroredEb(QVideoFrame *self, bool a0) {
  self->setMirrored(a0);
}

//  bool QVideoFrame::mirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVideoFrame8mirroredEv(const QVideoFrame *self) {
  return self->mirrored();
}

//  void QVideoFrame::setStreamFrameRate(qreal rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame18setStreamFrameRateEd(
    QVideoFrame *self,
    qreal rate) {
  self->setStreamFrameRate(rate);
}

//  qreal QVideoFrame::streamFrameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QVideoFrame15streamFrameRateEv(const QVideoFrame *self) {
  return self->streamFrameRate();
}

//  QImage QVideoFrame::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK11QVideoFrame7toImageEv(const QVideoFrame *self) {
  return new QImage(self->toImage());
}

//  QString QVideoFrame::subtitleText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QVideoFrame12subtitleTextEv(const QVideoFrame *self) {
  return new QString(self->subtitleText());
}

//  void QVideoFrame::setSubtitleText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame15setSubtitleTextERK7QString(
    QVideoFrame *self,
    const QString *text) {
  self->setSubtitleText(*text);
}

//  void QVideoFrame::paint(QPainter *painter, const QRectF &rect, const
//      PaintOptions &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVideoFrame5paintEP8QPainterRK6QRectFRKNS_12PaintOptionsE(
    QVideoFrame *self,
    QPainter *painter,
    const QRectF *rect,
    const QVideoFrame::PaintOptions *options) {
  self->paint(painter, *rect, *options);
}

#if QT_DEPRECATED_SINCE(6, 8)
//  QVideoFrame::QVideoFrame(QAbstractVideoBuffer *buffer, const
//      QVideoFrameFormat &format)
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN11QVideoFrameC1EP20QAbstractVideoBufferRK17QVideoFrameFormat(
    QAbstractVideoBuffer *buffer,
    const QVideoFrameFormat *format) {
  return new QVideoFrame(buffer, *format);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  QAbstractVideoBuffer *QVideoFrame::videoBuffer() const
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer *ritual_ZNK11QVideoFrame11videoBufferEv(
    const QVideoFrame *self) {
  return self->videoBuffer();
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  uchar *QVideoFrame::bits(int plane)
extern "C" Q_DECL_EXPORT
uchar *ritual_ZN11QVideoFrame4bitsEi(
    QVideoFrame *self,
    int plane) {
  return self->bits(plane);
}
