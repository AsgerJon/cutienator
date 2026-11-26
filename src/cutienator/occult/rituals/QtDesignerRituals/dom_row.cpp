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

//  DomRow::DomRow()
extern "C" Q_DECL_EXPORT
DomRow *ritual_ZN6DomRowC1Ev() {
  return new DomRow();
}

//  DomRow::~DomRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomRowD1Ev(DomRow *self) {
  delete self;
}

//  void DomRow::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomRow4readER16QXmlStreamReader(
    DomRow *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomRow::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6DomRow5writeER16QXmlStreamWriterRK7QString(
    const DomRow *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QList<DomProperty *> DomRow::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK6DomRow15elementPropertyEv(
    const DomRow *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomRow::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN6DomRow18setElementPropertyERK5QListIP11DomPropertyE(
    DomRow *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomRow *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomRow *> *ritual_list_make_DomRow_ptr() {
  return new QList<DomRow *>();
}

//  void QList<DomRow *>::append(const DomRow * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomRow_ptr(QList<DomRow *> *self, DomRow *element) {
  self->append(element);
}

//  qsizetype QList<DomRow *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomRow_ptr(const QList<DomRow *> *self) {
  return self->size();
}

//  const DomRow * &QList<DomRow *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomRow *ritual_list_at_DomRow_ptr(
    const QList<DomRow *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomRow *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomRow_ptr(QList<DomRow *> *self) {
  delete self;
}
