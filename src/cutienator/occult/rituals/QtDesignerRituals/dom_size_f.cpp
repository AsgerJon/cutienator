//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomSizeF::DomSizeF()
extern "C" Q_DECL_EXPORT
DomSizeF *ritual_ZN8DomSizeFC1Ev() {
  return new DomSizeF();
}

//  DomSizeF::~DomSizeF()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSizeFD1Ev(DomSizeF *self) {
  delete self;
}

//  void DomSizeF::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSizeF4readER16QXmlStreamReader(
    DomSizeF *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomSizeF::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8DomSizeF5writeER16QXmlStreamWriterRK7QString(
    const DomSizeF *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  double DomSizeF::elementWidth() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK8DomSizeF12elementWidthEv(const DomSizeF *self) {
  return self->elementWidth();
}

//  void DomSizeF::setElementWidth(double a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSizeF15setElementWidthEd(DomSizeF *self, double a) {
  self->setElementWidth(a);
}

//  bool DomSizeF::hasElementWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomSizeF15hasElementWidthEv(const DomSizeF *self) {
  return self->hasElementWidth();
}

//  void DomSizeF::clearElementWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSizeF17clearElementWidthEv(DomSizeF *self) {
  self->clearElementWidth();
}

//  double DomSizeF::elementHeight() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK8DomSizeF13elementHeightEv(const DomSizeF *self) {
  return self->elementHeight();
}

//  void DomSizeF::setElementHeight(double a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSizeF16setElementHeightEd(DomSizeF *self, double a) {
  self->setElementHeight(a);
}

//  bool DomSizeF::hasElementHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomSizeF16hasElementHeightEv(const DomSizeF *self) {
  return self->hasElementHeight();
}

//  void DomSizeF::clearElementHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomSizeF18clearElementHeightEv(DomSizeF *self) {
  self->clearElementHeight();
}
