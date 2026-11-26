//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomBrush::DomBrush()
extern "C" Q_DECL_EXPORT
DomBrush *ritual_ZN8DomBrushC1Ev() {
  return new DomBrush();
}

//  DomBrush::~DomBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrushD1Ev(DomBrush *self) {
  delete self;
}

//  void DomBrush::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush4readER16QXmlStreamReader(
    DomBrush *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomBrush::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8DomBrush5writeER16QXmlStreamWriterRK7QString(
    const DomBrush *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomBrush::hasAttributeBrushStyle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomBrush22hasAttributeBrushStyleEv(const DomBrush *self) {
  return self->hasAttributeBrushStyle();
}

//  QString DomBrush::attributeBrushStyle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8DomBrush19attributeBrushStyleEv(const DomBrush *self) {
  return new QString(self->attributeBrushStyle());
}

//  void DomBrush::setAttributeBrushStyle(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush22setAttributeBrushStyleERK7QString(
    DomBrush *self,
    const QString *a) {
  self->setAttributeBrushStyle(*a);
}

//  void DomBrush::clearAttributeBrushStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush24clearAttributeBrushStyleEv(DomBrush *self) {
  self->clearAttributeBrushStyle();
}

//  Kind DomBrush::kind() const
extern "C" Q_DECL_EXPORT
DomBrush::Kind ritual_ZNK8DomBrush4kindEv(const DomBrush *self) {
  return self->kind();
}

//  DomColor *DomBrush::elementColor() const
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZNK8DomBrush12elementColorEv(const DomBrush *self) {
  return self->elementColor();
}

//  DomColor *DomBrush::takeElementColor()
extern "C" Q_DECL_EXPORT
DomColor *ritual_ZN8DomBrush16takeElementColorEv(DomBrush *self) {
  return self->takeElementColor();
}

//  void DomBrush::setElementColor(DomColor *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush15setElementColorEP8DomColor(
    DomBrush *self,
    DomColor *a) {
  self->setElementColor(a);
}

//  DomProperty *DomBrush::elementTexture() const
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZNK8DomBrush14elementTextureEv(const DomBrush *self) {
  return self->elementTexture();
}

//  DomProperty *DomBrush::takeElementTexture()
extern "C" Q_DECL_EXPORT
DomProperty *ritual_ZN8DomBrush18takeElementTextureEv(DomBrush *self) {
  return self->takeElementTexture();
}

//  void DomBrush::setElementTexture(DomProperty *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush17setElementTextureEP11DomProperty(
    DomBrush *self,
    DomProperty *a) {
  self->setElementTexture(a);
}

//  DomGradient *DomBrush::elementGradient() const
extern "C" Q_DECL_EXPORT
DomGradient *ritual_ZNK8DomBrush15elementGradientEv(const DomBrush *self) {
  return self->elementGradient();
}

//  DomGradient *DomBrush::takeElementGradient()
extern "C" Q_DECL_EXPORT
DomGradient *ritual_ZN8DomBrush19takeElementGradientEv(DomBrush *self) {
  return self->takeElementGradient();
}

//  void DomBrush::setElementGradient(DomGradient *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush18setElementGradientEP11DomGradient(
    DomBrush *self,
    DomGradient *a) {
  self->setElementGradient(a);
}

//  void DomBrush::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomBrush5clearEv(DomBrush *self) {
  self->clear();
}
