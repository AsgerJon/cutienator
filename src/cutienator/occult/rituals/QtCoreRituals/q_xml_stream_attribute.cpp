//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(xmlstream)
#include <QtCore/qxmlstream.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QXmlStreamAttribute::QXmlStreamAttribute()
extern "C" Q_DECL_EXPORT
QXmlStreamAttribute *ritual_ZN19QXmlStreamAttributeC1Ev() {
  return new QXmlStreamAttribute();
}

//  QXmlStreamAttribute::QXmlStreamAttribute(const QString &qualifiedName,
//      const QString &value)
extern "C" Q_DECL_EXPORT
QXmlStreamAttribute *ritual_ZN19QXmlStreamAttributeC1ERK7QStringS2_(
    const QString *qualifiedName,
    const QString *value) {
  return new QXmlStreamAttribute(*qualifiedName, *value);
}

//  QXmlStreamAttribute::QXmlStreamAttribute(const QString &namespaceUri,
//      const QString &name, const QString &value)
extern "C" Q_DECL_EXPORT
QXmlStreamAttribute *ritual_ZN19QXmlStreamAttributeC1ERK7QStringS2_S2_(
    const QString *namespaceUri,
    const QString *name,
    const QString *value) {
  return new QXmlStreamAttribute(*namespaceUri, *name, *value);
}

//  QStringView QXmlStreamAttribute::namespaceUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QXmlStreamAttribute12namespaceUriEv(
    const QXmlStreamAttribute *self) {
  return new QString(self->namespaceUri().toString());
}

//  QStringView QXmlStreamAttribute::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QXmlStreamAttribute4nameEv(
    const QXmlStreamAttribute *self) {
  return new QString(self->name().toString());
}

//  QStringView QXmlStreamAttribute::qualifiedName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QXmlStreamAttribute13qualifiedNameEv(
    const QXmlStreamAttribute *self) {
  return new QString(self->qualifiedName().toString());
}

//  QStringView QXmlStreamAttribute::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QXmlStreamAttribute6prefixEv(
    const QXmlStreamAttribute *self) {
  return new QString(self->prefix().toString());
}

//  QStringView QXmlStreamAttribute::value() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QXmlStreamAttribute5valueEv(
    const QXmlStreamAttribute *self) {
  return new QString(self->value().toString());
}

//  bool QXmlStreamAttribute::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QXmlStreamAttribute9isDefaultEv(
    const QXmlStreamAttribute *self) {
  return self->isDefault();
}

//  bool operator==(const QXmlStreamAttribute &lhs, const QXmlStreamAttribute
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QXmlStreamAttributeS1_(
    const QXmlStreamAttribute *lhs,
    const QXmlStreamAttribute *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QXmlStreamAttribute &lhs, const QXmlStreamAttribute
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QXmlStreamAttributeS1_(
    const QXmlStreamAttribute *lhs,
    const QXmlStreamAttribute *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QXmlStreamAttribute::~QXmlStreamAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QXmlStreamAttributeD1Ev(QXmlStreamAttribute *self) {
  delete self;
}

#endif  // QT_CONFIG(xmlstream)
