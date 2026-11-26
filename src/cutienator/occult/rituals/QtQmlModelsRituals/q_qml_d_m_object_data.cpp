//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQmlDMObjectData' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#include <QtQmlModels/private/qqmllistaccessor_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetasequence.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qurl.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQmlModels__QQmlDMObjectData.cpp, line 1, as moc:QQmlDMObjectData
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16QQmlDMObjectDataE_t {};
} // unnamed namespace

template <> constexpr inline auto QQmlDMObjectData::qt_create_metaobjectdata<qt_meta_tag_ZN16QQmlDMObjectDataE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQmlDMObjectData",
        "modelDataChanged",
        "",
        "modelData"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'modelDataChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'modelData'
        QtMocHelpers::PropertyData<QObject*>(3, QMetaType::QObjectStar, QMC::DefaultPropertyFlags, 0),
        // property ''
        QtMocHelpers::PropertyData<QObject*>(2, QMetaType::QObjectStar, QMC::DefaultPropertyFlags | QMC::Final, 0),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQmlDMObjectData, qt_meta_tag_ZN16QQmlDMObjectDataE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQmlDMObjectData::staticMetaObject = { {
    QMetaObject::SuperData::link<QQmlDelegateModelItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QQmlDMObjectDataE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QQmlDMObjectDataE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16QQmlDMObjectDataE_t>.metaTypes,
    nullptr
} };

void QQmlDMObjectData::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQmlDMObjectData *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->modelDataChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQmlDMObjectData::*)()>(_a, &QQmlDMObjectData::modelDataChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QObject**>(_v) = _t->modelData(); break;
        case 1: *reinterpret_cast<QObject**>(_v) = _t->modelData(); break;
        default: break;
        }
    }
}

const QMetaObject *QQmlDMObjectData::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQmlDMObjectData::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QQmlDMObjectDataE_t>.strings))
        return static_cast<void*>(this);
    return QQmlDelegateModelItem::qt_metacast(_clname);
}

int QQmlDMObjectData::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQmlDelegateModelItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void QQmlDMObjectData::modelDataChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}

