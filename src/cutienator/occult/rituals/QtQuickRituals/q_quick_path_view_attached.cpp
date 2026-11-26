//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickPathViewAttached'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickpathview_p.h>
#include <QtQuick/private/qquickpathview_p_p.h>
#include <QtQuick/private/qquickflickablebehavior_p.h> //Contains flicking behavior defines
#include <QtQuick/private/qquicktext_p.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <private/qqmlchangeset_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/qevent.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qmath.h>
#include <cmath>
#if QT_CONFIG(quick_itemview)
#include <QtQuick/private/qquickitemview_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickPathViewAttached.cpp, line 1, as moc:QQuickPathViewAttached
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QQuickPathViewAttachedE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickPathViewAttached::qt_create_metaobjectdata<qt_meta_tag_ZN22QQuickPathViewAttachedE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickPathViewAttached",
        "currentItemChanged",
        "",
        "pathChanged",
        "view",
        "QQuickPathView*",
        "isCurrentItem",
        "onPath"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'currentItemChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'pathChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'view'
        QtMocHelpers::PropertyData<QQuickPathView*>(4, 0x80000000 | 5, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Constant | QMC::Final),
        // property 'isCurrentItem'
        QtMocHelpers::PropertyData<bool>(6, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 0),
        // property 'onPath'
        QtMocHelpers::PropertyData<bool>(7, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickPathViewAttached, qt_meta_tag_ZN22QQuickPathViewAttachedE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickPathViewAttached::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickPathViewAttachedE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickPathViewAttachedE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QQuickPathViewAttachedE_t>.metaTypes,
    nullptr
} };

void QQuickPathViewAttached::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickPathViewAttached *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->currentItemChanged(); break;
        case 1: _t->pathChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickPathViewAttached::*)()>(_a, &QQuickPathViewAttached::currentItemChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickPathViewAttached::*)()>(_a, &QQuickPathViewAttached::pathChanged, 1))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 0:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QQuickPathView* >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQuickPathView**>(_v) = _t->view(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->isCurrentItem(); break;
        case 2: *reinterpret_cast<bool*>(_v) = _t->isOnPath(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickPathViewAttached::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickPathViewAttached::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QQuickPathViewAttachedE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickPathViewAttached::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void QQuickPathViewAttached::currentItemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickPathViewAttached::pathChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 53, as _ZN22QQuickPathViewAttachedD1Ev
inline QQuickPathViewAttached::~QQuickPathViewAttached()
{
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 57, as _ZNK22QQuickPathViewAttached5valueERK10QByteArray
inline QVariant QQuickPathViewAttached::value(const QByteArray &name) const
{
    return m_metaobject->value(name);
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 61, as _ZN22QQuickPathViewAttached8setValueERK10QByteArrayRK8QVariant
inline void QQuickPathViewAttached::setValue(const QByteArray &name, const QVariant &val)
{
    m_metaobject->setValue(name, val);
}
//  -----------------------------------------------------------------------

//  A QQuickPathViewAttached that Python can take functions over in. Every QQuickPathViewAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathViewAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathViewAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathViewAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPathViewAttached : public QQuickPathViewAttached {
public:
  using QQuickPathViewAttached::QQuickPathViewAttached;
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
      CuteQQuickPathViewAttachedCall0 call = reinterpret_cast<CuteQQuickPathViewAttachedCall0>(taken[0]);
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
      CuteQQuickPathViewAttachedCall1 call = reinterpret_cast<CuteQQuickPathViewAttachedCall1>(taken[1]);
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
      CuteQQuickPathViewAttachedCall2 call = reinterpret_cast<CuteQQuickPathViewAttachedCall2>(taken[2]);
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
      CuteQQuickPathViewAttachedCall3 call = reinterpret_cast<CuteQQuickPathViewAttachedCall3>(taken[3]);
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
      CuteQQuickPathViewAttachedCall4 call = reinterpret_cast<CuteQQuickPathViewAttachedCall4>(taken[4]);
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
      CuteQQuickPathViewAttachedCall5 call = reinterpret_cast<CuteQQuickPathViewAttachedCall5>(taken[5]);
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
      CuteQQuickPathViewAttachedCall6 call = reinterpret_cast<CuteQQuickPathViewAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPathViewAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickPathViewAttached10metaObjectEv(
    const QQuickPathViewAttached *self) {
  return self->metaObject();
}

//  void *QQuickPathViewAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickPathViewAttached11qt_metacastEPKc(
    QQuickPathViewAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPathViewAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickPathViewAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPathViewAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPathViewAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickPathViewAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathViewAttached::tr(s, c, n));
}

//  QQuickPathViewAttached::~QQuickPathViewAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttachedD1Ev(QQuickPathViewAttached *self) {
  delete self;
}

//  QQuickPathView *QQuickPathViewAttached::view() const
extern "C" Q_DECL_EXPORT
QQuickPathView *ritual_ZNK22QQuickPathViewAttached4viewEv(
    const QQuickPathViewAttached *self) {
  return self->view();
}

//  bool QQuickPathViewAttached::isCurrentItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickPathViewAttached13isCurrentItemEv(
    const QQuickPathViewAttached *self) {
  return self->isCurrentItem();
}

//  void QQuickPathViewAttached::setIsCurrentItem(bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttached16setIsCurrentItemEb(
    QQuickPathViewAttached *self,
    bool c) {
  self->setIsCurrentItem(c);
}

//  QVariant QQuickPathViewAttached::value(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QQuickPathViewAttached5valueERK10QByteArray(
    const QQuickPathViewAttached *self,
    const QByteArray *name) {
  return new QVariant(self->value(*name));
}

//  void QQuickPathViewAttached::setValue(const QByteArray &name, const
//      QVariant &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttached8setValueERK10QByteArrayRK8QVariant(
    QQuickPathViewAttached *self,
    const QByteArray *name,
    const QVariant *val) {
  self->setValue(*name, *val);
}

//  bool QQuickPathViewAttached::isOnPath() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickPathViewAttached8isOnPathEv(
    const QQuickPathViewAttached *self) {
  return self->isOnPath();
}

//  void QQuickPathViewAttached::setOnPath(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttached9setOnPathEb(
    QQuickPathViewAttached *self,
    bool on) {
  self->setOnPath(on);
}

//  void QQuickPathViewAttached::currentItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttached18currentItemChangedEv(
    QQuickPathViewAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPathViewAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentItemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentItemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickPathViewAttached::pathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPathViewAttached11pathChangedEv(
    QQuickPathViewAttached *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickPathViewAttached")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "pathChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "pathChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuickPathViewAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathViewAttached(
    QQuickPathViewAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathViewAttached *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_pathview)
#endif  // QT_CONFIG(quick_pathview)
