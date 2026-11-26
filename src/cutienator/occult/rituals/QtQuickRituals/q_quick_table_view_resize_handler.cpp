//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickTableViewResizeHandler' is pasted in, cut from what the moc of Qt
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

//  from QtQuick__QQuickTableViewResizeHandler.cpp, line 1, as moc:QQuickTableViewResizeHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickTableViewResizeHandler::qt_create_metaobjectdata<qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickTableViewResizeHandler"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickTableViewResizeHandler, qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickTableViewResizeHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickTableViewPointerHandler::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t>.metaTypes,
    nullptr
} };

void QQuickTableViewResizeHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickTableViewResizeHandler *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickTableViewResizeHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickTableViewResizeHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN28QQuickTableViewResizeHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QQuickTableViewPointerHandler::qt_metacast(_clname);
}

int QQuickTableViewResizeHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickTableViewPointerHandler::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7259, as _ZN28QQuickTableViewResizeHandler13onGrabChangedEP20QQuickPointerHandlerN15QPointingDevice14GrabTransitionEP13QPointerEventR11QEventPoint
inline void QQuickTableViewResizeHandler::onGrabChanged(QQuickPointerHandler *grabber
                                     , QPointingDevice::GrabTransition transition
                                     , QPointerEvent *ev
                                     , QEventPoint &point)
{
    QQuickSinglePointHandler::onGrabChanged(grabber, transition, ev, point);

    switch (transition) {
    case QPointingDevice::GrabPassive:
    case QPointingDevice::GrabExclusive:
        break;
    case QPointingDevice::UngrabPassive:
    case QPointingDevice::UngrabExclusive:
    case QPointingDevice::CancelGrabPassive:
    case QPointingDevice::CancelGrabExclusive:
    case QPointingDevice::OverrideGrabPassive:
        if (m_state == DraggingStarted || m_state == Dragging) {
            m_state = DraggingFinished;
            updateDrag(ev, point);
        }
        break;
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7283, as _ZN28QQuickTableViewResizeHandler16handleEventPointEP13QPointerEventR11QEventPoint
inline void QQuickTableViewResizeHandler::handleEventPoint(QPointerEvent *event, QEventPoint &point)
{
    auto *tableView = static_cast<QQuickTableView *>(parentItem()->parent());
    auto *tableViewPrivate = QQuickTableViewPrivate::get(tableView);
    const auto *activeHandler = tableViewPrivate->activePointerHandler();
    if (activeHandler && !qobject_cast<const QQuickTableViewResizeHandler *>(activeHandler))
        return;

    // Resolve which state we're in first...
    updateState(point);
    // ...and act on it next
    updateDrag(event, point);
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7235, as _ZN29QQuickTableViewPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint
inline bool QQuickTableViewPointerHandler::wantsEventPoint(const QPointerEvent *event, const QEventPoint &point)
{
    if (!QQuickSinglePointHandler::wantsEventPoint(event, point))
        return false;

    // If we have a mouse wheel event then we do not want to do anything related to resizing.
    if (event->type() == QEvent::Type::Wheel)
        return false;

    // When the user is flicking, we disable resizing, so that
    // he doesn't start to resize by accident.
    const auto *tableView = static_cast<QQuickTableView *>(parentItem()->parent());
    return !tableView->isMoving();
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7227, as _ZN29QQuickTableViewPointerHandlerC2EP15QQuickTableView
inline QQuickTableViewPointerHandler::QQuickTableViewPointerHandler(QQuickTableView *view)
    : QQuickSinglePointHandler(view->contentItem())
{
    // Set a grab permission that stops the flickable, as well as
    // any drag handler inside the delegate, from stealing the drag.
    setGrabPermissions(QQuickPointerHandler::CanTakeOverFromAnything);
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7252, as _ZN28QQuickTableViewResizeHandlerC1EP15QQuickTableView
inline QQuickTableViewResizeHandler::QQuickTableViewResizeHandler(QQuickTableView *view)
    : QQuickTableViewPointerHandler(view)
{
    setMargin(5);
    setObjectName("tableViewResizeHandler");
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7297, as _ZN28QQuickTableViewResizeHandler11updateStateER11QEventPoint
inline void QQuickTableViewResizeHandler::updateState(QEventPoint &point)
{
    auto tableView = static_cast<QQuickTableView *>(parentItem()->parent());
    auto tableViewPrivate = QQuickTableViewPrivate::get(tableView);

    if (m_state == DraggingFinished)
        m_state = Listening;

    if (point.state() == QEventPoint::Pressed) {
        m_row = tableViewPrivate->resizableRows ? tableViewPrivate->hoverHandler->m_row : -1;
        m_column = tableViewPrivate->resizableColumns ? tableViewPrivate->hoverHandler->m_column : -1;
        if (m_row != -1 || m_column != -1)
            m_state = Tracking;
    } else if (point.state() == QEventPoint::Released) {
        if (m_state == DraggingStarted || m_state == Dragging)
            m_state = DraggingFinished;
        else
            m_state = Listening;
    } else if (point.state() == QEventPoint::Updated) {
        switch (m_state) {
        case Listening:
            break;
        case Tracking: {
            const qreal distX = m_column != -1 ? point.position().x() - point.pressPosition().x() : 0;
            const qreal distY = m_row != -1 ? point.position().y() - point.pressPosition().y() : 0;
            const qreal dragDist = qSqrt(distX * distX + distY * distY);
            if (dragDist > qApp->styleHints()->startDragDistance())
                m_state = DraggingStarted;
            break;}
        case DraggingStarted:
            m_state = Dragging;
            break;
        case Dragging:
            break;
        case DraggingFinished:
            // Handled at the top of the function
            Q_UNREACHABLE();
            break;
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7339, as _ZN28QQuickTableViewResizeHandler10updateDragEP13QPointerEventR11QEventPoint
inline void QQuickTableViewResizeHandler::updateDrag(QPointerEvent *event, QEventPoint &point)
{
    auto tableView = static_cast<QQuickTableView *>(parentItem()->parent());
#if QT_CONFIG(cursor)
    auto tableViewPrivate = QQuickTableViewPrivate::get(tableView);
#endif

    switch (m_state) {
    case Listening:
        break;
    case Tracking:
        setPassiveGrab(event, point, true);
        // Disable flicking while dragging. TableView uses filtering instead of
        // pointer handlers to do flicking, so setting an exclusive grab (together
        // with grab permissions) doens't work ATM.
        tableView->setFiltersChildMouseEvents(false);
#if QT_CONFIG(cursor)
        tableViewPrivate->setActivePointerHandler(this);
#endif
        break;
    case DraggingStarted:
        setExclusiveGrab(event, point, true);
        m_columnStartX = point.position().x();
        m_columnStartWidth = tableView->columnWidth(m_column);
        m_rowStartY = point.position().y();
        m_rowStartHeight = tableView->rowHeight(m_row);
#if QT_CONFIG(cursor)
        tableViewPrivate->updateCursor();
#endif
        Q_FALLTHROUGH();
    case Dragging: {
        const qreal distX = point.position().x() - m_columnStartX;
        const qreal distY = point.position().y() - m_rowStartY;
        if (m_column != -1)
            tableView->setColumnWidth(m_column, qMax(0.001, m_columnStartWidth + distX));
        if (m_row != -1)
            tableView->setRowHeight(m_row, qMax(0.001, m_rowStartHeight + distY));
        break; }
    case DraggingFinished: {
        tableView->setFiltersChildMouseEvents(true);
#if QT_CONFIG(cursor)
        tableViewPrivate->setActivePointerHandler(nullptr);
        tableViewPrivate->updateCursor();
#endif
        break; }
    }
}
//  -----------------------------------------------------------------------

//  A QQuickTableViewResizeHandler that Python can take functions over in. Every QQuickTableViewResizeHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickTableViewResizeHandlerCall0)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickTableViewResizeHandlerCall1)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewResizeHandlerCall2)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewResizeHandlerCall3)(const void *, int *);
typedef void (*CuteQQuickTableViewResizeHandlerCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewResizeHandlerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewResizeHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTableViewResizeHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickTableViewResizeHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickTableViewResizeHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewResizeHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewResizeHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewResizeHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewResizeHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewResizeHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewResizeHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTableViewResizeHandler : public QQuickTableViewResizeHandler {
public:
  using QQuickTableViewResizeHandler::QQuickTableViewResizeHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  bool QQuickTableViewPointerHandler::wantsEventPoint(const
  //      QPointerEvent *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall0 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall0>(taken[0]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickTableViewPointerHandler::wantsEventPoint(event, point);
  }

  //  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent
  //      *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall1 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickSinglePointHandler::wantsPointerEvent(event);
  }

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall2 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall3 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall4 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall5 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall6 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTableViewResizeHandlerCall7 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall7>(taken[7]);
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
      CuteQQuickTableViewResizeHandlerCall8 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall8>(taken[8]);
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
      CuteQQuickTableViewResizeHandlerCall9 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall9>(taken[9]);
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
      CuteQQuickTableViewResizeHandlerCall10 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall10>(taken[10]);
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
      CuteQQuickTableViewResizeHandlerCall11 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall11>(taken[11]);
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
      CuteQQuickTableViewResizeHandlerCall12 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall12>(taken[12]);
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
      CuteQQuickTableViewResizeHandlerCall13 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall13>(taken[13]);
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
      CuteQQuickTableViewResizeHandlerCall14 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall14>(taken[14]);
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
      CuteQQuickTableViewResizeHandlerCall15 call = reinterpret_cast<CuteQQuickTableViewResizeHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTableViewResizeHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickTableViewResizeHandler10metaObjectEv(
    const QQuickTableViewResizeHandler *self) {
  return self->metaObject();
}

//  void *QQuickTableViewResizeHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickTableViewResizeHandler11qt_metacastEPKc(
    QQuickTableViewResizeHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTableViewResizeHandler::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickTableViewResizeHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTableViewResizeHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTableViewResizeHandler::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuickTableViewResizeHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTableViewResizeHandler::tr(s, c, n));
}

//  QQuickTableViewResizeHandler::QQuickTableViewResizeHandler(QQuickTableVie
//      w *view)
extern "C" Q_DECL_EXPORT
QQuickTableViewResizeHandler *ritual_ZN28QQuickTableViewResizeHandlerC1EP15QQuickTableView(
    QQuickTableView *view) {
  return new CuteQQuickTableViewResizeHandler(view);
}

//  void QQuickTableViewResizeHandler::updateState(QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTableViewResizeHandler11updateStateER11QEventPoint(
    QQuickTableViewResizeHandler *self,
    QEventPoint *point) {
  self->updateState(*point);
}

//  void QQuickTableViewResizeHandler::updateDrag(QPointerEvent *event,
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTableViewResizeHandler10updateDragEP13QPointerEventR11QEventPoint(
    QQuickTableViewResizeHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->updateDrag(event, *point);
}

//  void QQuickTableViewResizeHandler::handleEventPoint(QPointerEvent *event,
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTableViewResizeHandler16handleEventPointEP13QPointerEventR11QEventPoint(
    QQuickTableViewResizeHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->handleEventPoint(event, *point);
}

//  void QQuickTableViewResizeHandler::onGrabChanged(QQuickPointerHandler
//      *grabber, QPointingDevice::GrabTransition transition, QPointerEvent
//      *ev, QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTableViewResizeHandler13onGrabChangedEP20QQuickPointerHandlerN15QPointingDevice14GrabTransitionEP13QPointerEventR11QEventPoint(
    QQuickTableViewResizeHandler *self,
    QQuickPointerHandler *grabber,
    QPointingDevice::GrabTransition transition,
    QPointerEvent *ev,
    QEventPoint *point) {
  self->onGrabChanged(grabber, transition, ev, *point);
}

//  a Python function taken by a CuteQQuickTableViewResizeHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTableViewResizeHandler(
    QQuickTableViewResizeHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTableViewResizeHandler *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_tableview)
