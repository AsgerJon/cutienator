//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetatype.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetatype.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

#if QT_DEPRECATED_SINCE(6, 0)
//  int QMetaType::type(const char *typeName)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType4typeEPKc(const char *typeName) {
  return QMetaType::type(typeName);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  const char *QMetaType::typeName(int type)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN9QMetaType8typeNameEi(int type) {
  return QMetaType::typeName(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  int QMetaType::sizeOf(int type)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType6sizeOfEi(int type) {
  return QMetaType::sizeOf(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  TypeFlags QMetaType::typeFlags(int type)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType9typeFlagsEi(int type) {
  return static_cast<int>(QMetaType::typeFlags(type).toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  const QMetaObject *QMetaType::metaObjectForType(int type)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN9QMetaType17metaObjectForTypeEi(int type) {
  return QMetaType::metaObjectForType(type);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

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

//  QMetaType::QMetaType(const QtPrivate::QMetaTypeInterface *d)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN9QMetaTypeC1EPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *d) {
  return new QMetaType(d);
}

//  QMetaType::QMetaType()
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN9QMetaTypeC1Ev() {
  return new QMetaType();
}

//  bool QMetaType::isValid(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType7isValidEN2Qt15Disambiguated_tE(
    const QMetaType *self,
    const Qt::Disambiguated_t *a0) {
  return self->isValid(*a0);
}

//  bool QMetaType::isRegistered(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType12isRegisteredEN2Qt15Disambiguated_tE(
    const QMetaType *self,
    const Qt::Disambiguated_t *a0) {
  return self->isRegistered(*a0);
}

//  void QMetaType::registerType() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QMetaType12registerTypeEv(const QMetaType *self) {
  self->registerType();
}

#if !(QT_CORE_REMOVED_SINCE(6, 1) || defined(Q_QDOC))
//  int QMetaType::id(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QMetaType2idEi(const QMetaType *self, int a0) {
  return self->id(a0);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 1) || defined(Q_QDOC))

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

#if !defined(QT_NO_DATASTREAM)
//  bool QMetaType::hasRegisteredDataStreamOperators() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType32hasRegisteredDataStreamOperatorsEv(
    const QMetaType *self) {
  return self->hasRegisteredDataStreamOperators();
}
#endif  // !defined(QT_NO_DATASTREAM)

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

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug d, QMetaType m)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebug9QMetaType(const QDebug *d, const QMetaType *m) {
  return new QDebug(operator<<(*d, *m));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  bool QMetaType::hasRegisteredDebugStreamOperator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType32hasRegisteredDebugStreamOperatorEv(
    const QMetaType *self) {
  return self->hasRegisteredDebugStreamOperator();
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
#if QT_DEPRECATED_SINCE(6, 0)
//  bool QMetaType::hasRegisteredDebugStreamOperator(int typeId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorEi(int typeId) {
  return QMetaType::hasRegisteredDebugStreamOperator(typeId);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)
#endif  // !defined(QT_NO_DEBUG_STREAM)

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

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  const QtPrivate::QMetaTypeInterface *QMetaType::iface()
extern "C" Q_DECL_EXPORT
const QtPrivate::QMetaTypeInterface *ritual_ZN9QMetaType5ifaceEv(
    QMetaType *self) {
  return self->iface();
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  const QtPrivate::QMetaTypeInterface *QMetaType::iface() const
extern "C" Q_DECL_EXPORT
const QtPrivate::QMetaTypeInterface *ritual_ZNK9QMetaType5ifaceEv(
    const QMetaType *self) {
  return self->iface();
}

//  bool QMetaType::isDefaultConstructible(const
//      QtPrivate::QMetaTypeInterface *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType22isDefaultConstructibleEPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *a0) {
  return QMetaType::isDefaultConstructible(a0);
}

//  bool QMetaType::isCopyConstructible(const QtPrivate::QMetaTypeInterface
//      *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType19isCopyConstructibleEPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *a0) {
  return QMetaType::isCopyConstructible(a0);
}

//  bool QMetaType::isMoveConstructible(const QtPrivate::QMetaTypeInterface
//      *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType19isMoveConstructibleEPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *a0) {
  return QMetaType::isMoveConstructible(a0);
}

//  bool QMetaType::isDestructible(const QtPrivate::QMetaTypeInterface *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType14isDestructibleEPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *a0) {
  return QMetaType::isDestructible(a0);
}

//  int QMetaType::registerHelper(const QtPrivate::QMetaTypeInterface *iface)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType14registerHelperEPKN9QtPrivate18QMetaTypeInterfaceE(
    const QtPrivate::QMetaTypeInterface *iface) {
  return QMetaType::registerHelper(iface);
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

//  QList<QMetaType>::QList()
extern "C" Q_DECL_EXPORT
QList<QMetaType> *ritual_list_make_QMetaType() {
  return new QList<QMetaType>();
}

//  void QList<QMetaType>::append(const QMetaType &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QMetaType(
    QList<QMetaType> *self,
    const QMetaType *element) {
  self->append(*element);
}

//  qsizetype QList<QMetaType>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QMetaType(const QList<QMetaType> *self) {
  return self->size();
}

//  const QMetaType &QList<QMetaType>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_list_at_QMetaType(
    const QList<QMetaType> *self,
    long long index) {
  return new QMetaType(self->at(index));
}

//  QList<QMetaType>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QMetaType(QList<QMetaType> *self) {
  delete self;
}
