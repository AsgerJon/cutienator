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

//  DomConnectionHint::DomConnectionHint()
extern "C" Q_DECL_EXPORT
DomConnectionHint *ritual_ZN17DomConnectionHintC1Ev() {
  return new DomConnectionHint();
}

//  DomConnectionHint::~DomConnectionHint()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHintD1Ev(DomConnectionHint *self) {
  delete self;
}

//  void DomConnectionHint::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint4readER16QXmlStreamReader(
    DomConnectionHint *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomConnectionHint::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17DomConnectionHint5writeER16QXmlStreamWriterRK7QString(
    const DomConnectionHint *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomConnectionHint::hasAttributeType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomConnectionHint16hasAttributeTypeEv(
    const DomConnectionHint *self) {
  return self->hasAttributeType();
}

//  QString DomConnectionHint::attributeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DomConnectionHint13attributeTypeEv(
    const DomConnectionHint *self) {
  return new QString(self->attributeType());
}

//  void DomConnectionHint::setAttributeType(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint16setAttributeTypeERK7QString(
    DomConnectionHint *self,
    const QString *a) {
  self->setAttributeType(*a);
}

//  void DomConnectionHint::clearAttributeType()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint18clearAttributeTypeEv(
    DomConnectionHint *self) {
  self->clearAttributeType();
}

//  int DomConnectionHint::elementX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17DomConnectionHint8elementXEv(const DomConnectionHint *self) {
  return self->elementX();
}

//  void DomConnectionHint::setElementX(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint11setElementXEi(
    DomConnectionHint *self,
    int a) {
  self->setElementX(a);
}

//  bool DomConnectionHint::hasElementX() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomConnectionHint11hasElementXEv(
    const DomConnectionHint *self) {
  return self->hasElementX();
}

//  void DomConnectionHint::clearElementX()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint13clearElementXEv(DomConnectionHint *self) {
  self->clearElementX();
}

//  int DomConnectionHint::elementY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17DomConnectionHint8elementYEv(const DomConnectionHint *self) {
  return self->elementY();
}

//  void DomConnectionHint::setElementY(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint11setElementYEi(
    DomConnectionHint *self,
    int a) {
  self->setElementY(a);
}

//  bool DomConnectionHint::hasElementY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomConnectionHint11hasElementYEv(
    const DomConnectionHint *self) {
  return self->hasElementY();
}

//  void DomConnectionHint::clearElementY()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomConnectionHint13clearElementYEv(DomConnectionHint *self) {
  self->clearElementY();
}

//  QList<DomConnectionHint *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomConnectionHint *> *ritual_list_make_DomConnectionHint_ptr() {
  return new QList<DomConnectionHint *>();
}

//  void QList<DomConnectionHint *>::append(const DomConnectionHint * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomConnectionHint_ptr(
    QList<DomConnectionHint *> *self,
    DomConnectionHint *element) {
  self->append(element);
}

//  qsizetype QList<DomConnectionHint *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomConnectionHint_ptr(
    const QList<DomConnectionHint *> *self) {
  return self->size();
}

//  const DomConnectionHint * &QList<DomConnectionHint *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
DomConnectionHint *ritual_list_at_DomConnectionHint_ptr(
    const QList<DomConnectionHint *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomConnectionHint *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomConnectionHint_ptr(
    QList<DomConnectionHint *> *self) {
  delete self;
}
