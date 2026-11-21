//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qxmlstream.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QXmlStreamNamespaceDeclaration::QXmlStreamNamespaceDeclaration()
extern "C" Q_DECL_EXPORT
QXmlStreamNamespaceDeclaration *ritual_ZN30QXmlStreamNamespaceDeclarationC1Ev() {
  return new QXmlStreamNamespaceDeclaration();
}

//  QXmlStreamNamespaceDeclaration::QXmlStreamNamespaceDeclaration(const
//      QString &prefix, const QString &namespaceUri)
extern "C" Q_DECL_EXPORT
QXmlStreamNamespaceDeclaration *ritual_ZN30QXmlStreamNamespaceDeclarationC1ERK7QStringS2_(
    const QString *prefix,
    const QString *namespaceUri) {
  return new QXmlStreamNamespaceDeclaration(*prefix, *namespaceUri);
}

//  QStringView QXmlStreamNamespaceDeclaration::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QXmlStreamNamespaceDeclaration6prefixEv(
    const QXmlStreamNamespaceDeclaration *self) {
  return new QString(self->prefix().toString());
}

//  QStringView QXmlStreamNamespaceDeclaration::namespaceUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QXmlStreamNamespaceDeclaration12namespaceUriEv(
    const QXmlStreamNamespaceDeclaration *self) {
  return new QString(self->namespaceUri().toString());
}

//  QXmlStreamNamespaceDeclaration::~QXmlStreamNamespaceDeclaration()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QXmlStreamNamespaceDeclarationD1Ev(
    QXmlStreamNamespaceDeclaration *self) {
  delete self;
}
