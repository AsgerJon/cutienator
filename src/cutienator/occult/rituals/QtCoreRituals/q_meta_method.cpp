//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaobject.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qobjectdefs.h>
#include <QtCore/qlist.h>

//  QMetaMethod::QMetaMethod()
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN11QMetaMethodC1Ev() {
  return new QMetaMethod();
}

//  QByteArray QMetaMethod::methodSignature() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QMetaMethod15methodSignatureEv(
    const QMetaMethod *self) {
  return new QByteArray(self->methodSignature());
}

//  QByteArray QMetaMethod::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QMetaMethod4nameEv(const QMetaMethod *self) {
  return new QByteArray(self->name());
}

//  QByteArrayView QMetaMethod::nameView() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK11QMetaMethod8nameViewEv(const QMetaMethod *self) {
  return new QByteArrayView(self->nameView());
}

//  const char *QMetaMethod::typeName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK11QMetaMethod8typeNameEv(const QMetaMethod *self) {
  return self->typeName();
}

//  int QMetaMethod::returnType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod10returnTypeEv(const QMetaMethod *self) {
  return self->returnType();
}

//  QMetaType QMetaMethod::returnMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK11QMetaMethod14returnMetaTypeEv(
    const QMetaMethod *self) {
  return new QMetaType(self->returnMetaType());
}

//  int QMetaMethod::parameterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod14parameterCountEv(const QMetaMethod *self) {
  return self->parameterCount();
}

//  int QMetaMethod::parameterType(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod13parameterTypeEi(
    const QMetaMethod *self,
    int index) {
  return self->parameterType(index);
}

//  QMetaType QMetaMethod::parameterMetaType(int index) const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK11QMetaMethod17parameterMetaTypeEi(
    const QMetaMethod *self,
    int index) {
  return new QMetaType(self->parameterMetaType(index));
}

//  void QMetaMethod::getParameterTypes(int *types) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QMetaMethod17getParameterTypesEPi(
    const QMetaMethod *self,
    int *types) {
  self->getParameterTypes(types);
}

//  QList<QByteArray> QMetaMethod::parameterTypes() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QMetaMethod14parameterTypesEv(
    const QMetaMethod *self) {
  return new QList<QByteArray>(self->parameterTypes());
}

//  QByteArray QMetaMethod::parameterTypeName(int index) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QMetaMethod17parameterTypeNameEi(
    const QMetaMethod *self,
    int index) {
  return new QByteArray(self->parameterTypeName(index));
}

//  QList<QByteArray> QMetaMethod::parameterNames() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK11QMetaMethod14parameterNamesEv(
    const QMetaMethod *self) {
  return new QList<QByteArray>(self->parameterNames());
}

//  const char *QMetaMethod::tag() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK11QMetaMethod3tagEv(const QMetaMethod *self) {
  return self->tag();
}

//  Access QMetaMethod::access() const
extern "C" Q_DECL_EXPORT
QMetaMethod::Access ritual_ZNK11QMetaMethod6accessEv(
    const QMetaMethod *self) {
  return self->access();
}

//  MethodType QMetaMethod::methodType() const
extern "C" Q_DECL_EXPORT
QMetaMethod::MethodType ritual_ZNK11QMetaMethod10methodTypeEv(
    const QMetaMethod *self) {
  return self->methodType();
}

//  int QMetaMethod::attributes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod10attributesEv(const QMetaMethod *self) {
  return self->attributes();
}

//  int QMetaMethod::methodIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod11methodIndexEv(const QMetaMethod *self) {
  return self->methodIndex();
}

//  int QMetaMethod::relativeMethodIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod19relativeMethodIndexEv(const QMetaMethod *self) {
  return self->relativeMethodIndex();
}

//  int QMetaMethod::revision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaMethod8revisionEv(const QMetaMethod *self) {
  return self->revision();
}

//  bool QMetaMethod::isConst() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod7isConstEv(const QMetaMethod *self) {
  return self->isConst();
}

//  const QMetaObject *QMetaMethod::enclosingMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMetaMethod19enclosingMetaObjectEv(
    const QMetaMethod *self) {
  return self->enclosingMetaObject();
}

#if QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)
//  bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
//      connectionType, QGenericReturnArgument returnValue, QGenericArgument
//      val0, QGenericArgument val1, QGenericArgument val2, QGenericArgument
//      val3, QGenericArgument val4, QGenericArgument val5, QGenericArgument
//      val6, QGenericArgument val7, QGenericArgument val8, QGenericArgument
//      val9) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod6invokeEP7QObjectN2Qt14ConnectionTypeE22QGenericReturnArgument16QGenericArgumentS5_S5_S5_S5_S5_S5_S5_S5_S5_(
    const QMetaMethod *self,
    QObject *object,
    Qt::ConnectionType connectionType,
    const QGenericReturnArgument *returnValue,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->invoke(
      object,
      connectionType,
      *returnValue,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}
#endif  // QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)
//  bool QMetaMethod::invoke(QObject *object, QGenericReturnArgument
//      returnValue, QGenericArgument val0, QGenericArgument val1,
//      QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
//      QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
//      QGenericArgument val8, QGenericArgument val9) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod6invokeEP7QObject22QGenericReturnArgument16QGenericArgumentS3_S3_S3_S3_S3_S3_S3_S3_S3_(
    const QMetaMethod *self,
    QObject *object,
    const QGenericReturnArgument *returnValue,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->invoke(
      object,
      *returnValue,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}
