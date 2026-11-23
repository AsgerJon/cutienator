//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetatype.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetatype.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdebug.h>

//  int QMetaType::type(const char *typeName)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType4typeEPKc(const char *typeName) {
  return QMetaType::type(typeName);
}

//  const char *QMetaType::typeName(int type)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN9QMetaType8typeNameEi(int type) {
  return QMetaType::typeName(type);
}

//  int QMetaType::sizeOf(int type)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType6sizeOfEi(int type) {
  return QMetaType::sizeOf(type);
}

//  TypeFlags QMetaType::typeFlags(int type)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType9typeFlagsEi(int type) {
  return static_cast<int>(QMetaType::typeFlags(type).toInt());
}

//  const QMetaObject *QMetaType::metaObjectForType(int type)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN9QMetaType17metaObjectForTypeEi(int type) {
  return QMetaType::metaObjectForType(type);
}

//  bool QMetaType::isRegistered(int type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType12isRegisteredEi(int type) {
  return QMetaType::isRegistered(type);
}

//  QMetaType::QMetaType(int type)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN9QMetaTypeC1Ei(int type) {
  return new QMetaType(type);
}

//  QMetaType::QMetaType()
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN9QMetaTypeC1Ev() {
  return new QMetaType();
}

//  void QMetaType::registerType() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QMetaType12registerTypeEv(const QMetaType *self) {
  self->registerType();
}

//  int QMetaType::id(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaType2idEi(const QMetaType *self, int a0) {
  return self->id(a0);
}

//  int QMetaType::rawId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaType5rawIdEv(const QMetaType *self) {
  return self->rawId();
}

//  qsizetype QMetaType::sizeOf() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QMetaType6sizeOfEv(const QMetaType *self) {
  return self->sizeOf();
}

//  qsizetype QMetaType::alignOf() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QMetaType7alignOfEv(const QMetaType *self) {
  return self->alignOf();
}

//  TypeFlags QMetaType::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaType5flagsEv(const QMetaType *self) {
  return static_cast<int>(self->flags().toInt());
}

//  const QMetaObject *QMetaType::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QMetaType10metaObjectEv(
    const QMetaType *self) {
  return self->metaObject();
}

//  const char *QMetaType::name() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK9QMetaType4nameEv(const QMetaType *self) {
  return self->name();
}

//  bool QMetaType::isDefaultConstructible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType22isDefaultConstructibleEv(const QMetaType *self) {
  return self->isDefaultConstructible();
}

//  bool QMetaType::isCopyConstructible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType19isCopyConstructibleEv(const QMetaType *self) {
  return self->isCopyConstructible();
}

//  bool QMetaType::isMoveConstructible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType19isMoveConstructibleEv(const QMetaType *self) {
  return self->isMoveConstructible();
}

//  bool QMetaType::isDestructible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType14isDestructibleEv(const QMetaType *self) {
  return self->isDestructible();
}

//  bool QMetaType::isEqualityComparable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType20isEqualityComparableEv(const QMetaType *self) {
  return self->isEqualityComparable();
}

//  bool QMetaType::isOrdered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType9isOrderedEv(const QMetaType *self) {
  return self->isOrdered();
}

//  bool QMetaType::hasRegisteredDataStreamOperators() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType32hasRegisteredDataStreamOperatorsEv(
    const QMetaType *self) {
  return self->hasRegisteredDataStreamOperators();
}

//  QMetaType QMetaType::underlyingType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK9QMetaType14underlyingTypeEv(const QMetaType *self) {
  return new QMetaType(self->underlyingType());
}

//  QMetaType QMetaType::fromName(QByteArrayView name)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN9QMetaType8fromNameE14QByteArrayView(
    const QByteArrayView *name) {
  return new QMetaType(QMetaType::fromName(*name));
}

//  bool operator==(const QMetaType &lhs, const QMetaType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QMetaTypeS1_(const QMetaType *lhs, const QMetaType *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMetaType &lhs, const QMetaType &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QMetaTypeS1_(const QMetaType *lhs, const QMetaType *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QDebug operator<<(QDebug d, QMetaType m)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebug9QMetaType(const QDebug *d, const QMetaType *m) {
  return new QDebug(operator<<(*d, *m));
}

//  bool QMetaType::hasRegisteredDebugStreamOperator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType32hasRegisteredDebugStreamOperatorEv(
    const QMetaType *self) {
  return self->hasRegisteredDebugStreamOperator();
}

//  bool QMetaType::hasRegisteredDebugStreamOperator(int typeId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorEi(int typeId) {
  return QMetaType::hasRegisteredDebugStreamOperator(typeId);
}

//  bool QMetaType::canConvert(QMetaType fromType, QMetaType toType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType10canConvertES_S_(
    const QMetaType *fromType,
    const QMetaType *toType) {
  return QMetaType::canConvert(*fromType, *toType);
}

//  bool QMetaType::canView(QMetaType fromType, QMetaType toType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType7canViewES_S_(
    const QMetaType *fromType,
    const QMetaType *toType) {
  return QMetaType::canView(*fromType, *toType);
}

//  bool QMetaType::hasRegisteredConverterFunction(QMetaType fromType,
//      QMetaType toType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType30hasRegisteredConverterFunctionES_S_(
    const QMetaType *fromType,
    const QMetaType *toType) {
  return QMetaType::hasRegisteredConverterFunction(*fromType, *toType);
}

//  bool QMetaType::hasRegisteredMutableViewFunction(QMetaType fromType,
//      QMetaType toType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredMutableViewFunctionES_S_(
    const QMetaType *fromType,
    const QMetaType *toType) {
  return QMetaType::hasRegisteredMutableViewFunction(*fromType, *toType);
}

//  void QMetaType::unregisterConverterFunction(QMetaType from, QMetaType to)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType27unregisterConverterFunctionES_S_(
    const QMetaType *from,
    const QMetaType *to) {
  QMetaType::unregisterConverterFunction(*from, *to);
}

//  void QMetaType::unregisterMutableViewFunction(QMetaType from, QMetaType
//      to)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType29unregisterMutableViewFunctionES_S_(
    const QMetaType *from,
    const QMetaType *to) {
  QMetaType::unregisterMutableViewFunction(*from, *to);
}

//  void QMetaType::unregisterMetaType(QMetaType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType18unregisterMetaTypeES_(const QMetaType *type) {
  QMetaType::unregisterMetaType(*type);
}

//  int QMetaType::registerHelper() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaType14registerHelperEv(const QMetaType *self) {
  return self->registerHelper();
}

//  QMetaType::~QMetaType()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaTypeD1Ev(QMetaType *self) {
  delete self;
}
