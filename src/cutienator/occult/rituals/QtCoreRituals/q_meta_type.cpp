//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetatype.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 15. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetatype.h>
#include <QtCore/qnamespace.h>
#include <QtCore/qcompare.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>

//  void QMetaType::registerNormalizedTypedef(const ::QByteArray
//      &normalizedTypeName, QMetaType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType25registerNormalizedTypedefERK10QByteArrayS_(
    const ::QByteArray *normalizedTypeName,
    const QMetaType *type) {
  QMetaType::registerNormalizedTypedef(*normalizedTypeName, *type);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  int QMetaType::type(const char *typeName)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType4typeEPKc(const char *typeName) {
  return QMetaType::type(typeName);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  int QMetaType::type(const ::QByteArray &typeName)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QMetaType4typeERK10QByteArray(const ::QByteArray *typeName) {
  return QMetaType::type(*typeName);
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

#if QT_DEPRECATED_SINCE(6, 0)
//  void *QMetaType::create(int type, const void *copy)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QMetaType6createEiPKv(int type, const void *copy) {
  return QMetaType::create(type, copy);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QMetaType::destroy(int type, void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType7destroyEiPv(int type, void *data) {
  QMetaType::destroy(type, data);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void *QMetaType::construct(int type, void *where, const void *copy)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QMetaType9constructEiPvPKv(
    int type,
    void *where,
    const void *copy) {
  return QMetaType::construct(type, where, copy);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QMetaType::destruct(int type, void *where)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType8destructEiPv(int type, void *where) {
  QMetaType::destruct(type, where);
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

//  void *QMetaType::create(const void *copy) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK9QMetaType6createEPKv(
    const QMetaType *self,
    const void *copy) {
  return self->create(copy);
}

//  void QMetaType::destroy(void *data) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QMetaType7destroyEPv(const QMetaType *self, void *data) {
  self->destroy(data);
}

//  void *QMetaType::construct(void *where, const void *copy) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK9QMetaType9constructEPvPKv(
    const QMetaType *self,
    void *where,
    const void *copy) {
  return self->construct(where, copy);
}

//  void QMetaType::destruct(void *data) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QMetaType8destructEPv(const QMetaType *self, void *data) {
  self->destruct(data);
}

//  QPartialOrdering QMetaType::compare(const void *lhs, const void *rhs)
//      const
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZNK9QMetaType7compareEPKvS1_(
    const QMetaType *self,
    const void *lhs,
    const void *rhs) {
  return new QPartialOrdering(self->compare(lhs, rhs));
}

//  bool QMetaType::equals(const void *lhs, const void *rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType6equalsEPKvS1_(
    const QMetaType *self,
    const void *lhs,
    const void *rhs) {
  return self->equals(lhs, rhs);
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
//  bool QMetaType::save(QDataStream &stream, const void *data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType4saveER11QDataStreamPKv(
    const QMetaType *self,
    QDataStream *stream,
    const void *data) {
  return self->save(*stream, data);
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  bool QMetaType::load(QDataStream &stream, void *data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType4loadER11QDataStreamPv(
    const QMetaType *self,
    QDataStream *stream,
    void *data) {
  return self->load(*stream, data);
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  bool QMetaType::hasRegisteredDataStreamOperators() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMetaType32hasRegisteredDataStreamOperatorsEv(
    const QMetaType *self) {
  return self->hasRegisteredDataStreamOperators();
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
#if QT_DEPRECATED_SINCE(6, 0)
//  bool QMetaType::save(QDataStream &stream, int type, const void *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType4saveER11QDataStreamiPKv(
    QDataStream *stream,
    int type,
    const void *data) {
  return QMetaType::save(*stream, type, data);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
#if QT_DEPRECATED_SINCE(6, 0)
//  bool QMetaType::load(QDataStream &stream, int type, void *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType4loadER11QDataStreamiPv(
    QDataStream *stream,
    int type,
    void *data) {
  return QMetaType::load(*stream, type, data);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)
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
//  bool QMetaType::debugStream(QDebug &dbg, const void *rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType11debugStreamER6QDebugPKv(
    QMetaType *self,
    QDebug *dbg,
    const void *rhs) {
  return self->debugStream(*dbg, rhs);
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
//  bool QMetaType::debugStream(QDebug &dbg, const void *rhs, int typeId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType11debugStreamER6QDebugPKvi(
    QDebug *dbg,
    const void *rhs,
    int typeId) {
  return QMetaType::debugStream(*dbg, rhs, typeId);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)
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

//  bool QMetaType::convert(QMetaType fromType, const void *from, QMetaType
//      toType, void *to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType7convertES_PKvS_Pv(
    const QMetaType *fromType,
    const void *from,
    const QMetaType *toType,
    void *to) {
  return QMetaType::convert(*fromType, from, *toType, to);
}

//  bool QMetaType::canConvert(QMetaType fromType, QMetaType toType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType10canConvertES_S_(
    const QMetaType *fromType,
    const QMetaType *toType) {
  return QMetaType::canConvert(*fromType, *toType);
}

//  bool QMetaType::view(QMetaType fromType, void *from, QMetaType toType,
//      void *to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType4viewES_PvS_S0_(
    const QMetaType *fromType,
    void *from,
    const QMetaType *toType,
    void *to) {
  return QMetaType::view(*fromType, from, *toType, to);
}

//  bool QMetaType::canView(QMetaType fromType, QMetaType toType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType7canViewES_S_(
    const QMetaType *fromType,
    const QMetaType *toType) {
  return QMetaType::canView(*fromType, *toType);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  bool QMetaType::convert(const void *from, int fromTypeId, void *to, int
//      toTypeId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType7convertEPKviPvi(
    const void *from,
    int fromTypeId,
    void *to,
    int toTypeId) {
  return QMetaType::convert(from, fromTypeId, to, toTypeId);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  bool QMetaType::compare(const void *lhs, const void *rhs, int typeId, int
//      *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType7compareEPKvS1_iPi(
    const void *lhs,
    const void *rhs,
    int typeId,
    int *result) {
  return QMetaType::compare(lhs, rhs, typeId, result);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  bool QMetaType::equals(const void *lhs, const void *rhs, int typeId, int
//      *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType6equalsEPKvS1_iPi(
    const void *lhs,
    const void *rhs,
    int typeId,
    int *result) {
  return QMetaType::equals(lhs, rhs, typeId, result);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

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

//  bool QMetaType::registerConverterFunction(const ConverterFunction &f,
//      QMetaType from, QMetaType to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType25registerConverterFunctionERKSt8functionIFbPKvPvEES_S_(
    const QMetaType::ConverterFunction *f,
    const QMetaType *from,
    const QMetaType *to) {
  return QMetaType::registerConverterFunction(*f, *from, *to);
}

//  void QMetaType::unregisterConverterFunction(QMetaType from, QMetaType to)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMetaType27unregisterConverterFunctionES_S_(
    const QMetaType *from,
    const QMetaType *to) {
  QMetaType::unregisterConverterFunction(*from, *to);
}

//  bool QMetaType::registerMutableViewFunction(const MutableViewFunction &f,
//      QMetaType from, QMetaType to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType27registerMutableViewFunctionERKSt8functionIFbPvS1_EES_S_(
    const QMetaType::MutableViewFunction *f,
    const QMetaType *from,
    const QMetaType *to) {
  return QMetaType::registerMutableViewFunction(*f, *from, *to);
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

//  static constexpr QMetaType QMetaType::fromType<int>()
extern "C" Q_DECL_EXPORT
QMetaType * ritual_ZN9QMetaType8fromTypeIiEES_v() {
  return new QMetaType(QMetaType::fromType<int>());
}

//  static constexpr QMetaType QMetaType::fromType<double>()
extern "C" Q_DECL_EXPORT
QMetaType * ritual_ZN9QMetaType8fromTypeIdEES_v() {
  return new QMetaType(QMetaType::fromType<double>());
}

//  static constexpr QMetaType QMetaType::fromType<bool>()
extern "C" Q_DECL_EXPORT
QMetaType * ritual_ZN9QMetaType8fromTypeIbEES_v() {
  return new QMetaType(QMetaType::fromType<bool>());
}

//  static constexpr QMetaType QMetaType::fromType<QString>()
extern "C" Q_DECL_EXPORT
QMetaType * ritual_ZN9QMetaType8fromTypeI7QStringEES_v() {
  return new QMetaType(QMetaType::fromType<QString>());
}

//  static constexpr QMetaType QMetaType::fromType<QVariant>()
extern "C" Q_DECL_EXPORT
QMetaType * ritual_ZN9QMetaType8fromTypeI8QVariantEES_v() {
  return new QMetaType(QMetaType::fromType<QVariant>());
}

//  static bool QMetaType::hasRegisteredConverterFunction<int, QString>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType30hasRegisteredConverterFunctionIi7QStringEEbv() {
  return QMetaType::hasRegisteredConverterFunction<int, QString>();
}

//  static bool QMetaType::hasRegisteredConverterFunction<QString, int>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType30hasRegisteredConverterFunctionI7QStringiEEbv() {
  return QMetaType::hasRegisteredConverterFunction<QString, int>();
}

