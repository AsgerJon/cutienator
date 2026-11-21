//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qxmlstream.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QXmlStreamAttributes::QXmlStreamAttributes()
extern "C" Q_DECL_EXPORT
QXmlStreamAttributes *ritual_ZN20QXmlStreamAttributesC1Ev() {
  return new QXmlStreamAttributes();
}

//  QStringView QXmlStreamAttributes::value(QAnyStringView namespaceUri,
//      QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QXmlStreamAttributes5valueE14QAnyStringViewS0_(
    const QXmlStreamAttributes *self,
    const QString *namespaceUri,
    const QString *name) {
  return new QString(
      self->value(
          QAnyStringView(*namespaceUri),
          QAnyStringView(*name)).toString());
}

//  QStringView QXmlStreamAttributes::value(QAnyStringView qualifiedName)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QXmlStreamAttributes5valueE14QAnyStringView(
    const QXmlStreamAttributes *self,
    const QString *qualifiedName) {
  return new QString(self->value(QAnyStringView(*qualifiedName)).toString());
}

//  void QXmlStreamAttributes::append(const QString &namespaceUri, const
//      QString &name, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlStreamAttributes6appendERK7QStringS2_S2_(
    QXmlStreamAttributes *self,
    const QString *namespaceUri,
    const QString *name,
    const QString *value) {
  self->append(*namespaceUri, *name, *value);
}

//  void QXmlStreamAttributes::append(const QString &qualifiedName, const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlStreamAttributes6appendERK7QStringS2_(
    QXmlStreamAttributes *self,
    const QString *qualifiedName,
    const QString *value) {
  self->append(*qualifiedName, *value);
}

//  bool QXmlStreamAttributes::hasAttribute(QAnyStringView qualifiedName)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QXmlStreamAttributes12hasAttributeE14QAnyStringView(
    const QXmlStreamAttributes *self,
    const QString *qualifiedName) {
  return self->hasAttribute(QAnyStringView(*qualifiedName));
}

//  bool QXmlStreamAttributes::hasAttribute(QAnyStringView namespaceUri,
//      QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QXmlStreamAttributes12hasAttributeE14QAnyStringViewS0_(
    const QXmlStreamAttributes *self,
    const QString *namespaceUri,
    const QString *name) {
  return self->hasAttribute(
      QAnyStringView(*namespaceUri),
      QAnyStringView(*name));
}

//  QXmlStreamAttributes::~QXmlStreamAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QXmlStreamAttributesD1Ev(QXmlStreamAttributes *self) {
  delete self;
}
