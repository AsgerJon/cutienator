//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlPropertyIndex::QQmlPropertyIndex()
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZN17QQmlPropertyIndexC1Ev() {
  return new QQmlPropertyIndex();
}

//  QQmlPropertyIndex QQmlPropertyIndex::fromEncoded(qint32 encodedIndex)
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZN17QQmlPropertyIndex11fromEncodedEi(
    qint32 encodedIndex) {
  return new QQmlPropertyIndex(QQmlPropertyIndex::fromEncoded(encodedIndex));
}

//  QQmlPropertyIndex::QQmlPropertyIndex(int coreIndex)
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZN17QQmlPropertyIndexC1Ei(int coreIndex) {
  return new QQmlPropertyIndex(coreIndex);
}

//  QQmlPropertyIndex::QQmlPropertyIndex(int coreIndex, int valueTypeIndex)
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZN17QQmlPropertyIndexC1Eii(
    int coreIndex,
    int valueTypeIndex) {
  return new QQmlPropertyIndex(coreIndex, valueTypeIndex);
}

//  bool QQmlPropertyIndex::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyIndex7isValidEv(const QQmlPropertyIndex *self) {
  return self->isValid();
}

//  int QQmlPropertyIndex::coreIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyIndex9coreIndexEv(
    const QQmlPropertyIndex *self) {
  return self->coreIndex();
}

//  int QQmlPropertyIndex::valueTypeIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyIndex14valueTypeIndexEv(
    const QQmlPropertyIndex *self) {
  return self->valueTypeIndex();
}

//  bool QQmlPropertyIndex::hasValueTypeIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyIndex17hasValueTypeIndexEv(
    const QQmlPropertyIndex *self) {
  return self->hasValueTypeIndex();
}

//  qint32 QQmlPropertyIndex::toEncoded() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK17QQmlPropertyIndex9toEncodedEv(
    const QQmlPropertyIndex *self) {
  return self->toEncoded();
}

//  int QQmlPropertyIndex::intValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyIndex8intValueEv(const QQmlPropertyIndex *self) {
  return self->intValue();
}

//  bool QQmlPropertyIndex::operator==(const QQmlPropertyIndex &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyIndexeqERKS_(
    const QQmlPropertyIndex *self,
    const QQmlPropertyIndex *other) {
  return self->operator==(*other);
}

//  bool QQmlPropertyIndex::operator!=(const QQmlPropertyIndex &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyIndexneERKS_(
    const QQmlPropertyIndex *self,
    const QQmlPropertyIndex *other) {
  return self->operator!=(*other);
}

//  qint32 QQmlPropertyIndex::encode(int coreIndex, int valueTypeIndex)
extern "C" Q_DECL_EXPORT
qint32 ritual_ZN17QQmlPropertyIndex6encodeEii(
    int coreIndex,
    int valueTypeIndex) {
  return QQmlPropertyIndex::encode(coreIndex, valueTypeIndex);
}

//  QQmlPropertyIndex::~QQmlPropertyIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyIndexD1Ev(QQmlPropertyIndex *self) {
  delete self;
}
