//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickDropAreaDrag' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickdroparea_p.h>
#include <QtQuick/private/qquickdrag_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtCore/qpointer.h>
#include <QtCore/qregularexpression.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 26, as local:qquickdroparea.cpp:QQuickDropAreaPrivate
class QQuickDropAreaPrivate : public QQuickItemPrivate
{
    Q_DECLARE_PUBLIC(QQuickDropArea)

public:
    QQuickDropAreaPrivate();
    ~QQuickDropAreaPrivate();

    bool hasMatchingKey(const QStringList &keys) const;

    QStringList getKeys(const QMimeData *mimeData) const;

    QStringList keys;
    QRegularExpression keyRegExp;
    QPointF dragPosition;
    QQuickDropAreaDrag *drag;
    QPointer<QObject> source;
    bool containsDrag;
};

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 46, as local:qquickdroparea.cpp:QQuickDropAreaPrivate::QQuickDropAreaPrivate
inline QQuickDropAreaPrivate::QQuickDropAreaPrivate()
    : drag(nullptr)
    , containsDrag(false)
{
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 52, as local:qquickdroparea.cpp:QQuickDropAreaPrivate::~QQuickDropAreaPrivate
inline QQuickDropAreaPrivate::~QQuickDropAreaPrivate()
{
    delete drag;
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 199, as local:qquickdroparea.cpp:QQuickDropAreaPrivate::hasMatchingKey
inline bool QQuickDropAreaPrivate::hasMatchingKey(const QStringList &keys) const
{
    if (keyRegExp.pattern().isEmpty())
        return true;

    for (const QString &key : keys) {
        if (key.contains(keyRegExp))
            return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 211, as local:qquickdroparea.cpp:QQuickDropAreaPrivate::getKeys
inline QStringList QQuickDropAreaPrivate::getKeys(const QMimeData *mimeData) const
{
    if (const QQuickDragMimeData *dragMime = qobject_cast<const QQuickDragMimeData *>(mimeData))
        return dragMime->keys();
    return mimeData->formats();
}

//  from QtQuick__QQuickDropAreaDrag.cpp, line 1, as moc:QQuickDropAreaDrag
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QQuickDropAreaDragE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickDropAreaDrag::qt_create_metaobjectdata<qt_meta_tag_ZN18QQuickDropAreaDragE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickDropAreaDrag",
        "QML.Element",
        "anonymous",
        "QML.AddedInVersion",
        "512",
        "positionChanged",
        "",
        "sourceChanged",
        "x",
        "y",
        "source"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'positionChanged'
        QtMocHelpers::SignalData<void()>(5, 6, QMC::AccessPublic, QMetaType::Void),
        // Signal 'sourceChanged'
        QtMocHelpers::SignalData<void()>(7, 6, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'x'
        QtMocHelpers::PropertyData<qreal>(8, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Final, 0),
        // property 'y'
        QtMocHelpers::PropertyData<qreal>(9, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Final, 0),
        // property 'source'
        QtMocHelpers::PropertyData<QObject*>(10, QMetaType::QObjectStar, QMC::DefaultPropertyFlags | QMC::Final, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickDropAreaDrag, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickDropAreaDrag::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickDropAreaDragE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickDropAreaDragE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QQuickDropAreaDragE_t>.metaTypes,
    nullptr
} };

void QQuickDropAreaDrag::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickDropAreaDrag *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->positionChanged(); break;
        case 1: _t->sourceChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickDropAreaDrag::*)()>(_a, &QQuickDropAreaDrag::positionChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickDropAreaDrag::*)()>(_a, &QQuickDropAreaDrag::sourceChanged, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<qreal*>(_v) = _t->x(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->y(); break;
        case 2: *reinterpret_cast<QObject**>(_v) = _t->source(); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickDropAreaDrag::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickDropAreaDrag::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQuickDropAreaDragE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickDropAreaDrag::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
void QQuickDropAreaDrag::positionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickDropAreaDrag::sourceChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 173, as _ZNK18QQuickDropAreaDrag1yEv
inline qreal QQuickDropAreaDrag::y() const
{
    return d->dragPosition.y();
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 155, as _ZNK18QQuickDropAreaDrag6sourceEv
inline QObject *QQuickDropAreaDrag::source() const
{
    return d->source;
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 16, as _ZN18QQuickDropAreaDragC1EP21QQuickDropAreaPrivateP7QObject
inline QQuickDropAreaDrag::QQuickDropAreaDrag(QQuickDropAreaPrivate *d, QObject *parent)
    : QObject(parent)
    , d(d)
{
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 22, as _ZN18QQuickDropAreaDragD1Ev
inline QQuickDropAreaDrag::~QQuickDropAreaDrag()
{
}

//  from ../qtdeclarative/src/quick/items/qquickdroparea.cpp, line 168, as _ZNK18QQuickDropAreaDrag1xEv
inline qreal QQuickDropAreaDrag::x() const
{
    return d->dragPosition.x();
}
//  -----------------------------------------------------------------------

//  A QQuickDropAreaDrag that Python can take functions over in. Every QQuickDropAreaDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDropAreaDragCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDropAreaDragCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaDragCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaDragCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaDragCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaDragCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDropAreaDragCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDropAreaDrag : public QQuickDropAreaDrag {
public:
  using QQuickDropAreaDrag::QQuickDropAreaDrag;
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
      CuteQQuickDropAreaDragCall0 call = reinterpret_cast<CuteQQuickDropAreaDragCall0>(taken[0]);
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
      CuteQQuickDropAreaDragCall1 call = reinterpret_cast<CuteQQuickDropAreaDragCall1>(taken[1]);
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
      CuteQQuickDropAreaDragCall2 call = reinterpret_cast<CuteQQuickDropAreaDragCall2>(taken[2]);
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
      CuteQQuickDropAreaDragCall3 call = reinterpret_cast<CuteQQuickDropAreaDragCall3>(taken[3]);
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
      CuteQQuickDropAreaDragCall4 call = reinterpret_cast<CuteQQuickDropAreaDragCall4>(taken[4]);
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
      CuteQQuickDropAreaDragCall5 call = reinterpret_cast<CuteQQuickDropAreaDragCall5>(taken[5]);
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
      CuteQQuickDropAreaDragCall6 call = reinterpret_cast<CuteQQuickDropAreaDragCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDropAreaDrag::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickDropAreaDrag10metaObjectEv(
    const QQuickDropAreaDrag *self) {
  return self->metaObject();
}

//  void *QQuickDropAreaDrag::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickDropAreaDrag11qt_metacastEPKc(
    QQuickDropAreaDrag *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickDropAreaDrag::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickDropAreaDrag11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickDropAreaDrag *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickDropAreaDrag::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickDropAreaDrag2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDropAreaDrag::tr(s, c, n));
}

//  void QQuickDropAreaDrag::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDropAreaDrag22qt_qmlMarker_anonymousEv(
    QQuickDropAreaDrag *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickDropAreaDrag::QQuickDropAreaDrag(QQuickDropAreaPrivate *d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickDropAreaDrag *ritual_ZN18QQuickDropAreaDragC1EP21QQuickDropAreaPrivateP7QObject(
    QQuickDropAreaPrivate *d,
    QObject *parent) {
  return new CuteQQuickDropAreaDrag(d, parent);
}

//  QQuickDropAreaDrag::~QQuickDropAreaDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDropAreaDragD1Ev(QQuickDropAreaDrag *self) {
  delete self;
}

//  qreal QQuickDropAreaDrag::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickDropAreaDrag1xEv(const QQuickDropAreaDrag *self) {
  return self->x();
}

//  void QQuickDropAreaDrag::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDropAreaDrag15positionChangedEv(
    QQuickDropAreaDrag *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickDropAreaDrag")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "positionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "positionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickDropAreaDrag::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickDropAreaDrag13sourceChangedEv(
    QQuickDropAreaDrag *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickDropAreaDrag")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuickDropAreaDrag, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDropAreaDrag(
    QQuickDropAreaDrag *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDropAreaDrag *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_draganddrop)
