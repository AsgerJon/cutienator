//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcanvascontext_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickCanvasContext' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcanvascontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickcanvascontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickCanvasContext.cpp, line 1, as moc:QQuickCanvasContext
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN19QQuickCanvasContextE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickCanvasContext::qt_create_metaobjectdata<qt_meta_tag_ZN19QQuickCanvasContextE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickCanvasContext",
        "textureChanged",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'textureChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickCanvasContext, qt_meta_tag_ZN19QQuickCanvasContextE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickCanvasContext::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QQuickCanvasContextE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QQuickCanvasContextE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN19QQuickCanvasContextE_t>.metaTypes,
    nullptr
} };

void QQuickCanvasContext::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickCanvasContext *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->textureChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickCanvasContext::*)()>(_a, &QQuickCanvasContext::textureChanged, 0))
            return;
    }
}

const QMetaObject *QQuickCanvasContext::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickCanvasContext::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QQuickCanvasContextE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickCanvasContext::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
    return _id;
}

// SIGNAL 0
void QQuickCanvasContext::textureChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvascontext.cpp, line 29, as _ZN19QQuickCanvasContext5flushEv
inline void QQuickCanvasContext::flush()
{
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvascontext.cpp, line 19, as _ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb
inline void QQuickCanvasContext::prepare(const QSize& canvasSize, const QSize& tileSize, const QRect& canvasWindow, const QRect& dirtyRect, bool smooth, bool antialiasing)
{
    Q_UNUSED(canvasSize);
    Q_UNUSED(tileSize);
    Q_UNUSED(canvasWindow);
    Q_UNUSED(dirtyRect);
    Q_UNUSED(smooth);
    Q_UNUSED(antialiasing);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvascontext.cpp, line 15, as _ZN19QQuickCanvasContextD1Ev
inline QQuickCanvasContext::~QQuickCanvasContext()
{
}
//  -----------------------------------------------------------------------

//  A QQuickCanvasContext that Python can take functions over in. Every QQuickCanvasContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasContextCall0)(const void *, const QSize *, const QSize *, const QRect *, const QRect *, bool, bool, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasContextCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickCanvasContextCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickCanvasContextCall3)(const void *, QV4::ExecutionEngine *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef QV4::ReturnedValue (*CuteQQuickCanvasContextCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef const QImage * (*CuteQQuickCanvasContextCall5)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickCanvasContextCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickCanvasContextCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasContextCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasContextCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasContextCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasContextCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCanvasContextCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickCanvasContext : public QQuickCanvasContext {
public:
  using QQuickCanvasContext::QQuickCanvasContext;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext5flushEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK19QQuickCanvasContext8v4EngineEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext11setV4EngineEPN3QV415ExecutionEngineE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK19QQuickCanvasContext7v4valueEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext7toImageERK6QRectF")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasContext::prepare(const QSize &canvasSize, const
  //      QSize &tileSize, const QRect &canvasWindow, const QRect
  //      &dirtyRect, bool smooth, bool antialiasing)
  void prepare(
      const QSize &canvasSize,
      const QSize &tileSize,
      const QRect &canvasWindow,
      const QRect &dirtyRect,
      bool smooth,
      bool antialiasing) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickCanvasContextCall0 call = reinterpret_cast<CuteQQuickCanvasContextCall0>(taken[0]);
      call(this, &canvasSize, &tileSize, &canvasWindow, &dirtyRect, smooth, antialiasing, &handled);
      if (handled) return;
    }
    QQuickCanvasContext::prepare(canvasSize, tileSize, canvasWindow, dirtyRect, smooth, antialiasing);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasContext::flush()
  void flush() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickCanvasContextCall1 call = reinterpret_cast<CuteQQuickCanvasContextCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickCanvasContext::flush();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QV4::ExecutionEngine *QQuickCanvasContext::v4Engine() const
  QV4::ExecutionEngine *v4Engine() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickCanvasContextCall2 call = reinterpret_cast<CuteQQuickCanvasContextCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QV4::ExecutionEngine *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickCanvasContext::setV4Engine(QV4::ExecutionEngine *engine)
  void setV4Engine(QV4::ExecutionEngine *engine) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickCanvasContextCall3 call = reinterpret_cast<CuteQQuickCanvasContextCall3>(taken[3]);
      call(this, engine, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QV4::ReturnedValue QQuickCanvasContext::v4value() const
  QV4::ReturnedValue v4value() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickCanvasContextCall4 call = reinterpret_cast<CuteQQuickCanvasContextCall4>(taken[4]);
      QV4::ReturnedValue given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QImage QQuickCanvasContext::toImage(const QRectF &bounds)
  QImage toImage(const QRectF &bounds) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickCanvasContextCall5 call = reinterpret_cast<CuteQQuickCanvasContextCall5>(taken[5]);
      const QImage * given = call(this, &bounds, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_canvas)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickCanvasContextCall6 call = reinterpret_cast<CuteQQuickCanvasContextCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickCanvasContextCall7 call = reinterpret_cast<CuteQQuickCanvasContextCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickCanvasContextCall8 call = reinterpret_cast<CuteQQuickCanvasContextCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickCanvasContextCall9 call = reinterpret_cast<CuteQQuickCanvasContextCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickCanvasContextCall10 call = reinterpret_cast<CuteQQuickCanvasContextCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickCanvasContextCall11 call = reinterpret_cast<CuteQQuickCanvasContextCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickCanvasContextCall12 call = reinterpret_cast<CuteQQuickCanvasContextCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickCanvasContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickCanvasContext10metaObjectEv(
    const QQuickCanvasContext *self) {
  return self->metaObject();
}

//  void *QQuickCanvasContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickCanvasContext11qt_metacastEPKc(
    QQuickCanvasContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickCanvasContext::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickCanvasContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickCanvasContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickCanvasContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickCanvasContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCanvasContext::tr(s, c, n));
}

