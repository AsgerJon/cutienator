//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusargument.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusargument.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtDBus/qdbusunixfiledescriptor.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

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

//  QDBusArgument::QDBusArgument(QDBusArgument &&other)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentC1EOS_(QDBusArgument *other) {
  return new QDBusArgument(std::move(*other));
}

//  QDBusArgument &QDBusArgument::operator=(QDBusArgument &&other)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentaSEOS_(
    QDBusArgument *self,
    QDBusArgument *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDBusArgument &QDBusArgument::operator=(const QDBusArgument &other)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentaSERKS_(
    QDBusArgument *self,
    const QDBusArgument *other) {
  return &(self->operator=(*other));
}

//  QDBusArgument::~QDBusArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgumentD1Ev(QDBusArgument *self) {
  delete self;
}

//  void QDBusArgument::swap(QDBusArgument &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusArgument4swapERS_(
    QDBusArgument *self,
    QDBusArgument *other) {
  self->swap(*other);
}

//  QDBusArgument &QDBusArgument::operator<<(uchar arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEh(QDBusArgument *self, uchar arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(bool arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEb(QDBusArgument *self, bool arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(short arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEs(QDBusArgument *self, short arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(ushort arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEt(
    QDBusArgument *self,
    ushort arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(int arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEi(QDBusArgument *self, int arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(uint arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEj(QDBusArgument *self, uint arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(qlonglong arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEx(
    QDBusArgument *self,
    qlonglong arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(qulonglong arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEy(
    QDBusArgument *self,
    qulonglong arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(double arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsEd(
    QDBusArgument *self,
    double arg) {
  return &(self->operator<<(arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QString &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK7QString(
    QDBusArgument *self,
    const QString *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QDBusVariant &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK12QDBusVariant(
    QDBusArgument *self,
    const QDBusVariant *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QDBusObjectPath &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK15QDBusObjectPath(
    QDBusArgument *self,
    const QDBusObjectPath *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QDBusSignature &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK14QDBusSignature(
    QDBusArgument *self,
    const QDBusSignature *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QDBusUnixFileDescriptor
//      &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK23QDBusUnixFileDescriptor(
    QDBusArgument *self,
    const QDBusUnixFileDescriptor *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QStringList &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK5QListI7QStringE(
    QDBusArgument *self,
    const QList<QString> *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusArgument &QDBusArgument::operator<<(const QByteArray &arg)
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZN13QDBusArgumentlsERK10QByteArray(
    QDBusArgument *self,
    const QByteArray *arg) {
  return &(self->operator<<(*arg));
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

//  const QDBusArgument &QDBusArgument::operator>>(QString &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER7QString(
    const QDBusArgument *self,
    QString *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(QDBusVariant &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER12QDBusVariant(
    const QDBusArgument *self,
    QDBusVariant *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(QDBusObjectPath &arg)
//      const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER15QDBusObjectPath(
    const QDBusArgument *self,
    QDBusObjectPath *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(QDBusSignature &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER14QDBusSignature(
    const QDBusArgument *self,
    QDBusSignature *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(QDBusUnixFileDescriptor
//      &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER23QDBusUnixFileDescriptor(
    const QDBusArgument *self,
    QDBusUnixFileDescriptor *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(QStringList &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER5QListI7QStringE(
    const QDBusArgument *self,
    QStringList *arg) {
  return new QDBusArgument(self->operator>>(*arg));
}

//  const QDBusArgument &QDBusArgument::operator>>(QByteArray &arg) const
extern "C" Q_DECL_EXPORT
QDBusArgument *ritual_ZNK13QDBusArgumentrsER10QByteArray(
    const QDBusArgument *self,
    QByteArray *arg) {
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
