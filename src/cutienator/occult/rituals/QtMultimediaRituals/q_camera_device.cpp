//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qcameradevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qcameradevice.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>

//  QCameraDevice::QCameraDevice()
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_ZN13QCameraDeviceC1Ev() {
  return new QCameraDevice();
}

//  QCameraDevice::QCameraDevice(const QCameraDevice &other)
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_ZN13QCameraDeviceC1ERKS_(const QCameraDevice *other) {
  return new QCameraDevice(*other);
}

//  QCameraDevice::~QCameraDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCameraDeviceD1Ev(QCameraDevice *self) {
  delete self;
}

//  bool QCameraDevice::operator==(const QCameraDevice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraDeviceeqERKS_(
    const QCameraDevice *self,
    const QCameraDevice *other) {
  return self->operator==(*other);
}

//  bool QCameraDevice::operator!=(const QCameraDevice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraDeviceneERKS_(
    const QCameraDevice *self,
    const QCameraDevice *other) {
  return self->operator!=(*other);
}

//  bool QCameraDevice::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraDevice6isNullEv(const QCameraDevice *self) {
  return self->isNull();
}

//  QByteArray QCameraDevice::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QCameraDevice2idEv(const QCameraDevice *self) {
  return new QByteArray(self->id());
}

//  QString QCameraDevice::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCameraDevice11descriptionEv(
    const QCameraDevice *self) {
  return new QString(self->description());
}

//  bool QCameraDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCameraDevice9isDefaultEv(const QCameraDevice *self) {
  return self->isDefault();
}

//  Position QCameraDevice::position() const
extern "C" Q_DECL_EXPORT
QCameraDevice::Position ritual_ZNK13QCameraDevice8positionEv(
    const QCameraDevice *self) {
  return self->position();
}

//  QList<QSize> QCameraDevice::photoResolutions() const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK13QCameraDevice16photoResolutionsEv(
    const QCameraDevice *self) {
  return new QList<QSize>(self->photoResolutions());
}

//  QList<QCameraFormat> QCameraDevice::videoFormats() const
extern "C" Q_DECL_EXPORT
QList<QCameraFormat> *ritual_ZNK13QCameraDevice12videoFormatsEv(
    const QCameraDevice *self) {
  return new QList<QCameraFormat>(self->videoFormats());
}

//  QtVideo::Rotation QCameraDevice::correctionAngle() const
extern "C" Q_DECL_EXPORT
QtVideo::Rotation ritual_ZNK13QCameraDevice15correctionAngleEv(
    const QCameraDevice *self) {
  return self->correctionAngle();
}

//  QCameraDevice::QCameraDevice(QCameraDevicePrivate *p)
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_ZN13QCameraDeviceC1EP20QCameraDevicePrivate(
    QCameraDevicePrivate *p) {
  return new QCameraDevice(p);
}

//  QList<QCameraDevice>::QList()
extern "C" Q_DECL_EXPORT
QList<QCameraDevice> *ritual_list_make_QCameraDevice() {
  return new QList<QCameraDevice>();
}

//  void QList<QCameraDevice>::append(const QCameraDevice &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCameraDevice(
    QList<QCameraDevice> *self,
    const QCameraDevice *element) {
  self->append(*element);
}

//  qsizetype QList<QCameraDevice>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCameraDevice(const QList<QCameraDevice> *self) {
  return self->size();
}

//  const QCameraDevice &QList<QCameraDevice>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_list_at_QCameraDevice(
    const QList<QCameraDevice> *self,
    long long index) {
  return new QCameraDevice(self->at(index));
}

//  QList<QCameraDevice>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCameraDevice(QList<QCameraDevice> *self) {
  delete self;
}
