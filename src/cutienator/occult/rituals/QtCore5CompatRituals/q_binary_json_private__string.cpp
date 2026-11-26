//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  QBinaryJsonPrivate::String::String(const char *data)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::String *ritual_ZN18QBinaryJsonPrivate6StringC1EPKc(
    const char *data) {
  return new QBinaryJsonPrivate::String(data);
}

//  uint QBinaryJsonPrivate::String::byteSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate6String8byteSizeEv(
    const QBinaryJsonPrivate::String *self) {
  return self->byteSize();
}

//  bool QBinaryJsonPrivate::String::isValid(uint maxSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate6String7isValidEj(
    const QBinaryJsonPrivate::String *self,
    uint maxSize) {
  return self->isValid(maxSize);
}

//  void QBinaryJsonPrivate::String::copy(char *dest, QStringView str)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate6String4copyEPc11QStringView(
    char *dest,
    const QString *str) {
  QBinaryJsonPrivate::String::copy(dest, QStringView(*str));
}

//  void QBinaryJsonPrivate::String::fillTrailingZeros(Data *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate6String17fillTrailingZerosEPNS0_4DataE(
    QBinaryJsonPrivate::String::Data *data) {
  QBinaryJsonPrivate::String::fillTrailingZeros(data);
}

//  bool QBinaryJsonPrivate::String::operator==(QStringView str) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate6StringeqE11QStringView(
    const QBinaryJsonPrivate::String *self,
    const QString *str) {
  return self->operator==(QStringView(*str));
}

//  bool QBinaryJsonPrivate::String::operator==(const String &str) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate6StringeqERKS0_(
    const QBinaryJsonPrivate::String *self,
    const QBinaryJsonPrivate::String *str) {
  return self->operator==(*str);
}

//  QString QBinaryJsonPrivate::String::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QBinaryJsonPrivate6String8toStringEv(
    const QBinaryJsonPrivate::String *self) {
  return new QString(self->toString());
}

//  QBinaryJsonPrivate::String::~String()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate6StringD1Ev(
    QBinaryJsonPrivate::String *self) {
  delete self;
}