#endif  // QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)
//  bool QMetaMethod::invoke(QObject *object, Qt::ConnectionType
//      connectionType, QGenericArgument val0, QGenericArgument val1,
//      QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
//      QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
//      QGenericArgument val8, QGenericArgument val9) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod6invokeEP7QObjectN2Qt14ConnectionTypeE16QGenericArgumentS4_S4_S4_S4_S4_S4_S4_S4_S4_(
    const QMetaMethod *self,
    QObject *object,
    Qt::ConnectionType connectionType,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->invoke(
      object,
      connectionType,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}
#endif  // QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)
//  bool QMetaMethod::invoke(QObject *object, QGenericArgument val0,
//      QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
//      QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
//      QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod6invokeEP7QObject16QGenericArgumentS2_S2_S2_S2_S2_S2_S2_S2_S2_(
    const QMetaMethod *self,
    QObject *object,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->invoke(
      object,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}
#endif  // QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)
//  bool QMetaMethod::invokeOnGadget(void *gadget, QGenericReturnArgument
//      returnValue, QGenericArgument val0, QGenericArgument val1,
//      QGenericArgument val2, QGenericArgument val3, QGenericArgument val4,
//      QGenericArgument val5, QGenericArgument val6, QGenericArgument val7,
//      QGenericArgument val8, QGenericArgument val9) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod14invokeOnGadgetEPv22QGenericReturnArgument16QGenericArgumentS2_S2_S2_S2_S2_S2_S2_S2_S2_(
    const QMetaMethod *self,
    void *gadget,
    const QGenericReturnArgument *returnValue,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->invokeOnGadget(
      gadget,
      *returnValue,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}
#endif  // QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)
//  bool QMetaMethod::invokeOnGadget(void *gadget, QGenericArgument val0,
//      QGenericArgument val1, QGenericArgument val2, QGenericArgument val3,
//      QGenericArgument val4, QGenericArgument val5, QGenericArgument val6,
//      QGenericArgument val7, QGenericArgument val8, QGenericArgument val9)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod14invokeOnGadgetEPv16QGenericArgumentS1_S1_S1_S1_S1_S1_S1_S1_S1_(
    const QMetaMethod *self,
    void *gadget,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->invokeOnGadget(
      gadget,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}
#endif  // QT_VERSION <= QT_VERSION_CHECK(7, 0, 0)

//  bool QMetaMethod::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaMethod7isValidEv(const QMetaMethod *self) {
  return self->isValid();
}

//  bool QMetaMethod::invokeImpl(QMetaMethod self_, void *target,
//      Qt::ConnectionType a2, qsizetype paramCount, const void *const
//      *parameters, const char *const *typeNames, const
//      QtPrivate::QMetaTypeInterface *const *metaTypes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaMethod10invokeImplES_PvN2Qt14ConnectionTypeExPKPKvPKPKcPKPKN9QtPrivate18QMetaTypeInterfaceE(
    const QMetaMethod *self_,
    void *target,
    Qt::ConnectionType a2,
    qsizetype paramCount,
    const void *const *parameters,
    const char *const *typeNames,
    const QtPrivate::QMetaTypeInterface *const *metaTypes) {
  return QMetaMethod::invokeImpl(
      *self_,
      target,
      a2,
      paramCount,
      parameters,
      typeNames,
      metaTypes);
}

//  QMetaMethod QMetaMethod::fromSignalImpl(const QMetaObject *a0, void **a1)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN11QMetaMethod14fromSignalImplEPK11QMetaObjectPPv(
    const QMetaObject *a0,
    void **a1) {
  return new QMetaMethod(QMetaMethod::fromSignalImpl(a0, a1));
}

//  QMetaMethod QMetaMethod::fromRelativeMethodIndex(const QMetaObject *mobj,
//      int index)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN11QMetaMethod23fromRelativeMethodIndexEPK11QMetaObjecti(
    const QMetaObject *mobj,
    int index) {
  return new QMetaMethod(QMetaMethod::fromRelativeMethodIndex(mobj, index));
}

//  QMetaMethod QMetaMethod::fromRelativeConstructorIndex(const QMetaObject
//      *mobj, int index)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN11QMetaMethod28fromRelativeConstructorIndexEPK11QMetaObjecti(
    const QMetaObject *mobj,
    int index) {
  return new QMetaMethod(
      QMetaMethod::fromRelativeConstructorIndex(
          mobj,
          index));
}

//  QMetaMethod::QMetaMethod(const QMetaObject *metaObject, const Data
//      &data_)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN11QMetaMethodC1EPK11QMetaObjectRKNS_4DataE(
    const QMetaObject *metaObject,
    const QMetaMethod::Data *data_) {
  return new QMetaMethod(metaObject, *data_);
}

//  bool operator==(const QMetaMethod &lhs, const QMetaMethod &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QMetaMethodS1_(
    const QMetaMethod *lhs,
    const QMetaMethod *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMetaMethod &lhs, const QMetaMethod &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QMetaMethodS1_(
    const QMetaMethod *lhs,
    const QMetaMethod *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QMetaMethod::~QMetaMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaMethodD1Ev(QMetaMethod *self) {
  delete self;
}
