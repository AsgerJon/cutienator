//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QMetaPropertyBuilder::QMetaPropertyBuilder()
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilder *ritual_ZN20QMetaPropertyBuilderC1Ev() {
  return new QMetaPropertyBuilder();
}

//  int QMetaPropertyBuilder::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QMetaPropertyBuilder5indexEv(
    const QMetaPropertyBuilder *self) {
  return self->index();
}

//  QByteArray QMetaPropertyBuilder::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QMetaPropertyBuilder4nameEv(
    const QMetaPropertyBuilder *self) {
  return new QByteArray(self->name());
}

//  QByteArray QMetaPropertyBuilder::type() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QMetaPropertyBuilder4typeEv(
    const QMetaPropertyBuilder *self) {
  return new QByteArray(self->type());
}

//  bool QMetaPropertyBuilder::hasNotifySignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder15hasNotifySignalEv(
    const QMetaPropertyBuilder *self) {
  return self->hasNotifySignal();
}

//  QMetaMethodBuilder QMetaPropertyBuilder::notifySignal() const
extern "C" Q_DECL_EXPORT
QMetaMethodBuilder *ritual_ZNK20QMetaPropertyBuilder12notifySignalEv(
    const QMetaPropertyBuilder *self) {
  return new QMetaMethodBuilder(self->notifySignal());
}

//  void QMetaPropertyBuilder::setNotifySignal(const QMetaMethodBuilder
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder15setNotifySignalERK18QMetaMethodBuilder(
    QMetaPropertyBuilder *self,
    const QMetaMethodBuilder *value) {
  self->setNotifySignal(*value);
}

//  void QMetaPropertyBuilder::removeNotifySignal()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder18removeNotifySignalEv(
    QMetaPropertyBuilder *self) {
  self->removeNotifySignal();
}

//  bool QMetaPropertyBuilder::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder10isReadableEv(
    const QMetaPropertyBuilder *self) {
  return self->isReadable();
}

//  bool QMetaPropertyBuilder::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder10isWritableEv(
    const QMetaPropertyBuilder *self) {
  return self->isWritable();
}

//  bool QMetaPropertyBuilder::isResettable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder12isResettableEv(
    const QMetaPropertyBuilder *self) {
  return self->isResettable();
}

//  bool QMetaPropertyBuilder::isDesignable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder12isDesignableEv(
    const QMetaPropertyBuilder *self) {
  return self->isDesignable();
}

//  bool QMetaPropertyBuilder::isScriptable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder12isScriptableEv(
    const QMetaPropertyBuilder *self) {
  return self->isScriptable();
}

//  bool QMetaPropertyBuilder::isStored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder8isStoredEv(
    const QMetaPropertyBuilder *self) {
  return self->isStored();
}

//  bool QMetaPropertyBuilder::isUser() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder6isUserEv(
    const QMetaPropertyBuilder *self) {
  return self->isUser();
}

//  bool QMetaPropertyBuilder::hasStdCppSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder12hasStdCppSetEv(
    const QMetaPropertyBuilder *self) {
  return self->hasStdCppSet();
}

//  bool QMetaPropertyBuilder::isEnumOrFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder12isEnumOrFlagEv(
    const QMetaPropertyBuilder *self) {
  return self->isEnumOrFlag();
}

//  bool QMetaPropertyBuilder::isConstant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder10isConstantEv(
    const QMetaPropertyBuilder *self) {
  return self->isConstant();
}

//  bool QMetaPropertyBuilder::isFinal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder7isFinalEv(
    const QMetaPropertyBuilder *self) {
  return self->isFinal();
}

//  bool QMetaPropertyBuilder::isVirtual() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder9isVirtualEv(
    const QMetaPropertyBuilder *self) {
  return self->isVirtual();
}

//  bool QMetaPropertyBuilder::isOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder10isOverrideEv(
    const QMetaPropertyBuilder *self) {
  return self->isOverride();
}

//  bool QMetaPropertyBuilder::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder7isAliasEv(
    const QMetaPropertyBuilder *self) {
  return self->isAlias();
}

//  bool QMetaPropertyBuilder::isBindable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder10isBindableEv(
    const QMetaPropertyBuilder *self) {
  return self->isBindable();
}

//  bool QMetaPropertyBuilder::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaPropertyBuilder10isRequiredEv(
    const QMetaPropertyBuilder *self) {
  return self->isRequired();
}

//  void QMetaPropertyBuilder::setReadable(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setReadableEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setReadable(value);
}

//  void QMetaPropertyBuilder::setWritable(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setWritableEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setWritable(value);
}

//  void QMetaPropertyBuilder::setResettable(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder13setResettableEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setResettable(value);
}

//  void QMetaPropertyBuilder::setDesignable(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder13setDesignableEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setDesignable(value);
}

//  void QMetaPropertyBuilder::setScriptable(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder13setScriptableEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setScriptable(value);
}

//  void QMetaPropertyBuilder::setStored(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder9setStoredEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setStored(value);
}

//  void QMetaPropertyBuilder::setUser(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder7setUserEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setUser(value);
}

//  void QMetaPropertyBuilder::setStdCppSet(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder12setStdCppSetEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setStdCppSet(value);
}

//  void QMetaPropertyBuilder::setEnumOrFlag(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder13setEnumOrFlagEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setEnumOrFlag(value);
}

//  void QMetaPropertyBuilder::setConstant(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setConstantEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setConstant(value);
}

//  void QMetaPropertyBuilder::setFinal(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder8setFinalEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setFinal(value);
}

//  void QMetaPropertyBuilder::setVirtual(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder10setVirtualEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setVirtual(value);
}

//  void QMetaPropertyBuilder::setOverride(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setOverrideEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setOverride(value);
}

//  void QMetaPropertyBuilder::setAlias(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder8setAliasEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setAlias(value);
}

//  void QMetaPropertyBuilder::setBindable(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setBindableEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setBindable(value);
}

//  void QMetaPropertyBuilder::setRequired(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setRequiredEb(
    QMetaPropertyBuilder *self,
    bool value) {
  self->setRequired(value);
}

//  int QMetaPropertyBuilder::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QMetaPropertyBuilder8revisionEv(
    const QMetaPropertyBuilder *self) {
  return self->revision();
}

//  void QMetaPropertyBuilder::setRevision(int revision)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilder11setRevisionEi(
    QMetaPropertyBuilder *self,
    int revision) {
  self->setRevision(revision);
}

//  QMetaPropertyBuilder::QMetaPropertyBuilder(const QMetaObjectBuilder
//      *mobj, int index)
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilder *ritual_ZN20QMetaPropertyBuilderC1EPK18QMetaObjectBuilderi(
    const QMetaObjectBuilder *mobj,
    int index) {
  return new QMetaPropertyBuilder(mobj, index);
}

//  QMetaPropertyBuilderPrivate *QMetaPropertyBuilder::d_func() const
extern "C" Q_DECL_EXPORT
QMetaPropertyBuilderPrivate *ritual_ZNK20QMetaPropertyBuilder6d_funcEv(
    const QMetaPropertyBuilder *self) {
  return self->d_func();
}

//  QMetaPropertyBuilder::~QMetaPropertyBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaPropertyBuilderD1Ev(QMetaPropertyBuilder *self) {
  delete self;
}
