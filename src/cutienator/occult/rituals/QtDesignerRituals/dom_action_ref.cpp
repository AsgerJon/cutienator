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

//  DomActionRef::DomActionRef()
extern "C" Q_DECL_EXPORT
DomActionRef *ritual_ZN12DomActionRefC1Ev() {
  return new DomActionRef();
}

//  DomActionRef::~DomActionRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomActionRefD1Ev(DomActionRef *self) {
  delete self;
}

//  void DomActionRef::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomActionRef4readER16QXmlStreamReader(
    DomActionRef *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomActionRef::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12DomActionRef5writeER16QXmlStreamWriterRK7QString(
    const DomActionRef *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomActionRef::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12DomActionRef16hasAttributeNameEv(const DomActionRef *self) {
  return self->hasAttributeName();
}

//  QString DomActionRef::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12DomActionRef13attributeNameEv(
    const DomActionRef *self) {
  return new QString(self->attributeName());
}

//  void DomActionRef::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomActionRef16setAttributeNameERK7QString(
    DomActionRef *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomActionRef::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomActionRef18clearAttributeNameEv(DomActionRef *self) {
  self->clearAttributeName();
}

//  QList<DomActionRef *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomActionRef *> *ritual_list_make_DomActionRef_ptr() {
  return new QList<DomActionRef *>();
}

//  void QList<DomActionRef *>::append(const DomActionRef * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomActionRef_ptr(
    QList<DomActionRef *> *self,
    DomActionRef *element) {
  self->append(element);
}

//  qsizetype QList<DomActionRef *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomActionRef_ptr(
    const QList<DomActionRef *> *self) {
  return self->size();
}

//  const DomActionRef * &QList<DomActionRef *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomActionRef *ritual_list_at_DomActionRef_ptr(
    const QList<DomActionRef *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomActionRef *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomActionRef_ptr(QList<DomActionRef *> *self) {
  delete self;
}
