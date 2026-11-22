//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qxmlstream.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  QXmlStreamEntityDeclaration::QXmlStreamEntityDeclaration()
extern "C" Q_DECL_EXPORT
QXmlStreamEntityDeclaration *ritual_ZN27QXmlStreamEntityDeclarationC1Ev() {
  return new QXmlStreamEntityDeclaration();
}

//  QStringView QXmlStreamEntityDeclaration::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QXmlStreamEntityDeclaration4nameEv(
    const QXmlStreamEntityDeclaration *self) {
  return new QString(self->name().toString());
}

//  QStringView QXmlStreamEntityDeclaration::notationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QXmlStreamEntityDeclaration12notationNameEv(
    const QXmlStreamEntityDeclaration *self) {
  return new QString(self->notationName().toString());
}

//  QStringView QXmlStreamEntityDeclaration::systemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QXmlStreamEntityDeclaration8systemIdEv(
    const QXmlStreamEntityDeclaration *self) {
  return new QString(self->systemId().toString());
}

//  QStringView QXmlStreamEntityDeclaration::publicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QXmlStreamEntityDeclaration8publicIdEv(
    const QXmlStreamEntityDeclaration *self) {
  return new QString(self->publicId().toString());
}

//  QStringView QXmlStreamEntityDeclaration::value() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QXmlStreamEntityDeclaration5valueEv(
    const QXmlStreamEntityDeclaration *self) {
  return new QString(self->value().toString());
}

//  bool operator==(const QXmlStreamEntityDeclaration &lhs, const
//      QXmlStreamEntityDeclaration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK27QXmlStreamEntityDeclarationS1_(
    const QXmlStreamEntityDeclaration *lhs,
    const QXmlStreamEntityDeclaration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QXmlStreamEntityDeclaration &lhs, const
//      QXmlStreamEntityDeclaration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK27QXmlStreamEntityDeclarationS1_(
    const QXmlStreamEntityDeclaration *lhs,
    const QXmlStreamEntityDeclaration *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QXmlStreamEntityDeclaration::~QXmlStreamEntityDeclaration()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QXmlStreamEntityDeclarationD1Ev(
    QXmlStreamEntityDeclaration *self) {
  delete self;
}
