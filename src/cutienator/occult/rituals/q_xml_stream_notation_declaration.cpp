//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qxmlstream.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

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

//  QXmlStreamNotationDeclaration::~QXmlStreamNotationDeclaration()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QXmlStreamNotationDeclarationD1Ev(
    QXmlStreamNotationDeclaration *self) {
  delete self;
}
