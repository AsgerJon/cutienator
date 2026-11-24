//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>

//  QBinaryJsonPrivate::Latin1String::Latin1String(const char *data)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Latin1String *ritual_ZN18QBinaryJsonPrivate12Latin1StringC1EPKc(
    const char *data) {
  return new QBinaryJsonPrivate::Latin1String(data);
}

//  uint QBinaryJsonPrivate::Latin1String::byteSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate12Latin1String8byteSizeEv(
    const QBinaryJsonPrivate::Latin1String *self) {
  return self->byteSize();
}

//  bool QBinaryJsonPrivate::Latin1String::isValid(uint maxSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate12Latin1String7isValidEj(
    const QBinaryJsonPrivate::Latin1String *self,
    uint maxSize) {
  return self->isValid(maxSize);
}

//  QLatin1String QBinaryJsonPrivate::Latin1String::toQLatin1String() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK18QBinaryJsonPrivate12Latin1String15toQLatin1StringEv(
    const QBinaryJsonPrivate::Latin1String *self) {
  return new QLatin1String(self->toQLatin1String());
}

//  QString QBinaryJsonPrivate::Latin1String::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QBinaryJsonPrivate12Latin1String8toStringEv(
    const QBinaryJsonPrivate::Latin1String *self) {
  return new QString(self->toString());
}

//  QBinaryJsonPrivate::Latin1String::~Latin1String()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate12Latin1StringD1Ev(
    QBinaryJsonPrivate::Latin1String *self) {
  delete self;
}
