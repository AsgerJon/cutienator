//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/qpdfdocumentrenderoptions.h, Qt 6.12.0. Changes made here are lost.
#include <QtPdf/qpdfdocumentrenderoptions.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QPdfDocumentRenderOptions::QPdfDocumentRenderOptions()
extern "C" Q_DECL_EXPORT
QPdfDocumentRenderOptions *ritual_ZN25QPdfDocumentRenderOptionsC1Ev() {
  return new QPdfDocumentRenderOptions();
}

//  Rotation QPdfDocumentRenderOptions::rotation() const
extern "C" Q_DECL_EXPORT
QPdfDocumentRenderOptions::Rotation ritual_ZNK25QPdfDocumentRenderOptions8rotationEv(
    const QPdfDocumentRenderOptions *self) {
  return self->rotation();
}

//  void QPdfDocumentRenderOptions::setRotation(Rotation r)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPdfDocumentRenderOptions11setRotationENS_8RotationE(
    QPdfDocumentRenderOptions *self,
    QPdfDocumentRenderOptions::Rotation r) {
  self->setRotation(r);
}

//  RenderFlags QPdfDocumentRenderOptions::renderFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QPdfDocumentRenderOptions11renderFlagsEv(
    const QPdfDocumentRenderOptions *self) {
  return static_cast<int>(self->renderFlags().toInt());
}

//  void QPdfDocumentRenderOptions::setRenderFlags(RenderFlags r)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPdfDocumentRenderOptions14setRenderFlagsE6QFlagsINS_10RenderFlagEE(
    QPdfDocumentRenderOptions *self,
    int r) {
  self->setRenderFlags(
      QFlags<QPdfDocumentRenderOptions::RenderFlag>::fromInt(r));
}

//  QRect QPdfDocumentRenderOptions::scaledClipRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK25QPdfDocumentRenderOptions14scaledClipRectEv(
    const QPdfDocumentRenderOptions *self) {
  return new QRect(self->scaledClipRect());
}

//  void QPdfDocumentRenderOptions::setScaledClipRect(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPdfDocumentRenderOptions17setScaledClipRectERK5QRect(
    QPdfDocumentRenderOptions *self,
    const QRect *r) {
  self->setScaledClipRect(*r);
}

//  QSize QPdfDocumentRenderOptions::scaledSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QPdfDocumentRenderOptions10scaledSizeEv(
    const QPdfDocumentRenderOptions *self) {
  return new QSize(self->scaledSize());
}

//  void QPdfDocumentRenderOptions::setScaledSize(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPdfDocumentRenderOptions13setScaledSizeERK5QSize(
    QPdfDocumentRenderOptions *self,
    const QSize *s) {
  self->setScaledSize(*s);
}

//  bool operator==(const QPdfDocumentRenderOptions &lhs, const
//      QPdfDocumentRenderOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK25QPdfDocumentRenderOptionsS1_(
    const QPdfDocumentRenderOptions *lhs,
    const QPdfDocumentRenderOptions *rhs) {
  return operator==(*lhs, *rhs);
}

//  QPdfDocumentRenderOptions::~QPdfDocumentRenderOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPdfDocumentRenderOptionsD1Ev(
    QPdfDocumentRenderOptions *self) {
  delete self;
}
