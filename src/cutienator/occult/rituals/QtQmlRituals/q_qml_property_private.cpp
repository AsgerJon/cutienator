//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlproperty_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  bool QQmlPropertyPrivate::resolveUrlsOnAssignment()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate23resolveUrlsOnAssignmentEv() {
  return QQmlPropertyPrivate::resolveUrlsOnAssignment();
}

//  QQmlPropertyPrivate::QQmlPropertyPrivate()
extern "C" Q_DECL_EXPORT
QQmlPropertyPrivate *ritual_ZN19QQmlPropertyPrivateC1Ev() {
  return new QQmlPropertyPrivate();
}

//  QQmlPropertyPrivate::~QQmlPropertyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivateD1Ev(QQmlPropertyPrivate *self) {
  delete self;
}

//  QQmlPropertyIndex QQmlPropertyPrivate::encodedIndex() const
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZNK19QQmlPropertyPrivate12encodedIndexEv(
    const QQmlPropertyPrivate *self) {
  return new QQmlPropertyIndex(self->encodedIndex());
}

//  QQmlPropertyIndex QQmlPropertyPrivate::encodedIndex(const
//      QQmlPropertyData &core, const QQmlPropertyData &valueTypeData)
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZN19QQmlPropertyPrivate12encodedIndexERK16QQmlPropertyDataS2_(
    const QQmlPropertyData *core,
    const QQmlPropertyData *valueTypeData) {
  return new QQmlPropertyIndex(
      QQmlPropertyPrivate::encodedIndex(
          *core,
          *valueTypeData));
}

//  void QQmlPropertyPrivate::initProperty(QObject *obj, const QString &name,
//      InitFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate12initPropertyEP7QObjectRK7QString6QFlagsINS_8InitFlagEE(
    QQmlPropertyPrivate *self,
    QObject *obj,
    const QString *name,
    int flags) {
  self->initProperty(
      obj,
      *name,
      QFlags<QQmlPropertyPrivate::InitFlag>::fromInt(flags));
}

//  void QQmlPropertyPrivate::initDefault(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate11initDefaultEP7QObject(
    QQmlPropertyPrivate *self,
    QObject *obj) {
  self->initDefault(obj);
}

//  bool QQmlPropertyPrivate::isValueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlPropertyPrivate11isValueTypeEv(
    const QQmlPropertyPrivate *self) {
  return self->isValueType();
}

//  QMetaType QQmlPropertyPrivate::propertyType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK19QQmlPropertyPrivate12propertyTypeEv(
    const QQmlPropertyPrivate *self) {
  return new QMetaType(self->propertyType());
}

//  QQmlProperty::Type QQmlPropertyPrivate::type() const
extern "C" Q_DECL_EXPORT
QQmlProperty::Type ritual_ZNK19QQmlPropertyPrivate4typeEv(
    const QQmlPropertyPrivate *self) {
  return self->type();
}

//  QQmlProperty::PropertyTypeCategory
//      QQmlPropertyPrivate::propertyTypeCategory() const
extern "C" Q_DECL_EXPORT
QQmlProperty::PropertyTypeCategory ritual_ZNK19QQmlPropertyPrivate20propertyTypeCategoryEv(
    const QQmlPropertyPrivate *self) {
  return self->propertyTypeCategory();
}

//  QVariant QQmlPropertyPrivate::readValueProperty()
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QQmlPropertyPrivate17readValuePropertyEv(
    QQmlPropertyPrivate *self) {
  return new QVariant(self->readValueProperty());
}

//  bool QQmlPropertyPrivate::writeValueProperty(const QVariant &a0,
//      QQmlPropertyData::WriteFlags a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate18writeValuePropertyERK8QVariant6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    QQmlPropertyPrivate *self,
    const QVariant *a0,
    int a1) {
  return self->writeValueProperty(
      *a0,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(a1));
}

//  QQmlMetaObject QQmlPropertyPrivate::rawMetaObjectForType(QMetaType
//      metaType)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN19QQmlPropertyPrivate20rawMetaObjectForTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlMetaObject(
      QQmlPropertyPrivate::rawMetaObjectForType(
          *metaType));
}

//  bool QQmlPropertyPrivate::writeEnumProperty(const QMetaProperty &prop,
//      int idx, QObject *object, const QVariant &value, int flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate17writeEnumPropertyERK13QMetaPropertyiP7QObjectRK8QVarianti(
    const QMetaProperty *prop,
    int idx,
    QObject *object,
    const QVariant *value,
    int flags) {
  return QQmlPropertyPrivate::writeEnumProperty(
      *prop,
      idx,
      object,
      *value,
      flags);
}

