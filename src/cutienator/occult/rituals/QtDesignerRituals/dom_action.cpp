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

//  DomAction::DomAction()
extern "C" Q_DECL_EXPORT
DomAction *ritual_ZN9DomActionC1Ev() {
  return new DomAction();
}

//  DomAction::~DomAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomActionD1Ev(DomAction *self) {
  delete self;
}

//  void DomAction::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction4readER16QXmlStreamReader(
    DomAction *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomAction::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9DomAction5writeER16QXmlStreamWriterRK7QString(
    const DomAction *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomAction::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomAction16hasAttributeNameEv(const DomAction *self) {
  return self->hasAttributeName();
}

//  QString DomAction::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomAction13attributeNameEv(const DomAction *self) {
  return new QString(self->attributeName());
}

//  void DomAction::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction16setAttributeNameERK7QString(
    DomAction *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomAction::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction18clearAttributeNameEv(DomAction *self) {
  self->clearAttributeName();
}

//  bool DomAction::hasAttributeMenu() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomAction16hasAttributeMenuEv(const DomAction *self) {
  return self->hasAttributeMenu();
}

//  QString DomAction::attributeMenu() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomAction13attributeMenuEv(const DomAction *self) {
  return new QString(self->attributeMenu());
}

//  void DomAction::setAttributeMenu(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction16setAttributeMenuERK7QString(
    DomAction *self,
    const QString *a) {
  self->setAttributeMenu(*a);
}

//  void DomAction::clearAttributeMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction18clearAttributeMenuEv(DomAction *self) {
  self->clearAttributeMenu();
}

//  QList<DomProperty *> DomAction::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK9DomAction15elementPropertyEv(
    const DomAction *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomAction::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction18setElementPropertyERK5QListIP11DomPropertyE(
    DomAction *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}

//  QList<DomProperty *> DomAction::elementAttribute() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK9DomAction16elementAttributeEv(
    const DomAction *self) {
  return new QList<DomProperty *>(self->elementAttribute());
}

//  void DomAction::setElementAttribute(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomAction19setElementAttributeERK5QListIP11DomPropertyE(
    DomAction *self,
    const QList<DomProperty *> *a) {
  self->setElementAttribute(*a);
}

//  QList<DomAction *>::QList()
extern "C" Q_DECL_EXPORT
QList<DomAction *> *ritual_list_make_DomAction_ptr() {
  return new QList<DomAction *>();
}

//  void QList<DomAction *>::append(const DomAction * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DomAction_ptr(
    QList<DomAction *> *self,
    DomAction *element) {
  self->append(element);
}

//  qsizetype QList<DomAction *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DomAction_ptr(const QList<DomAction *> *self) {
  return self->size();
}

//  const DomAction * &QList<DomAction *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DomAction *ritual_list_at_DomAction_ptr(
    const QList<DomAction *> *self,
    long long index) {
  return self->at(index);
}

//  QList<DomAction *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DomAction_ptr(QList<DomAction *> *self) {
  delete self;
}
