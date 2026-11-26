//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendercapture.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendercapture.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  const QMetaObject *Qt3DRender::QRenderCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender14QRenderCapture10metaObjectEv(
    const Qt3DRender::QRenderCapture *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderCapture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender14QRenderCapture11qt_metacastEPKc(
    Qt3DRender::QRenderCapture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderCapture::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender14QRenderCapture11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderCapture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  Qt3DRender::QRenderCapture::QRenderCapture(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCapture *ritual_ZN10Qt3DRender14QRenderCaptureC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new Qt3DRender::QRenderCapture(parent);
}

//  Qt3DRender::QRenderCaptureReply
//      *Qt3DRender::QRenderCapture::requestCapture(int captureId)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender14QRenderCapture14requestCaptureEi(
    Qt3DRender::QRenderCapture *self,
    int captureId) {
  return self->requestCapture(captureId);
}

//  Qt3DRender::QRenderCaptureReply
//      *Qt3DRender::QRenderCapture::requestCapture()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender14QRenderCapture14requestCaptureEv(
    Qt3DRender::QRenderCapture *self) {
  return self->requestCapture();
}

//  Qt3DRender::QRenderCaptureReply
//      *Qt3DRender::QRenderCapture::requestCapture(const QRect &rect)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender14QRenderCapture14requestCaptureERK5QRect(
    Qt3DRender::QRenderCapture *self,
    const QRect *rect) {
  return self->requestCapture(*rect);
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