//  QVariant QQmlPropertyPrivate::convertToWriteTargetType(const QVariant
//      &value, QMetaType targetMetaType)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QQmlPropertyPrivate24convertToWriteTargetTypeERK8QVariant9QMetaType(
    const QVariant *value,
    const QMetaType *targetMetaType) {
  return new QVariant(
      QQmlPropertyPrivate::convertToWriteTargetType(
          *value,
          *targetMetaType));
}

//  bool QQmlPropertyPrivate::reset(QObject *a0, const QQmlPropertyData &a1,
//      QQmlPropertyData::WriteFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate5resetEP7QObjectRK16QQmlPropertyData6QFlagsINS2_9WriteFlagEE(
    QObject *a0,
    const QQmlPropertyData *a1,
    int flags) {
  return QQmlPropertyPrivate::reset(
      a0,
      *a1,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  ResolvedAlias QQmlPropertyPrivate::findAliasTarget(QObject *baseObject,
//      QQmlPropertyIndex baseIndex)
extern "C" Q_DECL_EXPORT
QQmlPropertyPrivate::ResolvedAlias *ritual_ZN19QQmlPropertyPrivate15findAliasTargetEP7QObject17QQmlPropertyIndex(
    QObject *baseObject,
    const QQmlPropertyIndex *baseIndex) {
  return new QQmlPropertyPrivate::ResolvedAlias(
      QQmlPropertyPrivate::findAliasTarget(
          baseObject,
          *baseIndex));
}

//  void QQmlPropertyPrivate::setBinding(QQmlAbstractBinding *binding,
//      BindingFlags flags, QQmlPropertyData::WriteFlags writeFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate10setBindingEP19QQmlAbstractBinding6QFlagsINS_11BindingFlagEES2_IN16QQmlPropertyData9WriteFlagEE(
    QQmlAbstractBinding *binding,
    int flags,
    int writeFlags) {
  QQmlPropertyPrivate::setBinding(
      binding,
      QFlags<QQmlPropertyPrivate::BindingFlag>::fromInt(flags),
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(writeFlags));
}

//  bool QQmlPropertyPrivate::removeBinding(const QQmlProperty &that,
//      BindingFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate13removeBindingERK12QQmlProperty6QFlagsINS_11BindingFlagEE(
    const QQmlProperty *that,
    int flags) {
  return QQmlPropertyPrivate::removeBinding(
      *that,
      QFlags<QQmlPropertyPrivate::BindingFlag>::fromInt(flags));
}

//  bool QQmlPropertyPrivate::removeBinding(QObject *o, QQmlPropertyIndex
//      index, BindingFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate13removeBindingEP7QObject17QQmlPropertyIndex6QFlagsINS_11BindingFlagEE(
    QObject *o,
    const QQmlPropertyIndex *index,
    int flags) {
  return QQmlPropertyPrivate::removeBinding(
      o,
      *index,
      QFlags<QQmlPropertyPrivate::BindingFlag>::fromInt(flags));
}

//  bool QQmlPropertyPrivate::removeBinding(QQmlAbstractBinding *b,
//      QQmlPropertyPrivate::BindingFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate13removeBindingEP19QQmlAbstractBinding6QFlagsINS_11BindingFlagEE(
    QQmlAbstractBinding *b,
    int flags) {
  return QQmlPropertyPrivate::removeBinding(
      b,
      QFlags<QQmlPropertyPrivate::BindingFlag>::fromInt(flags));
}

//  QQmlAbstractBinding *QQmlPropertyPrivate::binding(QObject *a0,
//      QQmlPropertyIndex index)
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZN19QQmlPropertyPrivate7bindingEP7QObject17QQmlPropertyIndex(
    QObject *a0,
    const QQmlPropertyIndex *index) {
  return QQmlPropertyPrivate::binding(a0, *index);
}

//  int QQmlPropertyPrivate::signalIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQmlPropertyPrivate11signalIndexEv(
    const QQmlPropertyPrivate *self) {
  return self->signalIndex();
}

//  QQmlPropertyPrivate *QQmlPropertyPrivate::get(const QQmlProperty &p)
extern "C" Q_DECL_EXPORT
QQmlPropertyPrivate *ritual_ZN19QQmlPropertyPrivate3getERK12QQmlProperty(
    const QQmlProperty *p) {
  return QQmlPropertyPrivate::get(*p);
}

