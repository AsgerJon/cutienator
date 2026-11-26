//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiobufferinput_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiobufferinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>

//  const QMetaObject *QPlatformAudioBufferInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QPlatformAudioBufferInput10metaObjectEv(
    const QPlatformAudioBufferInput *self) {
  return self->metaObject();
}

//  void *QPlatformAudioBufferInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QPlatformAudioBufferInput11qt_metacastEPKc(
    QPlatformAudioBufferInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformAudioBufferInput::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QPlatformAudioBufferInput11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformAudioBufferInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformAudioBufferInput::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QPlatformAudioBufferInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformAudioBufferInput::tr(s, c, n));
}

//  QPlatformAudioBufferInput::QPlatformAudioBufferInput(const QAudioFormat
//      &format)
extern "C" Q_DECL_EXPORT
QPlatformAudioBufferInput *ritual_ZN25QPlatformAudioBufferInputC1ERK12QAudioFormat(
    const QAudioFormat *format) {
  return new QPlatformAudioBufferInput(*format);
}

//  const QAudioFormat &QPlatformAudioBufferInput::audioFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK25QPlatformAudioBufferInput11audioFormatEv(
    const QPlatformAudioBufferInput *self) {
  return new QAudioFormat(self->audioFormat());
}

//  QMediaInputEncoderInterface
//      *QPlatformAudioBufferInput::encoderInterface() const
extern "C" Q_DECL_EXPORT
QMediaInputEncoderInterface *ritual_ZNK25QPlatformAudioBufferInput16encoderInterfaceEv(
    const QPlatformAudioBufferInput *self) {
  return self->encoderInterface();
}

//  void QPlatformAudioBufferInput::setEncoderInterface(QMediaInputEncoderInt
//      erface *encoderInterface)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformAudioBufferInput19setEncoderInterfaceEP27QMediaInputEncoderInterface(
    QPlatformAudioBufferInput *self,
    QMediaInputEncoderInterface *encoderInterface) {
  self->setEncoderInterface(encoderInterface);
}

//  void QPlatformAudioBufferInput::encoderUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformAudioBufferInput14encoderUpdatedEv(
    QPlatformAudioBufferInput *self) {
  self->encoderUpdated();
}
