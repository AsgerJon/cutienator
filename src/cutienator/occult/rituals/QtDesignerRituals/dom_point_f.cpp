//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomPointF::DomPointF()
extern "C" Q_DECL_EXPORT
DomPointF *ritual_ZN9DomPointFC1Ev() {
  return new DomPointF();
}

//  DomPointF::~DomPointF()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomPointFD1Ev(DomPointF *self) {
  delete self;
}

//  void DomPointF::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomPointF4readER16QXmlStreamReader(
    DomPointF *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomPointF::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9DomPointF5writeER16QXmlStreamWriterRK7QString(
    const DomPointF *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  double DomPointF::elementX() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK9DomPointF8elementXEv(const DomPointF *self) {
  return self->elementX();
}

//  void DomPointF::setElementX(double a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomPointF11setElementXEd(DomPointF *self, double a) {
  self->setElementX(a);
}

//  bool DomPointF::hasElementX() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomPointF11hasElementXEv(const DomPointF *self) {
  return self->hasElementX();
}

//  void DomPointF::clearElementX()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomPointF13clearElementXEv(DomPointF *self) {
  self->clearElementX();
}

//  double DomPointF::elementY() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK9DomPointF8elementYEv(const DomPointF *self) {
  return self->elementY();
}

//  void DomPointF::setElementY(double a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomPointF11setElementYEd(DomPointF *self, double a) {
  self->setElementY(a);
}

//  bool DomPointF::hasElementY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomPointF11hasElementYEv(const DomPointF *self) {
  return self->hasElementY();
}

//  void DomPointF::clearElementY()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomPointF13clearElementYEv(DomPointF *self) {
  self->clearElementY();
}