//  from ../qtdeclarative/src/qmlmodels/qqmladaptormodel.cpp, line 13, as _ZN16QQmlAdaptorModel9AccessorsD2Ev
inline QQmlAdaptorModel::Accessors::~Accessors()
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 183, as _ZNK16QQmlListAccessor2atEx
inline QVariant QQmlListAccessor::at(qsizetype idx) const
{
    Q_ASSERT(idx >= 0 && idx < count());
    switch(m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        return QVariant::fromValue(reinterpret_cast<const QStringList *>(d.constData())->at(idx));
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        return QVariant::fromValue(reinterpret_cast<const QList<QUrl> *>(d.constData())->at(idx));
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        return reinterpret_cast<const QVariantList *>(d.constData())->at(idx);
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        return QVariant::fromValue(reinterpret_cast<const QList<QObject *> *>(d.constData())->at(idx));
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        return QVariant::fromValue(reinterpret_cast<const QQmlListReference *>(d.constData())->at(idx));
    case ValueSequence:
    case ObjectSequence: {
        Q_ASSERT(m_metaSequence != QMetaSequence());
        QVariant result;
        const QMetaType valueMetaType = m_metaSequence.valueMetaType();
        if (valueMetaType == QMetaType::fromType<QVariant>()) {
            m_metaSequence.valueAtIndex(d.constData(), idx, &result);
        } else {
            result = QVariant(valueMetaType);
            m_metaSequence.valueAtIndex(d.constData(), idx, result.data());
        }
        return result;
    }
    case Instance:
        return d;
    case Integer:
        return QVariant(idx);
    case Invalid:
        return QVariant();
    }
    Q_UNREACHABLE_RETURN(QVariant());
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 151, as _ZNK16QQmlListAccessor5countEv
inline qsizetype QQmlListAccessor::count() const
{
    switch(m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        return reinterpret_cast<const QStringList *>(d.constData())->size();
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        return reinterpret_cast<const QList<QUrl> *>(d.constData())->size();
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        return reinterpret_cast<const QVariantList *>(d.constData())->size();
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        return reinterpret_cast<const QList<QObject *> *>(d.constData())->size();
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        return reinterpret_cast<const QQmlListReference *>(d.constData())->count();
    case ValueSequence:
    case ObjectSequence:
        Q_ASSERT(m_metaSequence != QMetaSequence());
        return m_metaSequence.size(d.constData());
    case Instance:
        return 1;
    case Integer:
        return *reinterpret_cast<const int *>(d.constData());
    case Invalid:
        return 0;
    }
    Q_UNREACHABLE_RETURN(0);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmobjectdata.cpp, line 9, as _ZN16QQmlDMObjectDataC1ERK14QQmlRefPointerI29QQmlDelegateModelItemMetaTypeEP25VDMObjectDelegateDataTypeiiiP7QObject
inline QQmlDMObjectData::QQmlDMObjectData(const QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
        VDMObjectDelegateDataType *dataType,
        int index, int row, int column,
        QObject *object)
    : QQmlDelegateModelItem(metaType, dataType, index, row, column)
    , m_modelData(object)
{
    new QQmlDMObjectDataMetaObject(this, dataType);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmobjectdata.cpp, line 19, as _ZN16QQmlDMObjectData9initProxyEv
inline QQmlRefPointer<QQmlContextData> QQmlDMObjectData::initProxy()
{
    QQmlRefPointer<QQmlContextData> ctxt = QQmlContextData::createChild(contextData());
    QQDMIncubationTask *it = incubationTask();
    it->proxiedObject = m_modelData;
    it->proxyContext = ctxt;
    ctxt->setContextObject(this);
    // We don't own the proxied object. We need to clear it if it goes away.
    QObject::connect(m_modelData, &QObject::destroyed,
                     this, &QQmlDelegateModelItem::childContextObjectDestroyed);
    return ctxt;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQmlDMObjectData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlDMObjectData10metaObjectEv(
    const QQmlDMObjectData *self) {
  return self->metaObject();
}

//  void *QQmlDMObjectData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQmlDMObjectData11qt_metacastEPKc(
    QQmlDMObjectData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDMObjectData::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlDMObjectData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDMObjectData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlDMObjectData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlDMObjectData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDMObjectData::tr(s, c, n));
}

//  QQmlDMObjectData::QQmlDMObjectData(const
//      QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
//      VDMObjectDelegateDataType *dataType, int index, int row, int column,
//      QObject *object)
extern "C" Q_DECL_EXPORT
QQmlDMObjectData *ritual_ZN16QQmlDMObjectDataC1ERK14QQmlRefPointerI29QQmlDelegateModelItemMetaTypeEP25VDMObjectDelegateDataTypeiiiP7QObject(
    const QQmlRefPointer<QQmlDelegateModelItemMetaType> *metaType,
    VDMObjectDelegateDataType *dataType,
    int index,
    int row,
    int column,
    QObject *object) {
  return new QQmlDMObjectData(
      *metaType,
      dataType,
      index,
      row,
      column,
      object);
}

//  void QQmlDMObjectData::setModelData(QObject *modelData)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDMObjectData12setModelDataEP7QObject(
    QQmlDMObjectData *self,
    QObject *modelData) {
  self->setModelData(modelData);
}

//  QObject *QQmlDMObjectData::modelData() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QQmlDMObjectData9modelDataEv(
    const QQmlDMObjectData *self) {
  return self->modelData();
}

//  QQmlRefPointer<QQmlContextData> QQmlDMObjectData::initProxy()
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZN16QQmlDMObjectData9initProxyEv(
    QQmlDMObjectData *self) {
  return new QQmlRefPointer<QQmlContextData>(self->initProxy());
}

//  void QQmlDMObjectData::modelDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDMObjectData16modelDataChangedEv(
    QQmlDMObjectData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlDMObjectData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "modelDataChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "modelDataChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QQmlDMObjectData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDMObjectData__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
