//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(xmlstream)
#if QT_CONFIG(xmlstream)
#include <QtCore/qxmlstream.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>

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

//  bool operator==(const QXmlStreamNamespaceDeclaration &lhs, const
//      QXmlStreamNamespaceDeclaration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK30QXmlStreamNamespaceDeclarationS1_(
    const QXmlStreamNamespaceDeclaration *lhs,
    const QXmlStreamNamespaceDeclaration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QXmlStreamNamespaceDeclaration &lhs, const
//      QXmlStreamNamespaceDeclaration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK30QXmlStreamNamespaceDeclarationS1_(
    const QXmlStreamNamespaceDeclaration *lhs,
    const QXmlStreamNamespaceDeclaration *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QXmlStreamNamespaceDeclaration::~QXmlStreamNamespaceDeclaration()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QXmlStreamNamespaceDeclarationD1Ev(
    QXmlStreamNamespaceDeclaration *self) {
  delete self;
}

//  QList<QXmlStreamNamespaceDeclaration>::QList()
extern "C" Q_DECL_EXPORT
QList<QXmlStreamNamespaceDeclaration> *ritual_list_make_QXmlStreamNamespaceDeclaration() {
  return new QList<QXmlStreamNamespaceDeclaration>();
}

//  void QList<QXmlStreamNamespaceDeclaration>::append(const
//      QXmlStreamNamespaceDeclaration &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QXmlStreamNamespaceDeclaration(
    QList<QXmlStreamNamespaceDeclaration> *self,
    const QXmlStreamNamespaceDeclaration *element) {
  self->append(*element);
}

//  qsizetype QList<QXmlStreamNamespaceDeclaration>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QXmlStreamNamespaceDeclaration(
    const QList<QXmlStreamNamespaceDeclaration> *self) {
  return self->size();
}

//  const QXmlStreamNamespaceDeclaration
//      &QList<QXmlStreamNamespaceDeclaration>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QXmlStreamNamespaceDeclaration *ritual_list_at_QXmlStreamNamespaceDeclaration(
    const QList<QXmlStreamNamespaceDeclaration> *self,
    long long index) {
  return new QXmlStreamNamespaceDeclaration(self->at(index));
}

//  QList<QXmlStreamNamespaceDeclaration>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QXmlStreamNamespaceDeclaration(
    QList<QXmlStreamNamespaceDeclaration> *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstream)
#endif  // QT_CONFIG(xmlstream)
