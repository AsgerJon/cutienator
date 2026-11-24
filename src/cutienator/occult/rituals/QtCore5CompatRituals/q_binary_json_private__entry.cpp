//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  uint QBinaryJsonPrivate::Entry::size() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate5Entry4sizeEv(
    const QBinaryJsonPrivate::Entry *self) {
  return self->size();
}

//  String QBinaryJsonPrivate::Entry::shallowKey() const
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::String *ritual_ZNK18QBinaryJsonPrivate5Entry10shallowKeyEv(
    const QBinaryJsonPrivate::Entry *self) {
  return new QBinaryJsonPrivate::String(self->shallowKey());
}

//  Latin1String QBinaryJsonPrivate::Entry::shallowLatin1Key() const
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Latin1String *ritual_ZNK18QBinaryJsonPrivate5Entry16shallowLatin1KeyEv(
    const QBinaryJsonPrivate::Entry *self) {
  return new QBinaryJsonPrivate::Latin1String(self->shallowLatin1Key());
}

//  QString QBinaryJsonPrivate::Entry::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QBinaryJsonPrivate5Entry3keyEv(
    const QBinaryJsonPrivate::Entry *self) {
  return new QString(self->key());
}

//  bool QBinaryJsonPrivate::Entry::isValid(uint maxSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5Entry7isValidEj(
    const QBinaryJsonPrivate::Entry *self,
    uint maxSize) {
  return self->isValid(maxSize);
}

//  bool QBinaryJsonPrivate::Entry::operator==(QStringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5EntryeqE11QStringView(
    const QBinaryJsonPrivate::Entry *self,
    const QString *key) {
  return self->operator==(QStringView(*key));
}

//  bool QBinaryJsonPrivate::Entry::operator>=(QStringView key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate5EntrygeE11QStringView(
    const QBinaryJsonPrivate::Entry *self,
    const QString *key) {
  return self->operator>=(QStringView(*key));
}

//  QBinaryJsonPrivate::Entry::~Entry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate5EntryD1Ev(
    QBinaryJsonPrivate::Entry *self) {
  delete self;
}
