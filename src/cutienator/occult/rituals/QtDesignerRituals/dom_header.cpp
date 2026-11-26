//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomHeader::DomHeader()
extern "C" Q_DECL_EXPORT
DomHeader *ritual_ZN9DomHeaderC1Ev() {
  return new DomHeader();
}

//  DomHeader::~DomHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomHeaderD1Ev(DomHeader *self) {
  delete self;
}

//  void DomHeader::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomHeader4readER16QXmlStreamReader(
    DomHeader *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomHeader::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9DomHeader5writeER16QXmlStreamWriterRK7QString(
    const DomHeader *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QString DomHeader::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomHeader4textEv(const DomHeader *self) {
  return new QString(self->text());
}

//  void DomHeader::setText(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomHeader7setTextERK7QString(
    DomHeader *self,
    const QString *s) {
  self->setText(*s);
}

//  bool DomHeader::hasAttributeLocation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomHeader20hasAttributeLocationEv(const DomHeader *self) {
  return self->hasAttributeLocation();
}

//  QString DomHeader::attributeLocation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomHeader17attributeLocationEv(const DomHeader *self) {
  return new QString(self->attributeLocation());
}

//  void DomHeader::setAttributeLocation(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomHeader20setAttributeLocationERK7QString(
    DomHeader *self,
    const QString *a) {
  self->setAttributeLocation(*a);
}

//  void DomHeader::clearAttributeLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomHeader22clearAttributeLocationEv(DomHeader *self) {
  self->clearAttributeLocation();
}
