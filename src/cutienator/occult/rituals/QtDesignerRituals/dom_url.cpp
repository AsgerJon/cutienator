//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomUrl::DomUrl()
extern "C" Q_DECL_EXPORT
DomUrl *ritual_ZN6DomUrlC1Ev() {
  return new DomUrl();
}

//  DomUrl::~DomUrl()
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomUrlD1Ev(DomUrl *self) {
  delete self;
}

//  void DomUrl::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomUrl4readER16QXmlStreamReader(
    DomUrl *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomUrl::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6DomUrl5writeER16QXmlStreamWriterRK7QString(
    const DomUrl *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  DomString *DomUrl::elementString() const
extern "C" Q_DECL_EXPORT
DomString *ritual_ZNK6DomUrl13elementStringEv(const DomUrl *self) {
  return self->elementString();
}

//  DomString *DomUrl::takeElementString()
extern "C" Q_DECL_EXPORT
DomString *ritual_ZN6DomUrl17takeElementStringEv(DomUrl *self) {
  return self->takeElementString();
}

//  void DomUrl::setElementString(DomString *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomUrl16setElementStringEP9DomString(
    DomUrl *self,
    DomString *a) {
  self->setElementString(a);
}

//  bool DomUrl::hasElementString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6DomUrl16hasElementStringEv(const DomUrl *self) {
  return self->hasElementString();
}

//  void DomUrl::clearElementString()
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomUrl18clearElementStringEv(DomUrl *self) {
  self->clearElementString();
}
