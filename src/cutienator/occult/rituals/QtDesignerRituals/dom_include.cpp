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

//  DomInclude::DomInclude()
extern "C" Q_DECL_EXPORT
DomInclude *ritual_ZN10DomIncludeC1Ev() {
  return new DomInclude();
}

//  DomInclude::~DomInclude()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomIncludeD1Ev(DomInclude *self) {
  delete self;
}

//  void DomInclude::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomInclude4readER16QXmlStreamReader(
    DomInclude *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomInclude::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10DomInclude5writeER16QXmlStreamWriterRK7QString(
    const DomInclude *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QString DomInclude::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10DomInclude4textEv(const DomInclude *self) {
  return new QString(self->text());
}

//  void DomInclude::setText(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomInclude7setTextERK7QString(
    DomInclude *self,
    const QString *s) {
  self->setText(*s);
}

//  bool DomInclude::hasAttributeLocation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10DomInclude20hasAttributeLocationEv(const DomInclude *self) {
  return self->hasAttributeLocation();
}

//  QString DomInclude::attributeLocation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10DomInclude17attributeLocationEv(
    const DomInclude *self) {
  return new QString(self->attributeLocation());
}

//  void DomInclude::setAttributeLocation(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomInclude20setAttributeLocationERK7QString(
    DomInclude *self,
    const QString *a) {
  self->setAttributeLocation(*a);
}

//  void DomInclude::clearAttributeLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomInclude22clearAttributeLocationEv(DomInclude *self) {
  self->clearAttributeLocation();
}

//  bool DomInclude::hasAttributeImpldecl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10DomInclude20hasAttributeImpldeclEv(const DomInclude *self) {
  return self->hasAttributeImpldecl();
}

//  QString DomInclude::attributeImpldecl() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10DomInclude17attributeImpldeclEv(
    const DomInclude *self) {
  return new QString(self->attributeImpldecl());
}

//  void DomInclude::setAttributeImpldecl(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomInclude20setAttributeImpldeclERK7QString(
    DomInclude *self,
    const QString *a) {
  self->setAttributeImpldecl(*a);
}

//  void DomInclude::clearAttributeImpldecl()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomInclude22clearAttributeImpldeclEv(DomInclude *self) {
  self->clearAttributeImpldecl();
}

//  QList<DomInclude *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomInclude *> *ritual_list_make_DomInclude_ptr() {
  return new QList<DomInclude *>();
}

//  void QList<DomInclude *>::append(const DomInclude * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomInclude_ptr(
    QList<DomInclude *> *self,
    DomInclude *element) {
  self->append(element);
}

//  qsizetype QList<DomInclude *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomInclude_ptr(const QList<DomInclude *> *self) {
  return self->size();
}

//  const DomInclude * &QList<DomInclude *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomInclude *ritual_list_at_DomInclude_ptr(
    const QList<DomInclude *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomInclude *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomInclude_ptr(QList<DomInclude *> *self) {
  delete self;
}
