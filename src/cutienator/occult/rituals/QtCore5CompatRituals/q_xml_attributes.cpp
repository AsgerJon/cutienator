//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>

//  QXmlAttributes::QXmlAttributes()
extern "C" Q_DECL_EXPORT
QXmlAttributes *ritual_ZN14QXmlAttributesC1Ev() {
  return new QXmlAttributes();
}

//  QXmlAttributes::QXmlAttributes(const QXmlAttributes &a0)
extern "C" Q_DECL_EXPORT
QXmlAttributes *ritual_ZN14QXmlAttributesC1ERKS_(const QXmlAttributes *a0) {
  return new QXmlAttributes(*a0);
}

//  QXmlAttributes::QXmlAttributes(QXmlAttributes &&a0)
extern "C" Q_DECL_EXPORT
QXmlAttributes *ritual_ZN14QXmlAttributesC1EOS_(QXmlAttributes *a0) {
  return new QXmlAttributes(std::move(*a0));
}

//  QXmlAttributes &QXmlAttributes::operator=(const QXmlAttributes &a0)
extern "C" Q_DECL_EXPORT
QXmlAttributes *ritual_ZN14QXmlAttributesaSERKS_(
    QXmlAttributes *self,
    const QXmlAttributes *a0) {
  return &(self->operator=(*a0));
}

//  QXmlAttributes &QXmlAttributes::operator=(QXmlAttributes &&a0)
extern "C" Q_DECL_EXPORT
QXmlAttributes *ritual_ZN14QXmlAttributesaSEOS_(
    QXmlAttributes *self,
    QXmlAttributes *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QXmlAttributes::~QXmlAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXmlAttributesD1Ev(QXmlAttributes *self) {
  delete self;
}

//  void QXmlAttributes::swap(QXmlAttributes &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXmlAttributes4swapERS_(
    QXmlAttributes *self,
    QXmlAttributes *other) {
  self->swap(*other);
}

//  int QXmlAttributes::index(const QString &qName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXmlAttributes5indexERK7QString(
    const QXmlAttributes *self,
    const QString *qName) {
  return self->index(*qName);
}

//  int QXmlAttributes::index(QLatin1String qName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXmlAttributes5indexE13QLatin1String(
    const QXmlAttributes *self,
    const QLatin1String *qName) {
  return self->index(*qName);
}

//  int QXmlAttributes::index(const QString &uri, const QString &localPart)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXmlAttributes5indexERK7QStringS2_(
    const QXmlAttributes *self,
    const QString *uri,
    const QString *localPart) {
  return self->index(*uri, *localPart);
}

//  int QXmlAttributes::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXmlAttributes6lengthEv(const QXmlAttributes *self) {
  return self->length();
}

//  int QXmlAttributes::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXmlAttributes5countEv(const QXmlAttributes *self) {
  return self->count();
}

//  QString QXmlAttributes::localName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes9localNameEi(
    const QXmlAttributes *self,
    int index) {
  return new QString(self->localName(index));
}

//  QString QXmlAttributes::qName(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes5qNameEi(
    const QXmlAttributes *self,
    int index) {
  return new QString(self->qName(index));
}

//  QString QXmlAttributes::uri(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes3uriEi(
    const QXmlAttributes *self,
    int index) {
  return new QString(self->uri(index));
}

//  QString QXmlAttributes::type(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes4typeEi(
    const QXmlAttributes *self,
    int index) {
  return new QString(self->type(index));
}

//  QString QXmlAttributes::type(const QString &qName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes4typeERK7QString(
    const QXmlAttributes *self,
    const QString *qName) {
  return new QString(self->type(*qName));
}

//  QString QXmlAttributes::type(const QString &uri, const QString
//      &localName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes4typeERK7QStringS2_(
    const QXmlAttributes *self,
    const QString *uri,
    const QString *localName) {
  return new QString(self->type(*uri, *localName));
}

//  QString QXmlAttributes::value(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes5valueEi(
    const QXmlAttributes *self,
    int index) {
  return new QString(self->value(index));
}

//  QString QXmlAttributes::value(const QString &qName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes5valueERK7QString(
    const QXmlAttributes *self,
    const QString *qName) {
  return new QString(self->value(*qName));
}

//  QString QXmlAttributes::value(QLatin1String qName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes5valueE13QLatin1String(
    const QXmlAttributes *self,
    const QLatin1String *qName) {
  return new QString(self->value(*qName));
}

//  QString QXmlAttributes::value(const QString &uri, const QString
//      &localName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QXmlAttributes5valueERK7QStringS2_(
    const QXmlAttributes *self,
    const QString *uri,
    const QString *localName) {
  return new QString(self->value(*uri, *localName));
}

//  void QXmlAttributes::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXmlAttributes5clearEv(QXmlAttributes *self) {
  self->clear();
}

//  void QXmlAttributes::append(const QString &qName, const QString &uri,
//      const QString &localPart, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXmlAttributes6appendERK7QStringS2_S2_S2_(
    QXmlAttributes *self,
    const QString *qName,
    const QString *uri,
    const QString *localPart,
    const QString *value) {
  self->append(*qName, *uri, *localPart, *value);
}
