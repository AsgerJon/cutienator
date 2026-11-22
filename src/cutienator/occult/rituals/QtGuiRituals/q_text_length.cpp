//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtCore/qvariant.h>

//  QTextLength::QTextLength()
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZN11QTextLengthC1Ev() {
  return new QTextLength();
}

//  QTextLength::QTextLength(Type type, qreal value)
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZN11QTextLengthC1ENS_4TypeEd(
    QTextLength::Type type,
    qreal value) {
  return new QTextLength(type, value);
}

//  Type QTextLength::type() const
extern "C" Q_DECL_EXPORT
QTextLength::Type ritual_ZNK11QTextLength4typeEv(const QTextLength *self) {
  return self->type();
}

//  qreal QTextLength::value(qreal maximumLength) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QTextLength5valueEd(
    const QTextLength *self,
    qreal maximumLength) {
  return self->value(maximumLength);
}

//  qreal QTextLength::rawValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QTextLength8rawValueEv(const QTextLength *self) {
  return self->rawValue();
}

//  bool QTextLength::operator==(const QTextLength &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextLengtheqERKS_(
    const QTextLength *self,
    const QTextLength *other) {
  return self->operator==(*other);
}

//  bool QTextLength::operator!=(const QTextLength &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextLengthneERKS_(
    const QTextLength *self,
    const QTextLength *other) {
  return self->operator!=(*other);
}

//  QVariant QTextLength::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QTextLengthcv8QVariantEv(const QTextLength *self) {
  return new QVariant(self->operator QVariant());
}

//  QTextLength::~QTextLength()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLengthD1Ev(QTextLength *self) {
  delete self;
}
