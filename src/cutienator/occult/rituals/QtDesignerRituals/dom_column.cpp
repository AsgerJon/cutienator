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

//  DomColumn::DomColumn()
extern "C" Q_DECL_EXPORT
DomColumn *ritual_ZN9DomColumnC1Ev() {
  return new DomColumn();
}

//  DomColumn::~DomColumn()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomColumnD1Ev(DomColumn *self) {
  delete self;
}

//  void DomColumn::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomColumn4readER16QXmlStreamReader(
    DomColumn *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomColumn::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9DomColumn5writeER16QXmlStreamWriterRK7QString(
    const DomColumn *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QList<DomProperty *> DomColumn::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK9DomColumn15elementPropertyEv(
    const DomColumn *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomColumn::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomColumn18setElementPropertyERK5QListIP11DomPropertyE(
    DomColumn *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomColumn *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomColumn *> *ritual_list_make_DomColumn_ptr() {
  return new QList<DomColumn *>();
}

//  void QList<DomColumn *>::append(const DomColumn * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomColumn_ptr(
    QList<DomColumn *> *self,
    DomColumn *element) {
  self->append(element);
}

//  qsizetype QList<DomColumn *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomColumn_ptr(const QList<DomColumn *> *self) {
  return self->size();
}

//  const DomColumn * &QList<DomColumn *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomColumn *ritual_list_at_DomColumn_ptr(
    const QList<DomColumn *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomColumn *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomColumn_ptr(QList<DomColumn *> *self) {
  delete self;
}