//  static bool QMetaType::hasRegisteredConverterFunction<int, double>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType30hasRegisteredConverterFunctionIidEEbv() {
  return QMetaType::hasRegisteredConverterFunction<int, double>();
}

//  static bool QMetaType::hasRegisteredMutableViewFunction<int,
//      double>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredMutableViewFunctionIidEEbv() {
  return QMetaType::hasRegisteredMutableViewFunction<int, double>();
}

//  static bool QMetaType::hasRegisteredMutableViewFunction<QString,
//      QByteArray>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredMutableViewFunctionI7QString10QByteArrayEEbv() {
  return QMetaType::hasRegisteredMutableViewFunction<QString, QByteArray>(
      );
}

#if QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)
//  static bool QMetaType::hasRegisteredDebugStreamOperator<int>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorIiEEbv() {
  return QMetaType::hasRegisteredDebugStreamOperator<int>();
}
#endif  // QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)

#if QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)
//  static bool QMetaType::hasRegisteredDebugStreamOperator<double>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorIdEEbv() {
  return QMetaType::hasRegisteredDebugStreamOperator<double>();
}
#endif  // QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)

#if QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)
//  static bool QMetaType::hasRegisteredDebugStreamOperator<bool>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorIbEEbv() {
  return QMetaType::hasRegisteredDebugStreamOperator<bool>();
}
#endif  // QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)

#if QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)
//  static bool QMetaType::hasRegisteredDebugStreamOperator<QString>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorI7QStringEEbv() {
  return QMetaType::hasRegisteredDebugStreamOperator<QString>();
}
#endif  // QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)

#if QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)
//  static bool QMetaType::hasRegisteredDebugStreamOperator<QVariant>()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QMetaType32hasRegisteredDebugStreamOperatorI8QVariantEEbv() {
  return QMetaType::hasRegisteredDebugStreamOperator<QVariant>();
}
#endif  // QT_DEPRECATED_SINCE(6, 0) && !defined(QT_NO_DEBUG_STREAM)
