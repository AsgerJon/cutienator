//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusargument.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusargument.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QDBusArgument::QDBusArgument()
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentC1Ev() {
  return new QDBusArgument();
}

//  QDBusArgument::QDBusArgument(const QDBusArgument &other)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentC1ERKS_(const QDBusArgument *other) {
  return new QDBusArgument(*other);
}

//  QDBusArgument::~QDBusArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgumentD1Ev(QDBusArgument *self) {
  delete self;
}

//  void QDBusArgument::beginStructure()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument14beginStructureEv(QDBusArgument *self) {
  self->beginStructure();
}

//  void QDBusArgument::endStructure()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument12endStructureEv(QDBusArgument *self) {
  self->endStructure();
}

//  void QDBusArgument::beginArray(int elementMetaTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument10beginArrayEi(
    QDBusArgument *self,
    int elementMetaTypeId) {
  self->beginArray(elementMetaTypeId);
}

//  void QDBusArgument::beginArray(QMetaType elementMetaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument10beginArrayE9QMetaType(
    QDBusArgument *self,
    const QMetaType *elementMetaType) {
  self->beginArray(*elementMetaType);
}

//  void QDBusArgument::endArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument8endArrayEv(QDBusArgument *self) {
  self->endArray();
}

//  void QDBusArgument::beginMap(int keyMetaTypeId, int valueMetaTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument8beginMapEii(
    QDBusArgument *self,
    int keyMetaTypeId,
    int valueMetaTypeId) {
  self->beginMap(keyMetaTypeId, valueMetaTypeId);
}

//  void QDBusArgument::beginMap(QMetaType keyMetaType, QMetaType
//      valueMetaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument8beginMapE9QMetaTypeS0_(
    QDBusArgument *self,
    const QMetaType *keyMetaType,
    const QMetaType *valueMetaType) {
  self->beginMap(*keyMetaType, *valueMetaType);
}

//  void QDBusArgument::endMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument6endMapEv(QDBusArgument *self) {
  self->endMap();
}

//  void QDBusArgument::beginMapEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument13beginMapEntryEv(QDBusArgument *self) {
  self->beginMapEntry();
}

//  void QDBusArgument::endMapEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument11endMapEntryEv(QDBusArgument *self) {
  self->endMapEntry();
}

//  void QDBusArgument::appendVariant(const QVariant &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument13appendVariantERK8QVariant(
    QDBusArgument *self,
    const QVariant *v) {
  self->appendVariant(*v);
}

//  QString QDBusArgument::currentSignature() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusArgument16currentSignatureEv(
    const QDBusArgument *self) {
  return new QString(self->currentSignature());
}

//  ElementType QDBusArgument::currentType() const
extern "C" Q_DECL_EXPORT
QDBusArgument::ElementType ritual_ZNK13QDBusArgument11currentTypeEv(
    const QDBusArgument *self) {
  return self->currentType();
}

//  const QDBusArgument &QDBusArgument::operator>>(uchar &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERh(
    const QDBusArgument *self,
    uchar *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(bool &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERb(
    const QDBusArgument *self,
    bool *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(short &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERs(
    const QDBusArgument *self,
    short *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(ushort &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERt(
    const QDBusArgument *self,
    ushort *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(int &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERi(
    const QDBusArgument *self,
    int *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(uint &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERj(
    const QDBusArgument *self,
    uint *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(qlonglong &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERx(
    const QDBusArgument *self,
    qlonglong *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(qulonglong &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERy(
    const QDBusArgument *self,
    qulonglong *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(double &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsERd(
    const QDBusArgument *self,
    double *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  void QDBusArgument::beginStructure() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument14beginStructureEv(const QDBusArgument *self) {
  self->beginStructure();
}

//  void QDBusArgument::endStructure() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument12endStructureEv(const QDBusArgument *self) {
  self->endStructure();
}

//  void QDBusArgument::beginArray() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument10beginArrayEv(const QDBusArgument *self) {
  self->beginArray();
}

//  void QDBusArgument::endArray() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument8endArrayEv(const QDBusArgument *self) {
  self->endArray();
}

//  void QDBusArgument::beginMap() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument8beginMapEv(const QDBusArgument *self) {
  self->beginMap();
}

//  void QDBusArgument::endMap() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument6endMapEv(const QDBusArgument *self) {
  self->endMap();
}

//  void QDBusArgument::beginMapEntry() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument13beginMapEntryEv(const QDBusArgument *self) {
  self->beginMapEntry();
}

//  void QDBusArgument::endMapEntry() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QDBusArgument11endMapEntryEv(const QDBusArgument *self) {
  self->endMapEntry();
}

//  bool QDBusArgument::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDBusArgument5atEndEv(const QDBusArgument *self) {
  return self->atEnd();
}

//  QVariant QDBusArgument::asVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QDBusArgument9asVariantEv(const QDBusArgument *self) {
  return new QVariant(self->asVariant());
}

//  QDBusArgument::QDBusArgument(QDBusArgumentPrivate *d)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentC1EP20QDBusArgumentPrivate(
    QDBusArgumentPrivate *d) {
  return new QDBusArgument(d);
}

#endif  // !defined(QT_NO_DBUS)
