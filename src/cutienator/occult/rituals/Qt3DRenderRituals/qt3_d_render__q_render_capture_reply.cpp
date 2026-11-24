//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendercapture.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendercapture.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DRender::QRenderCaptureReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender19QRenderCaptureReply10metaObjectEv(
    const Qt3DRender::QRenderCaptureReply *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QRenderCaptureReply::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender19QRenderCaptureReply2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderCaptureReply::tr(s, c, n));
}

//  QRenderCaptureReplyPrivate *Qt3DRender::QRenderCaptureReply::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReplyPrivate *ritual_ZN10Qt3DRender19QRenderCaptureReply6d_funcEv(
    Qt3DRender::QRenderCaptureReply *self) {
  return self->d_func();
}

//  const QRenderCaptureReplyPrivate
//      *Qt3DRender::QRenderCaptureReply::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCaptureReplyPrivate *ritual_ZNK10Qt3DRender19QRenderCaptureReply6d_funcEv(
    const Qt3DRender::QRenderCaptureReply *self) {
  return self->d_func();
}
