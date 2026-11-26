//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendercapture.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendercapture.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>

//  const QMetaObject *Qt3DRender::QRenderCaptureReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender19QRenderCaptureReply10metaObjectEv(
    const Qt3DRender::QRenderCaptureReply *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderCaptureReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender19QRenderCaptureReply11qt_metacastEPKc(
    Qt3DRender::QRenderCaptureReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderCaptureReply::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender19QRenderCaptureReply11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderCaptureReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QImage Qt3DRender::QRenderCaptureReply::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK10Qt3DRender19QRenderCaptureReply5imageEv(
    const Qt3DRender::QRenderCaptureReply *self) {
  return new QImage(self->image());
}

//  int Qt3DRender::QRenderCaptureReply::captureId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderCaptureReply9captureIdEv(
    const Qt3DRender::QRenderCaptureReply *self) {
  return self->captureId();
}

//  bool Qt3DRender::QRenderCaptureReply::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCaptureReply10isCompleteEv(
    const Qt3DRender::QRenderCaptureReply *self) {
  return self->isComplete();
}

//  bool Qt3DRender::QRenderCaptureReply::saveImage(const QString &fileName)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender19QRenderCaptureReply9saveImageERK7QString(
    const Qt3DRender::QRenderCaptureReply *self,
    const QString *fileName) {
  return self->saveImage(*fileName);
}

//  void Qt3DRender::QRenderCaptureReply::completed()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderCaptureReply9completedEv(
    Qt3DRender::QRenderCaptureReply *self) {
  self->completed();
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

//  Qt3DRender::QRenderCaptureReply::QRenderCaptureReply(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderCaptureReply *ritual_ZN10Qt3DRender19QRenderCaptureReplyC1EP7QObject(
    QObject *parent) {
  return new Qt3DRender::QRenderCaptureReply(parent);
}
