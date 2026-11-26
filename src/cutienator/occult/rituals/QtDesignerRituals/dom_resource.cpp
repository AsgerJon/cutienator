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

//  DomResource::DomResource()
extern "C" Q_DECL_EXPORT
DomResource *ritual_ZN11DomResourceC1Ev() {
  return new DomResource();
}

//  DomResource::~DomResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomResourceD1Ev(DomResource *self) {
  delete self;
}

//  void DomResource::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomResource4readER16QXmlStreamReader(
    DomResource *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomResource::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11DomResource5writeER16QXmlStreamWriterRK7QString(
    const DomResource *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomResource::hasAttributeLocation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11DomResource20hasAttributeLocationEv(
    const DomResource *self) {
  return self->hasAttributeLocation();
}

//  QString DomResource::attributeLocation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11DomResource17attributeLocationEv(
    const DomResource *self) {
  return new QString(self->attributeLocation());
}

//  void DomResource::setAttributeLocation(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomResource20setAttributeLocationERK7QString(
    DomResource *self,
    const QString *a) {
  self->setAttributeLocation(*a);
}

//  void DomResource::clearAttributeLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomResource22clearAttributeLocationEv(DomResource *self) {
  self->clearAttributeLocation();
}

//  QList<DomResource *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomResource *> *ritual_list_make_DomResource_ptr() {
  return new QList<DomResource *>();
}

//  void QList<DomResource *>::append(const DomResource * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomResource_ptr(
    QList<DomResource *> *self,
    DomResource *element) {
  self->append(element);
}

//  qsizetype QList<DomResource *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomResource_ptr(
    const QList<DomResource *> *self) {
  return self->size();
}

//  const DomResource * &QList<DomResource *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomResource *ritual_list_at_DomResource_ptr(
    const QList<DomResource *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomResource *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomResource_ptr(QList<DomResource *> *self) {
  delete self;
}
