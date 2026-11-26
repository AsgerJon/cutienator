//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qcameradevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qcameradevice.h>
#include <QtCore/qsize.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QCameraFormat::QCameraFormat()
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_ZN13QCameraFormatC1Ev() {
  return new QCameraFormat();
}

//  QCameraFormat::QCameraFormat(const QCameraFormat &other)
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_ZN13QCameraFormatC1ERKS_(const QCameraFormat *other) {
  return new QCameraFormat(*other);
}

//  QCameraFormat &QCameraFormat::operator=(const QCameraFormat &other)
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_ZN13QCameraFormataSERKS_(
    QCameraFormat *self,
    const QCameraFormat *other) {
  return &(self->operator=(*other));
}

//  QCameraFormat::~QCameraFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCameraFormatD1Ev(QCameraFormat *self) {
  delete self;
}

//  QVideoFrameFormat::PixelFormat QCameraFormat::pixelFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZNK13QCameraFormat11pixelFormatEv(
    const QCameraFormat *self) {
  return self->pixelFormat();
}

//  QSize QCameraFormat::resolution() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QCameraFormat10resolutionEv(const QCameraFormat *self) {
  return new QSize(self->resolution());
}

//  float QCameraFormat::minFrameRate() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QCameraFormat12minFrameRateEv(const QCameraFormat *self) {
  return self->minFrameRate();
}

//  float QCameraFormat::maxFrameRate() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QCameraFormat12maxFrameRateEv(const QCameraFormat *self) {
  return self->maxFrameRate();
}

//  bool QCameraFormat::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraFormat6isNullEv(const QCameraFormat *self) {
  return self->isNull();
}

//  bool QCameraFormat::operator==(const QCameraFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraFormateqERKS_(
    const QCameraFormat *self,
    const QCameraFormat *other) {
  return self->operator==(*other);
}

//  bool QCameraFormat::operator!=(const QCameraFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraFormatneERKS_(
    const QCameraFormat *self,
    const QCameraFormat *other) {
  return self->operator!=(*other);
}

//  QCameraFormat::QCameraFormat(QCameraFormatPrivate *p)
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_ZN13QCameraFormatC1EP20QCameraFormatPrivate(
    QCameraFormatPrivate *p) {
  return new QCameraFormat(p);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCameraFormat &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK13QCameraFormat(
    const QDebug *a0,
    const QCameraFormat *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QCameraFormat>::QList()
extern "C" Q_DECL_EXPORT
QList<QCameraFormat> *ritual_list_make_QCameraFormat() {
  return new QList<QCameraFormat>();
}

//  void QList<QCameraFormat>::append(const QCameraFormat &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCameraFormat(
    QList<QCameraFormat> *self,
    const QCameraFormat *element) {
  self->append(*element);
}

//  qsizetype QList<QCameraFormat>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCameraFormat(const QList<QCameraFormat> *self) {
  return self->size();
}

//  const QCameraFormat &QList<QCameraFormat>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_list_at_QCameraFormat(
    const QList<QCameraFormat> *self,
    long long index) {
  return new QCameraFormat(self->at(index));
}

//  QList<QCameraFormat>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCameraFormat(QList<QCameraFormat> *self) {
  delete self;
}
