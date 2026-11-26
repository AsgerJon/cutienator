//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandinputmethodcontrol.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QWaylandInputMethodControl' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  4 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(im)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWaylandCompositor/qwaylandinputmethodcontrol.h>
#include <QtWaylandCompositor/private/qwaylandinputmethodcontrol_p.h>
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtWaylandCompositor/qwaylandseat.h>
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtWaylandCompositor/qwaylandtextinput.h>
#include <QtWaylandCompositor/qwaylandtextinputv3.h>
#include <QtWaylandCompositor/qwaylandqttextinputmethod.h>
#include <QtGui/QInputMethodEvent>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWaylandCompositor__QWaylandInputMethodControl.cpp, line 1, as moc:QWaylandInputMethodControl
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN26QWaylandInputMethodControlE_t {};
} // unnamed namespace

template <> constexpr inline auto QWaylandInputMethodControl::qt_create_metaobjectdata<qt_meta_tag_ZN26QWaylandInputMethodControlE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QWaylandInputMethodControl",
        "enabledChanged",
        "",
        "enabled",
        "updateInputMethod",
        "Qt::InputMethodQueries",
        "queries"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'enabledChanged'
        QtMocHelpers::SignalData<void(bool)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Bool, 3 },
        }}),
        // Signal 'updateInputMethod'
        QtMocHelpers::SignalData<void(Qt::InputMethodQueries)>(4, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 6 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'enabled'
        QtMocHelpers::PropertyData<bool>(3, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet, 0),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QWaylandInputMethodControl, qt_meta_tag_ZN26QWaylandInputMethodControlE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QWaylandInputMethodControl::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QWaylandInputMethodControlE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QWaylandInputMethodControlE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN26QWaylandInputMethodControlE_t>.metaTypes,
    nullptr
} };

void QWaylandInputMethodControl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QWaylandInputMethodControl *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->enabledChanged((*reinterpret_cast<std::add_pointer_t<bool>>(_a[1]))); break;
        case 1: _t->updateInputMethod((*reinterpret_cast<std::add_pointer_t<Qt::InputMethodQueries>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QWaylandInputMethodControl::*)(bool )>(_a, &QWaylandInputMethodControl::enabledChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QWaylandInputMethodControl::*)(Qt::InputMethodQueries )>(_a, &QWaylandInputMethodControl::updateInputMethod, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<bool*>(_v) = _t->enabled(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setEnabled(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QWaylandInputMethodControl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QWaylandInputMethodControl::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QWaylandInputMethodControlE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QWaylandInputMethodControl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QWaylandInputMethodControl::enabledChanged(bool _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QWaylandInputMethodControl::updateInputMethod(Qt::InputMethodQueries _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 84, as _ZNK26QWaylandInputMethodControl7enabledEv
inline bool QWaylandInputMethodControl::enabled() const
{
    Q_D(const QWaylandInputMethodControl);

    return d->enabled;
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 91, as _ZN26QWaylandInputMethodControl10setEnabledEb
inline void QWaylandInputMethodControl::setEnabled(bool enabled)
{
    Q_D(QWaylandInputMethodControl);

    if (d->enabled == enabled)
        return;

    d->enabled = enabled;
    emit enabledChanged(enabled);
    emit updateInputMethod(Qt::ImQueryInput);
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 136, as _ZN26QWaylandInputMethodControl15updateTextInputEv
inline void QWaylandInputMethodControl::updateTextInput()
{
    QWaylandTextInput *textInput = d_func()->textInput();

    if (textInput) {
        connect(textInput, &QWaylandTextInput::surfaceEnabled, this, &QWaylandInputMethodControl::surfaceEnabled, Qt::UniqueConnection);
        connect(textInput, &QWaylandTextInput::surfaceDisabled, this, &QWaylandInputMethodControl::surfaceDisabled, Qt::UniqueConnection);
        connect(textInput, &QWaylandTextInput::updateInputMethod, this, &QWaylandInputMethodControl::updateInputMethod, Qt::UniqueConnection);
    }
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 103, as _ZN26QWaylandInputMethodControl14surfaceEnabledEP15QWaylandSurface
inline void QWaylandInputMethodControl::surfaceEnabled(QWaylandSurface *surface)
{
    Q_D(QWaylandInputMethodControl);

    if (surface == d->surface)
        setEnabled(true);
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandinputmethodcontrol.cpp, line 111, as _ZN26QWaylandInputMethodControl15surfaceDisabledEP15QWaylandSurface
inline void QWaylandInputMethodControl::surfaceDisabled(QWaylandSurface *surface)
{
    Q_D(QWaylandInputMethodControl);

    if (surface == d->surface)
        setEnabled(false);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWaylandInputMethodControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWaylandInputMethodControl10metaObjectEv(
    const QWaylandInputMethodControl *self) {
  return self->metaObject();
}

//  void *QWaylandInputMethodControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWaylandInputMethodControl11qt_metacastEPKc(
    QWaylandInputMethodControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandInputMethodControl::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWaylandInputMethodControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandInputMethodControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandInputMethodControl::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWaylandInputMethodControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandInputMethodControl::tr(s, c, n));
}

//  QWaylandInputMethodControlPrivate *QWaylandInputMethodControl::d_func()
extern "C" Q_DECL_EXPORT
QWaylandInputMethodControlPrivate *ritual_ZN26QWaylandInputMethodControl6d_funcEv(
    QWaylandInputMethodControl *self) {
  return self->d_func();
}

//  const QWaylandInputMethodControlPrivate
//      *QWaylandInputMethodControl::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandInputMethodControlPrivate *ritual_ZNK26QWaylandInputMethodControl6d_funcEv(
    const QWaylandInputMethodControl *self) {
  return self->d_func();
}

//  bool QWaylandInputMethodControl::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWaylandInputMethodControl7enabledEv(
    const QWaylandInputMethodControl *self) {
  return self->enabled();
}

//  void QWaylandInputMethodControl::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl10setEnabledEb(
    QWaylandInputMethodControl *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QWaylandInputMethodControl::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl14enabledChangedEb(
    QWaylandInputMethodControl *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWaylandInputMethodControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWaylandInputMethodControl::updateInputMethod(Qt::InputMethodQueries
//      queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl17updateInputMethodE6QFlagsIN2Qt16InputMethodQueryEE(
    QWaylandInputMethodControl *self,
    int queries) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWaylandInputMethodControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateInputMethod(Qt::InputMethodQueries)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateInputMethod(Qt::InputMethodQueries)");
  Qt::InputMethodQueries value0 = QFlags<Qt::InputMethodQuery>::fromInt(queries);
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&value0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QWaylandInputMethodControl::surfaceEnabled(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl14surfaceEnabledEP15QWaylandSurface(
    QWaylandInputMethodControl *self,
    QWaylandSurface *surface) {
  self->surfaceEnabled(surface);
}

//  void QWaylandInputMethodControl::surfaceDisabled(QWaylandSurface
//      *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandInputMethodControl15surfaceDisabledEP15QWaylandSurface(
    QWaylandInputMethodControl *self,
    QWaylandSurface *surface) {
  self->surfaceDisabled(surface);
}

#endif  // QT_CONFIG(im)
