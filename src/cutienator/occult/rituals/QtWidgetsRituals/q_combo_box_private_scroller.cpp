//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qcombobox_p.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qlistview.h>
#if QT_CONFIG(tableview)
#include <QtWidgets/qtableview.h>
#endif
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qmap.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(treeview)
#include <QtWidgets/qtreeview.h>
#endif
#include <QtWidgets/qheaderview.h>
#include <QtCore/qmath.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(proxymodel)
#include <QtCore/qabstractproxymodel.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qlineedit_p.h>
#if QT_CONFIG(completer)
#include <QtWidgets/private/qcompleter_p.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(effects)
# include <QtWidgets/private/qeffects_p.h>
#endif
#include <QtWidgets/private/qstyle_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qpainter.h>
#include <QtCore/qpointer.h>
#include <array>
#include <chrono>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qcombobox.cpp, line 151, as _ZN24QComboBoxPrivateScroller10enterEventEP11QEnterEvent
inline void QComboBoxPrivateScroller::enterEvent(QEnterEvent *)
{
    startTimer();
}

//  from src/widgets/widgets/qcombobox.cpp, line 156, as _ZN24QComboBoxPrivateScroller10leaveEventEP6QEvent
inline void QComboBoxPrivateScroller::leaveEvent(QEvent *)
{
    stopTimer();
}

//  from src/widgets/widgets/qcombobox.cpp, line 189, as _ZN24QComboBoxPrivateScroller10paintEventEP11QPaintEvent
inline void QComboBoxPrivateScroller::paintEvent(QPaintEvent *)
{
    QPainter p(this);
    QStyleOptionMenuItem menuOpt;
    menuOpt.initFrom(this);
    menuOpt.checkType = QStyleOptionMenuItem::NotCheckable;
    menuOpt.menuRect = rect();
    menuOpt.maxIconWidth = 0;
    menuOpt.reservedShortcutWidth = 0;
    menuOpt.menuItemType = QStyleOptionMenuItem::Scroller;
    if (sliderAction == QAbstractSlider::SliderSingleStepAdd)
        menuOpt.state |= QStyle::State_DownArrow;
    p.eraseRect(rect());
    style()->drawControl(QStyle::CE_MenuScroller, &menuOpt, &p);
}

//  from src/widgets/widgets/qcombobox.cpp, line 161, as _ZN24QComboBoxPrivateScroller10timerEventEP11QTimerEvent
inline void QComboBoxPrivateScroller::timerEvent(QTimerEvent *e)
{
    if (e->matches(timer)) {
        emit doScroll(sliderAction);
        if (fast) {
            emit doScroll(sliderAction);
            emit doScroll(sliderAction);
        }
    }
}

//  from src/widgets/widgets/qcombobox.cpp, line 136, as _ZNK24QComboBoxPrivateScroller8sizeHintEv
inline QSize QComboBoxPrivateScroller::sizeHint() const
{
    return QSize(20, style()->pixelMetric(QStyle::PM_MenuScrollerHeight, nullptr, this));
}

//  from src/widgets/widgets/qcombobox.cpp, line 172, as _ZN24QComboBoxPrivateScroller9hideEventEP10QHideEvent
inline void QComboBoxPrivateScroller::hideEvent(QHideEvent *)
{
    stopTimer();
}

//  from src/widgets/widgets/qcombobox.cpp, line 177, as _ZN24QComboBoxPrivateScroller14mouseMoveEventEP11QMouseEvent
inline void QComboBoxPrivateScroller::mouseMoveEvent(QMouseEvent *e)
{
    // Enable fast scrolling if the cursor is directly above or below the popup.
    const int mouseX = e->position().toPoint().x();
    const int mouseY = e->position().toPoint().y();
    const bool horizontallyInside = pos().x() < mouseX && mouseX < rect().right() + 1;
    const bool verticallyOutside = (sliderAction == QAbstractSlider::SliderSingleStepAdd) ?
                rect().bottom() + 1 < mouseY : mouseY < pos().y();

    fast = horizontallyInside && verticallyOutside;
}

//  from src/widgets/widgets/qcombobox.cpp, line 141, as _ZN24QComboBoxPrivateScroller9stopTimerEv
inline void QComboBoxPrivateScroller::stopTimer()
{
    timer.stop();
}
//  -----------------------------------------------------------------------

