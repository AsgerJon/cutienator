//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendercapture.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendercapture.h>
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DRender::QRenderCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QRenderCapture10metaObjectEv(
    const Qt3DRender::QRenderCapture *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QRenderCapture::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender14QRenderCapture2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderCapture::tr(s, c, n));
}

//  QRenderCapturePrivate *Qt3DRender::QRenderCapture::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapturePrivate *ritual_ZN10Qt3DRender14QRenderCapture6d_funcEv(
    Qt3DRender::QRenderCapture *self) {
  return self->d_func();
}

//  const QRenderCapturePrivate *Qt3DRender::QRenderCapture::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderCapturePrivate *ritual_ZNK10Qt3DRender14QRenderCapture6d_funcEv(
    const Qt3DRender::QRenderCapture *self) {
  return self->d_func();
}
