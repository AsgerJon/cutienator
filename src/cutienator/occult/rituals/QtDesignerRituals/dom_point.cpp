//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomPoint::DomPoint()
extern "C" Q_DECL_EXPORT
DomPoint *ritual_ZN8DomPointC1Ev() {
  return new DomPoint();
}

//  DomPoint::~DomPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomPointD1Ev(DomPoint *self) {
  delete self;
}

//  void DomPoint::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomPoint4readER16QXmlStreamReader(
    DomPoint *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomPoint::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8DomPoint5writeER16QXmlStreamWriterRK7QString(
    const DomPoint *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  int DomPoint::elementX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8DomPoint8elementXEv(const DomPoint *self) {
  return self->elementX();
}

//  void DomPoint::setElementX(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomPoint11setElementXEi(DomPoint *self, int a) {
  self->setElementX(a);
}

//  bool DomPoint::hasElementX() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomPoint11hasElementXEv(const DomPoint *self) {
  return self->hasElementX();
}

//  void DomPoint::clearElementX()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomPoint13clearElementXEv(DomPoint *self) {
  self->clearElementX();
}

//  int DomPoint::elementY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8DomPoint8elementYEv(const DomPoint *self) {
  return self->elementY();
}

//  void DomPoint::setElementY(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomPoint11setElementYEi(DomPoint *self, int a) {
  self->setElementY(a);
}

//  bool DomPoint::hasElementY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8DomPoint11hasElementYEv(const DomPoint *self) {
  return self->hasElementY();
}

//  void DomPoint::clearElementY()
extern "C" Q_DECL_EXPORT
void ritual_ZN8DomPoint13clearElementYEv(DomPoint *self) {
  self->clearElementY();
}
