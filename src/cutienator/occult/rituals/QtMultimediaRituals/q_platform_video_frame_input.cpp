//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideoframeinput_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideoframeinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframeformat.h>

//  const QMetaObject *QPlatformVideoFrameInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QPlatformVideoFrameInput10metaObjectEv(
    const QPlatformVideoFrameInput *self) {
  return self->metaObject();
}

//  QString QPlatformVideoFrameInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QPlatformVideoFrameInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformVideoFrameInput::tr(s, c, n));
}

//  QPlatformVideoFrameInput::QPlatformVideoFrameInput(QVideoFrameFormat
//      format)
extern "C" Q_DECL_EXPORT
QPlatformVideoFrameInput *ritual_ZN24QPlatformVideoFrameInputC1E17QVideoFrameFormat(
    const QVideoFrameFormat *format) {
  return new QPlatformVideoFrameInput(*format);
}

//  void QPlatformVideoFrameInput::setActive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformVideoFrameInput9setActiveEb(
    QPlatformVideoFrameInput *self,
    bool a0) {
  self->setActive(a0);
}

//  bool QPlatformVideoFrameInput::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QPlatformVideoFrameInput8isActiveEv(
    const QPlatformVideoFrameInput *self) {
  return self->isActive();
}

//  QVideoFrameFormat QPlatformVideoFrameInput::frameFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK24QPlatformVideoFrameInput11frameFormatEv(
    const QPlatformVideoFrameInput *self) {
  return new QVideoFrameFormat(self->frameFormat());
}

//  QString QPlatformVideoFrameInput::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QPlatformVideoFrameInput11errorStringEv(
    const QPlatformVideoFrameInput *self) {
  return new QString(self->errorString());
}

//  QMediaInputEncoderInterface *QPlatformVideoFrameInput::encoderInterface()
//      const
extern "C" Q_DECL_EXPORT
QMediaInputEncoderInterface *ritual_ZNK24QPlatformVideoFrameInput16encoderInterfaceEv(
    const QPlatformVideoFrameInput *self) {
  return self->encoderInterface();
}

//  void
//      QPlatformVideoFrameInput::setEncoderInterface(QMediaInputEncoderInter
//      face *encoderInterface)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlatformVideoFrameInput19setEncoderInterfaceEP27QMediaInputEncoderInterface(
    QPlatformVideoFrameInput *self,
    QMediaInputEncoderInterface *encoderInterface) {
  self->setEncoderInterface(encoderInterface);
}