//  Only a class built on QComboBoxPrivateScroller may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQComboBoxPrivateScroller : QComboBoxPrivateScroller {
  using QComboBoxPrivateScroller::leaveEvent;
  using QComboBoxPrivateScroller::hideEvent;
  using QComboBoxPrivateScroller::mouseMoveEvent;
  using QComboBoxPrivateScroller::paintEvent;
};

//  A QComboBoxPrivateScroller that Python can take functions over in. Every QComboBoxPrivateScroller
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(combobox)
typedef const QSize * (*CuteQComboBoxPrivateScrollerCall0)(const void *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateScrollerCall1)(const void *, QEnterEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateScrollerCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateScrollerCall3)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateScrollerCall4)(const void *, QHideEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateScrollerCall5)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxPrivateScrollerCall6)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(combobox)
typedef int (*CuteQComboBoxPrivateScrollerCall7)(const void *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall8)(const void *, bool, int *);
typedef const QSize * (*CuteQComboBoxPrivateScrollerCall9)(const void *, int *);
typedef int (*CuteQComboBoxPrivateScrollerCall10)(const void *, int, int *);
typedef bool (*CuteQComboBoxPrivateScrollerCall11)(const void *, int *);
typedef void * (*CuteQComboBoxPrivateScrollerCall12)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQComboBoxPrivateScrollerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateScrollerCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall16)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQComboBoxPrivateScrollerCall17)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQComboBoxPrivateScrollerCall18)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall20)(const void *, QFocusEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall21)(const void *, QFocusEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall22)(const void *, QMoveEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall23)(const void *, QResizeEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall24)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQComboBoxPrivateScrollerCall25)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQComboBoxPrivateScrollerCall26)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQComboBoxPrivateScrollerCall27)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateScrollerCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateScrollerCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateScrollerCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateScrollerCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQComboBoxPrivateScrollerCall32)(const void *, QShowEvent *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall33)(const void *, QEvent *, int *);
typedef int (*CuteQComboBoxPrivateScrollerCall34)(const void *, int, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall35)(const void *, QPainter *, int *);
typedef void * (*CuteQComboBoxPrivateScrollerCall36)(const void *, QPoint *, int *);
typedef void * (*CuteQComboBoxPrivateScrollerCall37)(const void *, int *);
typedef void (*CuteQComboBoxPrivateScrollerCall38)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQComboBoxPrivateScrollerCall39)(const void *, int, int *);
typedef bool (*CuteQComboBoxPrivateScrollerCall40)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQComboBoxPrivateScrollerCall41)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateScrollerCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateScrollerCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateScrollerCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxPrivateScrollerCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQComboBoxPrivateScroller : public QComboBoxPrivateScroller {
public:
  using QComboBoxPrivateScroller::QComboBoxPrivateScroller;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[40] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(combobox)
  //  QSize QComboBoxPrivateScroller::sizeHint() const
  QSize sizeHint() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall0 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QComboBoxPrivateScroller::sizeHint();
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateScroller::enterEvent(QEnterEvent *a0)
  void enterEvent(QEnterEvent *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall1 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QComboBoxPrivateScroller::enterEvent(a0);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateScroller::leaveEvent(QEvent *a0)
  void leaveEvent(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall2 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QComboBoxPrivateScroller::leaveEvent(a0);
  }
#endif  // QT_CONFIG(combobox)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateScroller::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall3 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateScroller::timerEvent(e);
  }
#endif  // QT_CONFIG(combobox)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateScroller::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall4 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QComboBoxPrivateScroller::hideEvent(a0);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateScroller::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall5 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxPrivateScroller::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(combobox)
  //  void QComboBoxPrivateScroller::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall6 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QComboBoxPrivateScroller::paintEvent(a0);
  }
#endif  // QT_CONFIG(combobox)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall7 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall8 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall9 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall10 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall11 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall12 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall13 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall14 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall15 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall16 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall17 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall18 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall19 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall20 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall21 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall22 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall23 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall24 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall25 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall26 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall27 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall28 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall29 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall30 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall31 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall32 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall33 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall34 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall34>(taken[34]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall35 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall35>(taken[35]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall36 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall36>(taken[36]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall37 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall38 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall39 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[40]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall40 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall40>(taken[40]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall41 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall41>(taken[41]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall42 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall43 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall44 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQComboBoxPrivateScrollerCall45 call = reinterpret_cast<CuteQComboBoxPrivateScrollerCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QComboBoxPrivateScroller::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QComboBoxPrivateScroller10metaObjectEv(
    const QComboBoxPrivateScroller *self) {
  return self->metaObject();
}

