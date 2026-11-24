//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiodevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qlist.h>

//  QAudioDevice::QAudioDevice()
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN12QAudioDeviceC1Ev() {
  return new QAudioDevice();
}

//  QAudioDevice::QAudioDevice(const QAudioDevice &other)
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN12QAudioDeviceC1ERKS_(const QAudioDevice *other) {
  return new QAudioDevice(*other);
}

//  QAudioDevice::~QAudioDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioDeviceD1Ev(QAudioDevice *self) {
  delete self;
}

//  bool QAudioDevice::operator==(const QAudioDevice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioDeviceeqERKS_(
    const QAudioDevice *self,
    const QAudioDevice *other) {
  return self->operator==(*other);
}

//  bool QAudioDevice::operator!=(const QAudioDevice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioDeviceneERKS_(
    const QAudioDevice *self,
    const QAudioDevice *other) {
  return self->operator!=(*other);
}

//  bool QAudioDevice::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioDevice6isNullEv(const QAudioDevice *self) {
  return self->isNull();
}

//  QByteArray QAudioDevice::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QAudioDevice2idEv(const QAudioDevice *self) {
  return new QByteArray(self->id());
}

//  QString QAudioDevice::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QAudioDevice11descriptionEv(const QAudioDevice *self) {
  return new QString(self->description());
}

//  bool QAudioDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioDevice9isDefaultEv(const QAudioDevice *self) {
  return self->isDefault();
}

//  QAudioDevice::Mode QAudioDevice::mode() const
extern "C" Q_DECL_EXPORT
QAudioDevice::Mode ritual_ZNK12QAudioDevice4modeEv(
    const QAudioDevice *self) {
  return self->mode();
}

//  bool QAudioDevice::isFormatSupported(const QAudioFormat &format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioDevice17isFormatSupportedERK12QAudioFormat(
    const QAudioDevice *self,
    const QAudioFormat *format) {
  return self->isFormatSupported(*format);
}

//  QAudioFormat QAudioDevice::preferredFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK12QAudioDevice15preferredFormatEv(
    const QAudioDevice *self) {
  return new QAudioFormat(self->preferredFormat());
}

//  int QAudioDevice::minimumSampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioDevice17minimumSampleRateEv(const QAudioDevice *self) {
  return self->minimumSampleRate();
}

//  int QAudioDevice::maximumSampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioDevice17maximumSampleRateEv(const QAudioDevice *self) {
  return self->maximumSampleRate();
}

//  int QAudioDevice::minimumChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioDevice19minimumChannelCountEv(
    const QAudioDevice *self) {
  return self->minimumChannelCount();
}

//  int QAudioDevice::maximumChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioDevice19maximumChannelCountEv(
    const QAudioDevice *self) {
  return self->maximumChannelCount();
}

//  QAudioFormat::ChannelConfig QAudioDevice::channelConfiguration() const
extern "C" Q_DECL_EXPORT
QAudioFormat::ChannelConfig ritual_ZNK12QAudioDevice20channelConfigurationEv(
    const QAudioDevice *self) {
  return self->channelConfiguration();
}

#if QT_DEPRECATED_SINCE(6, 10)
//  const QAudioDevicePrivate *QAudioDevice::handle() const
extern "C" Q_DECL_EXPORT
const QAudioDevicePrivate *ritual_ZNK12QAudioDevice6handleEv(
    const QAudioDevice *self) {
  return self->handle();
}
#endif  // QT_DEPRECATED_SINCE(6, 10)

//  QAudioDevice::QAudioDevice(QAudioDevicePrivate *p)
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN12QAudioDeviceC1EP19QAudioDevicePrivate(
    QAudioDevicePrivate *p) {
  return new QAudioDevice(p);
}

//  QList<QAudioDevice>::QList()
extern "C" Q_DECL_EXPORT
QList<QAudioDevice> *ritual_list_make_QAudioDevice() {
  return new QList<QAudioDevice>();
}

//  void QList<QAudioDevice>::append(const QAudioDevice &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAudioDevice(
    QList<QAudioDevice> *self,
    const QAudioDevice *element) {
  self->append(*element);
}

//  qsizetype QList<QAudioDevice>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAudioDevice(const QList<QAudioDevice> *self) {
  return self->size();
}

//  const QAudioDevice &QList<QAudioDevice>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_list_at_QAudioDevice(
    const QList<QAudioDevice> *self,
    long long index) {
  return new QAudioDevice(self->at(index));
}

//  QList<QAudioDevice>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAudioDevice(QList<QAudioDevice> *self) {
  delete self;
}
