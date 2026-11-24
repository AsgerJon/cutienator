//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  int QBinaryJsonPrivate::Value::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QBinaryJsonPrivate5Value8intValueEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->intValue();
}

//  const char *QBinaryJsonPrivate::Value::data(const Base *b) const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK18QBinaryJsonPrivate5Value4dataEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->data(b);
}

//  bool QBinaryJsonPrivate::Value::toBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Value9toBooleanEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->toBoolean();
}

//  double QBinaryJsonPrivate::Value::toDouble(const Base *b) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK18QBinaryJsonPrivate5Value8toDoubleEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->toDouble(b);
}

//  QString QBinaryJsonPrivate::Value::toString(const Base *b) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QBinaryJsonPrivate5Value8toStringEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QString(self->toString(b));
}

//  String QBinaryJsonPrivate::Value::asString(const Base *b) const
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::String *ritual_ZNK18QBinaryJsonPrivate5Value8asStringEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QBinaryJsonPrivate::String(self->asString(b));
}

//  Latin1String QBinaryJsonPrivate::Value::asLatin1String(const Base *b)
//      const
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Latin1String *ritual_ZNK18QBinaryJsonPrivate5Value14asLatin1StringEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return new QBinaryJsonPrivate::Latin1String(self->asLatin1String(b));
}

//  const Base *QBinaryJsonPrivate::Value::base(const Base *b) const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::Base *ritual_ZNK18QBinaryJsonPrivate5Value4baseEPKNS_4BaseE(
    const QBinaryJsonPrivate::Value *self,
    const QBinaryJsonPrivate::Base *b) {
  return self->base(b);
}

//  void QBinaryJsonPrivate::Value::setIsLatinKey(bool isLatinKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value13setIsLatinKeyEb(
    QBinaryJsonPrivate::Value *self,
    bool isLatinKey) {
  self->setIsLatinKey(isLatinKey);
}

//  bool QBinaryJsonPrivate::Value::isLatinKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Value10isLatinKeyEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->isLatinKey();
}

//  void QBinaryJsonPrivate::Value::setIsLatinOrIntValue(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value20setIsLatinOrIntValueEb(
    QBinaryJsonPrivate::Value *self,
    bool v) {
  self->setIsLatinOrIntValue(v);
}

//  bool QBinaryJsonPrivate::Value::isLatinOrIntValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Value17isLatinOrIntValueEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->isLatinOrIntValue();
}

//  void QBinaryJsonPrivate::Value::setType(uint type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value7setTypeEj(
    QBinaryJsonPrivate::Value *self,
    uint type) {
  self->setType(type);
}

//  uint QBinaryJsonPrivate::Value::type() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate5Value4typeEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->type();
}

//  void QBinaryJsonPrivate::Value::setValue(uint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5Value8setValueEj(
    QBinaryJsonPrivate::Value *self,
    uint value) {
  self->setValue(value);
}

//  uint QBinaryJsonPrivate::Value::value() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate5Value5valueEv(
    const QBinaryJsonPrivate::Value *self) {
  return self->value();
}

//  QBinaryJsonPrivate::Value::~Value()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5ValueD1Ev(
    QBinaryJsonPrivate::Value *self) {
  delete self;
}