//  void *QComboBoxPrivateScroller::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QComboBoxPrivateScroller11qt_metacastEPKc(
    QComboBoxPrivateScroller *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QComboBoxPrivateScroller::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QComboBoxPrivateScroller11qt_metacallEN11QMetaObject4CallEiPPv(
    QComboBoxPrivateScroller *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QComboBoxPrivateScroller::~QComboBoxPrivateScroller()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScrollerD1Ev(
    QComboBoxPrivateScroller *self) {
  delete self;
}

//  QSize QComboBoxPrivateScroller::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QComboBoxPrivateScroller8sizeHintEv(
    const QComboBoxPrivateScroller *self) {
  return new QSize(self->sizeHint());
}

//  void QComboBoxPrivateScroller::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller9stopTimerEv(
    QComboBoxPrivateScroller *self) {
  self->stopTimer();
}

//  void QComboBoxPrivateScroller::enterEvent(QEnterEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller10enterEventEP11QEnterEvent(
    QComboBoxPrivateScroller *self,
    QEnterEvent *a0) {
  self->enterEvent(a0);
}

//  void QComboBoxPrivateScroller::leaveEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller10leaveEventEP6QEvent(
    QComboBoxPrivateScroller *self,
    QEvent *a0) {
  self->leaveEvent(a0);
}

//  void QComboBoxPrivateScroller::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller10timerEventEP11QTimerEvent(
    QComboBoxPrivateScroller *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QComboBoxPrivateScroller::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller9hideEventEP10QHideEvent(
    QComboBoxPrivateScroller *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QComboBoxPrivateScroller::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller14mouseMoveEventEP11QMouseEvent(
    QComboBoxPrivateScroller *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QComboBoxPrivateScroller::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller10paintEventEP11QPaintEvent(
    QComboBoxPrivateScroller *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QComboBoxPrivateScroller::doScroll(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QComboBoxPrivateScroller8doScrollEi(
    QComboBoxPrivateScroller *self,
    int action) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QComboBoxPrivateScroller")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "doScroll(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "doScroll(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&action)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQComboBoxPrivateScroller, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboBoxPrivateScroller(
    QComboBoxPrivateScroller *self,
    const char *key,
    void *call) {
  return static_cast<CuteQComboBoxPrivateScroller *>(self)->take(key, call);
}

//  QSize QComboBoxPrivateScroller::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK24QComboBoxPrivateScroller8sizeHintEv(
    const QComboBoxPrivateScroller *self) {
  return new QSize(self->QComboBoxPrivateScroller::sizeHint());
}

//  void QComboBoxPrivateScroller::leaveEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QComboBoxPrivateScroller10leaveEventEP6QEvent(
    QComboBoxPrivateScroller *self,
    QEvent *a0) {
  static_cast<OwnQComboBoxPrivateScroller *>(self)->OwnQComboBoxPrivateScroller::leaveEvent(
      a0);
}

//  void QComboBoxPrivateScroller::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QComboBoxPrivateScroller9hideEventEP10QHideEvent(
    QComboBoxPrivateScroller *self,
    QHideEvent *a0) {
  static_cast<OwnQComboBoxPrivateScroller *>(self)->OwnQComboBoxPrivateScroller::hideEvent(
      a0);
}

//  void QComboBoxPrivateScroller::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QComboBoxPrivateScroller14mouseMoveEventEP11QMouseEvent(
    QComboBoxPrivateScroller *self,
    QMouseEvent *e) {
  static_cast<OwnQComboBoxPrivateScroller *>(self)->OwnQComboBoxPrivateScroller::mouseMoveEvent(
      e);
}

//  void QComboBoxPrivateScroller::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QComboBoxPrivateScroller10paintEventEP11QPaintEvent(
    QComboBoxPrivateScroller *self,
    QPaintEvent *a0) {
  static_cast<OwnQComboBoxPrivateScroller *>(self)->OwnQComboBoxPrivateScroller::paintEvent(
      a0);
}

#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(combobox)
