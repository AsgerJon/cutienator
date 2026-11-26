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

//  DomStringList::DomStringList()
extern "C" Q_DECL_EXPORT
DomStringList *ritual_ZN13DomStringListC1Ev() {
  return new DomStringList();
}

//  DomStringList::~DomStringList()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringListD1Ev(DomStringList *self) {
  delete self;
}

//  void DomStringList::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList4readER16QXmlStreamReader(
    DomStringList *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomStringList::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13DomStringList5writeER16QXmlStreamWriterRK7QString(
    const DomStringList *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomStringList::hasAttributeNotr() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomStringList16hasAttributeNotrEv(
    const DomStringList *self) {
  return self->hasAttributeNotr();
}

//  QString DomStringList::attributeNotr() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomStringList13attributeNotrEv(
    const DomStringList *self) {
  return new QString(self->attributeNotr());
}

//  void DomStringList::setAttributeNotr(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList16setAttributeNotrERK7QString(
    DomStringList *self,
    const QString *a) {
  self->setAttributeNotr(*a);
}

//  void DomStringList::clearAttributeNotr()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList18clearAttributeNotrEv(DomStringList *self) {
  self->clearAttributeNotr();
}

//  bool DomStringList::hasAttributeComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomStringList19hasAttributeCommentEv(
    const DomStringList *self) {
  return self->hasAttributeComment();
}

//  QString DomStringList::attributeComment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomStringList16attributeCommentEv(
    const DomStringList *self) {
  return new QString(self->attributeComment());
}

//  void DomStringList::setAttributeComment(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList19setAttributeCommentERK7QString(
    DomStringList *self,
    const QString *a) {
  self->setAttributeComment(*a);
}

//  void DomStringList::clearAttributeComment()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList21clearAttributeCommentEv(DomStringList *self) {
  self->clearAttributeComment();
}

//  bool DomStringList::hasAttributeExtraComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomStringList24hasAttributeExtraCommentEv(
    const DomStringList *self) {
  return self->hasAttributeExtraComment();
}

//  QString DomStringList::attributeExtraComment() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomStringList21attributeExtraCommentEv(
    const DomStringList *self) {
  return new QString(self->attributeExtraComment());
}

//  void DomStringList::setAttributeExtraComment(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList24setAttributeExtraCommentERK7QString(
    DomStringList *self,
    const QString *a) {
  self->setAttributeExtraComment(*a);
}

//  void DomStringList::clearAttributeExtraComment()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList26clearAttributeExtraCommentEv(
    DomStringList *self) {
  self->clearAttributeExtraComment();
}

//  bool DomStringList::hasAttributeId() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13DomStringList14hasAttributeIdEv(const DomStringList *self) {
  return self->hasAttributeId();
}

//  QString DomStringList::attributeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13DomStringList11attributeIdEv(
    const DomStringList *self) {
  return new QString(self->attributeId());
}

//  void DomStringList::setAttributeId(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList14setAttributeIdERK7QString(
    DomStringList *self,
    const QString *a) {
  self->setAttributeId(*a);
}

//  void DomStringList::clearAttributeId()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList16clearAttributeIdEv(DomStringList *self) {
  self->clearAttributeId();
}

//  QStringList DomStringList::elementString() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13DomStringList13elementStringEv(
    const DomStringList *self) {
  return new QList<QString>(self->elementString());
}

//  void DomStringList::setElementString(const QStringList &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DomStringList16setElementStringERK5QListI7QStringE(
    DomStringList *self,
    const QList<QString> *a) {
  self->setElementString(*a);
}
