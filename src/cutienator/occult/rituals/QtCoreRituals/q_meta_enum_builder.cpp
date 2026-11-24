//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>

//  QMetaEnumBuilder::QMetaEnumBuilder()
extern "C" Q_DECL_EXPORT
QMetaEnumBuilder *ritual_ZN16QMetaEnumBuilderC1Ev() {
  return new QMetaEnumBuilder();
}

//  int QMetaEnumBuilder::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QMetaEnumBuilder5indexEv(const QMetaEnumBuilder *self) {
  return self->index();
}

//  QByteArray QMetaEnumBuilder::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QMetaEnumBuilder4nameEv(
    const QMetaEnumBuilder *self) {
  return new QByteArray(self->name());
}

//  QByteArray QMetaEnumBuilder::enumName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QMetaEnumBuilder8enumNameEv(
    const QMetaEnumBuilder *self) {
  return new QByteArray(self->enumName());
}

//  void QMetaEnumBuilder::setEnumName(const QByteArray &alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilder11setEnumNameERK10QByteArray(
    QMetaEnumBuilder *self,
    const QByteArray *alias) {
  self->setEnumName(*alias);
}

//  QMetaType QMetaEnumBuilder::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK16QMetaEnumBuilder8metaTypeEv(
    const QMetaEnumBuilder *self) {
  return new QMetaType(self->metaType());
}

//  void QMetaEnumBuilder::setMetaType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilder11setMetaTypeE9QMetaType(
    QMetaEnumBuilder *self,
    const QMetaType *metaType) {
  self->setMetaType(*metaType);
}

//  bool QMetaEnumBuilder::isFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaEnumBuilder6isFlagEv(const QMetaEnumBuilder *self) {
  return self->isFlag();
}

//  void QMetaEnumBuilder::setIsFlag(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilder9setIsFlagEb(
    QMetaEnumBuilder *self,
    bool value) {
  self->setIsFlag(value);
}

//  bool QMetaEnumBuilder::isScoped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaEnumBuilder8isScopedEv(const QMetaEnumBuilder *self) {
  return self->isScoped();
}

//  void QMetaEnumBuilder::setIsScoped(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilder11setIsScopedEb(
    QMetaEnumBuilder *self,
    bool value) {
  self->setIsScoped(value);
}

//  bool QMetaEnumBuilder::is64Bit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaEnumBuilder7is64BitEv(const QMetaEnumBuilder *self) {
  return self->is64Bit();
}

//  void QMetaEnumBuilder::setIs64Bit(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilder10setIs64BitEb(
    QMetaEnumBuilder *self,
    bool value) {
  self->setIs64Bit(value);
}

//  int QMetaEnumBuilder::keyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QMetaEnumBuilder8keyCountEv(const QMetaEnumBuilder *self) {
  return self->keyCount();
}

//  QByteArray QMetaEnumBuilder::key(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QMetaEnumBuilder3keyEi(
    const QMetaEnumBuilder *self,
    int index) {
  return new QByteArray(self->key(index));
}

//  int QMetaEnumBuilder::value(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QMetaEnumBuilder5valueEi(
    const QMetaEnumBuilder *self,
    int index) {
  return self->value(index);
}

//  int QMetaEnumBuilder::addKey(const QByteArray &name, int value)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QMetaEnumBuilder6addKeyERK10QByteArrayi(
    QMetaEnumBuilder *self,
    const QByteArray *name,
    int value) {
  return self->addKey(*name, value);
}

//  int QMetaEnumBuilder::addKey(const QByteArray &name, quint64 value)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QMetaEnumBuilder6addKeyERK10QByteArrayy(
    QMetaEnumBuilder *self,
    const QByteArray *name,
    quint64 value) {
  return self->addKey(*name, value);
}

//  void QMetaEnumBuilder::removeKey(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilder9removeKeyEi(
    QMetaEnumBuilder *self,
    int index) {
  self->removeKey(index);
}

//  QMetaEnumBuilder::QMetaEnumBuilder(const QMetaObjectBuilder *mobj, int
//      index)
extern "C" Q_DECL_EXPORT
QMetaEnumBuilder *ritual_ZN16QMetaEnumBuilderC1EPK18QMetaObjectBuilderi(
    const QMetaObjectBuilder *mobj,
    int index) {
  return new QMetaEnumBuilder(mobj, index);
}

//  QMetaEnumBuilder::~QMetaEnumBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaEnumBuilderD1Ev(QMetaEnumBuilder *self) {
  delete self;
}
