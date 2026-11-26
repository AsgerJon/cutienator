//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/qqmlengine.h>
#include <QtCore/private/qvariant_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstringlist.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 19, as local:qqmlglobal.cpp:printConversionWarning
static void printConversionWarning(QV4::ExecutionEngine *engine, const QString &propertyValue,
                                   const QString &propertyType, const QString &propertyName) {
    auto stackTrace = engine->stackTrace(1);
    QString errorLocation;
    if (!stackTrace.isEmpty()) {
        const auto& stackTop = stackTrace[0];
        errorLocation = QString::fromLatin1("%1:%2: ").arg(stackTop.source, QString::number(stackTop.line));
    }
    qWarning().noquote()
        << QLatin1String("%4Could not convert %1 to %2 for property %3")
                .arg(propertyValue, propertyType, propertyName, errorLocation);
}

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 33, as local:qqmlglobal.cpp:isConstructibleMetaType
static bool isConstructibleMetaType(const QMetaType metaType)
{
    switch (metaType.id()) {
        // The builtins are not constructible this way.
        case QMetaType::Void:
        case QMetaType::Nullptr:
        case QMetaType::QVariant:
        case QMetaType::Int:
        case QMetaType::UInt:
        case QMetaType::LongLong:
        case QMetaType::ULongLong:
        case QMetaType::Float:
        case QMetaType::Double:
        case QMetaType::Long:
        case QMetaType::ULong:
        case QMetaType::Short:
        case QMetaType::UShort:
        case QMetaType::Char:
        case QMetaType::SChar:
        case QMetaType::UChar:
        case QMetaType::QChar:
        case QMetaType::QString:
        case QMetaType::Bool:
        case QMetaType::QDateTime:
        case QMetaType::QDate:
        case QMetaType::QTime:
        case QMetaType::QUrl:
        case QMetaType::QRegularExpression:
        case QMetaType::QByteArray:
        case QMetaType::QLocale:
        return false;
    default:
        break;
    }

    // QJSValue is also builtin
    if (metaType == QMetaType::fromType<QJSValue>())
        return false;

    // We also don't want to construct pointers of any kind, or lists, or enums.
    if (metaType.flags() &
            (QMetaType::PointerToQObject
             | QMetaType::IsEnumeration
             | QMetaType::SharedPointerToQObject
             | QMetaType::WeakPointerToQObject
             | QMetaType::TrackingPointerToQObject
             | QMetaType::IsUnsignedEnumeration
             | QMetaType::PointerToGadget
             | QMetaType::IsPointer
             | QMetaType::IsQmlList)) {
        return false;
    }

    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 98, as local:qqmlglobal.cpp:coerceToJSValue
inline template<typename JSValue>
bool coerceToJSValue(QMetaType fromType, const void *from, JSValue *to)
{
    if (!fromType.isValid()) {
        *to = JSValue();
        return true;
    }

    if ((fromType.flags() & QMetaType::PointerToQObject)
            && *static_cast<QObject *const *>(from) == nullptr) {
        *to = nullValue<JSValue>();
        return true;
    }

    switch (fromType.id()) {
    case QMetaType::Void:
        *to = JSValue();
        return true;
    case QMetaType::Bool:
        *to = JSValue(*static_cast<const bool *>(from));
        return true;
    case QMetaType::Int:
        *to = JSValue(*static_cast<const int *>(from));
        return true;
    case QMetaType::Double:
        *to = JSValue(*static_cast<const double *>(from));
        return true;
    case QMetaType::QString:
        *to = JSValue(*static_cast<const QString *>(from));
        return true;
    case QMetaType::Nullptr:
        *to = nullValue<JSValue>();
        return true;
    }

    return false;
}

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 179, as local:qqmlglobal.cpp:createVariantData
static void *createVariantData(QMetaType type, QVariant *variant)
{
    const QtPrivate::QMetaTypeInterface *iface = type.iface();
    QVariant::Private *d = &variant->data_ptr();
    Q_ASSERT(d->is_null && !d->is_shared);
    *d = QVariant::Private(iface);
    if (QVariant::Private::canUseInternalSpace(iface))
        return d->data.data;

    // This is not exception safe.
    // If your value type throws an exception from its ctor bad things will happen anyway.
    d->data.shared = QVariant::PrivateShared::create(iface->size, iface->alignment);
    d->is_shared = true;
    return d->data.shared->data();
}

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 195, as local:qqmlglobal.cpp:callConstructor
static void callConstructor(
        const QMetaObject *targetMetaObject, int i, void **args, int argc, void *target)
{
    Q_ALLOCA_INIT();
    Q_ALLOCA_VAR(void *, p, (argc + 1) * sizeof(void *));
    p[0] = target;
    memcpy(p + 1, args, argc * sizeof(void *));
    targetMetaObject->static_metacall(QMetaObject::ConstructInPlace, i, p);
}

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 213, as local:qqmlglobal.cpp:fromVerifiedType
template<typename Allocate>
static void fromVerifiedType(
        const QMetaObject *targetMetaObject, int ctorIndex, void **args,
        Allocate &&allocate)
{
    const QMetaMethod ctor = targetMetaObject->constructor(ctorIndex);
    callConstructor(targetMetaObject, ctorIndex, args, ctor.parameterCount(), allocate());
}

//  from ../qtdeclarative/src/qml/qml/qqmlglobal.cpp, line 799, as _ZN21QQmlValueTypeProvider18constructValueTypeE9QMetaTypePK11QMetaObjectiPPv
inline QVariant QQmlValueTypeProvider::constructValueType(
        QMetaType targetMetaType, const QMetaObject *targetMetaObject,
        int ctorIndex, void **args)
{
    QVariant result;
    fromVerifiedType(targetMetaObject, ctorIndex, args,
                     [&]() { return createVariantData(targetMetaType, &result); });
    return result;
}
//  -----------------------------------------------------------------------

//  void *QQmlValueTypeProvider::heapCreateValueType(const QQmlType
//      &targetType, const QV4::Value &source, QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQmlValueTypeProvider19heapCreateValueTypeERK8QQmlTypeRKN3QV45ValueEPNS3_15ExecutionEngineE(
    const QQmlType *targetType,
    const QV4::Value *source,
    QV4::ExecutionEngine *engine) {
  return QQmlValueTypeProvider::heapCreateValueType(
      *targetType,
      *source,
      engine);
}

//  QVariant QQmlValueTypeProvider::constructValueType(QMetaType
//      targetMetaType, const QMetaObject *targetMetaObject, int ctorIndex,
//      void **args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN21QQmlValueTypeProvider18constructValueTypeE9QMetaTypePK11QMetaObjectiPPv(
    const QMetaType *targetMetaType,
    const QMetaObject *targetMetaObject,
    int ctorIndex,
    void **args) {
  return new QVariant(
      QQmlValueTypeProvider::constructValueType(
          *targetMetaType,
          targetMetaObject,
          ctorIndex,
          args));
}

//  QQmlValueTypeProvider::~QQmlValueTypeProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlValueTypeProviderD1Ev(QQmlValueTypeProvider *self) {
  delete self;
}
