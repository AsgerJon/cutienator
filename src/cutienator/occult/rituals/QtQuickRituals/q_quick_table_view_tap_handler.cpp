//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickTableViewTapHandler' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquicktableview_p.h>
#include <QtQuick/private/qquicktableview_p_p.h>
#include <QtCore/qdir.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qtimer.h>
#include <QtQml/private/qqmlincubator_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQmlModels/private/qqmldelegatecomponent_p.h>
#include <QtQmlModels/private/qqmldelegatemodel_p.h>
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQuick/qquickitemgrabresult.h>
#include <QtQuick/private/qquickflickable_p_p.h>
#include <QtQuick/private/qquickitemviewfxitem_p_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickTableViewTapHandler.cpp, line 1, as moc:QQuickTableViewTapHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickTableViewTapHandler::qt_create_metaobjectdata<qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickTableViewTapHandler"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickTableViewTapHandler, qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickTableViewTapHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickTapHandler::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t>.metaTypes,
    nullptr
} };

void QQuickTableViewTapHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickTableViewTapHandler *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickTableViewTapHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickTableViewTapHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QQuickTableViewTapHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QQuickTapHandler::qt_metacast(_clname);
}

int QQuickTableViewTapHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickTapHandler::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7723, as _ZN25QQuickTableViewTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint
inline bool QQuickTableViewTapHandler::wantsEventPoint(const QPointerEvent *event, const QEventPoint &point)
{
    auto tableView = static_cast<QQuickTableView *>(parentItem()->parent());
    auto tableViewPrivate = QQuickTableViewPrivate::get(tableView);
    return tableViewPrivate->pointerNavigationEnabled && QQuickTapHandler::wantsEventPoint(event, point);
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7717, as _ZN25QQuickTableViewTapHandlerC1EP15QQuickTableView
inline QQuickTableViewTapHandler::QQuickTableViewTapHandler(QQuickTableView *view)
    : QQuickTapHandler(view->contentItem())
{
    setObjectName("tableViewTapHandler");
}
//  -----------------------------------------------------------------------

//  A QQuickTableViewTapHandler that Python can take functions over in. Every QQuickTableViewTapHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickTableViewTapHandlerCall0)(const void *, const QPointerEvent *, const QEventPoint *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewTapHandlerCall1)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewTapHandlerCall2)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewTapHandlerCall3)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewTapHandlerCall4)(const void *, int *);
typedef void (*CuteQQuickTableViewTapHandlerCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewTapHandlerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewTapHandlerCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTableViewTapHandlerCall8)(const void *, int *);
typedef bool (*CuteQQuickTableViewTapHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickTableViewTapHandlerCall10)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewTapHandlerCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewTapHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewTapHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewTapHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewTapHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTableViewTapHandler : public QQuickTableViewTapHandler {
public:
  using QQuickTableViewTapHandler::QQuickTableViewTapHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onActiveChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQuickTableViewTapHandler::wantsEventPoint(const QPointerEvent
  //      *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall0 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall0>(taken[0]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickTableViewTapHandler::wantsEventPoint(event, point);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickTapHandler::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall1 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTapHandler::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent
  //      *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall2 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickSinglePointHandler::wantsPointerEvent(event);
  }

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall3 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall4 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall5 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall6 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall7 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall7>(taken[7]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall8 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onActiveChanged();
  }

  //  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
  //      QEventPoint &point)
  bool canGrab(QPointerEvent *event, const QEventPoint &point) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall9 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall9>(taken[9]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::canGrab(event, point);
  }

  //  bool QQuickPointerHandler::approveGrabTransition(QPointerEvent
  //      *event, const QEventPoint &point, QObject *proposedGrabber)
  bool approveGrabTransition(
      QPointerEvent *event,
      const QEventPoint &point,
      QObject *proposedGrabber) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall10 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall10>(taken[10]);
      bool given = call(this, event, &point, proposedGrabber, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::approveGrabTransition(event, point, proposedGrabber);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall11 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall12 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall13 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall14 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTableViewTapHandlerCall15 call = reinterpret_cast<CuteQQuickTableViewTapHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTableViewTapHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickTableViewTapHandler10metaObjectEv(
    const QQuickTableViewTapHandler *self) {
  return self->metaObject();
}

//  void *QQuickTableViewTapHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickTableViewTapHandler11qt_metacastEPKc(
    QQuickTableViewTapHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTableViewTapHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickTableViewTapHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTableViewTapHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTableViewTapHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickTableViewTapHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTableViewTapHandler::tr(s, c, n));
}

//  QQuickTableViewTapHandler::QQuickTableViewTapHandler(QQuickTableView
//      *view)
extern "C" Q_DECL_EXPORT
QQuickTableViewTapHandler *ritual_ZN25QQuickTableViewTapHandlerC1EP15QQuickTableView(
    QQuickTableView *view) {
  return new CuteQQuickTableViewTapHandler(view);
}

//  bool QQuickTableViewTapHandler::wantsEventPoint(const QPointerEvent
//      *event, const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickTableViewTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickTableViewTapHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->wantsEventPoint(event, *point);
}

//  a Python function taken by a CuteQQuickTableViewTapHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTableViewTapHandler(
    QQuickTableViewTapHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTableViewTapHandler *>(self)->take(key, call);
}

//  bool QQuickTableViewTapHandler::wantsEventPoint(const QPointerEvent
//      *event, const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QQuickTableViewTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickTableViewTapHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->QQuickTableViewTapHandler::wantsEventPoint(event, *point);
}

#endif  // QT_CONFIG(quick_tableview)
