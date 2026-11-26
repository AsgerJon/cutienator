//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQStyleKitVariationAttached' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  4 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKit__QQStyleKitVariationAttached.cpp, line 1, as moc:QQStyleKitVariationAttached
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t {};
} // unnamed namespace

template <> constexpr inline auto QQStyleKitVariationAttached::qt_create_metaobjectdata<qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQStyleKitVariationAttached",
        "variationsChanged",
        "",
        "controlTypeChanged",
        "variations",
        "controlType",
        "QQStyleKitExtendableControlType"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'variationsChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'controlTypeChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'variations'
        QtMocHelpers::PropertyData<QStringList>(4, QMetaType::QStringList, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 0),
        // property 'controlType'
        QtMocHelpers::PropertyData<QQStyleKitExtendableControlType>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQStyleKitVariationAttached, qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQStyleKitVariationAttached::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t>.metaTypes,
    nullptr
} };

void QQStyleKitVariationAttached::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQStyleKitVariationAttached *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->variationsChanged(); break;
        case 1: _t->controlTypeChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitVariationAttached::*)()>(_a, &QQStyleKitVariationAttached::variationsChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitVariationAttached::*)()>(_a, &QQStyleKitVariationAttached::controlTypeChanged, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QStringList*>(_v) = _t->variations(); break;
        case 1: *reinterpret_cast<QQStyleKitExtendableControlType*>(_v) = _t->controlType(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setVariations(*reinterpret_cast<QStringList*>(_v)); break;
        case 1: _t->setControlType(*reinterpret_cast<QQStyleKitExtendableControlType*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQStyleKitVariationAttached::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQStyleKitVariationAttached::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQStyleKitVariationAttachedE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQStyleKitVariationAttached::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
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
void QQStyleKitVariationAttached::variationsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQStyleKitVariationAttached::controlTypeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 186, as _ZN27QQStyleKitVariationAttachedC1EP7QObject
inline QQStyleKitVariationAttached::QQStyleKitVariationAttached(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 191, as _ZNK27QQStyleKitVariationAttached10variationsEv
inline QStringList QQStyleKitVariationAttached::variations() const
{
    return m_variations;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 196, as _ZN27QQStyleKitVariationAttached13setVariationsERK5QListI7QStringE
inline void QQStyleKitVariationAttached::setVariations(const QStringList &variations)
{
    if (m_variations == variations)
        return;

    m_variations = variations;
    emit variationsChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 205, as _ZNK27QQStyleKitVariationAttached11controlTypeEv
inline QQStyleKitExtendableControlType QQStyleKitVariationAttached::controlType() const
{
    return m_controlType;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 210, as _ZN27QQStyleKitVariationAttached14setControlTypeEj
inline void QQStyleKitVariationAttached::setControlType(QQStyleKitExtendableControlType type)
{
    if (m_controlType == type)
        return;

    m_controlType = type;
    emit controlTypeChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitVariationAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQStyleKitVariationAttached10metaObjectEv(
    const QQStyleKitVariationAttached *self) {
  return self->metaObject();
}

//  void *QQStyleKitVariationAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQStyleKitVariationAttached11qt_metacastEPKc(
    QQStyleKitVariationAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitVariationAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQStyleKitVariationAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitVariationAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitVariationAttached::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQStyleKitVariationAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitVariationAttached::tr(s, c, n));
}

//  QQStyleKitVariationAttached::QQStyleKitVariationAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitVariationAttached *ritual_ZN27QQStyleKitVariationAttachedC1EP7QObject(
    QObject *parent) {
  return new QQStyleKitVariationAttached(parent);
}

//  QStringList QQStyleKitVariationAttached::variations() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK27QQStyleKitVariationAttached10variationsEv(
    const QQStyleKitVariationAttached *self) {
  return new QList<QString>(self->variations());
}

//  void QQStyleKitVariationAttached::setVariations(const QStringList
//      &variations)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitVariationAttached13setVariationsERK5QListI7QStringE(
    QQStyleKitVariationAttached *self,
    const QList<QString> *variations) {
  self->setVariations(*variations);
}

//  QQStyleKitExtendableControlType
//      QQStyleKitVariationAttached::controlType() const
extern "C" Q_DECL_EXPORT
QQStyleKitExtendableControlType ritual_ZNK27QQStyleKitVariationAttached11controlTypeEv(
    const QQStyleKitVariationAttached *self) {
  return self->controlType();
}

//  void QQStyleKitVariationAttached::setControlType(QQStyleKitExtendableCont
//      rolType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitVariationAttached14setControlTypeEj(
    QQStyleKitVariationAttached *self,
    QQStyleKitExtendableControlType type) {
  self->setControlType(type);
}

//  void QQStyleKitVariationAttached::variationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitVariationAttached17variationsChangedEv(
    QQStyleKitVariationAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitVariationAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "variationsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "variationsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitVariationAttached::controlTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitVariationAttached18controlTypeChangedEv(
    QQStyleKitVariationAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitVariationAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controlTypeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controlTypeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
