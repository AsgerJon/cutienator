//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  DomDesignerData::DomDesignerData()
extern "C" Q_DECL_EXPORT
DomDesignerData *ritual_ZN15DomDesignerDataC1Ev() {
  return new DomDesignerData();
}

//  DomDesignerData::~DomDesignerData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomDesignerDataD1Ev(DomDesignerData *self) {
  delete self;
}

//  void DomDesignerData::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomDesignerData4readER16QXmlStreamReader(
    DomDesignerData *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomDesignerData::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15DomDesignerData5writeER16QXmlStreamWriterRK7QString(
    const DomDesignerData *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QList<DomProperty *> DomDesignerData::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK15DomDesignerData15elementPropertyEv(
    const DomDesignerData *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomDesignerData::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DomDesignerData18setElementPropertyERK5QListIP11DomPropertyE(
    DomDesignerData *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}