//  QQuickCanvasContext::~QQuickCanvasContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCanvasContextD1Ev(QQuickCanvasContext *self) {
  delete self;
}

//  QStringList QQuickCanvasContext::contextNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QQuickCanvasContext12contextNamesEv(
    const QQuickCanvasContext *self) {
  return new QList<QString>(self->contextNames());
}

//  void QQuickCanvasContext::init(QQuickCanvasItem *canvasItem, const
//      QVariantMap &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCanvasContext4initEP16QQuickCanvasItemRK4QMapI7QString8QVariantE(
    QQuickCanvasContext *self,
    QQuickCanvasItem *canvasItem,
    const QMap<QString, QVariant> *args) {
  self->init(canvasItem, *args);
}

//  void QQuickCanvasContext::prepare(const QSize &canvasSize, const QSize
//      &tileSize, const QRect &canvasWindow, const QRect &dirtyRect, bool
//      smooth, bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb(
    QQuickCanvasContext *self,
    const QSize *canvasSize,
    const QSize *tileSize,
    const QRect *canvasWindow,
    const QRect *dirtyRect,
    bool smooth,
    bool antialiasing) {
  self->prepare(
      *canvasSize,
      *tileSize,
      *canvasWindow,
      *dirtyRect,
      smooth,
      antialiasing);
}

//  void QQuickCanvasContext::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCanvasContext5flushEv(QQuickCanvasContext *self) {
  self->flush();
}

//  QV4::ExecutionEngine *QQuickCanvasContext::v4Engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK19QQuickCanvasContext8v4EngineEv(
    const QQuickCanvasContext *self) {
  return self->v4Engine();
}

//  void QQuickCanvasContext::setV4Engine(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCanvasContext11setV4EngineEPN3QV415ExecutionEngineE(
    QQuickCanvasContext *self,
    QV4::ExecutionEngine *engine) {
  self->setV4Engine(engine);
}

//  QV4::ReturnedValue QQuickCanvasContext::v4value() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK19QQuickCanvasContext7v4valueEv(
    const QQuickCanvasContext *self) {
  return self->v4value();
}

//  QImage QQuickCanvasContext::toImage(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QQuickCanvasContext7toImageERK6QRectF(
    QQuickCanvasContext *self,
    const QRectF *bounds) {
  return new QImage(self->toImage(*bounds));
}

//  void QQuickCanvasContext::textureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCanvasContext14textureChangedEv(
    QQuickCanvasContext *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickCanvasContext")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textureChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textureChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuickCanvasContext, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickCanvasContext(
    QQuickCanvasContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickCanvasContext *>(self)->take(key, call);
}

//  void QQuickCanvasContext::prepare(const QSize &canvasSize, const QSize
//      &tileSize, const QRect &canvasWindow, const QRect &dirtyRect, bool
//      smooth, bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb(
    QQuickCanvasContext *self,
    const QSize *canvasSize,
    const QSize *tileSize,
    const QRect *canvasWindow,
    const QRect *dirtyRect,
    bool smooth,
    bool antialiasing) {
  self->QQuickCanvasContext::prepare(
      *canvasSize,
      *tileSize,
      *canvasWindow,
      *dirtyRect,
      smooth,
      antialiasing);
}

//  void QQuickCanvasContext::flush()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickCanvasContext5flushEv(QQuickCanvasContext *self) {
  self->QQuickCanvasContext::flush();
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
