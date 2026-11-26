//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7396, as _ZN33QQuickTableViewSectionDragHandlerD1Ev
#if QT_CONFIG(quick_draganddrop)
inline QQuickTableViewSectionDragHandler::~QQuickTableViewSectionDragHandler()
{
    resetDragData();
}
#endif  // QT_CONFIG(quick_draganddrop)

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7435, as _ZN33QQuickTableViewSectionDragHandler11grabSectionEv
#if QT_CONFIG(quick_draganddrop)
inline void QQuickTableViewSectionDragHandler::grabSection()
{
    // Generate the transparent section image in pixmap
    QPixmap pixmap(m_grabResult->image().size());
    pixmap.fill(Qt::transparent);
    QPainter painter(&pixmap);
    painter.setOpacity(0.6);
    painter.drawImage(0, 0, m_grabResult->image());
    painter.end();

    // Specify the pixmap and mime data to be as drag object
    auto *mimeData = new QMimeData();
    mimeData->setImageData(pixmap);
    m_drag->setMimeData(mimeData);
    m_drag->setPixmap(pixmap);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7468, as _ZN33QQuickTableViewSectionDragHandler10handleDragEP15QQuickDragEvent
#if QT_CONFIG(quick_draganddrop)
inline void QQuickTableViewSectionDragHandler::handleDrag(QQuickDragEvent *event)
{
    Q_UNUSED(event);

    if (m_state == Dragging) {
        auto *tableView = static_cast<QQuickTableView *>(parentItem()->parent());
        const QPoint dragItemPosition(tableView->contentX() + event->x(), tableView->contentY() + event->y());
        const auto *sourceItem = qobject_cast<QQuickItem *>(m_drag->source());
        const QPoint targetCell = tableView->cellAtPosition(dragItemPosition, true);

        auto *tableViewPrivate = QQuickTableViewPrivate::get(tableView);
        const int newDestination = (m_sectionOrientation == Qt::Horizontal) ? targetCell.x() : targetCell.y();
        if (newDestination != m_destination) {
            // Reset the overlay property in the existing model delegate item
            resetSectionOverlay();
            // Set the overlay property in the new model delegate item
            const int row = (m_sectionOrientation == Qt::Horizontal) ? 0 : newDestination;
            const int column = (m_sectionOrientation == Qt::Horizontal) ? newDestination : 0;
            tableViewPrivate->setContainsDragOnDelegateItem(tableView->index(row, column), true);
            m_destination = newDestination;
        }

        // Scroll header view while section item moves out of the table boundary
        const QPoint dragItemStartPos = (m_sectionOrientation == Qt::Horizontal) ? QPoint(dragItemPosition.x() - sourceItem->width() / 2, dragItemPosition.y()) :
                QPoint(dragItemPosition.x(), dragItemPosition.y() - sourceItem->height() / 2);
        const QPoint dragItemEndPos = (m_sectionOrientation == Qt::Horizontal) ? QPoint(dragItemPosition.x() + sourceItem->width() / 2, dragItemPosition.y()) :
                QPoint(dragItemPosition.x(), dragItemPosition.y() + sourceItem->height() / 2);
        const bool useStartPos = (m_sectionOrientation == Qt::Horizontal) ? (dragItemStartPos.x() <= tableView->contentX()) : (dragItemStartPos.y() <= tableView->contentY());
        const bool useEndPos = (m_sectionOrientation == Qt::Horizontal) ? (dragItemEndPos.x() >= tableView->width()) : (dragItemEndPos.y() >= tableView->height());
        if (useStartPos || useEndPos) {
            if (!m_scrollTimer.isActive()) {
                m_dragPoint = (m_sectionOrientation == Qt::Horizontal) ? QPoint(useStartPos ? dragItemStartPos.x() : dragItemEndPos.x(), 0) :
                        QPoint(0, useStartPos ? dragItemStartPos.y() : dragItemEndPos.y());
                m_scrollTimer.start(1);
            }
        } else {
            if (m_scrollTimer.isActive())
                m_scrollTimer.stop();
        }
    }
}
#endif  // QT_CONFIG(quick_draganddrop)

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7452, as _ZN33QQuickTableViewSectionDragHandler10handleDropEP15QQuickDragEvent
#if QT_CONFIG(quick_draganddrop)
inline void QQuickTableViewSectionDragHandler::handleDrop(QQuickDragEvent *event)
{
    Q_UNUSED(event);

    if (m_state == Dragging) {
        auto *tableView = static_cast<QQuickTableView *>(parentItem()->parent());
        auto *tableViewPrivate = QQuickTableViewPrivate::get(tableView);
        tableViewPrivate->moveSection(m_source, m_destination, m_sectionOrientation);
        m_state = DraggingFinished;
        resetSectionOverlay();
        if (m_scrollTimer.isActive())
            m_scrollTimer.stop();
        event->accept();
    }
}
#endif  // QT_CONFIG(quick_draganddrop)

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7510, as _ZN33QQuickTableViewSectionDragHandler20handleDragDropActionEN2Qt10DropActionE
#if QT_CONFIG(quick_draganddrop)
inline void QQuickTableViewSectionDragHandler::handleDragDropAction(Qt::DropAction action)
{
    // Reset the overlay property in the model delegate item when drag or drop
    // happens outside specified drop area (i.e. during ignore action)
    if (action == Qt::IgnoreAction) {
        resetSectionOverlay();
        if (m_scrollTimer.isActive())
            m_scrollTimer.stop();
    }
}
#endif  // QT_CONFIG(quick_draganddrop)

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7401, as _ZN33QQuickTableViewSectionDragHandler13resetDragDataEv
#if QT_CONFIG(quick_draganddrop)
inline void QQuickTableViewSectionDragHandler::resetDragData()
{
    if (m_state != Listening) {
        m_state = Listening;
        resetSectionOverlay();
        m_source = -1;
        m_destination = -1;
        if (m_grabResult.data())
            m_grabResult.data()->disconnect();
        if (!m_drag.isNull()) {
            m_drag->disconnect();
            delete m_drag;
        }
        if (!m_dropArea.isNull()) {
            m_dropArea->disconnect();
            delete m_dropArea;
        }
        auto *tableView = static_cast<QQuickTableView *>(parentItem()->parent());
        tableView->setFiltersChildMouseEvents(true);
    }
}
#endif  // QT_CONFIG(quick_draganddrop)

//  from ../qtdeclarative/src/quick/items/qquicktableview.cpp, line 7423, as _ZN33QQuickTableViewSectionDragHandler19resetSectionOverlayEv
#if QT_CONFIG(quick_draganddrop)
inline void QQuickTableViewSectionDragHandler::resetSectionOverlay()
{
    if (m_destination != -1) {
        auto *tableView = static_cast<QQuickTableView *>(parentItem()->parent());
        auto *tableViewPrivate = QQuickTableViewPrivate::get(tableView);
        const int row = (m_sectionOrientation == Qt::Horizontal) ? 0 : m_destination;
        const int column = (m_sectionOrientation == Qt::Horizontal) ? m_destination : 0;
        tableViewPrivate->setContainsDragOnDelegateItem(tableView->index(row, column), false);
        m_destination = -1;
    }
}
#endif  // QT_CONFIG(quick_draganddrop)
//  -----------------------------------------------------------------------

//  A QQuickTableViewSectionDragHandler that Python can take functions over in. Every QQuickTableViewSectionDragHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickTableViewSectionDragHandlerCall0)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickTableViewSectionDragHandlerCall1)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewSectionDragHandlerCall2)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickTableViewSectionDragHandlerCall3)(const void *, int *);
typedef void (*CuteQQuickTableViewSectionDragHandlerCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewSectionDragHandlerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewSectionDragHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTableViewSectionDragHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickTableViewSectionDragHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickTableViewSectionDragHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTableViewSectionDragHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewSectionDragHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewSectionDragHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewSectionDragHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewSectionDragHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTableViewSectionDragHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTableViewSectionDragHandler : public QQuickTableViewSectionDragHandler {
public:
  using QQuickTableViewSectionDragHandler::QQuickTableViewSectionDragHandler;
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
      CuteQQuickTableViewSectionDragHandlerCall0 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall0>(taken[0]);
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
      CuteQQuickTableViewSectionDragHandlerCall1 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall1>(taken[1]);
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
      CuteQQuickTableViewSectionDragHandlerCall2 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTableViewSectionDragHandlerCall3 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTableViewSectionDragHandlerCall4 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall4>(taken[4]);
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
      CuteQQuickTableViewSectionDragHandlerCall5 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall5>(taken[5]);
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
      CuteQQuickTableViewSectionDragHandlerCall6 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTableViewSectionDragHandlerCall7 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall7>(taken[7]);
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
      CuteQQuickTableViewSectionDragHandlerCall8 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall8>(taken[8]);
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
      CuteQQuickTableViewSectionDragHandlerCall9 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall9>(taken[9]);
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
      CuteQQuickTableViewSectionDragHandlerCall10 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall10>(taken[10]);
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
      CuteQQuickTableViewSectionDragHandlerCall11 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall11>(taken[11]);
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
      CuteQQuickTableViewSectionDragHandlerCall12 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall12>(taken[12]);
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
      CuteQQuickTableViewSectionDragHandlerCall13 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall13>(taken[13]);
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
      CuteQQuickTableViewSectionDragHandlerCall14 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall14>(taken[14]);
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
      CuteQQuickTableViewSectionDragHandlerCall15 call = reinterpret_cast<CuteQQuickTableViewSectionDragHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTableViewSectionDragHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QQuickTableViewSectionDragHandler10metaObjectEv(
    const QQuickTableViewSectionDragHandler *self) {
  return self->metaObject();
}

//  void *QQuickTableViewSectionDragHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QQuickTableViewSectionDragHandler11qt_metacastEPKc(
    QQuickTableViewSectionDragHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTableViewSectionDragHandler::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QQuickTableViewSectionDragHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTableViewSectionDragHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickTableViewSectionDragHandler::~QQuickTableViewSectionDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandlerD1Ev(
    QQuickTableViewSectionDragHandler *self) {
  delete self;
}

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewSectionDragHandler::grabSection()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler11grabSectionEv(
    QQuickTableViewSectionDragHandler *self) {
  self->grabSection();
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewSectionDragHandler::handleDrag(QQuickDragEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler10handleDragEP15QQuickDragEvent(
    QQuickTableViewSectionDragHandler *self,
    QQuickDragEvent *event) {
  self->handleDrag(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewSectionDragHandler::handleDrop(QQuickDragEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler10handleDropEP15QQuickDragEvent(
    QQuickTableViewSectionDragHandler *self,
    QQuickDragEvent *event) {
  self->handleDrop(event);
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void
//      QQuickTableViewSectionDragHandler::handleDragDropAction(Qt::DropActio
//      n action)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler20handleDragDropActionEN2Qt10DropActionE(
    QQuickTableViewSectionDragHandler *self,
    Qt::DropAction action) {
  self->handleDragDropAction(action);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  void
//      QQuickTableViewSectionDragHandler::setSectionOrientation(Qt::Orientat
//      ion orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler21setSectionOrientationEN2Qt11OrientationE(
    QQuickTableViewSectionDragHandler *self,
    Qt::Orientation orientation) {
  self->setSectionOrientation(orientation);
}

//  void QQuickTableViewSectionDragHandler::handleEventPoint(QPointerEvent
//      *event, QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler16handleEventPointEP13QPointerEventR11QEventPoint(
    QQuickTableViewSectionDragHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->handleEventPoint(event, *point);
}

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewSectionDragHandler::resetDragData()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler13resetDragDataEv(
    QQuickTableViewSectionDragHandler *self) {
  self->resetDragData();
}
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
//  void QQuickTableViewSectionDragHandler::resetSectionOverlay()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickTableViewSectionDragHandler19resetSectionOverlayEv(
    QQuickTableViewSectionDragHandler *self) {
  self->resetSectionOverlay();
}
#endif  // QT_CONFIG(quick_draganddrop)

//  a Python function taken by a CuteQQuickTableViewSectionDragHandler, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTableViewSectionDragHandler(
    QQuickTableViewSectionDragHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTableViewSectionDragHandler *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_draganddrop)
#endif  // QT_CONFIG(quick_tableview)