//  QQmlAbstractBinding *QQmlPropertyPrivate::binding(const QQmlProperty
//      &that)
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding *ritual_ZN19QQmlPropertyPrivate7bindingERK12QQmlProperty(
    const QQmlProperty *that) {
  return QQmlPropertyPrivate::binding(*that);
}

//  void QQmlPropertyPrivate::setBinding(const QQmlProperty &that,
//      QQmlAbstractBinding *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate10setBindingERK12QQmlPropertyP19QQmlAbstractBinding(
    const QQmlProperty *that,
    QQmlAbstractBinding *a1) {
  QQmlPropertyPrivate::setBinding(*that, a1);
}

//  QQmlBoundSignalExpression *QQmlPropertyPrivate::signalExpression(const
//      QQmlProperty &that)
extern "C" Q_DECL_EXPORT
QQmlBoundSignalExpression *ritual_ZN19QQmlPropertyPrivate16signalExpressionERK12QQmlProperty(
    const QQmlProperty *that) {
  return QQmlPropertyPrivate::signalExpression(*that);
}

//  void QQmlPropertyPrivate::setSignalExpression(const QQmlProperty &that,
//      QQmlBoundSignalExpression *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate19setSignalExpressionERK12QQmlPropertyP25QQmlBoundSignalExpression(
    const QQmlProperty *that,
    QQmlBoundSignalExpression *a1) {
  QQmlPropertyPrivate::setSignalExpression(*that, a1);
}

//  void QQmlPropertyPrivate::takeSignalExpression(const QQmlProperty &that,
//      QQmlBoundSignalExpression *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate20takeSignalExpressionERK12QQmlPropertyP25QQmlBoundSignalExpression(
    const QQmlProperty *that,
    QQmlBoundSignalExpression *a1) {
  QQmlPropertyPrivate::takeSignalExpression(*that, a1);
}

//  bool QQmlPropertyPrivate::write(const QQmlProperty &that, const QVariant
//      &a1, QQmlPropertyData::WriteFlags a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate5writeERK12QQmlPropertyRK8QVariant6QFlagsIN16QQmlPropertyData9WriteFlagEE(
    const QQmlProperty *that,
    const QVariant *a1,
    int a2) {
  return QQmlPropertyPrivate::write(
      *that,
      *a1,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(a2));
}

//  QQmlPropertyIndex QQmlPropertyPrivate::propertyIndex(const QQmlProperty
//      &that)
extern "C" Q_DECL_EXPORT
QQmlPropertyIndex *ritual_ZN19QQmlPropertyPrivate13propertyIndexERK12QQmlProperty(
    const QQmlProperty *that) {
  return new QQmlPropertyIndex(QQmlPropertyPrivate::propertyIndex(*that));
}

//  QMetaMethod QQmlPropertyPrivate::findSignalByName(const QMetaObject *mo,
//      const QByteArray &a1)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN19QQmlPropertyPrivate16findSignalByNameEPK11QMetaObjectRK10QByteArray(
    const QMetaObject *mo,
    const QByteArray *a1) {
  return new QMetaMethod(QQmlPropertyPrivate::findSignalByName(mo, *a1));
}

//  QMetaProperty QQmlPropertyPrivate::findPropertyByName(const QMetaObject
//      *mo, const QByteArray &a1)
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZN19QQmlPropertyPrivate18findPropertyByNameEPK11QMetaObjectRK10QByteArray(
    const QMetaObject *mo,
    const QByteArray *a1) {
  return new QMetaProperty(QQmlPropertyPrivate::findPropertyByName(mo, *a1));
}

//  bool QQmlPropertyPrivate::connect(const QObject *sender, int
//      signal_index, const QObject *receiver, int method_index, int type,
//      int *types)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlPropertyPrivate7connectEPK7QObjectiS2_iiPi(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    int method_index,
    int type,
    int *types) {
  return QQmlPropertyPrivate::connect(
      sender,
      signal_index,
      receiver,
      method_index,
      type,
      types);
}

//  void QQmlPropertyPrivate::flushSignal(const QObject *sender, int
//      signal_index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPropertyPrivate11flushSignalEPK7QObjecti(
    const QObject *sender,
    int signal_index) {
  QQmlPropertyPrivate::flushSignal(sender, signal_index);
}

//  QList<QUrl> QQmlPropertyPrivate::urlSequence(const QVariant &value)
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZN19QQmlPropertyPrivate11urlSequenceERK8QVariant(
    const QVariant *value) {
  return new QList<QUrl>(QQmlPropertyPrivate::urlSequence(*value));
}
