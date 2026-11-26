//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickTableViewHoverHandler' is pasted in, cut from what the moc of Qt
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickTableViewHoverHandler.cpp, line 1, as moc:QQuickTableViewHoverHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickTableViewHoverHandler::qt_create_metaobjectdata<qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickTableViewHoverHandler"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickTableViewHoverHandler, qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickTableViewHoverHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickHoverHandler::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t>.metaTypes,
    nullptr
} };

void QQuickTableViewHoverHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickTableViewHoverHandler *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickTableViewHoverHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickTableViewHoverHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QQuickTableViewHoverHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QQuickHoverHandler::qt_metacast(_clname);
}

int QQuickTableViewHoverHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickHoverHandler::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7195, as _ZN27QQuickTableViewHoverHandler16handleEventPointEP13QPointerEventR11QEventPoint
inline void QQuickTableViewHoverHandler::handleEventPoint(QPointerEvent *event, QEventPoint &point)
{
    QQuickHoverHandler::handleEventPoint(event, point);

    auto tableView = static_cast<QQuickTableView *>(parentItem()->parent());
#if QT_CONFIG(cursor)
    auto tableViewPrivate = QQuickTableViewPrivate::get(tableView);
#endif

    const QPoint cell = tableView->cellAtPosition(point.position(), true);
    const auto item = tableView->itemAtCell(cell);
    if (!item) {
        m_row = -1;
        m_column = -1;
#if QT_CONFIG(cursor)
        tableViewPrivate->updateCursor();
#endif
        return;
    }

    const QPointF itemPos = item->mapFromItem(tableView->contentItem(), point.position());
    const bool hoveringRow = (itemPos.y() < margin() || itemPos.y() > item->height() - margin());
    const bool hoveringColumn = (itemPos.x() < margin() || itemPos.x() > item->width() - margin());
    m_row = hoveringRow ? itemPos.y() < margin() ? cell.y() - 1 : cell.y() : -1;
    m_column = hoveringColumn ? itemPos.x() < margin() ? cell.x() - 1 : cell.x() : -1;
#if QT_CONFIG(cursor)
    tableViewPrivate->updateCursor();
#endif
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7177, as _ZN27QQuickTableViewHoverHandlerC1EP15QQuickTableView
inline QQuickTableViewHoverHandler::QQuickTableViewHoverHandler(QQuickTableView *view)
    : QQuickHoverHandler(view->contentItem())
{
    setMargin(5);

    connect(this, &QQuickHoverHandler::hoveredChanged, this, [this] {
        if (!isHoveringGrid())
            return;
        m_row = -1;
        m_column = -1;
#if QT_CONFIG(cursor)
        auto tableView = static_cast<QQuickTableView *>(parentItem()->parent());
        auto tableViewPrivate = QQuickTableViewPrivate::get(tableView);
        tableViewPrivate->updateCursor();
#endif
    });
}
//  -----------------------------------------------------------------------

//  A QQuickTableViewHoverHandler that Python can take functions over in. Every QQuickTableViewHoverHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewHoverHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewHoverHandlerCall1)(const void *, int *);
typedef bool (*CuteQQuickTableViewHoverHandlerCall2)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewHoverHandlerCall3)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewHoverHandlerCall4)(const void *, int *);
typedef bool (*CuteQQuickTableViewHoverHandlerCall5)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef void (*CuteQQuickTableViewHoverHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTableViewHoverHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickTableViewHoverHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickTableViewHoverHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewHoverHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewHoverHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewHoverHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewHoverHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewHoverHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewHoverHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTableViewHoverHandler : public QQuickTableViewHoverHandler {
public:
  using QQuickTableViewHoverHandler::QQuickTableViewHoverHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onActiveChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickHoverHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall0 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickHoverHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickHoverHandler::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall1 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickHoverHandler::componentComplete();
  }

  //  bool QQuickHoverHandler::wantsPointerEvent(QPointerEvent *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall2 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickHoverHandler::wantsPointerEvent(event);
  }

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall3 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall4 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent
  //      *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall5 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall5>(taken[5]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall6 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall7 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onActiveChanged();
  }

  //  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
  //      QEventPoint &point)
  bool canGrab(QPointerEvent *event, const QEventPoint &point) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall8 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall9 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall9>(taken[9]);
      bool given = call(this, event, &point, proposedGrabber, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::approveGrabTransition(event, point, proposedGrabber);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall10 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall11 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTableViewHoverHandlerCall12 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall12>(taken[12]);
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
      CuteQQuickTableViewHoverHandlerCall13 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall13>(taken[13]);
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
      CuteQQuickTableViewHoverHandlerCall14 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall14>(taken[14]);
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
      CuteQQuickTableViewHoverHandlerCall15 call = reinterpret_cast<CuteQQuickTableViewHoverHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTableViewHoverHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickTableViewHoverHandler10metaObjectEv(
    const QQuickTableViewHoverHandler *self) {
  return self->metaObject();
}

//  void *QQuickTableViewHoverHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQuickTableViewHoverHandler11qt_metacastEPKc(
    QQuickTableViewHoverHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTableViewHoverHandler::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuickTableViewHoverHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTableViewHoverHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTableViewHoverHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuickTableViewHoverHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTableViewHoverHandler::tr(s, c, n));
}

//  QQuickTableViewHoverHandler::QQuickTableViewHoverHandler(QQuickTableView
//      *view)
extern "C" Q_DECL_EXPORT
QQuickTableViewHoverHandler *ritual_ZN27QQuickTableViewHoverHandlerC1EP15QQuickTableView(
    QQuickTableView *view) {
  return new CuteQQuickTableViewHoverHandler(view);
}

//  bool QQuickTableViewHoverHandler::isHoveringGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickTableViewHoverHandler14isHoveringGridEv(
    const QQuickTableViewHoverHandler *self) {
  return self->isHoveringGrid();
}

//  void QQuickTableViewHoverHandler::handleEventPoint(QPointerEvent *event,
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickTableViewHoverHandler16handleEventPointEP13QPointerEventR11QEventPoint(
    QQuickTableViewHoverHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->handleEventPoint(event, *point);
}

//  a Python function taken by a CuteQQuickTableViewHoverHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTableViewHoverHandler(
    QQuickTableViewHoverHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTableViewHoverHandler *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_tableview)
