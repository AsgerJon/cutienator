//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQmlDelegateModelParts'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 1 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtQmlModels/private/qqmlabstractdelegatecomponent_p.h>
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertytopropertybinding_p.h>
#include <QtQmlModels/private/qqmltableinstancemodel_p.h>
#include <QtQmlModels/private/qquickpackage_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQmlModels__QQmlDelegateModelParts.cpp, line 1, as moc:QQmlDelegateModelParts
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QQmlDelegateModelPartsE_t {};
} // unnamed namespace

template <> constexpr inline auto QQmlDelegateModelParts::qt_create_metaobjectdata<qt_meta_tag_ZN22QQmlDelegateModelPartsE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQmlDelegateModelParts"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQmlDelegateModelParts, qt_meta_tag_ZN22QQmlDelegateModelPartsE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQmlDelegateModelParts::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQmlDelegateModelPartsE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQmlDelegateModelPartsE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QQmlDelegateModelPartsE_t>.metaTypes,
    nullptr
} };

void QQmlDelegateModelParts::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQmlDelegateModelParts *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQmlDelegateModelParts::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQmlDelegateModelParts::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQmlDelegateModelPartsE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQmlDelegateModelParts::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 116, as _ZN32QQmlDelegateModelPartsMetaObject15propertyCreatedEiR20QMetaPropertyBuilder
inline void QQmlDelegateModelPartsMetaObject::propertyCreated(int, QMetaPropertyBuilder &prop)
{
    prop.setWritable(false);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 121, as _ZN32QQmlDelegateModelPartsMetaObject12initialValueEi
inline QVariant QQmlDelegateModelPartsMetaObject::initialValue(int id)
{
    QQmlDelegateModelParts *parts = static_cast<QQmlDelegateModelParts *>(object());
    QQmlPartsModel *m = new QQmlPartsModel(
            parts->model, QString::fromUtf8(name(id)), parts);
    parts->models.append(m);
    return QVariant::fromValue(static_cast<QObject *>(m));
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3718, as _ZN14QQmlPartsModelC1EP17QQmlDelegateModelRK7QStringP7QObject
inline QQmlPartsModel::QQmlPartsModel(QQmlDelegateModel *model, const QString &part, QObject *parent)
    : QQmlInstanceModel(*new QObjectPrivate, parent)
    , m_model(model)
    , m_part(part)
    , m_compositorGroup(Compositor::Cache)
    , m_inheritGroup(true)
{
    QQmlDelegateModelPrivate *d = QQmlDelegateModelPrivate::get(m_model);
    if (d->m_cacheMetaType) {
        QQmlDelegateModelGroupPrivate::get(d->m_groups[1])->emitters.insert(this);
        m_compositorGroup = Compositor::Default;
    } else {
        d->m_pendingParts.insert(this);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1232, as _ZN29QQmlDelegateModelGroupEmitterD2Ev
inline QQmlDelegateModelGroupEmitter::~QQmlDelegateModelGroupEmitter() = default;

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1233, as _ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupEmitter::createdPackage(int, QQuickPackage *) {}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1234, as _ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupEmitter::initPackage(int, QQuickPackage *) {}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1235, as _ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuickPackage
inline void QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage *) {}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 130, as _ZN22QQmlDelegateModelPartsC1EP17QQmlDelegateModel
inline QQmlDelegateModelParts::QQmlDelegateModelParts(QQmlDelegateModel *parent)
: QObject(parent), model(parent)
{
    new QQmlDelegateModelPartsMetaObject(this);
}
//  -----------------------------------------------------------------------

//  A QQmlDelegateModelParts that Python can take functions over in. Every QQmlDelegateModelParts
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelPartsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelPartsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelPartsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelPartsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelPartsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelPartsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelPartsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDelegateModelParts : public QQmlDelegateModelParts {
public:
  using QQmlDelegateModelParts::QQmlDelegateModelParts;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall0 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall1 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall2 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall3 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall4 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall5 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsCall6 call = reinterpret_cast<CuteQQmlDelegateModelPartsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDelegateModelParts::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlDelegateModelParts10metaObjectEv(
    const QQmlDelegateModelParts *self) {
  return self->metaObject();
}

//  void *QQmlDelegateModelParts::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQmlDelegateModelParts11qt_metacastEPKc(
    QQmlDelegateModelParts *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDelegateModelParts::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlDelegateModelParts11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDelegateModelParts *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlDelegateModelParts::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQmlDelegateModelParts2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDelegateModelParts::tr(s, c, n));
}

//  a Python function taken by a CuteQQmlDelegateModelParts, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelParts(
    QQmlDelegateModelParts *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelParts *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
