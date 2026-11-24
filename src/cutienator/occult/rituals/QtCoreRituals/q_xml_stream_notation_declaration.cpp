//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(xmlstream)
#include <QtCore/qxmlstream.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QXmlStreamNotationDeclaration::QXmlStreamNotationDeclaration()
extern "C" Q_DECL_EXPORT
QXmlStreamNotationDeclaration *ritual_ZN29QXmlStreamNotationDeclarationC1Ev() {
  return new QXmlStreamNotationDeclaration();
}

//  QStringView QXmlStreamNotationDeclaration::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QXmlStreamNotationDeclaration4nameEv(
    const QXmlStreamNotationDeclaration *self) {
  return new QString(self->name().toString());
}

//  QStringView QXmlStreamNotationDeclaration::systemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QXmlStreamNotationDeclaration8systemIdEv(
    const QXmlStreamNotationDeclaration *self) {
  return new QString(self->systemId().toString());
}

//  QStringView QXmlStreamNotationDeclaration::publicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QXmlStreamNotationDeclaration8publicIdEv(
    const QXmlStreamNotationDeclaration *self) {
  return new QString(self->publicId().toString());
}

//  bool operator==(const QXmlStreamNotationDeclaration &lhs, const
//      QXmlStreamNotationDeclaration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK29QXmlStreamNotationDeclarationS1_(
    const QXmlStreamNotationDeclaration *lhs,
    const QXmlStreamNotationDeclaration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QXmlStreamNotationDeclaration &lhs, const
//      QXmlStreamNotationDeclaration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK29QXmlStreamNotationDeclarationS1_(
    const QXmlStreamNotationDeclaration *lhs,
    const QXmlStreamNotationDeclaration *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QXmlStreamNotationDeclaration::~QXmlStreamNotationDeclaration()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QXmlStreamNotationDeclarationD1Ev(
    QXmlStreamNotationDeclaration *self) {
  delete self;
}

//  QList<QXmlStreamNotationDeclaration>::QList()
extern "C" Q_DECL_EXPORT
QList<QXmlStreamNotationDeclaration> *ritual_list_make_QXmlStreamNotationDeclaration() {
  return new QList<QXmlStreamNotationDeclaration>();
}

//  void QList<QXmlStreamNotationDeclaration>::append(const
//      QXmlStreamNotationDeclaration &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QXmlStreamNotationDeclaration(
    QList<QXmlStreamNotationDeclaration> *self,
    const QXmlStreamNotationDeclaration *element) {
  self->append(*element);
}

//  qsizetype QList<QXmlStreamNotationDeclaration>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QXmlStreamNotationDeclaration(
    const QList<QXmlStreamNotationDeclaration> *self) {
  return self->size();
}

//  const QXmlStreamNotationDeclaration
//      &QList<QXmlStreamNotationDeclaration>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QXmlStreamNotationDeclaration *ritual_list_at_QXmlStreamNotationDeclaration(
    const QList<QXmlStreamNotationDeclaration> *self,
    long long index) {
  return new QXmlStreamNotationDeclaration(self->at(index));
}

//  QList<QXmlStreamNotationDeclaration>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QXmlStreamNotationDeclaration(
    QList<QXmlStreamNotationDeclaration> *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstream)
