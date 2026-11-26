//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qquickgraphscolor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickGraphsColor' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qquickgraphscolor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGraphs/private/qquickgraphscolor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__QQuickGraphsColor.cpp, line 1, as moc:QQuickGraphsColor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN17QQuickGraphsColorE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickGraphsColor::qt_create_metaobjectdata<qt_meta_tag_ZN17QQuickGraphsColorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickGraphsColor",
        "QML.Element",
        "Color",
        "colorChanged",
        "",
        "QColor",
        "color"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'colorChanged'
        QtMocHelpers::SignalData<void(QColor)>(3, 4, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 5, 6 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'color'
        QtMocHelpers::PropertyData<QColor>(6, 0x80000000 | 5, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 0),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQuickGraphsColor, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickGraphsColor::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QQuickGraphsColorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QQuickGraphsColorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN17QQuickGraphsColorE_t>.metaTypes,
    nullptr
} };

void QQuickGraphsColor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickGraphsColor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->colorChanged((*reinterpret_cast<std::add_pointer_t<QColor>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickGraphsColor::*)(QColor )>(_a, &QQuickGraphsColor::colorChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QColor*>(_v) = _t->color(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setColor(*reinterpret_cast<QColor*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickGraphsColor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickGraphsColor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QQuickGraphsColorE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickGraphsColor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
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
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QQuickGraphsColor::colorChanged(QColor _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}
QT_WARNING_POP

//  from ../qtgraphs/src/common/theme/qquickgraphscolor.cpp, line 14, as _ZN17QQuickGraphsColorD0Ev
inline QQuickGraphsColor::~QQuickGraphsColor() {}

//  from ../qtgraphs/src/common/theme/qquickgraphscolor.cpp, line 10, as _ZN17QQuickGraphsColorC1EP7QObject
inline QQuickGraphsColor::QQuickGraphsColor(QObject *parent)
    : QObject(parent)
{}

//  from ../qtgraphs/src/common/theme/qquickgraphscolor.cpp, line 16, as _ZN17QQuickGraphsColor8setColorE6QColor
inline void QQuickGraphsColor::setColor(QColor color)
{
    if (m_color != color) {
        m_color = color;
        emit colorChanged(color);
    }
}

//  from ../qtgraphs/src/common/theme/qquickgraphscolor.cpp, line 24, as _ZNK17QQuickGraphsColor5colorEv
inline QColor QQuickGraphsColor::color() const
{
    return m_color;
}
//  -----------------------------------------------------------------------

//  A QQuickGraphsColor that Python can take functions over in. Every QQuickGraphsColor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsColorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickGraphsColorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsColorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsColorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsColorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsColorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickGraphsColorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickGraphsColor : public QQuickGraphsColor {
public:
  using QQuickGraphsColor::QQuickGraphsColor;
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
      CuteQQuickGraphsColorCall0 call = reinterpret_cast<CuteQQuickGraphsColorCall0>(taken[0]);
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
      CuteQQuickGraphsColorCall1 call = reinterpret_cast<CuteQQuickGraphsColorCall1>(taken[1]);
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
      CuteQQuickGraphsColorCall2 call = reinterpret_cast<CuteQQuickGraphsColorCall2>(taken[2]);
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
      CuteQQuickGraphsColorCall3 call = reinterpret_cast<CuteQQuickGraphsColorCall3>(taken[3]);
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
      CuteQQuickGraphsColorCall4 call = reinterpret_cast<CuteQQuickGraphsColorCall4>(taken[4]);
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
      CuteQQuickGraphsColorCall5 call = reinterpret_cast<CuteQQuickGraphsColorCall5>(taken[5]);
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
      CuteQQuickGraphsColorCall6 call = reinterpret_cast<CuteQQuickGraphsColorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickGraphsColor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickGraphsColor10metaObjectEv(
    const QQuickGraphsColor *self) {
  return self->metaObject();
}

//  void *QQuickGraphsColor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickGraphsColor11qt_metacastEPKc(
    QQuickGraphsColor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickGraphsColor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickGraphsColor11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickGraphsColor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickGraphsColor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickGraphsColor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGraphsColor::tr(s, c, n));
}

//  QQuickGraphsColor::QQuickGraphsColor(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickGraphsColor *ritual_ZN17QQuickGraphsColorC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickGraphsColor(parent);
}

//  QQuickGraphsColor::~QQuickGraphsColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickGraphsColorD1Ev(QQuickGraphsColor *self) {
  delete self;
}

//  void QQuickGraphsColor::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickGraphsColor8setColorE6QColor(
    QQuickGraphsColor *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QQuickGraphsColor::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QQuickGraphsColor5colorEv(
    const QQuickGraphsColor *self) {
  return new QColor(self->color());
}

//  void QQuickGraphsColor::colorChanged(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickGraphsColor12colorChangedE6QColor(
    QQuickGraphsColor *self,
    const QColor *color) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickGraphsColor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "colorChanged(QColor)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "colorChanged(QColor)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(color)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuickGraphsColor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGraphsColor(
    QQuickGraphsColor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGraphsColor *>(self)->take(key, call);
}

//  QList<QQuickGraphsColor *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickGraphsColor *> *ritual_list_make_QQuickGraphsColor_ptr() {
  return new QList<QQuickGraphsColor *>();
}

//  void QList<QQuickGraphsColor *>::append(const QQuickGraphsColor * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickGraphsColor_ptr(
    QList<QQuickGraphsColor *> *self,
    QQuickGraphsColor *element) {
  self->append(element);
}

//  qsizetype QList<QQuickGraphsColor *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickGraphsColor_ptr(
    const QList<QQuickGraphsColor *> *self) {
  return self->size();
}

//  const QQuickGraphsColor * &QList<QQuickGraphsColor *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuickGraphsColor *ritual_list_at_QQuickGraphsColor_ptr(
    const QList<QQuickGraphsColor *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickGraphsColor *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickGraphsColor_ptr(
    QList<QQuickGraphsColor *> *self) {
  delete self;
}
